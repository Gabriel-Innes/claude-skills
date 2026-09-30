# OE module - compiled AOM dictionary

## OEAUDD - Posting Journals - Details (view OE0100)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSTYPE+DAYENDNUM+ENTRYNUM+LINENUM; DAYENDNUM+ENTRYNUM+LINENUM
Fields (NAME type description [values]):
  TRANSTYPE Integer Transaction Type [1=Invoice,2=Credit Note,3=Shipment,4=Debit Note,5=Order]
  DAYENDNUM Long Day End Number
  ENTRYNUM Long Entry Number
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LINETYPE Integer Line Type [1=Item,2=Miscellaneous]
  ITEM String*24 Item Number
  MISCCHARGE String*6 Miscellaneous Charge Code
  DESC String*60 Description
  PRICELIST String*6 Price List
  CATEGORY String*6 Category
  LOCATION String*6 Location
  QTYSHIPPED BCD*10.4 Quantity Shipped
  INVUNIT String*10 Unit of Measure
  UNITPRICE BCD*10.6 Unit Price
  PRICEOVER Boolean Price Override
  UNITCOST BCD*10.6 Unit Cost
  EXTCOSTH BCD*10.3 Extended Cost (Functional)
  EXTCOSTS BCD*10.3 Extended Cost (Source)
  COSTVARH BCD*10.3 Cost Variance (Functional)
  COSTVARS BCD*10.3 Cost Variance (Source)
  EXTOVER Boolean Extended Amount Override
  EXTINVMISC BCD*10.3 Extended Amount
  REVAMTH BCD*10.3 Revenue (Functional)
  REVAMTS BCD*10.3 Revenue (Source)
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TAMOUNT1 BCD*10.3 Tax Amount 1
  TAMOUNT2 BCD*10.3 Tax Amount 2
  TAMOUNT3 BCD*10.3 Tax Amount 3
  TAMOUNT4 BCD*10.3 Tax Amount 4
  TAMOUNT5 BCD*10.3 Tax Amount 5
  REVENUACCT String*45 Revenue Account
  COGSACCT String*45 Cost of Goods Sold Account
  VARIANACCT String*45 Variance Account
  INVACCT String*45 Inventory Control Account
  RETURNTYPE Integer Return Type [1=Items Returned to Inventory,2=Damaged Items,3=Price Adjustment]
  SHPCLRACCT String*45 Shipment Clearing Account
  EXTCSTADJH BCD*10.3 Functional Adjusted Ext.Cost
  EXTCSTADJS BCD*10.3 Source Adjusted Ext. Cost
  CSTVARADJH BCD*10.3 Functional Adjusted Cost Variance
  CSTVARADJS BCD*10.3 Source Adjusted Cost Variance
  INVDISC BCD*10.3 Invoice Discount
  FROMDOC String*22 From Document
  DDTLNO String*6 Kit No.
  VALUES Long Optional Fields
  TERMDISCBL Integer Discountable [0=No,1=Yes]
  WEIGHTUNIT String*10 Weight Unit of Measure
  DEFUWEIGHT BCD*10.4 Def. Weight UOM Unit Weight
  DEFEXTWGHT BCD*10.4 Def. Weight UOM Ext. Unit Weight
  PRPRICEBY Integer Price By [1=Quantity,2=Weight]
  CAPPROVEBY String*8 Price Approved By
  TRAMOUNT1 BCD*10.3 Tax Reporting Amount 1
  TRAMOUNT2 BCD*10.3 Tax Reporting Amount 2
  TRAMOUNT3 BCD*10.3 Tax Reporting Amount 3
  TRAMOUNT4 BCD*10.3 Tax Reporting Amount 4
  TRAMOUNT5 BCD*10.3 Tax Reporting Amount 5
  JOBRELATED Boolean Job Related
  CONTRACT String*16 Contract Code
  PROJECT String*16 Project Code
  CCATEGORY String*16 Category Code
  COSTCLASS Integer Cost Class [0=,1=Labor,2=Material,3=Equipment,4=Subcontractor,5=Overhead,6=Miscellaneous]
  PROJSTYLE Integer Project Style [0=,1=Standard,2=Basic]
  PROJTYPE Integer Project Type [0=,1=Time and Materials,2=Fixed Price,3=Cost Plus]
  REVREC Integer Accounting Method [0=,1=Completed Project,2=Total Cost Percentage Complete,3=Labor Hours Percentage Complete,4=Billings and Costs,5=Project Percentage Complete,6=Category Percentage Complete,7=Completed Contract,8=Accrual-Basis]
  BILLTYPE Integer Billing Type [0=,1=Non-billable,2=Billable,3=No Charge]
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item Unit
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percent
  RTGDAYS Integer Retainage Days
  RTGDATEDUE Date Retainage Due Date
  RTGDDTOVR Boolean Retainage Due Date Override
  RTGAMTOVR Boolean Retainage Amount Override
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  OVERHDACCT String*45 Overhead Account
  OVERHDH BCD*10.3 Overhead (Functional)
  OVERHDS BCD*10.3 Overhead (Source)
  LABORACCT String*45 Labor Account
  LABORH BCD*10.3 Labor (Functional)
  LABORS BCD*10.3 Labor (Source)
  PMTRANSNBR Long PM Transaction Number
  EDN String*30 Export Declaration Number

## OEAUDDD - Posting Journals - Detail-Details (view OE0105)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSTYPE+DAYENDNUM+ENTRYNUM+LINENUM+COMPNUM; DAYENDNUM+ENTRYNUM+LINENUM+COMPNUM
Fields (NAME type description [values]):
  TRANSTYPE Integer Transaction Type [1=Invoice,2=Credit Note,3=Shipment,4=Debit Note,5=Order]
  DAYENDNUM Long Day End Number
  ENTRYNUM Long Entry Number
  LINENUM Integer Line Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPONENT String*24 Component Item
  DESC String*60 Description
  LOCATION String*6 Location
  QTYSHIPPED BCD*10.4 Quantity Shipped
  INVUNIT String*10 Unit of Measure
  UNITCOST BCD*10.6 Unit Cost
  EXTCOSTH BCD*10.3 Extended Cost (Functional)
  EXTCOSTS BCD*10.3 Extended Cost (Source)
  COSTVARH BCD*10.3 Cost Variance (Functional)
  COSTVARS BCD*10.3 Cost Variance (Source)
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  COGSACCT String*45 Cost of Goods Sold Account
  VARIANACCT String*45 Variance Account
  INVACCT String*45 Inventory Control Account
  SHPCLRACCT String*45 Shipment Clearing Account
  EXTCSTADJH BCD*10.3 Functional Adjusted Ext.Cost
  EXTCSTADJS BCD*10.3 Source Adjusted Ext. Cost
  CSTVARADJH BCD*10.3 Functional Adjusted Cost Variance
  CSTVARADJS BCD*10.3 Source Adjusted Cost Variance
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRNWGTCONV BCD*10.6 Parent Weight Conversion Factor
  PRNUWEIGHT BCD*10.4 Parent Weight UOM Unit Weight
  PRNEXTWGHT BCD*10.4 Parent WUOM Extended Unit Weight

## OEAUDDP - Posting Jnls Detail Opt. Fields (view OE0110)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSTYPE+DAYENDNUM+ENTRYNUM+LINENUM+OPTFIELD; OPTFIELD+TRANSTYPE+DAYENDNUM+ENTRYNUM+LINENUM
Fields (NAME type description [values]):
  TRANSTYPE Integer Transaction Type [1=Invoice,2=Credit Note,3=Shipment,4=Debit Note,5=Order]
  DAYENDNUM Long Day End Number
  ENTRYNUM Long Entry Number
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

## OEAUDH - Posting Journals (view OE0120)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSTYPE+DAYENDNUM+ENTRYNUM; TRANSTYPE+DOCNUM+DAYENDNUM+ENTRYNUM [D]; TRANSTYPE+TRANSDATE+DAYENDNUM+ENTRYNUM [D]; TRANSTYPE+CUSTOMER+DAYENDNUM+ENTRYNUM [D]
Fields (NAME type description [values]):
  TRANSTYPE Integer Transaction Type [1=Invoice,2=Credit Note,3=Shipment,4=Debit Note,5=Order]
  DAYENDNUM Long Day End Number
  ENTRYNUM Long Entry Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PRINTED Boolean Printed
  TRANSDATE Date Transaction Date
  FISCYR String*4 Fiscal Year
  FISCPER Integer Fiscal Period
  DOCNUM String*22 Document Number
  ARINVBATCH BCD*5.0 A/R Invoice Batch Number
  REFERENCE String*60 Reference
  DESC String*60 Description
  CUSTOMER String*12 Customer Number
  CUSTNAME String*60 Customer Name
  TAXGROUP String*12 Tax Group
  ORDNUMBER String*22 Order Number
  ORDDATE Date Order Date
  INVNUMBER String*22 Invoice Number
  INVDATE Date Invoice Date
  PONUMBER String*22 Purchase Order Number
  TERRITORY String*6 Territory
  INVDISCPER BCD*5.5 Discount Percentage
  INVDISCAMT BCD*10.3 Discount Amount
  INSOURCURR String*3 Invoice Currency
  INRATE BCD*8.7 Invoice Exchange Rate
  INRATETYPE String*2 Invoice Rate Type
  INRATEDATE Date Invoice Rate Date
  TAUTH1 String*12 Tax Authority 1
  TAUTH2 String*12 Tax Authority 2
  TAUTH3 String*12 Tax Authority 3
  TAUTH4 String*12 Tax Authority 4
  TAUTH5 String*12 Tax Authority 5
  TCLASS1 Integer Customer Tax Class 1
  TCLASS2 Integer Customer Tax Class 2
  TCLASS3 Integer Customer Tax Class 3
  TCLASS4 Integer Customer Tax Class 4
  TCLASS5 Integer Customer Tax Class 5
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TAMOUNT1H BCD*10.3 Tax Amount 1 - Functional
  TAMOUNT2H BCD*10.3 Tax Amount 2 - Functional
  TAMOUNT3H BCD*10.3 Tax Amount 3 - Functional
  TAMOUNT4H BCD*10.3 Tax Amount 4 - Functional
  TAMOUNT5H BCD*10.3 Tax Amount 5 - Functional
  TINAMT1S BCD*10.3 Tax Included Amount 1 - Source
  TINAMT2S BCD*10.3 Tax Included Amount 2 - Source
  TINAMT3S BCD*10.3 Tax Included Amount 3 - Source
  TINAMT4S BCD*10.3 Tax Included Amount 4 - Source
  TINAMT5S BCD*10.3 Tax Included Amount 5 - Source
  TEXAMT1S BCD*10.3 Tax Excluded Amount 1 - Source
  TEXAMT2S BCD*10.3 Tax Excluded Amount 2 - Source
  TEXAMT3S BCD*10.3 Tax Excluded Amount 3 - Source
  TEXAMT4S BCD*10.3 Tax Excluded Amount 4 - Source
  TEXAMT5S BCD*10.3 Tax Excluded Amount 5 - Source
  TACCT1 String*45 Tax G/L Account 1
  TACCT2 String*45 Tax G/L Account 2
  TACCT3 String*45 Tax G/L Account 3
  TACCT4 String*45 Tax G/L Account 4
  TACCT5 String*45 Tax G/L Account 5
  INVNETH BCD*10.3 Net Invoice Amount (Functional)
  INVNETS BCD*10.3 Net Invoice Amount (Source)
  SALESPER1 String*8 Salesperson 1
  SALESPER2 String*8 Salesperson 2
  SALESPER3 String*8 Salesperson 3
  SALESPER4 String*8 Salesperson 4
  SALESPER5 String*8 Salesperson 5
  SALESPLT1 BCD*5.5 Sales Percentage 1
  SALESPLT2 BCD*5.5 Sales Percentage 2
  SALESPLT3 BCD*5.5 Sales Percentage 3
  SALESPLT4 BCD*5.5 Sales Percentage 4
  SALESPLT5 BCD*5.5 Sales Percentage 5
  POSTDATE Date Posting Date
  MULTIDOC Boolean Multiple Documents
  VALUES Long Optional Fields
  TRCURRENCY String*3 Tax Reporting Currency
  TRRATE BCD*8.7 Tax Reporting Currency Rate
  TRRATETYPE String*2 Tax Reporting Currency Type
  TRRATEDATE Date Tax Reporting Currency Date
  TREAMOUNT1 BCD*10.3 TRC Excluded Amount 1
  TREAMOUNT2 BCD*10.3 TRC Excluded Amount 2
  TREAMOUNT3 BCD*10.3 TRC Excluded Amount 3
  TREAMOUNT4 BCD*10.3 TRC Excluded Amount 4
  TREAMOUNT5 BCD*10.3 TRC Excluded Amount 5
  TRIAMOUNT1 BCD*10.3 TRC Included Amount 1
  TRIAMOUNT2 BCD*10.3 TRC Included Amount 2
  TRIAMOUNT3 BCD*10.3 TRC Included Amount 3
  TRIAMOUNT4 BCD*10.3 TRC Included Amount 4
  TRIAMOUNT5 BCD*10.3 TRC Included Amount 5
  CUSACCTSET String*6 Customer Account Set
  JOBLINES Long Job Related Detail Lines
  LNINVABLE Long Invoiceable Detail Lines
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGTERMS String*6 Retainage Terms
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percent
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  DATEBUS Date Posting Date
  EDN String*30 Export Declaration Number

## OEAUDHP - Posting Journals Optional Fields (view OE0123)
Keys (first = PK; D=dups allowed, M=modifiable): TRANSTYPE+DAYENDNUM+ENTRYNUM+OPTFIELD; OPTFIELD+TRANSTYPE+DAYENDNUM+ENTRYNUM
Fields (NAME type description [values]):
  TRANSTYPE Integer Transaction Type [1=Invoice,2=Credit Note,3=Shipment,4=Debit Note,5=Order]
  DAYENDNUM Long Day End Number
  ENTRYNUM Long Entry Number
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

## OECOINC - Crd/Dbn Comments/Instructions (view OE0140)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+UNIQUIFIER
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
  UNIQUIFIER Integer Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COINTYPE Integer Comments/Instructions Type [1=Comment,2=Instruction]
  COIN String*80 Comments/Instructions

## OECOINI - Invoice Comments/Instructions (view OE0160)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+UNIQUIFIER
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  UNIQUIFIER Integer Line Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COINTYPE Integer Comments/Instructions Type [1=Comment,2=Instruction]
  COIN String*80 Comments/Instructions

## OECOINO - Order Comments/Instructions (view OE0180)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+UNIQUIFIER
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  UNIQUIFIER Integer Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COINTYPE Integer Comments/Instructions Type [1=Comment,2=Instruction]
  COIN String*80 Comments/Instructions
  INVOICED Boolean Invoiced

## OECOINS - Shipment Comments/Instructions (view OE0190)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+UNIQUIFIER
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  UNIQUIFIER Integer Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COINTYPE Integer Comments/Instructions Type [1=Comment,2=Instruction]
  COIN String*80 Comments/Instructions

## OECOMM - Commissions (view OE0200)
Keys (first = PK; D=dups allowed, M=modifiable): SALESPER+DAYENDNUM+ENTRYNUM+SALESPNUM; DATE+SALESPER+FISCYR+FISCPER+DAYENDNUM+ENTRYNUM+SALESPNUM [M]; FISCYR+FISCPER+SALESPER+DATE+DAYENDNUM+ENTRYNUM+SALESPNUM [M]
Fields (NAME type description [values]):
  SALESPER String*8 Salesperson Number
  DAYENDNUM Long Day End Number
  ENTRYNUM Long Entry Number
  SALESPNUM Integer Salesperson Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUSTOMER String*12 Customer Number
  CUSTNAME String*60 Customer Name
  TRANSTYPE Integer Transaction Type [1=Invoice,2=Credit Note,3=Shipment,4=Debit Note,5=Order]
  DOCNUM String*22 Document Number
  DATE Date Transaction Date
  TERRITORY String*6 Territory
  CATSALES BCD*10.3 Category Sales
  CATCOST BCD*10.3 Cost of Category Sales
  CATCOMM BCD*10.3 Commission on Category Sales
  NONCATSALE BCD*10.3 Noncategory Sales
  NONCATCOST BCD*10.3 Cost of Noncategory Sales
  NONCATCOM1 BCD*10.3 Commission on Noncat. Sales 1
  NONCATCOM2 BCD*10.3 Commission on Noncat. Sales 2
  NONCATCOM3 BCD*10.3 Commission on Noncat. Sales 3
  NONCATCOM4 BCD*10.3 Commission on Noncat. Sales 4
  NONCATCOM5 BCD*10.3 Commission on Noncat. Sales 5
  FISCYR String*4 Fiscal Year
  FISCPER Integer Fiecal Period

## OECRDD - Credit/Debit Details (view OE0220)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM; CRDUNIQ+DETAILNUM
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LINETYPE Integer Line Type [1=Item,2=Miscellaneous]
  ITEM String*24 Item
  MISCCHARGE String*6 Miscellaneous Charges Code
  DESC String*60 Description
  ACCTSET String*6 Item Account Set
  USERCOSTMD Boolean User-Specified Costing Method
  PRICELIST String*6 Price List
  CATEGORY String*6 Category
  LOCATION String*6 Location
  PICKSEQ String*10 Picking Sequence
  STOCKITEM Boolean Stock Item
  QTYRETURN BCD*10.4 Quantity Returned
  QTYSHIPPED BCD*10.4 Quantity Shipped
  QTYBACKORD BCD*10.4 Quantity Backordered
  CRDUNIT String*10 Credit/Debit Note UOM
  UNITCONV BCD*10.6 Unit Conversion
  UNITPRICE BCD*10.6 Unit Price
  PRICEOVER Boolean Price Override
  UNITCOST BCD*10.6 Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  UNITPRCDEC Integer Unit Price No. of Decimals
  PRICEUNIT String*10 Pricing Unit
  PRIUNTPRC BCD*10.6 Pricing Unit Price
  PRIUNTCONV BCD*10.6 Pricing Unit Conversion
  PRIPERCENT BCD*5.5 Price Discount Percentage
  PRIAMOUNT BCD*10.3 Price Discount Amount
  BASEUNIT String*10 Pricing Base Unit
  PRIBASPRC BCD*10.6 Pricing Base Unit Price
  PRIBASCONV BCD*10.6 Pricing Base Unit Conversion
  COSTUNIT String*10 Costing Unit
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTCCOST BCD*10.3 Extended Detail Cost
  EXTCRDMISC BCD*10.3 Extended Amount/Misc. Charge
  CRDDISC BCD*10.3 Credit Note Discount Amount
  EXTOVER Boolean Extended Amount Override
  EXTICOST BCD*10.3 Invoice Extended Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  RETURNTYPE Integer Return Type [1=Items Returned to Inventory,2=Damaged Items,3=Price Adjustment]
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TAMOUNT1 BCD*10.3 Tax Amount 1
  TAMOUNT2 BCD*10.3 Tax Amount 2
  TAMOUNT3 BCD*10.3 Tax Amount 3
  TAMOUNT4 BCD*10.3 Tax Amount 4
  TAMOUNT5 BCD*10.3 Tax Amount 5
  TRATE1 BCD*8.5 Tax Rate 1
  TRATE2 BCD*8.5 Tax Rate 2
  TRATE3 BCD*8.5 Tax Rate 3
  TRATE4 BCD*8.5 Tax Rate 4
  TRATE5 BCD*8.5 Tax Rate 5
  DETAILNUM Integer Detail Number
  COMMINST Boolean Have Comments/Instructions [0=No,1=Yes]
  GLNONSTKCR String*45 Non-stock Clearing Account
  AVGCOST BCD*10.6 Average Unit Cost
  LASTCOST BCD*10.6 Last Unit Cost
  SHIPTRACK String*36 Shipment Tracking Number
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  DISCPER BCD*5.5 Discount Percent
  EXPDATE Date Shipment Date
  QTYORDERED BCD*10.4 Invoice Current Qty. Outstanding
  INVUNIT String*10 Invoice Unit of Measure
  INVUNITCON BCD*10.6 Invoice Unit Conversion
  ORDQTYORD BCD*10.4 Order Quantity Ordered
  ORDQTYBKOR BCD*10.4 Order Quantity Backordered
  ORDQTYCOMM BCD*10.4 Order Quantity Committed
  ORDQTYSTD BCD*10.4 Order Quantity Shipped-to-date
  ORDUNIT String*10 Order Unit of Measure
  ORDUNITCON BCD*10.6 Order Unit Conversion
  MANITEMNO String*24 Manufacturer's Item Number
  CUSTITEMNO String*24 Customer Item Number
  VALUES Long Optional Fields
  DDTLTYPE Integer Kitting/BOM [0=None,1=Kitting,2=BOM]
  DDTLNO String*6 Kit/BOM Number
  BUILDQTY BCD*10.4 BOM Build Qty.
  BUILDUNIT String*10 BOM Build Unit
  BLDUNTCONV BCD*10.6 BOM Build Unit Conversion
  INVNUMBER String*22 Invoice Number
  NEXTCMPNUM Long Next Component Number
  EPOSPROMID Integer ePOS Promotion ID
  BASEWUNIT String*10 Pricing Base Weight Unit
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRWGHTUNIT String*10 Pricing Weight UOM
  PRWGHTCONV BCD*10.6 Pricing Weight Conversion Factor
  PRIBASWCNV BCD*10.6 Pricing Base Weight Conv. Factor
  DEFUWEIGHT BCD*10.4 Def. Weight UOM Unit Weight
  DEFEXTWGHT BCD*10.4 Def. Weight UOM Ext. Unit Weight
  PRPRICEBY Integer Price By [1=Quantity,2=Weight]
  NEEDPCHECK Boolean Price Check Pending
  CAPPROVEBY String*8 Price Approved By
  HDRDISC BCD*10.3 Header Discount
  CTRAMOUNT1 BCD*10.3 TR Tax Amount 1
  CTRAMOUNT2 BCD*10.3 TR Tax Amount 2
  CTRAMOUNT3 BCD*10.3 TR Tax Amount 3
  CTRAMOUNT4 BCD*10.3 TR Tax Amount 4
  CTRAMOUNT5 BCD*10.3 TR Tax Amount 5
  COG BCD*10.3 Cost of Goods
  COSTED Boolean Record Costed [0=No,1=Yes]
  JOBRELATED Boolean Job Related
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
  RTGDATEDUE Date Retainage Due Date
  RTGDDTOVR Boolean Retainage Due Date Override
  RTGAMTOVR Boolean Retainage Amount Override
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  PRICEOPT Integer Default O/E Price [0=,1=Billing Rate,2=Use Customer Price List,3=Use Specified Price List]
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]

## OECRDDB - Credit/Debit BOM Details (view OE0223)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
  LINENUM Integer Detail Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPONENT String*24 Component Item No.
  DESC String*60 Description
  QTY BCD*10.4 Component Quantity
  UNIT String*10 Unit of Measure
  QTYRETURN BCD*10.4 Quantity Returned
  DDTLNO String*6 Component's BOM Number
  BUILDQTY BCD*10.4 Component's BOM Build Qty.
  BUILDUNIT String*10 Component's BOM Build Unit
  BLDUNTCONV BCD*10.6 Component's BOM Build Unit Conv.
  UNITCONV BCD*10.6 Unit Conversion

## OECRDDD - Credit/Debit Kitting Details (view OE0222)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; CRDUNIQ+DETAILNUM+COMPNUM
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
  LINENUM Integer Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Line Number
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
  QTY BCD*10.4 Kitting Quantity
  PRNQTYRET BCD*10.4 Parent Quantity Returned
  PRNUNIT String*10 Parent Unit of Measure
  PRNUNTCONV BCD*10.6 Parent Unit Conversion
  QTYRETURN BCD*10.4 Quantity Returned
  CRDUNIT String*10 Unit of Measure
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
  EXTCCOST BCD*10.3 Extended Order Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  GLNONSTKCR String*45 Non-stock Clearing Account
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRNWGTCONV BCD*10.6 Parent Weight Conversion Factor
  PRNUWEIGHT BCD*10.4 Parent Weight UOM Unit Weight
  PRNEXTWGHT BCD*10.4 Parent WUOM Extended Unit Weight
  DDTLNO String*6 Kit No.
  COG BCD*10.3 Cost of Goods
  COSTED Boolean Record Costed [0=No,1=Yes]
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]

## OECRDDDL - Credit/Debit Kitting Detail Lot Numbers (view OE0225)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+LOTNUMF; LOTNUMF+CRDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; CRDUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 Credit Note Uniquifier
  LINENUM Integer Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  INVSTKQTY BCD*10.4 Inv. Qty. in Stocking UOM
  COST BCD*10.3 Cost

## OECRDDDS - Credit/Debit Kitting Serial Nos (view OE0224)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+SERIALNUMF; SERIALNUMF+CRDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; CRDUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
  LINENUM Integer Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COST BCD*10.3 Cost

## OECRDDL - Credit/Debit Detail Lot Numbers (view OE0226)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM+LOTNUMF; LOTNUMF+CRDUNIQ+LINENUM; CRDUNIQ+DETAILNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 Credit Note Uniquifier
  LINENUM Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  INVSTKQTY BCD*10.4 Inv. Qty. in Stocking UOM
  COST BCD*10.3 Cost

## OECRDDO - Credit/Debit Detail Opt. Fields (view OE0221)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM+OPTFIELD; OPTFIELD+CRDUNIQ+LINENUM
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
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

## OECRDDS - Credit/Debit Detail Serial Nos (view OE0227)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+LINENUM+SERIALNUMF; SERIALNUMF+CRDUNIQ+LINENUM; CRDUNIQ+DETAILNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 Credit Note Uniquifier
  LINENUM Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COST BCD*10.3 Cost

## OECRDH - Credit/Debit Notes (view OE0240)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ; CRDNUMBER; ORDNUMBER+CRDNUMBER; INVNUMBER+CRDNUMBER; DAYENDNUM; CUSTOMER [D,M]; REFERENCE+CRDNUMBER [M]; CUSTOMER+CRDNUMBER [D,M]
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDNUMBER String*22 Order Number
  INVNUMBER String*22 Invoice Number
  CRDNUMBER String*22 Credit/Debit Note Number
  DAYENDNUM BCD*10.0 I/C Day End Trans. Number
  CUSTOMER String*12 Customer Number
  BILNAME String*60 Bill To
  BILADDR1 String*60 Bill-To Address 1
  BILADDR2 String*60 Bill-To Address 2
  BILADDR3 String*60 Bill-To Address 3
  BILADDR4 String*60 Bill-To Address 4
  BILCITY String*30 Bill-To City
  BILSTATE String*30 Bill-To State
  BILZIP String*20 Bill-To Zip Code
  BILCOUNTRY String*30 Bill-To Country
  BILPHONE String*30 Bill-To Phone
  BILFAX String*30 Bill-To Fax
  BILCONTACT String*60 Bill-To Contact
  CUSTDISC Integer Customer Discount Level [0=Base,1=A,2=B,3=C,4=D,5=E]
  PRICELIST String*6 Default Price List Code
  PONUMBER String*22 Purchase Order Number
  TERRITORY String*6 Territory
  REFERENCE String*60 Reference
  ORDDATE Date Order Date
  FOB String*60 Free On Board Point
  TEMPLATE String*6 Template Code
  LOCATION String*6 Default Location Code
  DESC String*60 Description
  COMMENT String*250 Comment
  SHIPDATE Date Shipment Date
  INVDATE Date Invoice Date
  INVFISCYR String*4 Invoice Fiscal Year
  INVFISCPER Integer Invoice Fiscal Period
  INHOMECURR String*3 Invoice Home Currency
  INRATETYPE String*2 Invoice Rate Type
  INSOURCURR String*3 Invoice Source Currency
  INRATEDATE Date Invoice Rate Date
  INRATE BCD*8.7 Invoice Rate
  INSPREAD BCD*8.7 Invoice Spread
  INDATEMTCH Integer Invoice Rate Date Matching
  INRATEREP Integer Invoice Rate Operator
  INRATEOVER Boolean Invoice Rate Override Flag
  CRDTOTAL BCD*10.3 CR Item Subtotal
  CRDMTOTAL BCD*10.3 CR Misc. Charges Subtotal
  RETDATE Date Return Date
  CRDDATE Date Credit/Debit Note Date
  CRDFISCYR String*4 Credit/Debit Note Fiscal Year
  CRDFISCPER Integer Credit/Debit Note Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  CRDLINES Integer No of Lines in Credit/Debit Note
  CRDWEIGHT BCD*10.4 Credit/Debit Note Tot Est Weight
  NEXTDTLNUM Integer Next Detail Number
  CRDSTATUS Integer Credit/Debit Note Status [1=Document shipped not costed,2=Document costed]
  CRDPRINTED Boolean Credit/Debit Note Printed [0=No,1=Yes]
  CDISONMISC Boolean CN/DN Discount on Misc. Charges
  POSTDATE Date Posting Date
  COMPDATE Date Completion Date
  CRDNETNOTX BCD*10.3 Credit/Debit Note Tot Before Tax
  CRDITAXTOT BCD*10.3 CN/DN Included Tax Total Amt
  CRDITMTOT BCD*10.3 Credit/Debit Note Item Total Amt
  CRDDISCBAS BCD*10.3 Credit/Debit Note Discount Base
  CRDDISCPER BCD*5.5 Credit/Debit Note Discount Percentage
  CRDDISCAMT BCD*10.3 Credit/Debit Note Discount Amt
  CRDMISC BCD*10.3 CN/DN Total Misc Charges
  CRDSUBTOT BCD*10.3 Credit/Debit Note Subtotal Amt
  CRDNET BCD*10.3 CN/DN Total With CN Discount
  CRDETAXTOT BCD*10.3 CN/DN Excluded Tax Total Amount
  CRDNETWTX BCD*10.3 Credit/Debit Note Total
  CRHOMECURR String*3 Credit/Debit Note Home Currency
  CRRATETYPE String*2 Credit/Debit Note Rate Type
  CRSOURCURR String*3 Credit/Debit Note Source Curr
  CRRATEDATE Date Credit/Debit Note Rate Date
  CRRATE BCD*8.7 Credit/Debit Note Rate
  CRSPREAD BCD*8.7 Credit/Debit Note Spread
  CRDATEMTCH Integer CN/DN Rate Date Matching
  CRRATEREP Integer Credit/Debit Note Rate Operator
  CRRATEOVER Boolean CN/DN Rate Override Flag
  SALESPER1 String*8 Salesperson 1
  SALESPER2 String*8 Salesperson 2
  SALESPER3 String*8 Salesperson 3
  SALESPER4 String*8 Salesperson 4
  SALESPER5 String*8 Salesperson 5
  SALESPLT1 BCD*5.5 Sales Percentage 1
  SALESPLT2 BCD*5.5 Sales Percentage 2
  SALESPLT3 BCD*5.5 Sales Percentage 3
  SALESPLT4 BCD*5.5 Sales Percentage 4
  SALESPLT5 BCD*5.5 Sales Percentage 5
  RECALCTAX Boolean Recalculate Tax
  TAXOVERRD Boolean Tax Overridden
  TAXGROUP String*12 Tax Group
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TEAMOUNT1 BCD*10.3 Excluded Tax Amount 1
  TEAMOUNT2 BCD*10.3 Excluded Tax Amount 2
  TEAMOUNT3 BCD*10.3 Excluded Tax Amount 3
  TEAMOUNT4 BCD*10.3 Excluded Tax Amount 4
  TEAMOUNT5 BCD*10.3 Excluded Tax Amount 5
  TIAMOUNT1 BCD*10.3 Included Tax Amount 1
  TIAMOUNT2 BCD*10.3 Included Tax Amount 2
  TIAMOUNT3 BCD*10.3 Included Tax Amount 3
  TIAMOUNT4 BCD*10.3 Included Tax Amount 4
  TIAMOUNT5 BCD*10.3 Included Tax Amount 5
  TEXEMPT1 String*20 Registration 1
  TEXEMPT2 String*20 Registration 2
  TEXEMPT3 String*20 Registration 3
  TEXEMPT4 String*20 Registration 4
  TEXEMPT5 String*20 Registration 5
  AUTOTAXCAL Boolean Auto-Tax Calculation Status
  BILEMAIL String*50 Bill-To E-mail
  BILPHONEC String*30 Bill-To Contact Phone
  BILFAXC String*30 Bill-To Contact Fax
  BILEMAILC String*50 Bill-To Contact E-mail
  ADJTYPE Integer Type [1=Credit Note,2=Debit Note]
  SHIPTRACK String*36 Shipment Tracking Number
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  SHIPTO String*6 Ship-To Location Code
  SHPNAME String*60 Ship-To Name
  SHPADDR1 String*60 Ship-To Address Line 1
  SHPADDR2 String*60 Ship-To Address Line 2
  SHPADDR3 String*60 Ship-To Address Line 3
  SHPADDR4 String*60 Ship-To Address Line 4
  SHPCITY String*30 Ship-To City
  SHPSTATE String*30 Ship-To State/Province
  SHPZIP String*20 Ship-To Zip/Postal Code
  SHPCOUNTRY String*30 Ship-To Country
  SHPPHONE String*30 Ship-To Phone Number
  SHPFAX String*30 Ship-To Fax Number
  SHPCONTACT String*60 Ship-To Contact
  SHPEMAIL String*50 Ship-To E-mail
  SHPPHONEC String*30 Ship-To Contact Phone
  SHPFAXC String*30 Ship-To Contact Fax
  SHPEMAILC String*50 Ship-To Contact E-mail
  VALUES Long Optional Fields
  INVUNIQ BCD*10.0 Invoice Uniquifier
  OVERCREDIT Boolean Over Credit Limit
  APPROVELMT BCD*10.3 Approved Limit
  APPROVEBY String*8 Authorizing User ID
  ITEMDISTOT BCD*10.3 Item Detail Discount Total
  MISCDISTOT BCD*10.3 Misc. Charge Detail Discount Tot
  CTRMETHOD Integer Auto-Calc. Tax Reporting Amounts
  CTRCURRNCY String*3 Tax Reporting (TR) Currency
  CTRRATTYPE String*2 TR Rate Type
  CTRRATDATE Date TR Rate Date
  CTRRATE BCD*8.7 TR Rate
  CTRSPREAD BCD*8.7 TR Spread
  CTRDATMTCH Integer TR Rate Date Matching
  CTRRATEOP Integer TR Rate Operator
  CTRRATOVER Boolean TR Rate Override Flag
  CTREAMNT1 BCD*10.3 TR Excluded Tax Amount 1
  CTREAMNT2 BCD*10.3 TR Excluded Tax Amount 2
  CTREAMNT3 BCD*10.3 TR Excluded Tax Amount 3
  CTREAMNT4 BCD*10.3 TR Excluded Tax Amount 4
  CTREAMNT5 BCD*10.3 TR Excluded Tax Amount 5
  CTRIAMNT1 BCD*10.3 TR Included Tax Amount 1
  CTRIAMNT2 BCD*10.3 TR Included Tax Amount 2
  CTRIAMNT3 BCD*10.3 TR Included Tax Amount 3
  CTRIAMNT4 BCD*10.3 TR Included Tax Amount 4
  CTRIAMNT5 BCD*10.3 TR Included Tax Amount 5
  ITRCURRNCY String*3 Tax Reporting Invoice (TR) Curr
  ITRRATTYPE String*2 TR Invoice Rate Type
  ITRRATDATE Date TR Invoice Rate Date
  ITRRATE BCD*8.7 TR Invoice Rate
  ITRSPREAD BCD*8.7 TR Invoice Spread
  ITRDATMTCH Integer TR Invoice Rate Date Matching
  ITRRATEOP Integer TR Invoice Rate Operator
  ITRRATOVER Boolean TR Invoice Rate Override Flag
  TAXVERSION Long Tax Version
  DISAMTOVER Boolean CN/DN Discount Amount Override
  JOBLINES Long Job Related Detail Lines
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percent
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  CUSACCTSET String*6 Customer Account Set
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date

## OECRDHO - Credit/Debit Note Opt. Fields (view OE0242)
Keys (first = PK; D=dups allowed, M=modifiable): CRDUNIQ+OPTFIELD; OPTFIELD+CRDUNIQ
Fields (NAME type description [values]):
  CRDUNIQ BCD*10.0 CN Uniquifier
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

## OEGLREF - G/L Reference Integration (view OE0272)
Keys (first = PK; D=dups allowed, M=modifiable): SOURCE+GLDEST
Fields (NAME type description [values]):
  SOURCE Integer Source Transaction Type [0=Shipment,1=Shipment Detail,2=Invoice,3=Invoice Detail,4=Credit/Debit Note,5=Credit/Debit Note Detail]
  GLDEST Integer G/L Transaction Field [0=G/L Entry Description]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SEPARATOR Integer Separator [0=* Asterisk,1=- Hyphen,2=/ Forward Slash,3=\ Back Slash,4=. Period,5=( Left Parenthesis,6=) Right Parenthesis,7=# Number Sign,8=Space]
  SEGMENT1 Integer Included Segment 1 [0=None,8=Contact Name,7=Customer Name,6=Customer Number,1=Day End Number,11=Description,3=Entry Number,9=Order Number,12=Reference,5=Shipment Number,13=Ship-To Location,14=Ship-Via,15=Ship-Via Description,2=Source Code]
  SEGMENT2 Integer Included Segment 2 [0=None,8=Contact Name,7=Customer Name,6=Customer Number,1=Day End Number,11=Description,3=Entry Number,9=Order Number,12=Reference,5=Shipment Number,13=Ship-To Location,14=Ship-Via,15=Ship-Via Description,2=Source Code]
  SEGMENT3 Integer Included Segment 3 [0=None,8=Contact Name,7=Customer Name,6=Customer Number,1=Day End Number,11=Description,3=Entry Number,9=Order Number,12=Reference,5=Shipment Number,13=Ship-To Location,14=Ship-Via,15=Ship-Via Description,2=Source Code]
  SEGMENT4 Integer Included Segment 4 [0=None,8=Contact Name,7=Customer Name,6=Customer Number,1=Day End Number,11=Description,3=Entry Number,9=Order Number,12=Reference,5=Shipment Number,13=Ship-To Location,14=Ship-Via,15=Ship-Via Description,2=Source Code]
  SEGMENT5 Integer Included Segment 5 [0=None,8=Contact Name,7=Customer Name,6=Customer Number,1=Day End Number,11=Description,3=Entry Number,9=Order Number,12=Reference,5=Shipment Number,13=Ship-To Location,14=Ship-Via,15=Ship-Via Description,2=Source Code]

## OEINPP - Invoice Prepayments (view OE0278)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUSTOMER String*12 Customer Number
  CUSTDESC String*60 Customer Name
  CUSTCURN String*3 Customer Currency
  CRATE BCD*8.7 Cust Rate
  CRATEDATE Date Cust Rate Date
  CRATETYPE String*2 Cust Rate Type
  CRATEOPER Integer Oper. Cust. Curn. to Func.
  DOCTOTAL BCD*10.3 Document Total
  DISCAVAIL BCD*10.3 Discount Available
  AMOUNTDUE BCD*10.3 Amount Due
  BATCHNUM BCD*5.0 Receipt Batch Number
  BANKCODE String*8 Bank Code
  RECPTYPE String*12 Receipt Type
  CHECKNUM String*24 Check/Receipt No.
  RECPDATE Date Receipt Date
  RECPAMOUNT BCD*10.3 Receipt Amount
  BANKCURN String*3 Bank Currency
  RATETYPE String*2 Rate Type
  BANKRATE BCD*8.7 Bank Rate
  RATEDATE Date Rate Date
  PAYMTYPE Integer Payment Type [0=(None),1=Cash,2=Check,3=Credit Card,4=Other,5=SPS Credit Card]
  PAUTHCURR String*3 Pre-auth Currency
  TRANIDPRE String*36 Pre-auth Transaction ID
  TRANIDCAP String*36 Capture Transaction ID
  TRANIDVOID String*36 Void Transaction ID
  PAUTHAMT BCD*10.3 Pre-auth Amount
  CHARGESTTS Integer Credit Card Charge Status [0=None,1=Charged,2=Voided,3=Pending,4=Card Declined,5=Card Error]
  YPPROCCODE String*12 YP Process Code

## OEINTL - Invoice Lot For DEP (view OE0310)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+LOTNUMF
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  DETAILNUM Integer Detail Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STKQTY BCD*10.4 Delta Quantity in Stocking UOM
  QTY BCD*10.4 Delta Quantity
  COST BCD*10.3 Cost

## OEINTS - Invoice Serial For DEP (view OE0313)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+SERIALNUMF
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  DETAILNUM Integer Detail Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation
  COST BCD*10.3 Cost

## OEINVD - Invoice Details (view OE0400)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM; INVUNIQ+DETAILNUM; SHINUMBER+SHIDTLNUM+INVUNIQ+DETAILNUM; ORDNUMBER+ORDDTLNUM+INVUNIQ+DETAILNUM [M]
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Line Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LINETYPE Integer Line Type [1=Item,2=Miscellaneous]
  ITEM String*24 Item
  MISCCHARGE String*6 Miscellaneous Charges Code
  DESC String*60 Description
  ACCTSET String*6 Item Account Set
  USERCOSTMD Boolean User-Specified Costing Method
  PRICELIST String*6 Price List
  CATEGORY String*6 Category
  LOCATION String*6 Location
  PICKSEQ String*10 Picking Sequence
  EXPDATE Date Shipment Date
  STOCKITEM Boolean Stock Item
  QTYORDERED BCD*10.4 Current Quantity Outstanding
  QTYSHIPPED BCD*10.4 Quantity Shipped
  QTYBACKORD BCD*10.4 Quantity Backordered
  INVUNIT String*10 Invoice Unit of Measure
  UNITCONV BCD*10.6 Unit Conversion
  UNITPRICE BCD*10.6 Unit Price
  PRICEOVER Boolean Price Override
  UNITCOST BCD*10.6 Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  UNITPRCDEC Integer Unit Price No. of Decimals
  PRICEUNIT String*10 Pricing Unit
  PRIUNTPRC BCD*10.6 Pricing Unit Price
  PRIUNTCONV BCD*10.6 Pricing Unit Conversion
  PRIPERCENT BCD*5.5 Price Discount Percentage
  PRIAMOUNT BCD*10.3 Price Discount Amount
  BASEUNIT String*10 Pricing Base Unit
  PRIBASPRC BCD*10.6 Pricing Base Unit Price
  PRIBASCONV BCD*10.6 Pricing Base Unit Conversion
  COSTUNIT String*10 Costing Unit
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTICOST BCD*10.3 Extended Detail Cost
  EXTINVMISC BCD*10.3 Extended Shipped Price/Misc. Charges Amount
  INVDISC BCD*10.3 Invoice Discount Amount
  EXTOVER Boolean Extended Amount Override
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TAMOUNT1 BCD*10.3 Tax Amount 1
  TAMOUNT2 BCD*10.3 Tax Amount 2
  TAMOUNT3 BCD*10.3 Tax Amount 3
  TAMOUNT4 BCD*10.3 Tax Amount 4
  TAMOUNT5 BCD*10.3 Tax Amount 5
  TRATE1 BCD*8.5 Tax Rate 1
  TRATE2 BCD*8.5 Tax Rate 2
  TRATE3 BCD*8.5 Tax Rate 3
  TRATE4 BCD*8.5 Tax Rate 4
  TRATE5 BCD*8.5 Tax Rate 5
  DETAILNUM Integer Detail Number
  COMMINST Boolean Have Comments/Instructions [0=No,1=Yes]
  GLNONSTKCR String*45 Non-stock Clearing Account
  AVGCOST BCD*10.6 Average Unit Cost
  LASTCOST BCD*10.6 Last Unit Cost
  SHINUMBER String*22 Shipment Number
  SHIDTLNUM Integer Shipment Detail Line Number
  SHIPTRACK String*36 Shipment Tracking Number
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  DISCPER BCD*5.5 Discount Percent
  ORDQTYORD BCD*10.4 Order Quantity Ordered
  ORDQTYBKOR BCD*10.4 Order Quantity Backordered
  ORDQTYCOMM BCD*10.4 Order Quantity Committed
  ORDQTYTCOM BCD*10.4 Order Quantity True Committed
  ORDQTYSTD BCD*10.4 Order Quantity Shipped-to-date
  ORDUNIT String*10 Order Unit of Measure
  ORDUNITCON BCD*10.6 Order Unit Conversion
  MANITEMNO String*24 Manufacturer's Item Number
  CUSTITEMNO String*24 Customer Item Number
  QTYCOMMIT BCD*10.4 Quantity Committed
  QTYTRUECOM BCD*10.4 Quantity True Committed
  ORDNUMBER String*22 Order Number
  ORDDTLNUM Integer Order Detail Number
  REFRESH Boolean Refresh Order Qty. at Update [0=No,1=Yes]
  ORIGQTYSHP BCD*10.4 Original Quantity shipped
  VALUES Long Optional Fields
  DDTLTYPE Integer Kitting/BOM [0=None,1=Kitting,2=BOM]
  DDTLNO String*6 Kit/BOM Number
  BUILDQTY BCD*10.4 BOM Build Qty.
  BUILDUNIT String*10 BOM Build Unit
  BLDUNTCONV BCD*10.6 BOM Build Unit Conversion
  EPOSPROMID Integer ePOS Promotion ID
  TERMDISCBL Integer Subject to Payment Discount [0=No,1=Yes]
  BASEWUNIT String*10 Pricing Base Weight Unit
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRWGHTUNIT String*10 Pricing Weight UOM
  PRWGHTCONV BCD*10.6 Pricing Weight Conversion Factor
  PRIBASWCNV BCD*10.6 Pricing Base Weight Conv. Factor
  DEFUWEIGHT BCD*10.4 Def. Weight UOM Unit Weight
  DEFEXTWGHT BCD*10.4 Def. Weight UOM Ext. Unit Weight
  PRPRICEBY Integer Price By [1=Quantity,2=Weight]
  NEEDPCHECK Boolean Price Check Pending
  CAPPROVEBY String*8 Price Approved By
  HDRDISC BCD*10.3 Header Discount
  ITRAMOUNT1 BCD*10.3 TR Tax Amount 1
  ITRAMOUNT2 BCD*10.3 TR Tax Amount 2
  ITRAMOUNT3 BCD*10.3 TR Tax Amount 3
  ITRAMOUNT4 BCD*10.3 TR Tax Amount 4
  ITRAMOUNT5 BCD*10.3 TR Tax Amount 5
  COG BCD*10.3 Cost of Goods
  COSTED Boolean Record Costed [0=No,1=Yes]
  JOBRELATED Boolean Job Related
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
  RTGDATEDUE Date Retainage Due Date
  RTGDDTOVR Boolean Retainage Due Date Override
  RTGAMTOVR Boolean Retainage Amount Override
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  PRICEOPT Integer Default O/E Price [0=,1=Billing Rate,2=Use Customer Price List,3=Use Specified Price List]
  PAYMNTDIST BCD*10.3 Prepayment Distributed
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]
  COMPANYID Long Sage CRM Company ID
  OPPOID Long Sage CRM Opportunity ID
  EDN String*30 Export Declaration Number

## OEINVDB - Invoice BOM Details (view OE0403)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM+PRNCOMPNUM+COMPNUM
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Detail Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPONENT String*24 Component Item No.
  DESC String*60 Description
  QTY BCD*10.4 Component Quantity
  UNIT String*10 Unit of Measure
  QTYSHIPPED BCD*10.4 Quantity Shipped
  DDTLNO String*6 Component's BOM Number
  BUILDQTY BCD*10.4 Component's BOM Build Qty.
  BUILDUNIT String*10 Component's BOM Build Unit
  BLDUNTCONV BCD*10.6 Component's BOM Build Unit Conv.
  UNITCONV BCD*10.6 Unit Conversion

## OEINVDD - Invoice Kitting Details (view OE0402)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; INVUNIQ+LINENUM+COMPNUM; INVUNIQ+DETAILNUM+COMPNUM
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Detail Line Number
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
  QTY BCD*10.4 Kitting Quantity
  PRNQTYSHIP BCD*10.4 Parent Quantity Shipped
  PRNUNIT String*10 Parent Unit of Measure
  PRNUNTCONV BCD*10.6 Parent Unit Conversion
  QTYSHIPPED BCD*10.4 Quantity Shipped
  INVUNIT String*10 Invoice Unit of Measure
  UNITCONV BCD*10.6 Invoice Unit Conversion
  UNITCOST BCD*10.6 Invoice Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  AVGCOST BCD*10.6 Average Unit Cost
  LASTCOST BCD*10.6 Last Unit Cost
  COSTUNIT String*10 Costing Unit of Measure
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTICOST BCD*10.3 Extended Invoice Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  GLNONSTKCR String*45 Non-stock Clearing Account
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRNWGTCONV BCD*10.6 Parent Weight Conversion Factor
  PRNUWEIGHT BCD*10.4 Parent Weight UOM Unit Weight
  PRNEXTWGHT BCD*10.4 Parent WUOM Extended Unit Weight
  DDTLNO String*6 Kit No.
  COG BCD*10.3 Cost of Goods
  COSTED Boolean Record Costed [0=No,1=Yes]
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]

## OEINVDDL - Invoice Kitting Detail Lot Numbers (view OE0405)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+LOTNUMF; LOTNUMF+INVUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; INVUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  COST BCD*10.3 Cost

## OEINVDDS - Invoice Kitting Serial Numbers (view OE0404)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+SERIALNUMF; SERIALNUMF+INVUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; INVUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Detail Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COST BCD*10.3 Cost

## OEINVDL - Invoice Detail Lot Numbers (view OE0406)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM+LOTNUMF; LOTNUMF+INVUNIQ+LINENUM; INVUNIQ+DETAILNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  COST BCD*10.3 Cost

## OEINVDO - Invoice Detail Optional Fields (view OE0401)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM+OPTFIELD; OPTFIELD+INVUNIQ+LINENUM
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Line Uniquifier
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

## OEINVDS - Invoice Detail Serial Numbers (view OE0407)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM+SERIALNUMF; SERIALNUMF+INVUNIQ+LINENUM; INVUNIQ+DETAILNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COST BCD*10.3 Cost

## OEINVH - Invoices (view OE0420)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ; ORDNUMBER+INVNUMBER; DAYENDNUM; CUSTOMER [D,M]; CUSTOMER+INVNUMBER; REFERENCE+INVNUMBER [M]; INVNUMBER; SHINUMBER+INVNUMBER
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDNUMBER String*22 Order Number
  DAYENDNUM BCD*10.0 I/C Day End Trans. Number
  CUSTOMER String*12 Customer Number
  BILNAME String*60 Bill To
  BILADDR1 String*60 Bill-To Address 1
  BILADDR2 String*60 Bill-To Address 2
  BILADDR3 String*60 Bill-To Address 3
  BILADDR4 String*60 Bill-To Address 4
  BILCITY String*30 Bill-To City
  BILSTATE String*30 Bill-To State
  BILZIP String*20 Bill-To Zip Code
  BILCOUNTRY String*30 Bill-To Country
  BILPHONE String*30 Bill-To Phone
  BILFAX String*30 Bill-To Fax
  BILCONTACT String*60 Bill-To Contact
  SHIPTO String*6 Ship to Address Code
  SHPNAME String*60 Ship To
  SHPADDR1 String*60 Ship-To Address 1
  SHPADDR2 String*60 Ship-To Address 2
  SHPADDR3 String*60 Ship-To Address 3
  SHPADDR4 String*60 Ship-To Address 4
  SHPCITY String*30 Ship-To City
  SHPSTATE String*30 Ship-To State
  SHPZIP String*20 Ship-To Zip Code
  SHPCOUNTRY String*30 Ship-To Country
  SHPPHONE String*30 Ship-To Phone
  SHPFAX String*30 Ship-To Fax
  SHPCONTACT String*60 Ship-To Contact
  CUSTDISC Integer Customer Discount Level [0=Base,1=A,2=B,3=C,4=D,5=E]
  PRICELIST String*6 Price List Code
  PONUMBER String*22 Purchase Order Number
  TERRITORY String*6 Territory
  TERMS String*6 Terms Code
  TERMTTLDUE BCD*10.3 Total Terms Amount Due
  TERMOVERRD Boolean Terms Rate Override
  REFERENCE String*60 Reference
  ORDDATE Date Order Date
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  FOB String*60 Free On Board Point
  TEMPLATE String*6 Template Code
  LOCATION String*6 Location
  DESC String*60 Description
  COMMENT String*250 Comment
  SHIPDATE Date Shipment Date
  INVDATE Date Invoice Date
  INVFISCYR String*4 Invoice Fiscal Year
  INVFISCPER Integer Invoice Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  INVLINES Integer Number of Lines in Invoice
  NUMLABELS Integer Number of Labels
  NUMPAYMENT BCD*3.0 Number of Terms Payments
  PAYMNTASOF Date Terms Payments As Of Date
  INVWEIGHT BCD*10.4 Invoice Total Estimated Weight
  NEXTDTLNUM Integer Next Detail Number
  INVSTATUS Integer Invoice Status [1=Document shipped not costed,2=Document costed]
  INVPRINTED Boolean Invoice Printed [0=No,1=Yes]
  IDISONMISC Boolean Invoice Disc. on Misc. Charges
  POSTDATE Date Posting Date
  COMPDATE Date Completion Date
  SHIPLABEL Boolean Requires Shipping Labels
  LBLPRINTED Boolean Shipping Labels Printed
  INVNETNOTX BCD*10.3 Invoice Total Before Tax
  INVITAXTOT BCD*10.3 Invoice Included Tax Tot. Amount
  INVITMTOT BCD*10.3 Invoice Item Total Amount
  INVDISCBAS BCD*10.3 Invoice Discount Base
  INVDISCPER BCD*5.5 Invoice Discount Percentage
  INVDISCAMT BCD*10.3 Invoice Discount Amount
  INVMISC BCD*10.3 Invoice Total Misc. Charges
  INVSUBTOT BCD*10.3 Invoice Subtotal Amount
  INVNET BCD*10.3 Invoice Total With Invoice Disc.
  INVETAXTOT BCD*10.3 Invoice Excluded Tax Tot. Amount
  INVNETWTX BCD*10.3 Invoice Total With Tax
  INHOMECURR String*3 Invoice Home Currency
  INRATETYPE String*2 Invoice Rate Type
  INSOURCURR String*3 Invoice Source Currency
  INRATEDATE Date Invoice Rate Date
  INRATE BCD*8.7 Invoice Rate
  INSPREAD BCD*8.7 Invoice Spread
  INDATEMTCH Integer Invoice Rate Date Matching
  INRATEREP Integer Invoice Rate Operator
  INRATEOVER Boolean Invoice Rate Override Flag
  SALESPER1 String*8 Salesperson 1
  SALESPER2 String*8 Salesperson 2
  SALESPER3 String*8 Salesperson 3
  SALESPER4 String*8 Salesperson 4
  SALESPER5 String*8 Salesperson 5
  SALESPLT1 BCD*5.5 Sales Percentage 1
  SALESPLT2 BCD*5.5 Sales Percentage 2
  SALESPLT3 BCD*5.5 Sales Percentage 3
  SALESPLT4 BCD*5.5 Sales Percentage 4
  SALESPLT5 BCD*5.5 Sales Percentage 5
  TAXOVERRD Boolean Tax Overridden
  TAXGROUP String*12 Tax Group
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TEAMOUNT1 BCD*10.3 Excluded Tax Amount 1
  TEAMOUNT2 BCD*10.3 Excluded Tax Amount 2
  TEAMOUNT3 BCD*10.3 Excluded Tax Amount 3
  TEAMOUNT4 BCD*10.3 Excluded Tax Amount 4
  TEAMOUNT5 BCD*10.3 Excluded Tax Amount 5
  TIAMOUNT1 BCD*10.3 Included Tax Amount 1
  TIAMOUNT2 BCD*10.3 Included Tax Amount 2
  TIAMOUNT3 BCD*10.3 Included Tax Amount 3
  TIAMOUNT4 BCD*10.3 Included Tax Amount 4
  TIAMOUNT5 BCD*10.3 Included Tax Amount 5
  TEXEMPT1 String*20 Registration 1
  TEXEMPT2 String*20 Registration 2
  TEXEMPT3 String*20 Registration 3
  TEXEMPT4 String*20 Registration 4
  TEXEMPT5 String*20 Registration 5
  AUTOTAXCAL Boolean Auto-Tax Calculation Status
  BILEMAIL String*50 Bill-To E-mail
  BILPHONEC String*30 Bill-To Contact Phone
  BILFAXC String*30 Bill-To Contact Fax
  BILEMAILC String*50 Bill-To Contact E-mail
  SHPEMAIL String*50 Ship-To E-mail
  SHPPHONEC String*30 Ship-To Contact Phone
  SHPFAXC String*30 Ship-To Contact Fax
  SHPEMAILC String*50 Ship-To Contact E-mail
  RECALCTAX Boolean Recalculate Tax
  DISCAVAIL BCD*10.3 Discount Available
  SHHOMECURR String*3 Shipment Home Currency
  SHRATETYPE String*2 Shipment Rate Type
  SHSOURCURR String*3 Shipment Source Currency
  SHRATEDATE Date Shipment Rate Date
  SHRATE BCD*8.7 Shipment Rate
  SHSPREAD BCD*8.7 Shipment Spread
  SHDATEMTCH Integer Shipment Rate Date Matching
  SHRATEREP Integer Shipment Rate Operator
  SHRATEOVER Boolean Shipment Rate Override Flag
  SHINUMBER String*22 Shipment Number
  MULTISHI Boolean Generate From Multiple Shipments [0=No,1=Yes]
  SHIS Integer From How Many Shipments
  INVNUMBER String*22 Invoice Number
  SHIPTRACK String*36 Shipment Tracking Number
  OVERCREDIT Boolean Over Credit Limit
  APPROVELMT BCD*10.3 Approved Limit
  APPROVEBY String*8 Authorizing User ID
  VALUES Long Optional Fields
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  TERMDBWT BCD*10.3 Document Discount Base With Tax
  TERMDBNT BCD*10.3 Document Discount Base w/o Tax
  ITEMDISTOT BCD*10.3 Item Detail Discount Total
  MISCDISTOT BCD*10.3 Misc. Charge Detail Discount Total
  ITRMETHOD Integer Auto-Calc. Tax Reporting Amounts
  ITRCURRNCY String*3 Tax Reporting (TR) Currency
  ITRRATTYPE String*2 TR Rate Type
  ITRRATDATE Date TR Rate Date
  ITRRATE BCD*8.7 TR Rate
  ITRSPREAD BCD*8.7 TR Spread
  ITRDATMTCH Integer TR Rate Date Matching
  ITRRATEOP Integer TR Rate Operator
  ITRRATOVER Boolean TR Rate Override Flag
  ITREAMNT1 BCD*10.3 TR Excluded Tax Amount 1
  ITREAMNT2 BCD*10.3 TR Excluded Tax Amount 2
  ITREAMNT3 BCD*10.3 TR Excluded Tax Amount 3
  ITREAMNT4 BCD*10.3 TR Excluded Tax Amount 4
  ITREAMNT5 BCD*10.3 TR Excluded Tax Amount 5
  ITRIAMNT1 BCD*10.3 TR Included Tax Amount 1
  ITRIAMNT2 BCD*10.3 TR Included Tax Amount 2
  ITRIAMNT3 BCD*10.3 TR Included Tax Amount 3
  ITRIAMNT4 BCD*10.3 TR Included Tax Amount 4
  ITRIAMNT5 BCD*10.3 TR Included Tax Amount 5
  STRCURRNCY String*3 Tax Reporting Shipment (TR) Currency
  STRRATTYPE String*2 TR Shipment Rate Type
  STRRATDATE Date TR Shipment Rate Date
  STRRATE BCD*8.7 TR Shipment Rate
  STRSPREAD BCD*8.7 TR Shipment Spread
  STRDATMTCH Integer TR Shipment Rate Date Matching
  STRRATEOP Integer TR Shipment Rate Operator
  STRRATOVER Boolean TR Shipment Rate Override Flag
  TAXVERSION Long Tax Version
  DISAMTOVER Boolean Invoice Discount Amount Override
  JOBLINES Long Job Related Detail Lines
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGTERMS String*6 Retainage Terms
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percent
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  CUSACCTSET String*6 Customer Account Set
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  OPPOLINES Integer Sage CRM Opportunity Lines
  EDN String*30 Export Declaration Number
  SFPAURL String*100 Payments Acceptance URL
  SFPAID String*36 Payments Acceptance ID

## OEINVHO - Invoice Optional Fields (view OE0422)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+OPTFIELD; OPTFIELD+INVUNIQ
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
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

## OEINVR - Multiple Shipments to Invoice (view OE0427)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+LINENUM; INVUNIQ+SHIUNIQ; SHIUNIQ [D]
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  SHINUMBER String*22 Shipment Number
  PONUMBER String*22 PO Number

## OEMISC - Miscellaneous Charges (view OE0440)
Keys (first = PK; D=dups allowed, M=modifiable): CURRENCY+MISCCHARGE; MISCCHARGE [D,M]
Fields (NAME type description [values]):
  CURRENCY String*3 Currency
  MISCCHARGE String*6 Miscellaneous Charge Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  MISCACCT String*45 Misc. Charge Revenue Account
  AMOUNT BCD*10.3 Amount
  VALUES Long Optional Fields
  HASJOB Boolean Job Related [0=No,1=Yes]
  EXTCOST BCD*10.3 Extended Cost
  MCCOSTEXP String*45 Misc. Charge Expense Account
  MCCLEARING String*45 Misc. Charge Clearing Account
  TARIFFCODE String*20 Tariff Code

## OEMISCO - Misc. Charge Optional Fields (view OE0450)
Keys (first = PK; D=dups allowed, M=modifiable): CURRENCY+MISCCHARGE+OPTFIELD; OPTFIELD+CURRENCY+MISCCHARGE
Fields (NAME type description [values]):
  CURRENCY String*3 Currency
  MISCCHARGE String*6 Miscellaneous Charge Code
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

## OEMISCT - Miscellaneous Charge Taxes (view OE0460)
Keys (first = PK; D=dups allowed, M=modifiable): CURRENCY+MISCCHARGE+AUTHORITY
Fields (NAME type description [values]):
  CURRENCY String*3 Currency
  MISCCHARGE String*6 Miscellaneous Charge Code
  AUTHORITY String*12 Authority
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TAXCLASS Integer Sales Tax Class

## OEMSG - E-mail Messages (view OE0465)
Keys (first = PK; D=dups allowed, M=modifiable): MSGTYPE+MSGID
Fields (NAME type description [values]):
  MSGTYPE Integer Message Type [0=Order Confirmation,1=Quote,2=Invoice,3=Credit/Debit Note]
  MSGID String*16 Message ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TEXTDESC String*60 Description
  ACTIVESW Boolean Status [0=Inactive,1=Active]
  DATEINAC Date Inactive Date
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

## OEOFD - Optional Fields (view OE0470)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Miscellaneous Charges,1=Orders,2=Order Details,3=Shipments,4=Shipment Details,5=Invoices,6=Invoice Details,7=Credit/Debit Notes,8=Credit/Debit Note Details]
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
  SWICCTL Integer Inventory Control [99=Not Applicable]
  SWSHCLRSH Integer Shipment Clearing [99=Not Applicable]
  SWNSCLR Integer Non-stock Clearing [99=Not Applicable]
  SWCV Integer Cost Variance [99=Not Applicable]
  SWARINV Integer A/R Invoices Optional Fields [99=Not Applicable]
  SWSALES Integer Sales/Shipment Clearing/COGS [99=Not Applicable]
  SWMISC Integer Miscellaneous Charges [99=Not Applicable]
  SWRETURN Integer Returns [99=Not Applicable]
  SWDAMAGE Integer Damaged Goods [99=Not Applicable]
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]
  SWPM Integer External Cost Transactions [99=Not Applicable]
  SWPMLABOR Integer Labor [99=Not Applicable]
  SWPMOH Integer Overhead [99=Not Applicable]
  SWCNDNCLR Integer Credit/Debit Note Clearing [99=Not Applicable]

## OEOFH - Optional Field Locations (view OE0475)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Miscellaneous Charges,1=Orders,2=Order Details,3=Shipments,4=Shipment Details,5=Invoices,6=Invoice Details,7=Credit/Debit Notes,8=Credit/Debit Note Details]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## OEOPT - O/E Options (view OE0480)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PHONE String*30 Phone
  FAX String*30 Fax
  CONTACT String*60 Contact Name
  DAYEND Boolean Day End Pending
  DIRECT Boolean Direct Printing on Invoices
  ORDHIST Boolean Keep Order History
  COMMISSION Boolean Track Commissions
  COMMTYPE Integer Commission Type [1=Sales,2=Margin]
  BACKORD Boolean Calculate Backorder Quantities
  ALLOWSHIP Boolean Allow Qty Shipped on Orders
  STATACCUM Boolean Accumulate Statistics
  STATEDIT Boolean Allow Edit Statistics
  STATCLNDR Integer Accumulate Statistics By [1=Calendar Year,2=Fiscal Year]
  STATPRD Integer Statistics Period By [1=Weekly,2=Seven Days,3=Bi-weekly,4=Four Weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Annually,10=Fiscal Period]
  AGING1 Integer Aging Period 1
  AGING2 Integer Aging Period 2
  AGING3 Integer Aging Period 3
  RATETYPE String*2 Default Rate Type
  TRANHIST Boolean Accumulate Sales History
  TRANCLNDR Integer Accumulate Sales History By [1=Calendar Year,2=Fiscal Year]
  TRANPRD Integer Sales History Period By [1=Weekly,2=Seven Days,3=Bi-weekly,4=Four Weeks,5=Monthly,6=Bi-monthly,7=Quarterly,8=Semi-annually,9=Annually,10=Fiscal Period]
  DEFTEMP String*6 Default Template Code
  ORDNUMBERL Integer Order Number Length
  ORDPREFIXD String*6 Order Number Prefix
  ORDBODYD String*22 Next Order Number
  NEXTOUNIQ BCD*10.0 Next Order Uniquifier Key
  INVNUMBERL Integer Invoice Number Length
  INVPREFIXD String*6 Invoice Number Prefix
  INVBODYD String*22 Next Invoice Number
  CRDNUMBERL Integer Credit Note Number Length
  CRDPREFIXD String*6 Credit Note Number Prefix
  CRDBODYD String*22 Next Credit Note Number
  NEXTCUNIQ BCD*10.0 Next Credit Note Uniquifier Key
  BROWSENUM BCD*10.0 Day End Browse Number
  QUONUMBERL Integer Quote Number Length
  QUOPREFIXD String*6 Quote Number Prefix
  QUOBODYD String*22 Next Quote Number
  UOMBY Integer Default Order UOM [1=Stocking Unit,2=Pricing Unit]
  NONCUST Boolean Allow post to non-exist customer
  QUOEXPIRE Integer Default quote expiring days
  DBNNUMBERL Integer Debit Note Number Length
  DBNPREFIXD String*6 Debit Note Number Prefix
  DBNBODYD String*22 Next Debit Note Number
  NEXTIUNIQ BCD*10.0 Next Invoice Uniquifier Key
  SHINUMBERL Integer Shipment Number Length
  SHIPREFIXD String*6 Shipment Number Prefix
  SHIBODYD String*22 Next Shipment Number
  NEXTSUNIQ BCD*10.0 Next Shipment Uniquifier Key
  DEFERGLPST Boolean Deferred G/L Posting
  GLDAYEND Long G/L Trans Created Thru Day End
  APPENDGL Integer Append To G/L Batch [1=Adding to an Existing Batch,0=Creating a New Batch,2=Creating and Posting a New Batch]
  CONSOLGL Integer Consolidate G/L Batch [1=Do Not Consolidate,9=Consolidate Transaction Details by Account,2=Consolidate by Account and Fiscal Period,3=Consolidate by Account, Fiscal Period, and Source]
  REFCHOICE Integer G/L Reference Field [1=Document Number,2=Reference Number,3=Source Code/Day End Number/Entry Number,4=Header Description,5=Customer/Vendor Number,6=Customer/Vendor Name]
  DESCCHOICE Integer G/L Description Field [1=Document Number,2=Reference Number,3=Source Code/Day End Number/Entry Number,4=Header Description,5=Customer/Vendor Number,6=Customer/Vendor Name]
  DEFQCOMMIT Boolean Default Qty. Ordered to Committed?
  CREATEINV Boolean Create Invoice When Qty. Shipped? [0=No,1=Yes]
  INCREDITED Integer Apply CN to invoice that was credited. [0=Ignore,1=Warning,2=Error]
  INCARPEND Boolean Include Pending A/R Transactions in Credit Limit Check
  INCOEPEND Boolean Include Pending O/E Transactions in Credit Limit Check
  INCXXPEND Boolean Include Other Pending Transactions in Credit Limit Check
  TAXREPCALC Integer Tax Reporting Calculation Method
  WUOMBY Integer Default Order Weight UOM [1=Item Weight Unit,2=Pricing Weight Unit]
  DEFERARPST Integer Deferred A/R Posting. [0=During Day End Processing,1=On Request Using Create Batch Icon]
  SRCTYPESH String*2 O/E Shipments
  SRCTYPEIN String*2 O/E Invoices
  SRCTYPECN String*2 O/E Credit Notes
  SRCTYPEDN String*2 O/E Debit Notes
  SRCTYPECO String*2 O/E Consolidated Entry
  DATEBUSDFT Integer Default Posting Date [1=Document Date,2=Session Date]
  PURGEEXPQT Boolean Clear Expired Quotes [0=No,1=Yes]
  QTPURGEDAY Integer Clear Expired Quotes Days

## OEORDD - Order Details (view OE0500)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM; ORDUNIQ+DETAILNUM; ITEM+EXPDATE+ORDUNIQ+DETAILNUM [M]; EXPDATE+DDTLTYPE+QTYORDERED+QTYBACKORD+ITEM+LOCATION [D,M]; EXPDATE+DDTLTYPE+QTYCOMMIT+ITEM+LOCATION [D,M]; ITEM+DDTLTYPE+EXPDATE+LOCATION+LINETYPE+COMPLETE [D,M]; ORDUNIQ+ITEM+DDTLTYPE+EXPDATE+LOCATION+LINETYPE+COMPLETE [D,M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LINETYPE Integer Line Type [1=Item,2=Miscellaneous]
  ITEM String*24 Item
  MISCCHARGE String*6 Miscellaneous Charges Code
  DESC String*60 Description
  ACCTSET String*6 Item Account Set
  USERCOSTMD Boolean User-Specified Costing Method
  PRICELIST String*6 Price List
  CATEGORY String*6 Category
  LOCATION String*6 Location
  PICKSEQ String*10 Picking Sequence
  EXPDATE Date Expected Shipment Date
  STOCKITEM Boolean Stock Item
  QTYORDERED BCD*10.4 Quantity Ordered
  QTYSHIPPED BCD*10.4 Quantity Shipped
  QTYBACKORD BCD*10.4 Quantity Backordered
  QTYSHPTODT BCD*10.4 Quantity Shipped-to-date
  ORIGQTY BCD*10.4 Original Quantity Ordered
  QTYPO BCD*10.4 P/O Quantity Ordered
  ORDUNIT String*10 Order Unit of Measure
  UNITCONV BCD*10.6 Order Unit Conversion
  UNITPRICE BCD*10.6 Order Unit Price
  PRICEOVER Boolean Price Override [0=No,1=Yes]
  UNITCOST BCD*10.6 Order Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  UNITPRCDEC Integer Unit Price No. of Decimals
  PRICEUNIT String*10 Pricing Unit of Measure
  PRIUNTPRC BCD*10.6 Pricing Unit Price
  PRIUNTCONV BCD*10.6 Pricing Unit Conversion
  PRIPERCENT BCD*5.5 Price Discount Percentage
  PRIAMOUNT BCD*10.3 Price Discount Amount
  BASEUNIT String*10 Pricing Base Unit
  PRIBASPRC BCD*10.6 Pricing Base Unit Price
  PRIBASCONV BCD*10.6 Pricing Base Unit Conversion
  COSTUNIT String*10 Costing Unit of Measure
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTOPRICE BCD*10.3 Extended Order Amount
  EXTOCOST BCD*10.3 Extended Order Cost
  EXTINVMISC BCD*10.3 Extended Amount
  INVDISC BCD*10.3 Order Discount Amount
  EXTICOST BCD*10.3 Extended Detail Cost
  EXTOVER Boolean Extended Shipped Amt. Override
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  COMPLETE Integer Detail Completed [0=Not completed,1=Completed/Not In Database,2=Completed,3=Processed by day end]
  ADDTOILOC Boolean Recognized In Item/Location
  SALESLOST BCD*10.3 Lost Sales Amount
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TAMOUNT1 BCD*10.3 Tax Amount 1
  TAMOUNT2 BCD*10.3 Tax Amount 2
  TAMOUNT3 BCD*10.3 Tax Amount 3
  TAMOUNT4 BCD*10.3 Tax Amount 4
  TAMOUNT5 BCD*10.3 Tax Amount 5
  TRATE1 BCD*8.5 Tax Rate 1
  TRATE2 BCD*8.5 Tax Rate 2
  TRATE3 BCD*8.5 Tax Rate 3
  TRATE4 BCD*8.5 Tax Rate 4
  TRATE5 BCD*8.5 Tax Rate 5
  DETAILNUM Integer Detail Number
  COMMINST Boolean Use Comments/Instructions [0=No,1=Yes]
  GLNONSTKCR String*45 Non-stock Clearing Account
  AVGCOST BCD*10.6 Average Unit Cost
  LASTCOST BCD*10.6 Last Unit Cost
  COPYDETAIL Boolean Copy This Detail Line [0=No,1=Yes]
  QUONUMBER String*22 Quote Number
  QUODTLNUM Integer Quote Detail Line Number
  SHIPTRACK String*36 Shipment Tracking Number
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  DISCPER BCD*5.5 Discount Percent
  QTYCOMMIT BCD*10.4 Quantity Committed
  MANITEMNO String*24 Manufacturer's Item Number
  CUSTITEMNO String*24 Customer Item Number
  QTYTRUECOM BCD*10.4 True Quantity Committed
  VALUES Long Optional Fields
  DDTLTYPE Integer Kitting/BOM [0=None,1=Kitting,2=BOM]
  DDTLNO String*6 Kit/BOM Number
  BUILDQTY BCD*10.4 BOM Build Qty.
  BUILDUNIT String*10 BOM Build Unit
  BLDUNTCONV BCD*10.6 BOM Build Unit Conversion
  FRMNUMBER String*22 Predecessor Number
  NEXTCMPNUM Long Next Component Number
  EPOSPROMID Integer ePOS Promotion ID
  BASEWUNIT String*10 Pricing Base Weight Unit
  WEIGHTUNIT String*10 Order Weight UOM
  WEIGHTCONV BCD*10.6 Order Weight Conversion Factor
  PRWGHTUNIT String*10 Pricing Weight UOM
  PRWGHTCONV BCD*10.6 Pricing Weight Conversion Factor
  PRIBASWCNV BCD*10.6 Pricing Base Weight Conv. Factor
  DEFUWEIGHT BCD*10.4 Def. Weight UOM Unit Weight
  DEFEXTWGHT BCD*10.4 Def. Weight UOM Ext. Unit Weight
  PRPRICEBY Integer Price By [1=Quantity,2=Weight]
  NEEDPCHECK Boolean Price Check Pending
  CAPPROVEBY String*8 Price Approved By
  HDRDISC BCD*10.3 Header Discount
  OTRAMOUNT1 BCD*10.3 TR Tax Amount 1
  OTRAMOUNT2 BCD*10.3 TR Tax Amount 2
  OTRAMOUNT3 BCD*10.3 TR Tax Amount 3
  OTRAMOUNT4 BCD*10.3 TR Tax Amount 4
  OTRAMOUNT5 BCD*10.3 TR Tax Amount 5
  PSPRINTED Boolean Picking Slip Printed
  JOBRELATED Boolean Job Related
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
  RTGPERCENT BCD*5.5 Retainage Percent
  RTGDAYS Integer Retainage Days
  PRICEOPT Integer Default O/E Price [0=,1=Billing Rate,2=Use Customer Price List,3=Use Specified Price List]
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item Unit
  PAYMNTDIST BCD*10.3 Prepayment Distributed
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SQTYMOVED Long Serial Qty. Shipped
  LQTYMOVED BCD*10.4 Lot Qty. Shipped
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]
  REQUESDATE Date Date Requested

## OEORDDB - Order BOM Details (view OE0503)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; COMPONENT+ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM [D,M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Detail Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPONENT String*24 Component Item Number
  DESC String*60 Description
  QTY BCD*10.4 Component Quantity
  UNIT String*10 Unit of Measure
  QTYORDERED BCD*10.4 Quantity Ordered
  QTYSHIPPED BCD*10.4 Quantity Shipped
  DDTLNO String*6 Component's BOM Number
  BUILDQTY BCD*10.4 Component's BOM Build Qty.
  BUILDUNIT String*10 Component's BOM Build Unit
  BLDUNTCONV BCD*10.6 Component's BOM Build Unit Conv.
  UNITCONV BCD*10.6 Unit Conversion

## OEORDDD - Order Kitting Details (view OE0502)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; ORDUNIQ+LINENUM+COMPNUM; ORDUNIQ+DETAILNUM+COMPNUM; COMPONENT+ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Detail Line Number
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
  QTY BCD*10.4 Kitting Quantity
  PRNQTYORD BCD*10.4 Parent Quantity Ordered
  PRNQTYSHIP BCD*10.4 Parent Quantity Shipped
  PRNUNIT String*10 Parent Unit of Measure
  PRNUNTCONV BCD*10.6 Parent Unit Conversion
  QTYORDERED BCD*10.4 Quantity Ordered
  QTYSHIPPED BCD*10.4 Quantity Shipped
  QTYPO BCD*10.4 P/O Quantity Ordered
  ORDUNIT String*10 Order Unit of Measure
  UNITCONV BCD*10.6 Order Unit Conversion
  UNITCOST BCD*10.6 Order Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  AVGCOST BCD*10.6 Average Unit Cost
  LASTCOST BCD*10.6 Last Unit Cost
  COSTUNIT String*10 Costing Unit of Measure
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTOCOST BCD*10.3 Extended Order Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  GLNONSTKCR String*45 Non-stock Clearing Account
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRNWGTCONV BCD*10.6 Parent Weight Conversion Factor
  PRNUWEIGHT BCD*10.4 Parent Weight UOM Unit Weight
  PRNEXTWGHT BCD*10.4 Parent WUOM Extended Unit Weight
  DDTLNO String*6 Kit No.
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SQTYMOVED Long Serial Qty. Shipped
  LQTYMOVED BCD*10.4 Lot Qty. Shipped
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]

## OEORDDDL - Order Kitting Detail Lot Numbers (view OE0506)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+LOTNUMF; LOTNUMF+ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; ORDUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  STKQTYMOVE BCD*10.4 Qty Shipped in Stocking UOM
  QTYMOVED BCD*10.4 Quantity Shipped

## OEORDDDS - Order Kitting Serial Numbers (view OE0504)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+SERIALNUMF; SERIALNUMF+ORDUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; ORDUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Detail Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  MOVED Boolean Shipped?

## OEORDDL - Order Detail Lot Numbers (view OE0507)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM+LOTNUMF; LOTNUMF+ORDUNIQ+LINENUM; ORDUNIQ+DETAILNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  STKQTYMOVE BCD*10.4 Qty Shipped in Stocking UOM
  QTYMOVED BCD*10.4 Quantity Shipped

## OEORDDO - Order Detail Optional Fields (view OE0501)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM+OPTFIELD; OPTFIELD+ORDUNIQ+LINENUM
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
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

## OEORDDS - Order Detail Serial Numbers (view OE0508)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM+SERIALNUMF; SERIALNUMF+ORDUNIQ+LINENUM; ORDUNIQ+DETAILNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  MOVED Boolean Shipped?

## OEORDH - Orders (view OE0520)
Physical tables of this view: OEORDH, OEORDH1 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ; ORDNUMBER; CUSTOMER [D,M]; TYPE+COMPLETE+ORDUNIQ [M]; CUSTOMER+ORDNUMBER [M]; REFERENCE+ORDNUMBER [M]; CUSTOMER+PONUMBER [D,M]; CUSTOMER+ONHOLD+TYPE [D,M]; COMPANYID+OPPOID [D,M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDNUMBER String*22 Order Number
  CUSTOMER String*12 Customer Number
  CUSTGROUP String*6 Customer Group Code
  BILNAME String*60 Bill-To Name
  BILADDR1 String*60 Bill-To Address Line 1
  BILADDR2 String*60 Bill-To Address Line 2
  BILADDR3 String*60 Bill-To Address Line 3
  BILADDR4 String*60 Bill-To Address Line 4
  BILCITY String*30 Bill-To City
  BILSTATE String*30 Bill-To State/Province
  BILZIP String*20 Bill-To Zip/Postal Code
  BILCOUNTRY String*30 Bill-To Country
  BILPHONE String*30 Bill-To Phone Number
  BILFAX String*30 Bill-To Fax Number
  BILCONTACT String*60 Bill-To Contact
  SHIPTO String*6 Ship-To Location Code
  SHPNAME String*60 Ship-To Name
  SHPADDR1 String*60 Ship-To Address Line 1
  SHPADDR2 String*60 Ship-To Address Line 2
  SHPADDR3 String*60 Ship-To Address Line 3
  SHPADDR4 String*60 Ship-To Address Line 4
  SHPCITY String*30 Ship-To City
  SHPSTATE String*30 Ship-To State/Province
  SHPZIP String*20 Ship-To Zip/Postal Code
  SHPCOUNTRY String*30 Ship-To Country
  SHPPHONE String*30 Ship-To Phone Number
  SHPFAX String*30 Ship-To Fax Number
  SHPCONTACT String*60 Ship-To Contact
  CUSTDISC Integer Customer Discount Level [0=Base,1=A,2=B,3=C,4=D,5=E]
  PRICELIST String*6 Default Price List Code
  PONUMBER String*22 Purchase Order Number
  TERRITORY String*6 Territory
  TERMS String*6 Terms Code
  TERMTTLDUE BCD*10.3 Total Terms Amount Due
  DISCAVAIL BCD*10.3 Discount Available
  TERMOVERRD Boolean Terms Rate Override
  REFERENCE String*60 Order Reference
  TYPE Integer Order Type [1=Active,2=Future,3=Standing,4=Quote]
  ORDDATE Date Order Date
  EXPDATE Date Expected Ship Date
  QTEXPDATE Date Quote Expiration Date
  ORDFISCYR String*4 Order Fiscal Year
  ORDFISCPER Integer Order Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  LASTINVNUM String*22 Last Invoice Number
  NUMINVOICE Integer Number of Invoices
  FOB String*60 Free On Board Point
  TEMPLATE String*6 Template Code
  LOCATION String*6 Default Location Code
  ONHOLD Boolean On Hold [0=No,1=Yes]
  DESC String*60 Order Description
  COMMENT String*250 Order Comment
  PRINTSTAT Integer Order Print Status [1=,2=Quote printed,3=Picking slip printed,0=Internet,-1=Electronic Commerce]
  LASTPOST Date Last Posting Date
  ORNOPREPAY Integer Order No. of Prepayments
  OVERCREDIT Boolean Over Credit Limit
  APPROVELMT BCD*10.3 Approved Limit
  APPROVEBY String*8 Authorizing User ID
  SHIPLABEL Boolean Requires Shipping Labels
  LBLPRINTED Boolean Shipping Labels Printed
  ORHOMECURR String*3 Order Home Currency
  ORRATETYPE String*2 Order Rate Type
  ORSOURCURR String*3 Order Source Currency
  ORRATEDATE Date Order Rate Date
  ORRATE BCD*8.7 Order Rate
  ORSPREAD BCD*8.7 Order Spread
  ORDATEMTCH Integer Order Rate Date Matching
  ORRATEREP Integer Order Rate Operator
  ORRATEOVER Boolean Order Rate Override Flag
  ORDTOTAL BCD*10.3 Total Amt. Items
  ORDMTOTAL BCD*10.3 Total Amt. Misc. Charges
  ORDLINES Integer Number of Lines on Order
  NUMLABELS Integer Number of Labels
  ORDPAYTOT BCD*10.3 Prev. Payments Total
  ORDPYDSTOT BCD*10.3 Prev. Payment Disc. Total
  SALESPER1 String*8 Salesperson 1
  SALESPER2 String*8 Salesperson 2
  SALESPER3 String*8 Salesperson 3
  SALESPER4 String*8 Salesperson 4
  SALESPER5 String*8 Salesperson 5
  SALESPLT1 BCD*5.5 Sales Percentage 1
  SALESPLT2 BCD*5.5 Sales Percentage 2
  SALESPLT3 BCD*5.5 Sales Percentage 3
  SALESPLT4 BCD*5.5 Sales Percentage 4
  SALESPLT5 BCD*5.5 Sales Percentage 5
  RECALCTAX Boolean Recalculate Tax
  TAXOVERRD Boolean Tax Overridden
  TAXGROUP String*12 Tax Group
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TEAMOUNT1 BCD*10.3 Excluded Tax Amount 1
  TEAMOUNT2 BCD*10.3 Excluded Tax Amount 2
  TEAMOUNT3 BCD*10.3 Excluded Tax Amount 3
  TEAMOUNT4 BCD*10.3 Excluded Tax Amount 4
  TEAMOUNT5 BCD*10.3 Excluded Tax Amount 5
  TIAMOUNT1 BCD*10.3 Included Tax Amount 1
  TIAMOUNT2 BCD*10.3 Included Tax Amount 2
  TIAMOUNT3 BCD*10.3 Included Tax Amount 3
  TIAMOUNT4 BCD*10.3 Included Tax Amount 4
  TIAMOUNT5 BCD*10.3 Included Tax Amount 5
  TEXEMPT1 String*20 Registration 1
  TEXEMPT2 String*20 Registration 2
  TEXEMPT3 String*20 Registration 3
  TEXEMPT4 String*20 Registration 4
  TEXEMPT5 String*20 Registration 5
  COMPLETE Integer Order Completed [1=Incomplete/Not Included,2=Incomplete/Included,3=Complete/Not Included,4=Complete/Included,5=Complete/Day End]
  COMPDATE Date Order Completion Date
  INVNUMBER String*22 Invoice Number
  SHIPDATE Date Shipment Date
  INVDATE Date Invoice Date
  INVFISCYR String*4 Invoice Fiscal Year
  INVFISCPER Integer Invoice Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  NUMPAYMENT BCD*3.0 No. of Terms Payments
  PAYMNTASOF Date Terms Payments As Of Date
  INVWEIGHT BCD*10.4 Order Total Est. Weight
  NEXTDTLNUM Integer Next Detail Number
  POSTINV Boolean Post Invoice
  IDISONMISC Boolean Invoice Disc. Misc. Charges
  INNOPREPAY Integer Invoice No. of Prepayments
  NOSHIPLINE Integer No. Lines Qty. Shipped
  NOMISCLINE Integer No. Misc. Charges Lines
  INVNETNOTX BCD*10.3 Order Total Before Tax
  INVITAXTOT BCD*10.3 Order Incl. Tax Total
  INVITMTOT BCD*10.3 Order Item Total Amount
  INVDISCBAS BCD*10.3 Order Discount Base
  INVDISCPER BCD*5.5 Order Discount Percentage
  INVDISCAMT BCD*10.3 Order Discount Amount
  INVMISC BCD*10.3 Order Total Misc. Charges
  INVSUBTOT BCD*10.3 Order Subtotal Amount
  INVNET BCD*10.3 Order Total With Inv. Disc.
  INVETAXTOT BCD*10.3 Order Excl. Tax Total
  INVNETWTX BCD*10.3 Order Total
  INVAMTDUE BCD*10.3 Order Amount Due
  INHOMECURR String*3 Order Home Currency
  INRATETYPE String*2 Order Rate Type
  INSOURCURR String*3 Order Source Currency
  INRATEDATE Date Order Rate Date
  INRATE BCD*8.7 Order Rate
  INSPREAD BCD*8.7 Order Spread
  INDATEMTCH Integer Order Rate Date Matching
  INRATEREP Integer Order Rate Operator
  INRATEOVER Boolean Order Rate Override Flag
  ORDERSOURC Integer Order Source [0=Entered,1=Internet,2=Electronic Commerce,3=ePOS]
  COMPANYID Long Sage CRM Company ID
  OPPOID Long Sage CRM Opportunity ID
  PERSONID Long Sage CRM Person ID
  INCOPPOTOT Boolean Include In CRM Opportunity Total
  QTEXPIRED Boolean Quote Expired [0=No,1=Yes]
  QUOORDUNIQ BCD*10.0 Order Uniq. Activated From Quote
  QUOORDNUM String*22 Order Number Activated From Quote

## OEORDH1 - Orders (view OE0520)
Physical tables of this view: OEORDH, OEORDH1 (join 1:1 on the primary key)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  AUTOTAXCAL Boolean Auto-Tax Calculation Status
  QUONUMBER String*22 Originating Quote Number
  BILEMAIL String*50 Bill-To E-mail
  BILPHONEC String*30 Bill-To Contact Phone
  BILFAXC String*30 Bill-To Contact Fax
  BILEMAILC String*50 Bill-To Contact E-mail
  SHPEMAIL String*50 Ship-To E-mail
  SHPPHONEC String*30 Ship-To Contact Phone
  SHPFAXC String*30 Ship-To Contact Fax
  SHPEMAILC String*50 Ship-To Contact E-mail
  MULTIQUO Boolean Multiple Quotes [0=No,1=Yes]
  QUOS Integer Number of Quotes
  LASTSHINUM String*22 Last Shipment Number
  NUMSHPMENT Integer Number of Shipments
  SHIPTRACK String*36 Shipment Tracking Number
  VALUES Long Optional Fields
  FRMUNIQ BCD*10.0 Predecessor Uniquifier
  FRMNUMBER String*22 Predecessor Number
  ITEMDISTOT BCD*10.3 Item Detail Discount Total
  MISCDISTOT BCD*10.3 Misc. Charge Detail Discount Total
  OTRMETHOD Integer Auto-Calc. Tax Reporting Amounts
  OTRCURRNCY String*3 Tax Reporting (TR) Currency
  OTRRATTYPE String*2 TR Rate Type
  OTRRATDATE Date TR Rate Date
  OTRRATE BCD*8.7 TR Rate
  OTRSPREAD BCD*8.7 TR Spread
  OTRDATMTCH Integer TR Rate Date Matching
  OTRRATEOP Integer TR Rate Operator
  OTRRATOVER Boolean TR Rate Override Flag
  OTREAMNT1 BCD*10.3 TR Excluded Tax Amount 1
  OTREAMNT2 BCD*10.3 TR Excluded Tax Amount 2
  OTREAMNT3 BCD*10.3 TR Excluded Tax Amount 3
  OTREAMNT4 BCD*10.3 TR Excluded Tax Amount 4
  OTREAMNT5 BCD*10.3 TR Excluded Tax Amount 5
  OTRIAMNT1 BCD*10.3 TR Included Tax Amount 1
  OTRIAMNT2 BCD*10.3 TR Included Tax Amount 2
  OTRIAMNT3 BCD*10.3 TR Included Tax Amount 3
  OTRIAMNT4 BCD*10.3 TR Included Tax Amount 4
  OTRIAMNT5 BCD*10.3 TR Included Tax Amount 5
  DISAMTOVER Boolean Order Discount Amount Override
  JOBLINES Long Job Related Detail Lines
  LNINVABLE Long Invoiceable Detail Lines
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGTERMS String*6 Retainage Terms
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  CUSACCTSET String*6 Customer Account Set
  ENTEREDBY String*8 Entered By
  PFSEGLEN Integer ePOS Segment Length
  PAYMONORD Integer Payment Type On Order [0=(None),1=Cash,2=Check,3=Credit Card,4=Other,5=SPS Credit Card]
  PAYMCODE String*12 Payment Code On Order
  IDCARD String*12 Payment Card ID
  HOLDREASON String*60 On-hold Reason
  REQUESDATE Date Date Requested

## OEORDHO - Order Optional Fields (view OE0522)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+OPTFIELD; OPTFIELD+ORDUNIQ
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
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

## OEORDQ - Order from Quotes (view OE0526)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+LINENUM; ORDUNIQ+QUONUMBER; QUOUNIQ+ORDUNIQ
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QUOUNIQ BCD*10.0 Quote Uniquifier
  QUONUMBER String*22 Quote Number

## OEORPP - Order Prepayments (view OE0530)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUSTOMER String*12 Customer Number
  CUSTDESC String*60 Customer Name
  CUSTCURN String*3 Customer Currency
  CRATE BCD*8.7 Cust Rate
  CRATEDATE Date Cust Rate Date
  CRATETYPE String*2 Cust Rate Type
  CRATEOPER Integer Oper. Cust. Curn. to Func.
  DOCTOTAL BCD*10.3 Document Total
  DISCAVAIL BCD*10.3 Discount Available
  AMOUNTDUE BCD*10.3 Amount Due
  BATCHNUM BCD*5.0 Receipt Batch Number
  BANKCODE String*8 Bank Code
  RECPTYPE String*12 Receipt Type
  CHECKNUM String*24 Check/Receipt No.
  RECPDATE Date Receipt Date
  RECPAMOUNT BCD*10.3 Receipt Amount
  BANKCURN String*3 Bank Currency
  RATETYPE String*2 Rate Type
  BANKRATE BCD*8.7 Bank Rate
  RATEDATE Date Rate Date
  PAYMTYPE Integer Payment Type [0=(None),1=Cash,2=Check,3=Credit Card,4=Other,5=SPS Credit Card]
  PAUTHCURR String*3 Pre-auth Currency
  TRANIDPRE String*36 Pre-auth Transaction ID
  TRANIDCAP String*36 Capture Transaction ID
  TRANIDVOID String*36 Void Transaction ID
  PAUTHAMT BCD*10.3 Pre-auth Amount
  CHARGESTTS Integer Credit Card Charge Status [0=None,1=Charged,2=Voided,3=Pending,4=Card Declined,5=Card Error]
  YPPROCCODE String*12 YP Process Code

## OEPAUTH - Order Pre-Authorization (view OE0535)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ; TRANSTATUS+ORDUNIQ [M]
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUSTOMER String*12 Customer
  TRANIDPRE String*36 Preauth Transaction ID
  TRANIDCAP String*36 Capture Transaction ID
  TRANIDVOID String*36 Void Transaction ID
  TRANSTATUS Integer Transaction Status [0=None,1=Preauth Pending,2=Capture Pending,3=Void Pending,4=Success,5=Captured,6=Voided,7=Card Declined,8=Card Error]
  YPPROCCODE String*12 YP Process Code
  BANKCODE String*8 Bank Code
  PAYMCODE String*12 Payment Code
  PAYMTYPE Integer Payment Type
  PAUTHCURR String*3 Pre-Auth Amount Currency
  SOURCURR String*3 Source Currency
  RATETYPE String*2 Rate Type
  RATEDATE Date Rate Date
  RATE BCD*8.7 Exchange Rate
  SPREAD BCD*8.7 Rate Spread
  DATEMTCH Integer Rate Date Matching
  RATEREP Integer Rate Operator
  RATEOVER Boolean Rate Override Falg
  ORDPOSTED Boolean Order Posted
  PAUTHAMT BCD*10.3 Pre-Auth Amount

## OEPLAT - Templates (view OE0540)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE
Fields (NAME type description [values]):
  TEMPLATE String*6 Template Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PLATEDESC String*60 Template Description
  ORDTYPE Integer Default Order Type [1=Active,2=Future,3=Standing,4=Quote]
  FOB String*60 Default Free On Board Point
  ONHOLD Boolean Default On Hold
  LOCATION String*6 Default Location
  DESC String*60 Default Description
  REFERENCE String*60 Default Reference
  COMMENT String*250 Default Comment
  SHIPVIA String*6 Default Ship-Via Code
  CUSTDISC Integer Default Customer Type [0=Base,1=A,2=B,3=C,4=D,5=E]
  PRICELIST String*6 Default Price List
  TERRITORY String*6 Default Territory
  TAXGROUP String*12 Default Tax Group
  TERMS String*6 Default Payment Terms
  HOLDREASON String*60 On-hold Reason
  CUSACCTSET String*6 Default Account Set

## OEPPPMTD - Preauthorized Payment Details (view OE0127)
Keys (first = PK; D=dups allowed, M=modifiable): YPPROCCODE+ORDNUMBER
Fields (NAME type description [values]):
  YPPROCCODE String*12 Processing Code
  ORDNUMBER String*22 Order Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHINUMBER String*22 Shipment Number
  ORDDATE Date Order Date
  CUSTOMER String*12 Customer Number
  CUSTNAME String*60 Customer Name
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  ORDUNIQ BCD*10.0 Order Uniquifier
  STATUS Integer Processing Status [0=,1=Capture Successful,2=Card Declined,3=Card Error,4=Error Processing Capture,5=Invoice Successful,6=Error Creating Invoice,7=Pre-authorization Not Found,8=Locked by Other User]
  SWAPPLY Integer Apply [0=No,1=Yes]

## OEPPRE - Posted Prepayments (view OE0620)
Keys (first = PK; D=dups allowed, M=modifiable): APPLYTO+DOCNUMBER+PPNUMBER
Fields (NAME type description [values]):
  APPLYTO Integer Apply To [2=Invoice No.,4=Order No.,9=Shipment No.]
  DOCNUMBER String*22 Document Number
  PPNUMBER Integer Prepayment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REBATCHNUM BCD*5.0 Receipt Batch Number
  BANKCODE String*8 Bank Code
  BANKRECTYP String*12 Receipt Type
  CHECKDATE Date Check Date
  CHKFISCYR String*4 Check Fiscal Year
  CHKFISCPER Integer Check Fiscal Period
  CHECKNUM String*24 Check Number
  PAYMENT BCD*10.3 Payment in Customer Currency
  INVPAYDISC BCD*10.3 Payment Discount
  BANKPAYMNT BCD*10.3 Payment in Bank Currency
  PAHOMECURR String*3 Payment Home Currency
  PARATETYPE String*2 Payment Rate Type
  PASOURCURR String*3 Payment Source Currency
  PARATEDATE Date Payment Rate Date
  PARATE BCD*8.7 Payment Rate
  PASPREAD BCD*8.7 Payment Spread
  PADATEMTCH Integer Payment Rate Date Matching
  PARATEREP Integer Payment Rate Operator
  IDPPD String*22 Prepayment ID
  PAYMTYPE Integer Payment Type [0=(None),1=Cash,2=Check,3=Credit Card,4=Other,5=SPS Credit Card]
  TRANIDPRE String*36 Pre-auth Transaction ID
  TRANIDCAP String*36 Capture Transaction ID
  PAUTHAMT BCD*10.3 Pre-auth amount

## OEPPRED - Posted Prepayment Details (view OE0622)
Keys (first = PK; D=dups allowed, M=modifiable): APPLYTO+DOCNUMBER+PPNUMBER+DETAILNUM
Fields (NAME type description [values]):
  APPLYTO Integer Apply To [2=Invoice No.,4=Order No.,9=Shipment No.]
  DOCNUMBER String*22 Document Number
  PPNUMBER Integer Prepayment Number
  DETAILNUM Integer Detail Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BANKPAYMNT BCD*10.3 Payment in Bank Currency
  PAYMENT BCD*10.3 Payment in Customer Currency

## OEQTOD - Promote Quote to Order Details (view OE0637)
Keys (first = PK; D=dups allowed, M=modifiable): COMPANYID+OPPOID+ORDNUMBER
Fields (NAME type description [values]):
  COMPANYID Long Company ID
  OPPOID Long Opportunity ID
  ORDNUMBER String*22 Quote Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDUNIQ BCD*10.0 Quote Uniquifier
  PROMOTE Boolean Promote to Order? [0=No,1=Yes]
  INCOPPOTOT Boolean Include in Opportunity Total? [0=No,1=Yes]
  QUOTEINCL Boolean Included in Quote?
  ORDDATE Date Quote Date
  QTEXPDATE Date Expiration Date
  INVNETWTX BCD*10.3 Amount
  ORDLINES Integer Number of Lines on Quote
  DESC String*60 Description
  REFERENCE String*60 Reference
  COMMENT String*250 Comment
  COMPLETE Integer Quote Completed [1=Incomplete/Not Included,2=Incomplete/Included,3=Complete/Not Included,4=Complete/Included,5=Complete/Day End]
  QTEXPIRED Boolean Quote Expired [0=No,1=Yes]
  QUOORDUNIQ BCD*10.0 Order Uniq. Activated From Quote
  QUOORDNUM String*22 Order Number Activated From Quote

## OEQTOH - Promote Quote to Order Header (view OE0638)
Keys (first = PK; D=dups allowed, M=modifiable): COMPANYID+OPPOID
Fields (NAME type description [values]):
  COMPANYID Long Company ID
  OPPOID Long Opportunity ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SESSIONID Long Session ID
  OPPOSTATUS Integer Opportunity Status [1=In Progress,2=Won,3=Lost]
  CUSTOMER String*12 Customer Number
  ORSOURCURR String*3 Source Currency
  OPPOTOTAL BCD*10.3 Opportunity Total
  UNPROMTOT BCD*10.3 Unpromoted Total
  PROMTOT BCD*10.3 Promoted Total
  QUOORDUNIQ BCD*10.0 Order Uniq. Activated From Quote

## OERSTRT - Restart (view OE0634)
Keys (first = PK; D=dups allowed, M=modifiable): KEY+USERID
Fields (NAME type description [values]):
  KEY String*50 Key
  USERID String*8 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DATA1 Binary*255 Data Block 1

## OESHCD - Shipment Cost-To-Clear Details (view OE0683)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+DETAILNUM; SHINUMBER+DETAILNUM
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHINUMBER String*22 Shipment Number
  QTYSHIPPED BCD*10.4 Quantity Shipped
  SHIUNIT String*10 Shipping Unit
  UNITCONV BCD*10.6 Shipment Unit Conversion
  COST BCD*10.3 Cost to Shp. Clr. Acct.
  ACTUALCOST BCD*10.3 Actual Cost to IC Ctl. Acct.

## OESHCDD - Shipment Cost-To-Clear Details of Details (view OE0688)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+DETAILNUM+COMPNUM
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QTYSHIPPED BCD*10.4 Quantity Shipped
  SHIUNIT String*10 Shipping Unit
  UNITCONV BCD*10.6 Shipment Unit Conversion
  COST BCD*10.3 Cost to Shp. Clr. Acct.
  ACTUALCOST BCD*10.3 Actual Cost to IC Ctl. Acct.

## OESHCDDL - Shipment Cost-To-Clear Kitting Lots (view OE0689)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+DETAILNUM+COMPNUM+LOTNUMF
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  COMPNUM Long Component Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Lot Quantity
  COST BCD*10.3 Cost

## OESHCDDS - Shipment Cost-To-Clear Kitting Serials (view OE0687)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+DETAILNUM+COMPNUM+SERIALNUMF
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  COMPNUM Long Component Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COST BCD*10.3 Cost

## OESHCDL - Shipment Cost-To-Clear Lots (view OE0686)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+DETAILNUM+LOTNUMF
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  LOTNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Lot Quantity
  COST BCD*10.3 Cost

## OESHCDS - Shipment Cost-To-Clear Serials (view OE0681)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+DETAILNUM+SERIALNUMF
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COST BCD*10.3 Cost

## OESHCH - Shipment Cost-To-Clear (view OE0684)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ; SHINUMBER
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHINUMBER String*22 Shipment Number
  SHRATE BCD*8.7 Shipment Rate

## OESHDT - Sales History Details (view OE0685)
Keys (first = PK; D=dups allowed, M=modifiable): CUSTOMER+ITEM+YR+PERIOD+TRANDATE+DAYENDSEQ+TRANSSEQ+LINENO; ITEM+CUSTOMER+YR+PERIOD+TRANDATE+DAYENDSEQ+TRANSSEQ+LINENO; SALESPER+YR+PERIOD+CUSTOMER+TRANTYPE+TRANNUM [D,M]; CUSTOMER+ITEM+TRANDATE+YR+PERIOD+DAYENDSEQ+TRANSSEQ+LINENO; ITEM+CUSTOMER+TRANDATE+YR+PERIOD+DAYENDSEQ+TRANSSEQ+LINENO; SALESPER+TRANDATE+YR+PERIOD+CUSTOMER+TRANTYPE+TRANNUM [D,M]
Fields (NAME type description [values]):
  CUSTOMER String*12 Customer Number
  ITEM String*24 Item Number
  YR String*4 Year
  PERIOD Integer Period
  TRANDATE Date Trans. Date
  DAYENDSEQ Long Day End Number
  TRANSSEQ Long Entry Number
  LINENO Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TRANNUM String*22 Trans. Number
  TRANTYPE Integer Trans. Type [1=Invoice,2=Credit Note,4=Debit Note]
  ORDDATE Date Order Date
  ORDNUMBER String*22 Order Number
  SHIPDATE Date Ship Date
  SALESPER String*8 Salesperson
  TERRITORY String*6 Territory
  LOCATION String*6 Location
  CATEGORY String*6 Category
  QTYSOLD BCD*10.4 Quantity Sold
  SCURN String*3 Cust. Currency
  FCSTSALES BCD*10.3 Func. Cost of Sales
  SCSTSALES BCD*10.3 Srce. Cost of Sales
  FAMTSALES BCD*10.3 Func. Sales Amount
  SAMTSALES BCD*10.3 Srce. Sales Amount
  FRETSALES BCD*10.3 Func. Return Amount
  SRETSALES BCD*10.3 Srce. Return Amount
  PONUMBER String*22 Purchase Order Number
  FAMTTRAN BCD*10.3 Functional Amount
  SAMTTRAN BCD*10.3 Source Amount
  FAMTDISC BCD*10.3 Functional Discount Amount
  SAMTDISC BCD*10.3 Source Discount Amount
  SHINUMBER String*22 Shipment Number
  SHIDTLNUM Integer Shipment Detail Number

## OESHHD - Sales History (view OE0690)
Keys (first = PK; D=dups allowed, M=modifiable): CUSTOMER+ITEM+YR+PERIOD; ITEM+CUSTOMER+YR+PERIOD
Fields (NAME type description [values]):
  CUSTOMER String*12 Customer Number
  ITEM String*24 Unformatted Item Number
  YR String*4 Year
  PERIOD Integer Period
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SCURN String*3 Currency
  QTYSOLD BCD*10.4 Quantity Sold
  FTOTSALES BCD*10.3 Func. Sales Amount
  STOTSALES BCD*10.3 Srce. Sales Amount
  FCSTSALES BCD*10.3 Func. Cost of Sales
  SCSTSALES BCD*10.3 Srce. Cost of Sales
  SALESCNT Integer Sales Count
  RETCNT Integer Returns Count
  FRETSALES BCD*10.3 Func. Return Amount
  SRETSALES BCD*10.3 Srce. Return Amount

## OESHID - Shipment Details (view OE0691)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM; SHIUNIQ+DETAILNUM; ORDNUMBER+ORDDTLNUM+SHIUNIQ+DETAILNUM; ITEM+SHIUNIQ+LINENUM [D,M]
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  LINETYPE Integer Line Type [1=Item,2=Miscellaneous]
  ITEM String*24 Item
  MISCCHARGE String*6 Miscellaneous Charges Code
  DESC String*60 Description
  ACCTSET String*6 Item Account Set
  USERCOSTMD Boolean User-Specified Costing Method
  PRICELIST String*6 Price List
  CATEGORY String*6 Category
  LOCATION String*6 Location
  PICKSEQ String*10 Picking Sequence
  EXPDATE Date Shipment Date
  STOCKITEM Boolean Stock Item
  ORDQTYORD BCD*10.4 Order Quantity Ordered
  ORDQTYBKOR BCD*10.4 Order Quantity Backordered
  ORDQTYCOMM BCD*10.4 Order Quantity Committed
  ORDQTYTCOM BCD*10.4 Order True Quantity Committed
  ORDQTYSTD BCD*10.4 Order Quantity Shipped-to-date
  ORDUNIT String*10 Order Unit of Measure
  ORDUNITCON BCD*10.6 Order Unit Conversion
  QTYORDERED BCD*10.4 Current Quantity Outstanding
  QTYSHIPPED BCD*10.4 Quantity Shipped
  QTYBACKORD BCD*10.4 Quantity Backordered
  QTYCOMMIT BCD*10.4 Quantity Committed
  QTYTRUECOM BCD*10.4 True Quantity Committed
  SHIUNIT String*10 Shipment Unit of Measure
  UNITCONV BCD*10.6 Shipment Unit Conversion
  UNITPRICE BCD*10.6 Shipment Unit Price
  PRICEOVER Boolean Price Override [0=No,1=Yes]
  UNITCOST BCD*10.6 Shipment Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  AVGCOST BCD*10.6 Average Cost
  LASTCOST BCD*10.6 Last Cost
  UNITPRCDEC Integer Unit Price No. of Decimals
  PRICEUNIT String*10 Pricing Unit of Measure
  PRIUNTPRC BCD*10.6 Pricing Unit Price
  PRIUNTCONV BCD*10.6 Pricing Unit Conversion
  PRIPERCENT BCD*5.5 Price Discount Percentage
  PRIAMOUNT BCD*10.3 Price Discount Amount
  BASEUNIT String*10 Pricing Base Unit
  PRIBASPRC BCD*10.6 Pricing Base Unit Price
  PRIBASCONV BCD*10.6 Pricing Base Unit Conversion
  COSTUNIT String*10 Costing Unit of Measure
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTSHIMISC BCD*10.3 Extended Amount
  SHIDISC BCD*10.3 Shipment Discount Amount
  EXTSCOST BCD*10.3 Extended Shipment Cost
  EXTOVER Boolean Extended Shipped Amt. Override
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  COMPLETE Integer Detail Completed [0=Not completed,1=Completed/Not In Database,2=Completed,3=Processed by day end]
  FINISHORD Boolean Shipment Completes Order Detail [0=No,1=Yes]
  ADDTOILOC Boolean Recognized In Item/Location
  SALESLOST BCD*10.3 Lost Sales Amount
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TAMOUNT1 BCD*10.3 Tax Amount 1
  TAMOUNT2 BCD*10.3 Tax Amount 2
  TAMOUNT3 BCD*10.3 Tax Amount 3
  TAMOUNT4 BCD*10.3 Tax Amount 4
  TAMOUNT5 BCD*10.3 Tax Amount 5
  TRATE1 BCD*8.5 Tax Rate 1
  TRATE2 BCD*8.5 Tax Rate 2
  TRATE3 BCD*8.5 Tax Rate 3
  TRATE4 BCD*8.5 Tax Rate 4
  TRATE5 BCD*8.5 Tax Rate 5
  DETAILNUM Integer Detail Number
  COMMINST Boolean Use Comments/Instructions [0=No,1=Yes]
  GLNONSTKCR String*45 Non-stock Clearing Account
  ORDNUMBER String*22 Order Number
  ORDDTLNUM Integer Order Detail Number
  INDBTABLE Boolean Stored in Database Table [0=No,1=Yes]
  REFRESH Boolean Refresh Order Qty. at Update [0=No,1=Yes]
  SHIPTRACK String*36 Shipment Tracking Number
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  DISCPER BCD*5.5 Discount Percent
  MANITEMNO String*24 Manufacturer's ItemNumber
  CUSTITEMNO String*24 Customer Item Number
  VALUES Long Optional Fields
  DDTLTYPE Integer Kitting/BOM [0=None,1=Kitting,2=BOM]
  DDTLNO String*6 Kit/BOM Number
  BUILDQTY BCD*10.4 BOM Build Qty.
  BUILDUNIT String*10 BOM Build Unit
  BLDUNTCONV BCD*10.6 BOM Build Unit Conversion
  NEXTCMPNUM Long Next Component Number
  EPOSPROMID Integer ePOS Promotion ID
  BASEWUNIT String*10 Pricing Base Weight Unit
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRWGHTUNIT String*10 Pricing Weight UOM
  PRWGHTCONV BCD*10.6 Pricing Weight Conversion Factor
  PRIBASWCNV BCD*10.6 Pricing Base Weight Conv. Factor
  DEFUWEIGHT BCD*10.4 Def. Weight UOM Unit Weight
  DEFEXTWGHT BCD*10.4 Def. Weight UOM Ext. Unit Weight
  PRPRICEBY Integer Price By [1=Quantity,2=Weight]
  NEEDPCHECK Boolean Price Check Pending
  CAPPROVEBY String*8 Price Approved By
  HDRDISC BCD*10.3 Header Discount
  STRAMOUNT1 BCD*10.3 TR Tax Amount 1
  STRAMOUNT2 BCD*10.3 TR Tax Amount 2
  STRAMOUNT3 BCD*10.3 TR Tax Amount 3
  STRAMOUNT4 BCD*10.3 TR Tax Amount 4
  STRAMOUNT5 BCD*10.3 TR Tax Amount 5
  PSPRINTED Boolean Picking Slip Printed
  COG BCD*10.3 Cost of Goods
  JOBRELATED Boolean Job Related
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
  RTGAMTOVR Boolean Retainage Amount Override
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  PMTRANSNBR Long PM Transaction Number
  PRICEOPT Integer Default O/E Price [0=,1=Billing Rate,2=Use Customer Price List,3=Use Specified Price List]
  ARITEMNO String*16 A/R Item Number
  ARUNIT String*10 A/R Item Unit
  PAYMNTDIST BCD*10.3 Prepayment Distributed
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]
  COMPANYID Long Sage CRM Company ID
  OPPOID Long Sage CRM Opportunity ID

## OESHIDB - Shipment BOM Details (view OE0705)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM+PRNCOMPNUM+COMPNUM
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Detail Line Number
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
  QTYSHIPPED BCD*10.4 Quantity Shipped
  DDTLNO String*6 Component's BOM Number
  BUILDQTY BCD*10.4 Component's BOM Build Qty.
  BUILDUNIT String*10 Component's BOM Build Unit
  BLDUNTCONV BCD*10.6 Component's BOM Build Unit Conv.
  UNITCONV BCD*10.6 Unit Conversion

## OESHIDD - Shipment Kitting Details (view OE0703)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; SHIUNIQ+LINENUM+COMPNUM; SHIUNIQ+DETAILNUM+COMPNUM
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Detail Line Number
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
  QTY BCD*10.4 Kitting Quantity
  PRNQTYSHIP BCD*10.4 Parent Quantity Shipped
  PRNUNIT String*10 Parent Unit of Measure
  PRNUNTCONV BCD*10.6 Parent Unit Conversion
  QTYSHIPPED BCD*10.4 Quantity Shipped
  SHIUNIT String*10 Shipment Unit of Measure
  UNITCONV BCD*10.6 Shipment Unit Conversion
  UNITCOST BCD*10.6 Shipment Unit Cost
  MOSTREC BCD*10.6 Most Recent Unit Cost
  STDCOST BCD*10.6 Standard Unit Cost
  COST1 BCD*10.6 Alternate Unit Cost 1
  COST2 BCD*10.6 Alternate Unit Cost 2
  AVGCOST BCD*10.6 Average Unit Cost
  LASTCOST BCD*10.6 Last Unit Cost
  COSTUNIT String*10 Costing Unit of Measure
  COSUNTCST BCD*10.6 Costing Unit Cost
  COSUNTCONV BCD*10.6 Costing Unit Conversion
  EXTSCOST BCD*10.3 Extended Shipment Cost
  UNITWEIGHT BCD*10.4 Unit Weight
  EXTWEIGHT BCD*10.4 Extended Weight
  GLNONSTKCR String*45 Non-stock Clearing Account
  WEIGHTUNIT String*10 Weight Unit of Measure
  WEIGHTCONV BCD*10.6 Weight Conversion Factor
  PRNWGTCONV BCD*10.6 Parent Weight Conversion Factor
  PRNUWEIGHT BCD*10.4 Parent Weight UOM Unit Weight
  PRNEXTWGHT BCD*10.4 Parent WUOM Extended Unit Weight
  DDTLNO String*6 Kit No.
  COG BCD*10.3 Cost of Goods
  SERIALQTY Long Serial Quantity
  LOTQTY BCD*10.4 Lot Quantity
  SLITEM Integer Item Serialized/Lotted? [0=None,1=Serialized,2=Lotted,3=Both]

## OESHIDDL - Shipment Kitting Detail Lot Numbers (view OE0707)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+LOTNUMF; LOTNUMF+SHIUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; SHIUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  COST BCD*10.3 Cost

## OESHIDDS - Shipment Kitting Serial Numbers (view OE0706)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM+PRNCOMPNUM+COMPNUM+SERIALNUMF; SERIALNUMF+SHIUNIQ+LINENUM+PRNCOMPNUM+COMPNUM; SHIUNIQ+DETAILNUM+PRNCOMPNUM+COMPNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Detail Line Number
  PRNCOMPNUM Long Parent Component Number
  COMPNUM Long Component Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COST BCD*10.3 Cost

## OESHIDL - Shipment Detail Lot Numbers (view OE0708)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM+LOTNUMF; LOTNUMF+SHIUNIQ+LINENUM; SHIUNIQ+DETAILNUM+LOTNUMF [M]
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Line Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  EXPIRYDATE Date Expiration Date
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Transaction Quantity
  COST BCD*10.3 Cost

## OESHIDO - Shipment Detail Optional Fields (view OE0702)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM+OPTFIELD; OPTFIELD+SHIUNIQ+LINENUM
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
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

## OESHIDS - Shipment Detail Serial Numbers (view OE0709)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM+SERIALNUMF; SERIALNUMF+SHIUNIQ+LINENUM; SHIUNIQ+DETAILNUM+SERIALNUMF [M]
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Line Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DETAILNUM Integer Detail Number
  COST BCD*10.3 Cost

## OESHIH - Shipments (view OE0692)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ; SHINUMBER; ORDNUMBER+SHINUMBER; CUSTOMER+SHINUMBER; REFERENCE+SHINUMBER [M]; COMPLETE+SHIUNIQ [M]; CUSTOMER+PONUMBER+ORDNUMBER [D,M]; ORDUNIQ+COMPLETE [D,M]
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHINUMBER String*22 Shipment Number
  ORDNUMBER String*22 Order Number
  DAYENDNUM BCD*10.0 I/C Day End Trans. Number
  CUSTOMER String*12 Customer Number
  CUSTGROUP String*6 Customer Group Code
  BILNAME String*60 Bill-To Name
  BILADDR1 String*60 Bill-To Address Line 1
  BILADDR2 String*60 Bill-To Address Line 2
  BILADDR3 String*60 Bill-To Address Line 3
  BILADDR4 String*60 Bill-To Address Line 4
  BILCITY String*30 Bill-To City
  BILSTATE String*30 Bill-To State/Province
  BILZIP String*20 Bill-To Zip/Postal Code
  BILCOUNTRY String*30 Bill-To Country
  BILPHONE String*30 Bill-To Phone Number
  BILFAX String*30 Bill-To Fax Number
  BILCONTACT String*60 Bill-To Contact
  BILEMAIL String*50 Bill-To E-mail
  BILPHONEC String*30 Bill-To Contact Phone
  BILFAXC String*30 Bill-To Contact Fax
  BILEMAILC String*50 Bill-To Contact E-mail
  SHIPTO String*6 Ship-To Location Code
  SHPNAME String*60 Ship-To Name
  SHPADDR1 String*60 Ship-To Address Line 1
  SHPADDR2 String*60 Ship-To Address Line 2
  SHPADDR3 String*60 Ship-To Address Line 3
  SHPADDR4 String*60 Ship-To Address Line 4
  SHPCITY String*30 Ship-To City
  SHPSTATE String*30 Ship-To State/Province
  SHPZIP String*20 Ship-To Zip/Postal Code
  SHPCOUNTRY String*30 Ship-To Country
  SHPPHONE String*30 Ship-To Phone Number
  SHPFAX String*30 Ship-To Fax Number
  SHPCONTACT String*60 Ship-To Contact
  SHPEMAIL String*50 Ship-To E-mail
  SHPPHONEC String*30 Ship-To Contact Phone
  SHPFAXC String*30 Ship-To Contact Fax
  SHPEMAILC String*50 Ship-To Contact E-mail
  CUSTDISC Integer Customer Discount Level [0=Base,1=A,2=B,3=C,4=D,5=E]
  PRICELIST String*6 Default Price List Code
  PONUMBER String*22 Purchase Order Number
  TERRITORY String*6 Territory
  TERMS String*6 Terms Code
  REFERENCE String*60 Shipment Reference
  SHIDATE Date Shipment Date
  EXPDATE Date Expected Ship Date
  SHIPVIA String*6 Ship-Via Code
  VIADESC String*60 Ship-Via Code Description
  SHIFISCYR String*4 Shipment Fiscal Year
  SHIFISCPER Integer Shipment Fiscal Period [1=1,2=2,3=3,4=4,5=5,6=6,7=7,8=8,9=9,10=10,11=11,12=12]
  LASTINVNUM String*22 Last Invoice Number
  NUMINVOICE Integer Number of Invoices
  FOB String*60 Free On Board Point
  TEMPLATE String*6 Template Code
  LOCATION String*6 Default Location Code
  DESC String*60 Shipment Description
  COMMENT String*250 Shipment Comment
  OVERCREDIT Boolean Over Credit Limit
  APPROVELMT BCD*10.3 Approved Limit
  APPROVEBY String*8 Authorizing User ID
  PRINTSTAT Integer Order Print Status [1=,2=Quote printed,3=Picking slip printed,0=Internet,-1=Electronic Commerce]
  LASTPOST Date Last Posting Date
  SHIPLABEL Boolean Requires Shipping Labels
  LBLPRINTED Boolean Shipping Labels Printed
  SHHOMECURR String*3 Shipment Home Currency
  SHRATETYPE String*2 Shipment Rate Type
  SHSOURCURR String*3 Shipment Source Currency
  SHRATEDATE Date Shipment Rate Date
  SHRATE BCD*8.7 Shipment Rate
  SHSPREAD BCD*8.7 Shipment Spread
  SHDATEMTCH Integer Shipment Rate Date Matching
  SHRATEREP Integer Shipment Rate Operator
  SHRATEOVER Boolean Shipment Rate Override Flag
  SHITOTAL BCD*10.3 Total Amt. Items
  SHIMTOTAL BCD*10.3 Total Amt. Misc. Charges
  SHILINES Integer Number of Lines on Shipment
  NUMLABELS Integer Number of Labels
  SHIPAYTOT BCD*10.3 Prev. Payments Total
  SHIPYDSTOT BCD*10.3 Prev. Payment Disc. Total
  SALESPER1 String*8 Salesperson 1
  SALESPER2 String*8 Salesperson 2
  SALESPER3 String*8 Salesperson 3
  SALESPER4 String*8 Salesperson 4
  SALESPER5 String*8 Salesperson 5
  SALESPLT1 BCD*5.5 Sales Percentage 1
  SALESPLT2 BCD*5.5 Sales Percentage 2
  SALESPLT3 BCD*5.5 Sales Percentage 3
  SALESPLT4 BCD*5.5 Sales Percentage 4
  SALESPLT5 BCD*5.5 Sales Percentage 5
  RECALCTAX Boolean Recalculate Tax
  TAXOVERRD Boolean Tax Overridden
  TAXGROUP String*12 Tax Group
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
  TBASE1 BCD*10.3 Tax Base 1
  TBASE2 BCD*10.3 Tax Base 2
  TBASE3 BCD*10.3 Tax Base 3
  TBASE4 BCD*10.3 Tax Base 4
  TBASE5 BCD*10.3 Tax Base 5
  TEAMOUNT1 BCD*10.3 Excluded Tax Amount 1
  TEAMOUNT2 BCD*10.3 Excluded Tax Amount 2
  TEAMOUNT3 BCD*10.3 Excluded Tax Amount 3
  TEAMOUNT4 BCD*10.3 Excluded Tax Amount 4
  TEAMOUNT5 BCD*10.3 Excluded Tax Amount 5
  TIAMOUNT1 BCD*10.3 Included Tax Amount 1
  TIAMOUNT2 BCD*10.3 Included Tax Amount 2
  TIAMOUNT3 BCD*10.3 Included Tax Amount 3
  TIAMOUNT4 BCD*10.3 Included Tax Amount 4
  TIAMOUNT5 BCD*10.3 Included Tax Amount 5
  TEXEMPT1 String*20 Registration 1
  TEXEMPT2 String*20 Registration 2
  TEXEMPT3 String*20 Registration 3
  TEXEMPT4 String*20 Registration 4
  TEXEMPT5 String*20 Registration 5
  COMPLETE Integer Shipment Completed [1=Incomplete/Not Included,2=Incomplete/Included,3=Complete/Not Included,4=Complete/Included,5=Complete/Day End]
  COMPDATE Date Shipment Completion Date
  SHIWEIGHT BCD*10.4 Shipment Total Est. Weight
  NEXTDTLNUM Integer Next Detail Number
  SDISONMISC Boolean Shipment Disc. Misc. Charges
  NOSHIPLINE Integer No. Lines Qty. Shipped
  NOMISCLINE Integer No. Misc. Charges Lines
  SHINETNOTX BCD*10.3 Shipment Total Before Tax
  SHIITAXTOT BCD*10.3 Shipment Incl. Tax Total
  SHIITMTOT BCD*10.3 Shipment Item Total Amount
  SHIDISCBAS BCD*10.3 Shipment Discount Base
  SHIDISCPER BCD*5.5 Shipment Discount Percentage
  SHIDISCAMT BCD*10.3 Shipment Discount Amount
  SHIMISC BCD*10.3 Shipment Total Misc. Charges
  SHISUBTOT BCD*10.3 Shipment Subtotal Amount
  SHINET BCD*10.3 Shipment Total With Inv. Disc.
  SHIETAXTOT BCD*10.3 Shipment Excl. Tax Total
  SHINETWTX BCD*10.3 Shipment Total
  ORDDATE Date Order Date
  ORHOMECURR String*3 Order Home Currency
  ORRATETYPE String*2 Order Rate Type
  ORSOURCURR String*3 Order Source Currency
  ORRATEDATE Date Order Rate Date
  ORRATE BCD*8.7 Order Rate
  ORSPREAD BCD*8.7 Order Spread
  ORDATEMTCH Integer Order Rate Date Matching
  ORRATEREP Integer Order Rate Operator
  ORRATEOVER Boolean Order Rate Override Flag
  AUTOTAXCAL Boolean Auto-Tax Calculation Status
  MULTIORD Boolean Generate From Multiple Orders [0=No,1=Yes]
  ORDS Integer From How Many Orders
  SHIPTRACK String*36 Shipment Tracking Number
  NUMSHPMENT Integer Number of Shipments
  VALUES Long Optional Fields
  ORDUNIQ BCD*10.0 Order Uniquifier
  ITEMDISTOT BCD*10.3 Item Detail Discount Total
  MISCDISTOT BCD*10.3 Misc. Charge Detail Discount Total
  STRMETHOD Integer Auto-Calc. Tax Reporting Amounts
  STRCURRNCY String*3 Tax Reporting (TR) Currency
  STRRATTYPE String*2 TR Rate Type
  STRRATDATE Date TR Rate Date
  STRRATE BCD*8.7 TR Rate
  STRSPREAD BCD*8.7 TR Spread
  STRDATMTCH Integer TR Rate Date Matching
  STRRATEOP Integer TR Rate Operator
  STRRATOVER Boolean TR Rate Override Flag
  STREAMNT1 BCD*10.3 TR Excluded Tax Amount 1
  STREAMNT2 BCD*10.3 TR Excluded Tax Amount 2
  STREAMNT3 BCD*10.3 TR Excluded Tax Amount 3
  STREAMNT4 BCD*10.3 TR Excluded Tax Amount 4
  STREAMNT5 BCD*10.3 TR Excluded Tax Amount 5
  STRIAMNT1 BCD*10.3 TR Included Tax Amount 1
  STRIAMNT2 BCD*10.3 TR Included Tax Amount 2
  STRIAMNT3 BCD*10.3 TR Included Tax Amount 3
  STRIAMNT4 BCD*10.3 TR Included Tax Amount 4
  STRIAMNT5 BCD*10.3 TR Included Tax Amount 5
  OTRCURRNCY String*3 Tax Reporting (TR) Order Currency
  OTRRATTYPE String*2 TR Order Rate Type
  OTRRATDATE Date TR Order Rate Date
  OTRRATE BCD*8.7 TR Order Rate
  OTRSPREAD BCD*8.7 TR Order Spread
  OTRDATMTCH Integer TR Order Rate Date Matching
  OTRRATEOP Integer TR Order Rate Operator
  OTRRATOVER Boolean TR Order Rate Override Flag
  DISAMTOVER Boolean Shipment Discount Amount Override
  SHNOPREPAY Integer Shipment No. of Prepayments
  JOBLINES Long Job Related Detail Lines
  LNINVABLE Long Invoiceable Detail Lines
  HASRTG Boolean Has Retainage [0=No,1=Yes]
  RTGTERMS String*6 Retainage Terms
  RTGAMOUNT BCD*10.3 Retainage Amount
  RTGPERCENT BCD*5.5 Retainage Percent
  RTGRATE Integer Retainage Exchange Rate [0=Use Original Document Exchange Rate,1=Use Current Exchange Rate]
  RTGTXBASE1 BCD*10.3 Retainage Tax Base 1
  RTGTXBASE2 BCD*10.3 Retainage Tax Base 2
  RTGTXBASE3 BCD*10.3 Retainage Tax Base 3
  RTGTXBASE4 BCD*10.3 Retainage Tax Base 4
  RTGTXBASE5 BCD*10.3 Retainage Tax Base 5
  RTGTXAMT1 BCD*10.3 Retainage Tax Amount 1
  RTGTXAMT2 BCD*10.3 Retainage Tax Amount 2
  RTGTXAMT3 BCD*10.3 Retainage Tax Amount 3
  RTGTXAMT4 BCD*10.3 Retainage Tax Amount 4
  RTGTXAMT5 BCD*10.3 Retainage Tax Amount 5
  CUSACCTSET String*6 Customer Account Set
  ENTEREDBY String*8 Entered By
  DATEBUS Date Posting Date
  OPPOLINES Integer Sage CRM Opportunity Lines

## OESHIHO - Shipment Optional Fields (view OE0704)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+OPTFIELD; OPTFIELD+SHIUNIQ
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
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

## OESHIR - Multiple Orders to Shipment (view OE0694)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+LINENUM; SHIUNIQ+ORDUNIQ; ORDUNIQ [D]
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDUNIQ BCD*10.0 Order Uniquifier
  ORDNUMBER String*22 Order Number
  PONUMBER String*22 PO Number

## OESHPP - Shipment Prepayments (view OE0710)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CUSTOMER String*12 Customer Number
  CUSTDESC String*60 Customer Name
  CUSTCURN String*3 Customer Currency
  CRATE BCD*8.7 Cust Rate
  CRATEDATE Date Cust Rate Date
  CRATETYPE String*2 Cust Rate Type
  CRATEOPER Integer Oper. Cust. Curn. to Func.
  DOCTOTAL BCD*10.3 Document Total
  DISCAVAIL BCD*10.3 Discount Available
  AMOUNTDUE BCD*10.3 Amount Due
  BATCHNUM BCD*5.0 Receipt Batch Number
  BANKCODE String*8 Bank Code
  RECPTYPE String*12 Receipt Type
  CHECKNUM String*24 Check/Receipt No.
  RECPDATE Date Receipt Date
  RECPAMOUNT BCD*10.3 Receipt Amount
  BANKCURN String*3 Bank Currency
  RATETYPE String*2 Rate Type
  BANKRATE BCD*8.7 Bank Rate
  RATEDATE Date Rate Date
  PAYMTYPE Integer Payment Type [0=(None),1=Cash,2=Check,3=Credit Card,4=Other,5=SPS Credit Card]
  PAUTHCURR String*3 Pre-auth Currency
  TRANIDPRE String*36 Pre-auth Transaction ID
  TRANIDCAP String*36 Capture Transaction ID
  TRANIDVOID String*36 Void Transaction ID
  PAUTHAMT BCD*10.3 Pre-auth Amount
  CHARGESTTS Integer Credit Card Charge Status [0=None,1=Charged,2=Voided,3=Pending,4=Card Declined,5=Card Error]
  YPPROCCODE String*12 YP Process Code

## OESHTD - Shipment Day End Details (view OE0697)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDNUM+SHIUNIQ+DETAILNUM
Fields (NAME type description [values]):
  DAYENDNUM BCD*10.0 Day End Number
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation
  QTYSHIPPED BCD*10.4 Quantity Shipped
  SHIUNIT String*10 Shipment Unit of Measure
  UNITCONV BCD*10.6 Shipment Unit Conversion
  EXTSCOST BCD*10.3 Extended Shipment Cost
  COG BCD*10.3 Cost of Goods
  OLDQTYSHIP BCD*10.4 Old Quantity Shipped
  OLDSHIUNIT String*10 Old Shipment UOM
  OLDUNITCNV BCD*10.6 Old Shipment Unit Conversion
  OLDEXTSCST BCD*10.3 Old Extended Shipment Cost
  OLDCOG BCD*10.3 Old Cost of Goods
  COSTED Boolean Record Costed [0=No,1=Yes]

## OESHTDD - Shipment Day End Details of Details (view OE0699)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDNUM+SHIUNIQ+DETAILNUM+COMPNUM
Fields (NAME type description [values]):
  DAYENDNUM BCD*10.0 Day End Number
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  COMPNUM Long Component Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation
  QTYSHIPPED BCD*10.4 Quantity Shipped
  SHIUNIT String*10 Shipment Unit of Measure
  UNITCONV BCD*10.6 Shipment Unit Conversion
  EXTSCOST BCD*10.3 Extended Shipment Cost
  COG BCD*10.3 Cost of Goods
  OLDQTYSHIP BCD*10.4 Old Quantity Shipped
  OLDSHIUNIT String*10 Old Shipment UOM
  OLDUNITCNV BCD*10.6 Old Shipment Unit Conversion
  OLDEXTSCST BCD*10.3 Old Extended Shipment Cost
  OLDCOG BCD*10.3 Old Cost of Goods
  COSTED Boolean Record Costed [0=No,1=Yes]

## OESHTDDL - Shipment Day End Kitting Lots (view OE0675)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDNUM+SHIUNIQ+DETAILNUM+COMPNUM+LOTNUMF
Fields (NAME type description [values]):
  DAYENDNUM BCD*10.0 Day End Number
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  COMPNUM Long Component Number
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation
  OLDSTKQTY BCD*10.4 Old Qty in Stocking UOM
  OLDQTY BCD*10.4 Old Lot Quantity
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Lot Quantity
  COST BCD*10.3 Cost

## OESHTDDS - Shipment Day End Kitting Serials (view OE0676)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDNUM+SHIUNIQ+DETAILNUM+COMPNUM+SERIALNUMF
Fields (NAME type description [values]):
  DAYENDNUM BCD*10.0 Day End Number
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  COMPNUM Long Component Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation
  COST BCD*10.3 Cost

## OESHTDL - Shipment Day End Lots (view OE0670)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDNUM+SHIUNIQ+DETAILNUM+LOTNUMF
Fields (NAME type description [values]):
  DAYENDNUM BCD*10.0 Day End Number
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  LOTNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation
  OLDSTKQTY BCD*10.4 Old Qty in Stocking UOM
  OLDQTY BCD*10.4 Old Lot Quantity
  STKQTY BCD*10.4 Quantity in Stocking UOM
  QTY BCD*10.4 Lot Quantity
  COST BCD*10.3 Cost

## OESHTDS - Shipment Day End Serials (view OE0671)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDNUM+SHIUNIQ+DETAILNUM+SERIALNUMF
Fields (NAME type description [values]):
  DAYENDNUM BCD*10.0 Day End Number
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  DETAILNUM Integer Detail Number
  SERIALNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERATION Integer Operation
  COST BCD*10.3 Cost

## OESHTH - Shipments Day End (view OE0698)
Keys (first = PK; D=dups allowed, M=modifiable): DAYENDNUM
Fields (NAME type description [values]):
  DAYENDNUM BCD*10.0 Day End Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SHINUMBER String*22 Shipment Number
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  OPERATION Integer Operation
  SHRATE BCD*8.7 Shipment Rate

## OESTATS - Sales Statistics (view OE0700)
Keys (first = PK; D=dups allowed, M=modifiable): YR+PERIOD+CURRENCY
Fields (NAME type description [values]):
  YR String*4 Year
  PERIOD Integer Period
  CURRENCY String*3 Currency
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NUMORD Long Number of Orders
  QTYSOLD BCD*10.4 Net Quantity Sold
  SALESAMTF BCD*10.3 Net Sales Amount (Func.)
  SALESAMTS BCD*10.3 Net Sales Amount (Srce.)
  INVAMTF BCD*10.3 Net Invoice Amount (Func.)
  INVAMTS BCD*10.3 Net Invoice Amount (Srce.)
  COGSF BCD*10.3 Cost of Sales (Func.)
  COGSS BCD*10.3 Cost of Sales (Srce.)
  INVCOUNT Long Number of Invoices
  AVGINVF BCD*10.3 Average Invoice (Func.)
  AVGINVS BCD*10.3 Average Invoice (Srce.)
  LARGSTINF BCD*10.3 Largest Invoice (Func.)
  LARGSTINS BCD*10.3 Largest Invoice (Srce.)
  LINVCUST String*12 Customer (Largest Invoice)
  SMALSTINF BCD*10.3 Smallest Invoice (Func.)
  SMALSTINS BCD*10.3 Smallest Invoice (Srce.)
  SINVCUST String*12 Customer (Smallest Invoice)
  CNCOUNT Long Number of Credit Notes
  AVGCNF BCD*10.3 Average Credit Note (Func.)
  AVGCNS BCD*10.3 Average Credit Note (Srce.)
  LARGSTCNF BCD*10.3 Largest Credit Note (Func.)
  LARGSTCNS BCD*10.3 Largest Credit Note (Srce.)
  LCNCUST String*12 Customer (Largest Credit Note)
  SMALSTCNF BCD*10.3 Smallest Credit Note (Func.)
  SMALSTCNS BCD*10.3 Smallest Credit Note (Srce.)
  TSLELOSTF BCD*10.3 Total Sales Lost (Func.)
  TSLELOSTS BCD*10.3 Total Sales Lost (Srce.)
  SCNCUST String*12 Customer (Smallest Credit Note)
  DNCOUNT Long Number of Debit Notes
  AVGDNF BCD*10.3 Average Debit Note (Func.)
  AVGDNS BCD*10.3 Average Debit Note (Srce.)
  LARGSTDNF BCD*10.3 Largest Debit Note (Func.)
  LARGSTDNS BCD*10.3 Largest Debit Note (Srce.)
  LDNCUST String*12 Customer (Largest Debit Note)
  SMALSTDNF BCD*10.3 Smallest Debit Note (Func.)
  SMALSTDNS BCD*10.3 Smallest Debit Note (Srce.)
  SDNCUST String*12 Customer (Smallest Debit Note)

## OETERMI - Invoice Payment Schedules (view OE0720)
Keys (first = PK; D=dups allowed, M=modifiable): INVUNIQ+PAYMENT
Fields (NAME type description [values]):
  INVUNIQ BCD*10.0 Invoice Uniquifier
  PAYMENT Integer Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISCBASE BCD*10.3 Discount Base
  DISCDATE Date Discount Date
  DISCPER BCD*5.5 Discount Percentage
  DISCAMT BCD*10.3 Discount Amount
  DUEBASE BCD*10.3 Due Amount Base
  DUEDATE Date Due Date
  DUEPER BCD*5.5 Percentage Due
  DUEAMT BCD*10.3 Amount Due

## OETERMO - Order Payment Schedules (view OE0740)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ+PAYMENT
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  PAYMENT Integer Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISCBASE BCD*10.3 Discount Base
  DISCDATE Date Discount Date
  DISCPER BCD*5.5 Discount Percentage
  DISCAMT BCD*10.3 Discount Amount
  DUEBASE BCD*10.3 Amount Due Base
  DUEDATE Date Due Date
  DUEPER BCD*5.5 Percentage Due
  DUEAMT BCD*10.3 Amount Due

## OETERMS - Shipment Payment Schedules (view OE0745)
Keys (first = PK; D=dups allowed, M=modifiable): SHIUNIQ+PAYMENT
Fields (NAME type description [values]):
  SHIUNIQ BCD*10.0 Shipment Uniquifier
  PAYMENT Integer Payment Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISCBASE BCD*10.3 Discount Base
  DISCDATE Date Discount Date
  DISCPER BCD*5.5 Discount Percentage
  DISCAMT BCD*10.3 Discount Amount
  DUEBASE BCD*10.3 Amount Due Base
  DUEDATE Date Due Date
  DUEPER BCD*5.5 Percentage Due
  DUEAMT BCD*10.3 Amount Due

## OEVIA - Ship-Via Codes (view OE0760)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*6 Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*60 Name
  ADDRESS1 String*60 Address Line 1
  ADDRESS2 String*60 Address Line 2
  ADDRESS3 String*60 Address Line 3
  ADDRESS4 String*60 Address Line 4
  CITY String*30 City
  STATE String*30 State/Province
  ZIP String*20 Zip/Postal Code
  COUNTRY String*30 Country
  PHONE String*30 Phone Number
  FAX String*30 Fax Number
  CONTACT String*60 Contact
  COMMENT String*80 Comment
  EMAIL String*50 Ship-Via E-mail
  PHONEC String*30 Contact Phone
  FAXC String*30 Contact Fax
  EMAILC String*50 Contact E-mail
