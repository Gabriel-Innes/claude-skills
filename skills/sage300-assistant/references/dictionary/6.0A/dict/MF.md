# MF module - compiled AOM dictionary

Types: String*n=CHAR(n); BCD*b.d=DECIMAL(2b-1,d); Date=DECIMAL(9,0) YYYYMMDD; Time=DECIMAL(9,0) HHMMSSHH; Integer=SMALLINT; Long=INT; Boolean=SMALLINT 0/1.

## MFABD - Auto Build Details (view MF0071)
Keys (first = PK; D=dups allowed, M=modifiable): ABUNIQ+LINENUM
Fields (NAME type description [values]):
  ABUNIQ BCD*10.0 Auto Build Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item No.
  ITEMTYPE Integer Item Type [0=Milestone,1=Auto-Build]
  ITEMDESC String*40 Description
  BOMLINE Integer BOM Line
  LEVEL Integer Level
  ORDUOM String*10 UOM
  ORDQTY BCD*10.4 Qty Order
  LOCATION String*6 Location
  QTYONHAND BCD*10.4 Qty On Hand
  RECPQTY BCD*10.4 Receipt Qty
  ISSQTY BCD*10.4 Issue Qty
  MOUNIQ String*250 MO Uniq.
  MONUM String*250 MO Number
  MOSERIES String*250 MO Series
  MOTYPE String*250 MO Type
  DETAILNUM Integer Detail Number
  ISSUELINE Integer Issue line
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]

## MFABDL - Auto Build Line Details (view MF0072)
Keys (first = PK; D=dups allowed, M=modifiable): ABUNIQ+LINENUM; ABUNIQ+DETAILNUM [D]
Fields (NAME type description [values]):
  ABUNIQ BCD*10.0 AutoBuild Uniquifier
  LINENUM Integer Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Parent ID
  COMPID String*24 Component ID
  OPERNO String*5 Oper No.
  ITEMLINE Integer Item Line
  COMPDESC String*40 Component Desc
  LOCATION String*6 Location
  UOM String*10 UOM
  REQQTY BCD*10.4 Request Qty
  ISSQTY BCD*10.4 Issue Qty
  ONHANDQTY BCD*10.4 On Hand Qty
  MOUNIQ String*250 MO Uniq.
  MONUM String*250 MO Number
  MOSERIES String*250 MO Series
  MOTYPE String*250 MO Type
  ITEMRPL String*24 Item Replaced
  BOMLINE Integer BOM Line
  DETAILNUM Integer DETAILNUM
  ITEMTY Integer Item Type [0=,1=Milestone]
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]

## MFABH - Auto Build Header (view MF0070)
Keys (first = PK; D=dups allowed, M=modifiable): ABUNIQ; ABNUM
Fields (NAME type description [values]):
  ABUNIQ BCD*10.0 AutoBuild Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ABNUM String*19 AutoBuild No.
  ITEMNO String*24 Item No.
  ITEMDESC String*60 Item Desc
  BOMNO String*24 BOM No.
  BOMREV String*3 BOM Rev.
  BOMDESC String*40 BOM Desc
  ORDQTYUM BCD*10.4 Order Qty.
  ORDUOM String*10 UOM
  AREACD String*10 Area code
  LOCATION String*6 Location
  ORDERDT Date ORDERDT
  MOREF String*40 MO Reference
  MODESC String*60 MO Description
  POSTED Boolean Posted [0=No,1=Yes]

## MFACSET - Manufacturing Account Set (view MF0010)
Keys (first = PK; D=dups allowed, M=modifiable): ACCTSET
Fields (NAME type description [values]):
  ACCTSET String*6 Account Set Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  WIPCATG String*6 WIP Category
  WIPACCT String*45 WIP
  SETLABACCT String*45 Setup Labor
  RUNLABACCT String*45 Run Labor
  SUBACCT String*45 Subcontract
  OVHACCT String*45 Overhead
  MTVARACCT String*45 Material Variance
  PDVARACCT String*45 Production Variance
  MATERLVAR String*24 Material Variance (NS)
  LABORVAR String*24 Setup Labor Variance (NS)
  RUNLABVAR String*24 Run Labor Variance (NS)
  SUBCONVAR String*24 Subcontract Variance (NS)
  OVHAVAR String*24 Overhead Variance (NS)

## MFALOCD - Allocation Detail (view MF0036)
Keys (first = PK; D=dups allowed, M=modifiable): ALOCUNIQ+LINENUM
Fields (NAME type description [values]):
  ALOCUNIQ BCD*10.0 Allocation Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE Integer Item Line
  COMPID String*24 Component
  COMPDESC String*60 Description
  MOUNIQ BCD*10.0 MO Uniquifier
  MONUM String*16 MO No.
  MOSERIES String*2 MO Series
  MODESC String*60 MO Description
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  COMPUOM String*10 UOM
  ALOCQTY BCD*10.4 Qty to Allocate
  ALOCUOM String*10 UOM
  OPERNO String*5 Oper No.
  SUBCON String*12 Subcontractor Code
  SUBCONDESC String*60 Subcontractor Description
  ALOCDESC String*60 Allocation Description
  REF String*40 Reference

## MFALOCH - Allocations (view MF0035)
Keys (first = PK; D=dups allowed, M=modifiable): ALOCUNIQ; ALOCNO
Fields (NAME type description [values]):
  ALOCUNIQ BCD*10.0 Allocation Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ALOCNO String*19 Allocation Number
  ALOCDT Date Date
  AREACD String*10 Production Area
  AREADESC String*60 Area Description
  ALOCDESC String*60 Description
  ALOCREF String*40 Reference
  VALUES Long Optional Field
  POSTED Boolean Posted [0=No,1=Yes]

## MFALOCO - Allocation Optional Field (view MF0514)
Keys (first = PK; D=dups allowed, M=modifiable): ALOCUNIQ+OPTFIELD; OPTFIELD+ALOCUNIQ
Fields (NAME type description [values]):
  ALOCUNIQ BCD*10.0 Allocation Uniquifier
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

## MFBISSD - Batch Issuance Lines (view MF0048)
Keys (first = PK; D=dups allowed, M=modifiable): BISSUNIQ+ITEMNO+OPERNO; ITEMNO+OPERNO [D]
Fields (NAME type description [values]):
  BISSUNIQ BCD*10.0 Batch Issuance Uniquifier
  ITEMNO String*24 Item
  OPERNO String*5 Oper No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Description
  UOM String*10 UOM
  REQQTY BCD*10.4 Qty Req
  ISSDQTY BCD*10.4 Qty Issued
  ONHANDQTY BCD*10.4 On Hand
  ISSQTY BCD*10.4 Issue Qty
  LOCATION String*6 Location
  ITEMLINE String*250 Item Line
  COMPTYPE Integer Component Type
  MOUNIQ String*250 MO Uniq.
  MONUM String*250 MO Number
  MOSERIES String*250 MO Series
  MOTYPE String*250 MO Type
  REQQTYMO String*250 Req. Qty per MO
  ITEMRPL String*24 Item Replaced
  DETAILNUM Integer Detail line
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]

## MFBISSDL - Batch Issuance Line Details (view MF0064)
Keys (first = PK; D=dups allowed, M=modifiable): BISSUNIQ+ITEMNO+OPERNO+LINENUM; LINENUM [D]
Fields (NAME type description [values]):
  BISSUNIQ BCD*10.0 Batch Issuance Uniquifier
  ITEMNO String*24 Item
  OPERNO String*5 Oper No.
  LINENUM Integer Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE Integer Item Line
  MOUNIQ String*10 MO Uniq.
  MONUM String*16 MO Number
  MOSERIES String*2 MO Series
  MOTYPE Boolean MO Type
  REQQTYMO BCD*10.4 Req. Qty per MO

## MFBISSH - Batch Issuances (view MF0047)
Keys (first = PK; D=dups allowed, M=modifiable): BISSUNIQ; BISSNO
Fields (NAME type description [values]):
  BISSUNIQ BCD*10.0 Batch Issuance Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BISSNO String*19 Issuance No.
  ISSUEDT Date Date
  LOCATION String*6 Location
  AREACD String*10 Production Area
  AREADESC String*60 Description
  BMONUM String*19 Batch MO No.
  USERID String*8 Updated By
  POSTED Boolean Posted [0=No,1=Yes]
  VALUES Long Optional Field

## MFBISSUO - Batch Issuances Optional Field (view MF0508)
Keys (first = PK; D=dups allowed, M=modifiable): BISSUNIQ+OPTFIELD; OPTFIELD+BISSUNIQ
Fields (NAME type description [values]):
  BISSUNIQ BCD*10.0 Batch Issuance Uniquifier
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

## MFBMCOM - Bills of Material Component (view MF0015)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+LINENUM; BOMNO+REVNO+ITEMNO+COMPID [D]
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Parent Item
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPID String*24 Component
  COMPDESC String*60 Description
  COMPTYPE Integer Type [1=Direct,2=Packaging]
  BASIS Integer Basis [0=Variable,1=Fixed]
  REQQTY BCD*10.6 Qty
  COMPUOM String*10 UOM
  LOCATION String*6 Location
  SCRAP BCD*3.2 % Scrap
  ALLOW BCD*3.2 % Allow
  STARTDT Date Start Date
  ENDDT Date End Date
  OPERNO String*5 Operation
  COMMENTS String*250 Comments
  REFERENCE String*40 Reference
  DMCALCOST BCD*10.6 DM Calculated
  PMCALCOST BCD*10.6 PM Calculated
  EXTCOST BCD*10.6 Extended Cost
  SCRAPCOST BCD*10.6 Scrap Cost

## MFBMCP - Bills of Material Co-product (view MF0056)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+LINENUM; BOMNO+REVNO+ITEMNO+CPID [D]
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Parent Item
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CPID String*24 Co-product
  CPDESC String*60 Description
  CPUOM String*10 UOM
  LOCATION String*6 Location
  EXPQTY BCD*10.4 Expected Qty
  COSTALOC BCD*3.2 Cost Allocation
  COMMENTS String*250 Comments

## MFBMIN - Bills of Material Instructions (view MF0053)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+LINENUM
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Parent Item
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INSTR String*250 Instructions

## MFBMOP - Bills of Material Operations (view MF0012)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+LINENUM; BOMNO+REVNO+ITEMNO+OPERNO [D]
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Parent Item
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERNO String*5 Operation
  OPERDESC String*60 Description
  OPERTY Boolean Type [0=Internal,1=Subcontract]
  WCCD String*10 Work Center
  SETUPTIME BCD*10.6 Setup Time
  RUNTIME BCD*10.6 Run Time
  CLEANTIME BCD*10.6 Cleanup Time
  WAITTIME BCD*10.6 Wait Time
  SETUPUOM Integer Setup UOM [1=Hour,2=Minute]
  RUNUOM Integer Run UOM [1=Hour,2=Minute]
  CLEANUOM Integer Cleanup UOM [1=Hour,2=Minute]
  WAITUOM Integer Wait UOM [1=Hour,2=Minute]
  OVERLAP BCD*3.2 % Overlap
  REMARKS String*250 Remarks
  RSCSLCAL BCD*10.6 SL Cost
  RSCDLCAL BCD*10.6 DL Cost
  RSCOVHCAL BCD*10.6 Overhead Cost
  TOOLCAL BCD*10.6 Tool Cost

## MFBMRSC - Bills of Material Resource (view MF0013)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+LINENUM+RESRCENO; RESRCENO [D]
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Parent Item
  LINENUM Integer Line
  RESRCENO String*10 Resource Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RSCDESC String*60 Description
  OPERNO String*5 Operation No.
  RSCTYPE Integer Type [1=Setup Labor,2=Run Labor,3=Overhead]
  UOMTYPE Integer UOM [1=Hour,2=Minute,3=Others]
  REQQTY BCD*10.4 Qty
  UNITCOST BCD*10.6 Unit Cost

## MFBMSUB - Bills of Material Subcontractor (view MF0016)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+VENDOR; VENDOR [D]
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Parent Item
  VENDOR String*12 Vendor Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VENDDESC String*60 Description
  DEFAULT Integer Default? [0=No,1=Yes]
  VENDITEM String*24 Vendor Item Code
  RATING BCD*2.2 Rating
  STATUS Integer Status [1=New,2=Qualified,3=On Hold,4=Barred]
  VENDCTAC String*40 Contact
  VENDCOM String*40 Comments

## MFBMTL - Bills of Material Tool (view MF0014)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+LINENUM+TOOLTYNO; TOOLTYNO [D]
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Parent Item
  LINENUM Integer Line
  TOOLTYNO String*10 Tool Type Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TOOLDESC String*60 Description
  OPERNO String*5 Operation No.
  REQQTY BCD*10.4 Qty
  UNITCOST BCD*10.6 Unit Cost

## MFBOM - Bills of Material (view MF0011)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO; ITEMNO [D]
Fields (NAME type description [values]):
  BOMNO String*24
  REVNO String*3
  ITEMNO String*24
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60
  BOMDESC String*60
  STATUS Integer [1=Under Development,2=Approved,3=On Hold,4=Discontinued]
  LASTMAINDT Date
  CREATEDT Date
  BOMTY Boolean [0=Assembled,1=Phantom]
  BATCHSIZE BCD*8.4
  SETUPQTY BCD*10.4
  DEFAULT Boolean [0=No,1=Yes]
  SUBCON Boolean [0=No,1=Yes]
  COMMENTS String*250
  ECONO String*10
  ECODATE Date
  REF String*40
  AUTHBY String*8
  APPVBY String*8
  EFFTDT Date
  DISCONDT Date
  SRCDOC String*150
  DMATCAL BCD*10.6
  PACKCAL BCD*10.6
  SLCAL BCD*10.6
  DLCAL BCD*10.6
  OVHCAL BCD*10.6
  SUBCONCAL BCD*10.6
  TOOLCAL BCD*10.6
  VALUES Long

## MFBOMI - Item BOM INFO (view MF0063)
Keys (first = PK; D=dups allowed, M=modifiable): SBOMNO+SREVNO+SITEM+ITEMNO+PITEM+TREENO
Fields (NAME type description [values]):
  SBOMNO String*24 Starting BOM No.
  SREVNO String*3 Starting Rev No.
  SITEM String*24 Starting Item
  ITEMNO String*24 Item Number
  PITEM String*24 Parent Item
  TREENO Integer Tree No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BOMLV Integer BOM Level
  QTYPER BCD*10.6 Qty Per
  REQQTY BCD*10.6 Req. Qty
  SCRAP BCD*3.2 % Scrap
  BOMNO String*24 BOM No.
  REVNO String*3 Rev No.

## MFBOMO - Bills of Material Optional Field (view MF0503)
Keys (first = PK; D=dups allowed, M=modifiable): BOMNO+REVNO+ITEMNO+OPTFIELD; OPTFIELD+BOMNO+REVNO+ITEMNO
Fields (NAME type description [values]):
  BOMNO String*24 BOM Number
  REVNO String*3 Revision No.
  ITEMNO String*24 Item Number
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

## MFBORDD - Batch MO Lines (view MF0046)
Keys (first = PK; D=dups allowed, M=modifiable): BMOUNIQ+LINENUM
Fields (NAME type description [values]):
  BMOUNIQ BCD*10.0 Batch MO Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Product
  ITEMDESC String*60 Description
  BOMNO String*24 BOM No.
  REVNO String*3 Rev No.
  ORDQTYUM BCD*10.4 Qty Ordered
  ORDUOM String*10 UOM
  ALLOCATE BCD*3.2 Allocate %
  MOSERIES String*2 MO Series
  MONUM String*16 MO Number
  DETAILDESC String*60 Description
  DETAILREF String*40 Reference
  SDETAILNUM Integer SO Details number

## MFBORDH - Batch MOs (view MF0045)
Keys (first = PK; D=dups allowed, M=modifiable): BMOUNIQ; BMONUM
Fields (NAME type description [values]):
  BMOUNIQ BCD*10.0 Batch MO Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BMONUM String*19 Batch MO Number
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  MOSTATUS Integer MO Status [0=New,1=Approved,2=Released,3=On Hold,4=Closed]
  MOREF String*40 MO Reference
  MODESC String*60 Description
  ORDERDT Date Order Date
  DUEDT Date Due Date
  PLANSDT Date Planned Start
  PLANEDT Date Planned End
  ACTUALSDT Date Actual Start
  ACTUALEDT Date Actual End
  AREACD String*10 Product Area
  PLANNER String*8 Planner
  INCHARGE String*8 In Charge
  ALLOCATE Boolean ALLOCATE?
  APPVBY String*8 Approved By
  APPVDT Date Approved Date
  RELEASEBY String*8 Released By
  RELEASEDT Date Released Date
  VALUES Long Optional Field
  CLOSEBY String*8 Closed By
  CLOSEDT Date Closeout Date

## MFBORDO - Batch MO Optional Field (view MF0505)
Keys (first = PK; D=dups allowed, M=modifiable): BMOUNIQ+OPTFIELD; OPTFIELD+BMOUNIQ
Fields (NAME type description [values]):
  BMOUNIQ BCD*10.0 Batch MO Uniquifier
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

## MFBORDU - Batch MO Lines Date Update (view MF0220)
Keys (first = PK; D=dups allowed, M=modifiable): BMOUNIQ+LINENUM
Fields (NAME type description [values]):
  BMOUNIQ BCD*10.0 Batch MO Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  UPDATE Boolean Update
  BMONUM String*19 Batch MO No.
  SONUM String*22 SO No.
  MOUNIQ BCD*10.0 MO Uniquifier
  MONUM String*16 MO Number
  MOSERIES String*2 MO Series
  NAMECUST String*60 Customer Name
  ORDDATE Date Order Date
  DUEDATE Date Due Date
  ITEMNO String*24 Item No.
  ITEMDESC String*60 Item Description
  ORDUOM String*10 UOM
  ORDQTY BCD*10.4 Order Qty
  PROCESSCMD Integer Process Command
  FRMBMO String*19 Batch MO No. From
  TOBMO String*19 To
  FRMSO String*22 SO No. From
  TOSO String*22 To
  FRMCUST String*12 Customer No. From
  TOCUST String*12 To
  FRMDUE Date Due Date From
  TODUE Date To
  SORDDATE Date Set Order Date to
  SDUEDATE Date Set Due Date to

## MFBRCPD - Batch Receipt Lines (view MF0052)
Keys (first = PK; D=dups allowed, M=modifiable): BRCPUNIQ+LINENUM
Fields (NAME type description [values]):
  BRCPUNIQ BCD*10.0 Batch Receipt Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item
  ITEMDESC String*60 Description
  UOM String*10 UOM
  ORDQTY BCD*10.4 Qty Ordered
  PRODQTY BCD*10.4 Receipt Qty
  RECPQTY BCD*10.4 Qty to Receive
  LOCATION String*6 Location
  MOUNIQ String*10 MO Uniq.
  MONUM String*16 MO No.
  MOSERIES String*250 MO Series
  MOTYPE Integer MO Type
  DETAILNUM Integer Detail line
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]

## MFBRCPH - Batch Receipts (view MF0051)
Keys (first = PK; D=dups allowed, M=modifiable): BRCPUNIQ; BRCPNO
Fields (NAME type description [values]):
  BRCPUNIQ BCD*10.0
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BRCPNO String*19
  RECPDT Date
  LOCATION String*6
  AREACD String*10
  AREADESC String*60
  BMONUM String*19
  USERID String*8
  POSTED Boolean
  VALUES Long

## MFBRCPO - Batch Receipts Optional Field (view MF0512)
Keys (first = PK; D=dups allowed, M=modifiable): BRCPUNIQ+OPTFIELD; OPTFIELD+BRCPUNIQ
Fields (NAME type description [values]):
  BRCPUNIQ BCD*10.0 Batch Receipt Uniquifier
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

## MFBRTND - Batch Return Lines (view MF0050)
Keys (first = PK; D=dups allowed, M=modifiable): BRTNUNIQ+ITEMNO+OPERNO; ITEMNO+OPERNO [D]
Fields (NAME type description [values]):
  BRTNUNIQ BCD*10.0 Batch Return Uniquifier
  ITEMNO String*24 Item
  OPERNO String*5 Oper No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE String*250 Item Line
  ITEMDESC String*60 Description
  UOM String*10 UOM
  REQQTY BCD*10.4 Qty Req
  ISSDQTY BCD*10.4 Qty Issued
  CONSUMED BCD*10.4 Qty Consumed
  SCPDQTY BCD*10.4 Qty Scrapped
  RETNQTY BCD*10.4 Qty to Return
  LOCATION String*6 Location
  REASON String*60 Reason
  COMPTYPE Integer Component Type
  MOUNIQ String*250 MO Uniquifier
  MONUM String*250 MO No.
  MOSERIES String*250 MO Series
  MOTYPE String*250 MO Type
  QTYMO String*250 Iss. Qty per MO
  DETAILNUM Integer Detail line
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]

## MFBRTNDL - Batch Return Line Details (view MF0065)
Keys (first = PK; D=dups allowed, M=modifiable): BRTNUNIQ+ITEMNO+OPERNO+LINENUM; LINENUM [D]
Fields (NAME type description [values]):
  BRTNUNIQ BCD*10.0 Batch Return Uniquifier
  ITEMNO String*24 Item
  OPERNO String*5 Oper No.
  LINENUM Integer Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE Integer Item Line
  MOUNIQ String*10 MO Uniq.
  MONUM String*16 MO Number
  MOSERIES String*2 MO Series
  MOTYPE Boolean MO Type
  QTYMO BCD*10.4 Iss. Qty per MO

## MFBRTNH - Batch Returns (view MF0049)
Keys (first = PK; D=dups allowed, M=modifiable): BRTNUNIQ; BRTNNO
Fields (NAME type description [values]):
  BRTNUNIQ BCD*10.0 Batch Return Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BRTNNO String*19 Return No.
  RETNDT Date Date
  LOCATION String*6 Location
  AREACD String*10 Production Area
  AREADESC String*60 Description
  BMONUM String*19 Batch MO No.
  USERID String*8 Updated By
  POSTED Boolean Posted [0=No,1=Yes]
  VALUES Long Optional Field

## MFBRTNO - Batch Returns Optional Field (view MF0510)
Keys (first = PK; D=dups allowed, M=modifiable): BRTNUNIQ+OPTFIELD; OPTFIELD+BRTNUNIQ
Fields (NAME type description [values]):
  BRTNUNIQ BCD*10.0 Batch Return Uniquifier
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

## MFCHG - Item Number Change (view MF0061)
Keys (first = PK; D=dups allowed, M=modifiable): OLDITEMNO; NEWITEMNO [D,M]
Fields (NAME type description [values]):
  OLDITEMNO String*24 Old Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NEWITEMNO String*24 Current Item Number
  NEWUNFMT String*24 New Unformatted Item Number
  NEWDESCRIP String*60 New Description
  NEWSTKUOM String*10 New Stock UOM
  NEWSEG1 String*60 Segment 1
  NEWSEG2 String*60 Segment 2
  NEWSEG3 String*60 Segment 3
  NEWSEG4 String*60 Segment 4
  NEWSEG5 String*60 Segment 5
  NEWSEG6 String*60 Segment 6
  NEWSEG7 String*60 Segment 7
  NEWSEG8 String*60 Segment 8
  NEWSEG9 String*60 Segment 9
  NEWSEG10 String*60 Segment 10
  ACTION Integer Action [1=Item Number Change,2=Description Change]

## MFCOSTR - Cost Rollup (view MF0400)
Keys (first = PK; D=dups allowed, M=modifiable): TOKEN+BOMNO+BOMREV+ITEMNO
Fields (NAME type description [values]):
  TOKEN String*32 Token
  BOMNO String*24 BOM Number
  BOMREV String*3 BOM Rev.
  ITEMNO String*24 Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## MFGENBD - Create Batch MO from OE Detail (view MF0088)
Keys (first = PK; D=dups allowed, M=modifiable): GENBUNIQ+LINENUM; GENBUNIQ+SONUM
Fields (NAME type description [values]):
  GENBUNIQ BCD*10.0 Tracking Uniquifier
  LINENUM Integer Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SONUM String*22 SO Number
  CUSTNO String*12 Customer No.
  NAMECUST String*60 Customer Name
  DUEDT Date Due Date
  ORDDT Date Order Date
  PLANSDT Date Planned Start
  PLANEDT Date Planned End
  PLANNER String*8 Planner
  SODESC String*60 Description
  SOREF String*40 Reference
  AREACD String*10 Product Area
  CREATEORD Boolean Create Order? [0=No,1=Yes]

## MFGENBDF - Create Batch MO from OE Finder (view MF0089)
Keys (first = PK; D=dups allowed, M=modifiable): ORDUNIQ; ORDNUMBER
Fields (NAME type description [values]):
  ORDUNIQ BCD*10.0 Order Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ORDNUMBER String*16 Order Number
  CUSTOMER String*12 Customer Number
  REFERENCE String*60 Reference
  TYPE Integer Order Type [1=,2=,3=,4=]
  ORDDATE Date Order Date
  DESC String*60 Order Description
  ONHOLD Boolean On Hold Status
  COMMENT String*250 Order Comment
  COMPLETE Integer Order Completed [1=,2=,3=,4=,5=]
  COMPDATE Date Order Completion Date

## MFGENBH - Create Batch MO from OE (view MF0087)
Keys (first = PK; D=dups allowed, M=modifiable): GENBUNIQ; GENBNO
Fields (NAME type description [values]):
  GENBUNIQ BCD*10.0 Tracking Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  GENBNO String*19 Tracking Number
  GENDATE Date Date
  SONUM String*22 SO Number
  CUSTNO String*12 Customer No.
  CALENDAR String*10 Calendar
  CALEDESC String*60 Description
  AREACD String*10 Area Code
  MOSTATUS Integer MO Status [0=New,1=Approved,2=Released]
  GENBREF String*40 Reference
  GENBDESC String*60 Description

## MFGENMO - Create MO (view MF0055)
Keys (first = PK; D=dups allowed, M=modifiable): LINENUM
Fields (NAME type description [values]):
  LINENUM Integer Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CREATEORD Boolean Create Order? [0=No,1=Yes]
  BOMTY Boolean BOM Type [0=Assembled,1=Phantom]
  ITEMNO String*24 Item Code
  ITEMDESC String*60 Description
  BONUM String*19 BOM No.
  UOM String*10 UOM
  DUEDT Date Due Date
  ORDQTY BCD*10.4 Ordered Qty
  AREACD String*10 Product Area
  LOCATION String*6 Location
  TYPE Boolean Type [0=Internal,1=Subcontract]
  PKEY String*24 Parent Key
  TKEY String*24 Key
  SUBCON String*12 Subcontractor

## MFGENOED - Create MO from OE Detail (view MF0042)
Keys (first = PK; D=dups allowed, M=modifiable): GENOEUNIQ+LINENUM
Fields (NAME type description [values]):
  GENOEUNIQ BCD*10.0 Tracking Uniquifier
  LINENUM Integer Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMNO String*24 Item Code
  ITEMDESC String*60 Description
  SOLINENUM Integer SO Line No.
  SONUM String*22 SO Number
  UOM String*10 UOM
  DUEDT Date Due Date
  ORDQTY BCD*10.4 Ordered Qty
  RELQTY BCD*10.4 Released Qty
  TOORDQTY BCD*10.4 To Order Qty
  CUSTNO String*12 Customer No.
  GENREF String*40 Reference
  GENDESC String*60 Description
  AREACD String*10 Product Area
  MONUM String*16 MO Created
  MOSTATUS Integer MO Status [0=New,1=Approved,2=Released]
  BOMLEVEL Integer BOM Level [0=Top Level,1=First Level,2=All Level]

## MFGENOEH - Create MO from OE (view MF0041)
Keys (first = PK; D=dups allowed, M=modifiable): GENOEUNIQ; GENOENO
Fields (NAME type description [values]):
  GENOEUNIQ BCD*10.0 Tracking Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  GENOENO String*19 Tracking Number
  GENDATE Date Date
  SONUM String*22 SO Number
  STARTMO String*16 Starting MO No.
  CUSTNO String*12 Customer No.
  GENREF String*40 Reference
  GENDESC String*60 Description

## MFHIST - Transaction Histories (view MF0039)
Keys (first = PK; D=dups allowed, M=modifiable): DOCNUM+LINENUM+TRANDT+TRANTP; MONUM+MOSERIES [D]; MONUM+MOSERIES+TRANDT+TRANTP [D]; MONUM+MOSERIES+TRANTP [D]
Fields (NAME type description [values]):
  DOCNUM String*19 Document No.
  LINENUM Integer Line No.
  TRANDT Date Transaction Date
  TRANTP Integer Transaction Type [1=Issuance,2=Return,3=Receipt,4=Allocation,5=Scrap,6=MO Closeout,7=Reverse Issuance,8=Reverse Receipt,9=Reverse MO,10=Transfer,11=Reverse Return,12=Reverse Transfer]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MONUM String*16 MO No.
  MOSERIES String*2 MO Series
  MOTYPE Boolean MO Type
  COMPID String*24 Item No.
  COMPTYPE Integer Component Type [1=Direct,2=Packaging]
  QTY BCD*10.4 Quantity
  MATLCOST BCD*10.3 Material Cost
  RCSLCOST BCD*10.3 Setup Labor Cost
  RCRLCOST BCD*10.3 Run Labor Cost
  RCOVHCOST BCD*10.3 Overhead Cost
  SUBCONCOST BCD*10.3 Subcontract Cost
  LOCATION String*6 Location
  USERID String*8 User ID
  COSTED Boolean Costed [0=No,1=Yes]
  LKDOCLINE Integer Linked Doc Line
  REQCOST BCD*10.3 Required Cost
  DAYENDSEQ Long Day End No.
  TRANSSEQ Long Transaction No.
  DELINENO Integer Day End Line No.
  LKDOCNUM String*22 Linked Doc No.
  ITEMLINE Integer Item Line
  UOM String*10 UOM
  CONVERSION BCD*10.6 Conversion

## MFISSUD - Issuance Detail (view MF0030)
Keys (first = PK; D=dups allowed, M=modifiable): ISSUNIQ+LINENUM
Fields (NAME type description [values]):
  ISSUNIQ BCD*10.0 Issuance Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE Integer Item Line
  COMPID String*24 Component
  COMPDESC String*60 Description
  MOUNIQ BCD*10.0 MO Uniquifier
  MONUM String*16 MO No.
  MOSERIES String*2 MO Series
  MODESC String*60 MO Description
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  COMPUOM String*10 UOM
  COMPTYPE Integer Component Type [1=Direct,2=Packaging]
  ISSQTY BCD*10.4 Issue Qty
  ISSUOM String*10 UOM
  LOCATION String*6 Location
  OPERNO String*5 Oper No.
  SUBCON String*12 Subcontractor Code
  SUBCONDESC String*60 Subcontractor Description
  ISSUEDESC String*60 Issuance Description
  REF String*40 Reference
  SHIPLINE Integer Shipment line no.
  ITEMRPL String*24 Item Replaced
  NUMRPL Integer Number Replaced
  DETAILNUM Integer Detail line
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]
  STOCKUNIT String*10 SKU
  SKUQTY BCD*10.4 Qty in SKU
  CONVERSION BCD*10.6 Conversion

## MFISSUH - Issuance (view MF0029)
Keys (first = PK; D=dups allowed, M=modifiable): ISSUNIQ; ISSUENO
Fields (NAME type description [values]):
  ISSUNIQ BCD*10.0 Issuance Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ISSUENO String*19 Issuance Number
  ISSUEDT Date Date
  LOCATION String*6 Location
  AREACD String*10 Production Area
  AREADESC String*60 Area Description
  ISSDESC String*60 Description
  ISSREF String*40 Reference
  VALUES Long Optional Field
  POSTED Boolean Posted [0=No,1=Yes]

## MFISSUO - Issuance Optional Field (view MF0507)
Keys (first = PK; D=dups allowed, M=modifiable): ISSUNIQ+OPTFIELD; OPTFIELD+ISSUNIQ
Fields (NAME type description [values]):
  ISSUNIQ BCD*10.0 Issuance Uniquifier
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

## MFITMCT - Item Costs (view MF0019)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MTLSTD BCD*10.6 Material Cost
  PACKSTD BCD*10.6 Packaging Cost
  SETUPSTD BCD*10.6 Setup Cost
  LABSTD BCD*10.6 Labor Cost
  OVHSTD BCD*10.6 Overhead Cost
  SUBCONSTD BCD*10.6 Subcontract Cost
  TOOLSTD BCD*10.6 Tool Cost

## MFMTMPD - Material Template Details (view MF0097)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE+LINENUM
Fields (NAME type description [values]):
  TEMPLATE String*10 Material Template
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPID String*24 Component ID
  COMPDESC String*60 Component Description
  COMPUOM String*10 UOM
  LOCATION String*6 Location
  TMPQTY BCD*10.9 Qty Per
  COMMENTS String*250 Comments

## MFMTMPH - Material Template (view MF0096)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE
Fields (NAME type description [values]):
  TEMPLATE String*10 Material Template
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  STATUS Boolean Inactive
  COMMENTS String*250 Comments
  DATELASTMN Date Last Maintained

## MFOFD - Optional Fields (view MF0500)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION+OPTFIELD
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Bill of Material,1=MO Entries and Batch MO Enteries,2=Issuances and Batch Issuances,3=Returns and Batch Returns,4=Receipts and Batch Receipts,5=Transfer,6=Allocation,7=WIP Scraps,8=Operations Status]
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
  SWREQUIRED Integer Required [0=No,1=Yes]
  SWSET Integer Value Set [0=No,1=Yes]

## MFOFH - Optional Field Locations (view MF0501)
Keys (first = PK; D=dups allowed, M=modifiable): LOCATION
Fields (NAME type description [values]):
  LOCATION Integer Location [0=Bill of Material,1=MO Entries and Batch MO Enteries,2=Issuances and Batch Issuances,3=Returns and Batch Returns,4=Receipts and Batch Receipts,5=Transfer,6=Allocation,7=WIP Scraps,8=Operations Status]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  VALUES Long Number of Values

## MFOPERD - Operation Work Center (view MF0018)
Keys (first = PK; D=dups allowed, M=modifiable): OPERNO+WCCD; WCCD [D]
Fields (NAME type description [values]):
  OPERNO String*5 Operation No.
  WCCD String*10 Work Center No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## MFOPERH - Operation (view MF0017)
Keys (first = PK; D=dups allowed, M=modifiable): OPERNO
Fields (NAME type description [values]):
  OPERNO String*5 Operation No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERDESC String*60 Description
  OPERTY Boolean Operation Type [0=Internal,1=Subcontract]
  CREATEBY String*8 Created By
  CREATEDT Date Creation Date
  COMMENTS String*250 Comments

## MFOPT - Manufacturing Options (view MF0998)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy Key
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MOLENGTH String*2 Order Number Length
  MOPREFIX String*6 Order Number Prefix
  NEXTMONUM String*14 Next Order Number
  NEXTMOUNIQ BCD*10.0 Next Order Uniquifier
  MSLENGTH String*2 Subcontract Number Length
  MSPREFIX String*6 Subcontract Number Prefix
  NEXTMSNUM String*14 Next Subcontract Number
  NEXTMSUNIQ BCD*10.0 Next Subcontract Uniquifier
  KBLENGTH String*2 Kanban Number Length
  KBPREFIX String*6 Kanban Number Prefix
  NEXTKBNUM String*14 Next Kanban Number
  NEXTKBUNIQ BCD*10.0 Next Kanban Uniquifier
  ISLENGTH String*2 Issuance Number Length
  ISPREFIX String*6 Issuance Number Prefix
  NEXTISNUM String*17 Next Issuance Number
  NEXTISUNIQ BCD*10.0 Next Issuance Uniquifier
  RTLENGTH String*2 Return Number Length
  RTPREFIX String*6 Return Number Prefix
  NEXTRTNUM String*17 Next Return Number
  NEXTRTUNIQ BCD*10.0 Next Return Uniquifier
  RCLENGTH String*2 Receipt Number Length
  RCPREFIX String*6 Receipt Number Prefix
  NEXTRCNUM String*17 Next Receipt Number
  NEXTRCUNIQ BCD*10.0 Next Receipt Uniquifier
  ALLENGTH String*2 Allocation Number Length
  ALPREFIX String*6 Allocation Number Prefix
  NEXTALNUM String*17 Next Allocation Number
  NEXTALUNIQ BCD*10.0 Next Allocation Uniquifier
  SCLENGTH String*2 Scrap Number Length
  SCPREFIX String*6 Scrap Number Prefix
  NEXTSCNUM String*17 Next Scrap Number
  NEXTSCUNIQ BCD*10.0 Next Scrap Uniquifier
  GSLENGTH String*2 SO to MO Tracking Number Length
  GSPREFIX String*6 SO to MO Tracking Number Prefix
  NEXTGSNUM String*17 Next SO to MO Tracking Number
  NEXTGSUNIQ BCD*10.0 Next SO to MO Tracking Uniquifie
  UDLENGTH String*2 Operation Entry Length
  UDPREFIX String*6 Operation Entry Prefix
  NEXTUDNUM String*17 Next Operation Entry Number
  NEXTUDUNIQ BCD*10.0 Next Operation Entry Uniquifier
  BOLENGTH String*2 Bactch MO Number Length
  BOPREFIX String*6 Bactch MO Prefix
  NEXTBONUM String*17 Next Batch MO Number
  NEXTBOUNIQ BCD*10.0 Next Batch MO Uniquifier
  BSLENGTH String*2 Batch Issuance Number Length
  BSPREFIX String*6 Batch Issuance Number Prefix
  NEXTBSNUM String*17 Next Batch Issuance Number
  NEXTBSUNIQ BCD*10.0 Next Batch Issuance Uniquifier
  BTLENGTH String*2 Batch Return Number Length
  BTPREFIX String*6 Batch Return Number Prefix
  NEXTBTNUM String*17 Next Batch Return Number
  NEXTBTUNIQ BCD*10.0 Next Batch Return Uniquifier
  BCLENGTH String*2 Batch Receipt Number Length
  BCPREFIX String*6 Batch Receipt Number Prefix
  NEXTBCNUM String*17 Next Batch Receipt Number
  NEXTBCUNIQ BCD*10.0 Next Batch Receipt Uniquifier
  TFLENGTH String*2 Transfer Number Length
  TFPREFIX String*6 Transfer Number Prefix
  NEXTTFNUM String*17 Next Transfer Number
  NEXTTFUNIQ BCD*10.0 Next Transfer Uniquifier
  GBLENGTH String*2 GB Number Length
  GBPREFIX String*6 GB Number Prefix
  NEXTGBNUM String*17 Next GB Number
  NEXTGBUNIQ BCD*10.0 Next GB Uniquifier
  QTLENGTH String*2 Quotation Number Length
  QTPREFIX String*6 Quotation Number Prefix
  NEXTQTNUM String*17 Next Quotation Number
  NEXTQTUNIQ BCD*10.0 Next Quotation Uniquifier
  ABLENGTH String*2 AutoBuild Number Length
  ABPREFIX String*6 AutoBuild Number Prefix
  NEXTABNUM String*17 Next AutoBuild Number
  NEXTABUNIQ BCD*10.0 Next AutoBuild Uniquifier
  JOLENGTH String*2 Job Number Length
  JOPREFIX String*6 Job Number Prefix
  NEXTJONUM String*17 Next Job Number
  FRMTFLOC String*6 Transfer From Location
  TOTFLOC String*6 Transfer To Location
  AUTOCLSMO Boolean Allow Auto-close MO [0=No,1=Yes]
  ADVARIANCE Boolean Closeout Variance [0=No,1=Yes]
  GLACCTRES Boolean Assign G/L Account per Resource [0=No,1=Yes]
  USEALPHA Boolean Use alpha-numeric BOM Version [0=No,1=Yes]
  CLSTOL BCD*3.2 Auto-close Tolerance
  MOSERIES Boolean Activate MO Series Functionality [0=No,1=Yes]
  LCOSTDEC Boolean Allow 6 decimal Standard Unit Co [0=No,1=Yes]
  RECNOISS Boolean Allow Receive without Issuance [0=No,1=Yes]
  EXISSTOL Integer Exceed Issue Tolerance [0=None,1=Warning,2=Error]
  ISSTOL BCD*3.2 Issue Tolerance
  EXRECTOL Integer Exceed Receipt Tolerance [0=None,1=Warning,2=Error]
  RECTOL BCD*3.2 Receipt Tolerance
  COSTMETH Integer Costing Method [0=Average,1=Standard]
  LOCATION String*6 Location
  AREACD String*10 Production Area
  AREADESC String*60 Area Description
  SPLITBATCH Boolean Split SO into multiple Batch MO [0=No,1=Yes]
  LSTRANUSER String*8 User
  LSTRANDATE Date Date
  LSTRANTIME Time Time
  MOSTATUS Integer Default MO Status [0=New,1=Approved,2=Released]
  COPROSTD Integer Closeout Method [0=Standard,1=Adjust to Main Product,2=Distribute Cost]

## MFOPUDD - MO Operation Entry Line (view MF0044)
Keys (first = PK; D=dups allowed, M=modifiable): UDTUNIQ+LINENUM
Fields (NAME type description [values]):
  UDTUNIQ BCD*10.0 Update Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MONUM String*16 MO Number
  MOSERIES String*250 MO Series
  OPERNO String*5 Operation No.
  OPDESC String*60 Description
  DUEDATE Date Expected Due
  STARTDATE Date Actual Start
  ENDDATE Date Actual End
  REQQTY BCD*10.4 Req. Qty
  BALQTY BCD*10.4 Balance
  PRODQTY BCD*10.4 Prod. Qty
  SCRAPQTY BCD*10.4 Scrap Qty
  CHANGED Boolean Changed
  REF String*250 Reference/Comments

## MFOPUDH - MO Operation Entry (view MF0043)
Keys (first = PK; D=dups allowed, M=modifiable): UDTUNIQ; UDTNO
Fields (NAME type description [values]):
  UDTUNIQ BCD*10.0 Update Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  UDTNO String*19 Update Number
  UDTDATE Date Date
  USERID String*8 User ID
  UDTREF String*40 Reference
  UDTDESC String*60 Description
  VALUES Long Optional Field
  POSTED Boolean Posted

## MFOPUDO - Operation Status Optional Field (view MF0516)
Keys (first = PK; D=dups allowed, M=modifiable): UDTUNIQ+OPTFIELD; OPTFIELD+UDTUNIQ
Fields (NAME type description [values]):
  UDTUNIQ BCD*10.0 Update Uniquifier
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

## MFORDCH - Manufacturing Order Children (view MF0040)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+MONUM+MOSERIES; MONUM+MOSERIES [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  MONUM String*16 MO Number
  MOSERIES String*2 MO Series
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## MFORDCP - Manufacturing Order Co-product (view MF0057)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+LINENUM; MOUNIQ+CPID [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CPID String*24 Co-product
  CPDESC String*60 Description
  BASIS Integer [0=Variable,1=Fixed]
  CPUOM String*10 UOM
  LOCATION String*6 Location
  QTYPER BCD*10.6 Qty per Item
  BOMQTY BCD*10.6 BOM Exp. Qty
  BATCHQTY BCD*8.4 BOM Batch Qty
  EXPQTY BCD*10.4 Expected Qty
  COSTALOC BCD*3.2 Cost Allocation
  COMMENTS String*250 Comments
  RCPQTY BCD*10.4 Receipt Qty
  LASTRECDT Date Last Receipt Date

## MFORDD - Manufacturing Order Material (view MF0023)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+LINENUM; COMPID [D]; MOUNIQ+DETAILNUM [D]; MOUNIQ+COMPID [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPID String*24 Component
  COMPDESC String*60 Description
  COMPUOM String*10 UOM
  COMPTYPE Integer Type [1=Direct,2=Packaging]
  LOCATION String*6 Location
  BOMQTY BCD*10.9 Qty per Item
  BOMREQQTY BCD*10.6 BOM Req. Qty
  BATCHQTY BCD*8.4 BOM Batch Qty
  SCRAP BCD*3.2 % Scrap
  REQQTY BCD*10.4 Req. Qty
  ISSUEQTY BCD*10.4 Issued Qty
  SCRAPQTY BCD*10.4 Scrapped Qty
  LASTISSDT Date Last Issued
  LASTALDT Date Last Allocated
  CONSUMED BCD*10.4 Consumed
  REQDATE Date Date Required
  OPERNO String*5 Operation
  COMMENTS String*250 Comments
  REFERENCE String*40 Reference
  DETAILNUM Integer Detail line
  DMPROJCOST BCD*10.3 DM Proj Cost
  PMPROJCOST BCD*10.3 PM Proj Cost
  PARENTID String*24 Parent ID

## MFORDH - Manufacturing Orders (view MF0022)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ; MONUM+MOSERIES; BOMNO+BOMREV [D,M]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MONUM String*16 Mfg Order Number
  MOSERIES String*2 Series
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  MOSTATUS Integer MO Status [0=New,1=Approved,2=Released,3=On Hold,4=Closed,5=Reverse]
  BATCHMO Boolean Batch MO [0=No,1=Yes]
  MOCATEGORY Integer MO Category [0=Internal,1=Subcontract,2=Kanban,3=Backflush,4=Job]
  ITEMNO String*24 Item Number
  ITEMDESC String*60 Item Description
  SUBCON String*12 Subcontractor
  MOREF String*60 MO Reference
  MODESC String*60 Description
  ORDQTY BCD*10.4 Qty Ordered (Stock Unit)
  STKUOM String*10 Stock UOM
  ORDQTYUM BCD*10.4 Qty Ordered
  ORDUOM String*10 UOM
  PRODQTY BCD*10.4 Qty Produced
  BOMNO String*24 BOM No.
  BOMREV String*3 Version
  BOMDESC String*60 BOM Description
  ORDERDT Date Order Date
  DUEDT Date Due Date
  PLANSDT Date Planned Start
  PLANEDT Date Planned End
  ACTUALSDT Date Actual Start
  ACTUALEDT Date Actual End
  AREACD String*10 Product Area
  PLANNER String*8 Planner
  INCHARGE String*8 In Charge
  APPVBY String*8 Approved By
  APPVDT Date Approved Date
  RELEASEBY String*8 Released By
  RELEASEDT Date Released Date
  CLOSEBY String*8 Closed By
  CLOSEDT Date Closeout Date
  SONUM String*22 SO Number
  SODUEDT Date SO Due Date
  SOREF String*60 SO Reference
  SOCUST String*12 Customer
  SOORDQTY BCD*10.4 Qty Ordered
  SOUNIT String*10 UOM
  SOLOC String*6 SO Location
  SODESC String*60 SO Description
  SOITEMLINE Integer Item Line
  OPERTMP String*10 Operation Template
  MATTMP String*10 Material Template
  COMMENTS String*250 Comments
  RAWMATPJ BCD*10.6 Raw Matl Proj
  PACKPJ BCD*10.6 Packaging Proj
  SLABPJ BCD*10.6 Setup Labor Proj
  DLABPJ BCD*10.6 Direct Labor Proj
  OVHPJ BCD*10.6 Overhead Proj
  SUBCONPJ BCD*10.6 Subcontract Proj
  TOOLPJ BCD*10.6 Tool Proj
  SLABACT BCD*10.3 Setup Labor Actual
  DLABACT BCD*10.3 Direct Labor Actual
  OVHACT BCD*10.3 Overhead Actual
  SUBCONACT BCD*10.3 Subcontract Actual
  TOOLACT BCD*10.3 Tool Actual
  LASTRECDT Date Last Receipt Date
  RESERVELS Boolean Reserved Lot/Serial [0=No,1=Yes]
  VALUES Long Optional Field

## MFORDIN - Manufacturing Order Instructions (view MF0054)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+LINENUM
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INSTR String*250 Instructions

## MFORDL - Reserve Lot for MO (view MF0210)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+LOTNUMF
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  LOTNUMF String*40 Lot Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  USED Boolean Used?

## MFORDO - Manufacturing Order Optional Field (view MF0504)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+OPTFIELD; OPTFIELD+MOUNIQ
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
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

## MFORDOP - Manufacturing Order Operations (view MF0024)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+LINENUM; MOUNIQ+OPERNO [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERNO String*5 Operation
  DESC String*60 Description
  OPERTY Boolean Type [0=Internal,1=Subcontract]
  WCCD String*10 Work Center
  SETUPTIME BCD*10.6 Proj. Setup Time
  RUNTIME BCD*10.6 Proj. Run Time
  CLEANTIME BCD*10.6 Proj. Clean Tme
  WAITTIME BCD*10.6 Proj. Wait Time
  SETUPUOM Integer UOM [1=Hour,2=Minute]
  RUNUOM Integer UOM [1=Hour,2=Minute]
  CLEANUOM Integer UOM [1=Hour,2=Minute]
  WAITUOM Integer UOM [1=Hour,2=Minute]
  ASETUPTIME BCD*10.6 Actual Setup Time
  ARUNTIME BCD*10.6 Actual Run Time
  ACLEANTIME BCD*10.6 Actual Clean Tme
  AWAITTIME BCD*10.6 Actual Wait Time
  ASETUPUOM Integer UOM [1=Hour,2=Minute]
  ARUNUOM Integer UOM [1=Hour,2=Minute]
  ACLEANUOM Integer UOM [1=Hour,2=Minute]
  AWAITUOM Integer UOM [1=Hour,2=Minute]
  STARTDT Date Start Date
  ENDDT Date End Date
  REMARKS String*250 Remarks
  SLSCOST BCD*10.6 SL Std Cost
  SLACOST BCD*10.3 SL Actual Cost
  RLSCOST BCD*10.6 RL Std Cost
  RLACOST BCD*10.3 RL Actual Cost
  OVHSCOST BCD*10.6 Overhead Std Cost
  OVHACOST BCD*10.3 Overhead Actual Cost
  TLSCOST BCD*10.6 Tool Std Cost
  TLACOST BCD*10.3 Tool Actual Cost
  PARENTID String*24 Parent ID
  RCREQQTY BCD*10.6 Resource Req. Qty
  BATCHSIZE BCD*8.4 Batchsize
  MODESC String*60

## MFORDPO - Manufacturing Order Purchases (view MF0028)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+PONUM+ITEMLINE; PONUM [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  PONUM String*22 PO No.
  ITEMLINE BCD*10.0 Item Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## MFORDRC - Manufacturing Order Resources (view MF0025)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+LINENUM+RESRCENO; RESRCENO [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  LINENUM Integer Line
  RESRCENO String*10 Resource
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERNO String*5 Operation No.
  RSCTYPE Integer Resource Type [1=Setup Labor,2=Run Labor,3=Overhead]
  UOMTYPE Integer UOM Type [1=Hour,2=Minute,3=Others]
  REQQTY BCD*10.4 Required Qty
  USEDQTY BCD*10.4 Used Qty
  UNITCOST BCD*10.6 Unit Cost
  ACTUALCOST BCD*10.3 Actual Cost
  BOMREQQTY BCD*10.6 BOM Req. Qty

## MFORDS - Reserve Serial for MO (view MF0211)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+SERNUMF
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  SERNUMF String*40 Serial Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  USED Boolean Used?

## MFORDSC - Manufacturing Order Subcontracts (view MF0027)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+MONUM+MOSERIES; MONUM+MOSERIES [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  MONUM String*16 Subcon No.
  MOSERIES String*2 MO Series
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## MFORDSO - Manufacturing Order Sales (view MF0058)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+SONUM+ITEMLINE; SONUM [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  SONUM String*22 SO No.
  ITEMLINE Integer Item Line No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6

## MFORDTL - Manufacturing Order Tools (view MF0026)
Keys (first = PK; D=dups allowed, M=modifiable): MOUNIQ+LINENUM+TOOLCODE; TOOLCODE [D]
Fields (NAME type description [values]):
  MOUNIQ BCD*10.0 Mfg Order Uniquifier
  LINENUM Integer Line
  TOOLCODE String*10 Tool
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERNO String*5 Operation No.
  REQQTY BCD*10.4 Required Qty
  USEDQTY BCD*10.4 Used Qty
  ACTUALCOST BCD*10.3 Actual Cost

## MFOTMPD - Operation Template Details (view MF0099)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE+LINENUM; TEMPLATE+OPERNO [D]
Fields (NAME type description [values]):
  TEMPLATE String*10 Operation Template
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERNO String*5 Operation
  DESC String*60 Description
  OPERTY Boolean Type [0=Internal,1=Subcontract]
  WCCD String*10 Work Center
  SETUPTIME BCD*10.6 Setup Time
  RUNTIME BCD*10.6 Run Time
  CLEANTIME BCD*10.6 Cleanup Time
  WAITTIME BCD*10.6 Wait Time
  SETUPUOM Integer Setup UOM [1=Hour,2=Minute]
  RUNUOM Integer Run UOM [1=Hour,2=Minute]
  CLEANUOM Integer Cleanup UOM [1=Hour,2=Minute]
  WAITUOM Integer Wait UOM [1=Hour,2=Minute]
  REMARKS String*250 Remarks
  RSCSLCAL BCD*10.6 Mfg Order Uniquifier
  RSCDLCAL BCD*10.6 Lot Number
  RSCOVHCAL BCD*10.6 Used?
  TOOLCAL BCD*10.6

## MFOTMPH - Operation Template (view MF0098)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE
Fields (NAME type description [values]):
  TEMPLATE String*10 Operation Template
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  STATUS Boolean Inactive
  COMMENTS String*250 Comments
  DATELASTMN Date Last Maintained

## MFOTMPRC - Operation Template Resources (view MF0100)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE+LINENUM+RESRCENO; RESRCENO [D]
Fields (NAME type description [values]):
  TEMPLATE String*10 Template
  LINENUM Integer Line
  RESRCENO String*10 Resource Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RSCDESC String*40 Description
  OPERNO String*5 Operation No.
  RSCTYPE Integer Type [1=Setup Labor,2=Run Labor,3=Overhead]
  UOMTYPE Integer UOM [1=Hour,2=Minute,3=Others]
  REQQTY BCD*10.4 Qty
  UNITCOST BCD*10.6 Unit Cost

## MFOTMPTL - Operation Template Tools (view MF0101)
Keys (first = PK; D=dups allowed, M=modifiable): TEMPLATE+LINENUM+TOOLTYNO; TOOLTYNO [D]
Fields (NAME type description [values]):
  TEMPLATE String*10 Template
  LINENUM Integer Line
  TOOLTYNO String*10 Tool Type Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TOOLDESC String*40 Description
  OPERNO String*5 Operation No.
  REQQTY BCD*10.4 Qty
  UNITCOST BCD*10.6 Unit Cost

## MFPRDARE - Production Area Master (view MF0004)
Keys (first = PK; D=dups allowed, M=modifiable): AREACD
Fields (NAME type description [values]):
  AREACD String*10 Area Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  AREATY Boolean Area Type [0=Internal,1=Subcontract]
  STATUS Boolean Status [0=Active,1=Inactive]
  ADDR1 String*40 Address Line 1
  ADDR2 String*40 Address Line 2
  ADDR3 String*40 Address Line 3
  ADDR4 String*40 Address Line 4
  CTACNAME String*20 Contact Person
  CTACPOS String*20 Contact Position
  TEXTPHON String*20 Telephone No.
  TEXTFAX String*20 Fax No.
  TEXTEMAIL String*35 Email Address
  LOCATION String*6 IC Location

## MFPRDUSR - Production Area User (view MF0005)
Keys (first = PK; D=dups allowed, M=modifiable): AREACD+PRDUSERID; PRDUSERID [D]
Fields (NAME type description [values]):
  AREACD String*10 Area Code
  PRDUSERID String*8 User ID
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  USERDESC String*60 User Description

## MFQMOC - Quick MO Closeout (view MF0059)
Keys (first = PK; D=dups allowed, M=modifiable): LINENUM
Fields (NAME type description [values]):
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CREATEMO Boolean Closeout? [0=No,1=Yes]
  DUEDT Date Due Date
  MONUM String*16 Mfg Order Number
  MOSERIES String*2 Series
  MOTYPE Boolean [0=Internal,1=Subcontract]
  ITEMNO String*24 Product Code
  ITEMDESC String*60 Product Description
  ORDUOM String*10 UOM
  ORDQTYUM BCD*10.4 Ordered Quantity
  RCVQTYUM BCD*10.4 Received Quantity
  COMPLETE BCD*3.2 % Comp
  MODESC String*60 Description
  MOREF String*40 MO Reference

## MFQORD - Quick MO Entry (view MF0060)
Keys (first = PK; D=dups allowed, M=modifiable): TOKEN+LINENUM
Fields (NAME type description [values]):
  TOKEN String*32 TOKEN
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MONUM String*16 Mfg Order Number
  MOSERIES String*2 Series
  MOTYPE Integer MO Type [0=Internal,1=Subcontract]
  MOSTATUS Integer MO Status [0=New,1=Approved,2=Released,3=On Hold,4=Closed]
  BATCHMO Boolean Batch MO [0=No,1=Yes]
  ITEMNO String*24 Product Code
  ITEMDESC String*60 Product Description
  SUBCON String*12 Subcontractor
  MOREF String*40 MO Reference
  MODESC String*60 Description
  ORDQTY BCD*10.4 Qty Ordered (Stock Unit)
  STKUOM String*10 Stock UOM
  ORDQTYUM BCD*10.4 Qty Ordered
  ORDUOM String*10 UOM
  PRODQTY BCD*10.4 Qty Produced
  BOMNO String*24 BOM No.
  BOMREV String*3 Version
  BOMDESC String*60 BOM Description
  ORDERDT Date Order Date
  DUEDT Date Due Date
  PLANSDT Date Planned Start
  PLANEDT Date Planned End
  ACTUALSDT Date Actual Start
  ACTUALEDT Date Actual End
  AREACD String*10 Product Area
  PLANNER String*8 Planner
  INCHARGE String*8 In Charge
  APPVBY String*8 Approved By
  APPVDT Date Approved Date
  RELEASEBY String*8 Released By
  RELEASEDT Date Released Date
  CLOSEBY String*8 Closed By
  CLOSEDT Date Closeout Date
  SONUM String*22 SO Number
  SODUEDT Date SO Due Date
  SOREF String*60 SO Reference
  SOCUST String*12 Customer
  SOORDQTY BCD*10.4 Qty Ordered
  SOUNIT String*10 UOM
  SOLOC String*6 SO Location
  SODESC String*60 SO Description
  COMMENTS String*250 Comments
  RAWMATPJ BCD*10.3 Raw Matl Proj
  PACKPJ BCD*10.3 Packaging Proj
  SLABPJ BCD*10.3 Setup Labor Proj
  DLABPJ BCD*10.3 Direct Labor Proj
  OVHPJ BCD*10.3 Overhead Proj
  SUBCONPJ BCD*10.3 Subcontract Proj
  TOOLPJ BCD*10.3 Tool Proj
  SLABACT BCD*10.3 Setup Labor Actual
  DLABACT BCD*10.3 Direct Labor Actual
  OVHACT BCD*10.3 Overhead Actual
  SUBCONACT BCD*10.3 Subcontract Actual
  TOOLACT BCD*10.3 Tool Actual
  LASTRECDT Date Last Receipt Date
  VALUES Long
  VENDOR String*12 Vendor

## MFQTED - Manufacturing Quotation Material (view MF0081)
Keys (first = PK; D=dups allowed, M=modifiable): QTUNIQ+LINENUM; COMPID [D]; QTUNIQ+DETAILNUM [D]; QTUNIQ+COMPID [D]
Fields (NAME type description [values]):
  QTUNIQ BCD*10.0 Mfg Quotation Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  COMPID String*24 Item No.
  COMPDESC String*60 Item Description
  COMPUOM String*10 UOM
  COMPTYPE Integer Type [1=Direct,2=Packaging]
  LOCATION String*6 Location
  BASIS Integer Basis [0=Variable,1=Fixed]
  BOMQTY BCD*10.9 BOM Qty
  BOMREQQTY BCD*10.6 Required Qty
  BATCHQTY BCD*8.4 BATCH Qty
  OPERNO String*5 Oper No.
  SCRAP BCD*3.2 Scrap %
  REQQTY BCD*10.4 Required quantity
  UNITCOST BCD*10.6 Unit Cost
  EXTCOST BCD*10.6 Extended Cost
  DETAILNUM Integer Detail Number
  COMMENTS String*250 Comments
  DMPROJCOST BCD*10.6 DM Proj Cost
  PMPROJCOST BCD*10.6 PM Proj Cost

## MFQTEH - Manufacturing Quotation (view MF0080)
Keys (first = PK; D=dups allowed, M=modifiable): QTUNIQ; QTNUM
Fields (NAME type description [values]):
  QTUNIQ BCD*10.0 Mfg Quotation Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  QTNUM String*19 Mfg Quotation Number
  REVNO String*3 Revision No.
  QTSTATUS Integer Status [0=New,1=Approved,2=Revised,3=Converted]
  IDCUST String*12 Customer No.
  NAMECUST String*60 Customer Name
  ITEMNO String*24 Item No.
  ITEMDESC String*60 Item Description
  QTREF String*40 Reference
  QTDESC String*60 Description
  CONTRACT String*19 Contact
  RFQNO String*19 RFQ No.
  DWINFO String*60 Drawing Info.
  BOMNO String*24 BOM No.
  BOMREV String*3 BOM Rev No.
  BOMDESC String*40 BOM Description
  BATCHSIZE BCD*8.4 BOM Batch Size
  QTDT Date Quote Date
  DUEDT Date Due Date
  EXPDT Integer Days Good
  LASTRVDT Date Last Revised
  APPDT Date Approved Date
  CONDT Date Converted Date
  LINKSO String*19 Linked SO
  LINKMO String*19 Linked MO
  QTY1 BCD*10.4 Quantity 1
  QTY2 BCD*10.4 Quantity 2
  QTY3 BCD*10.4 Quantity 3
  QTY4 BCD*10.4 Quantity 4
  QTY5 BCD*10.4 Quantity 5
  QTUOM String*10 UOM
  COMMENTS String*250 Comments
  SRCDOC String*150 Source Document
  MATCAL1 BCD*10.6 Material Calculated Cost 1
  MATCAL2 BCD*10.6 Material Calculated Cost 2
  MATCAL3 BCD*10.6 Material Calculated Cost 3
  MATCAL4 BCD*10.6 Material Calculated Cost 4
  MATCAL5 BCD*10.6 Material Calculated Cost 5
  LABCAL1 BCD*10.6 Labour Calculated Cost 1
  LABCAL2 BCD*10.6 Labour Calculated Cost 2
  LABCAL3 BCD*10.6 Labour Calculated Cost 3
  LABCAL4 BCD*10.6 Labour Calculated Cost 4
  LABCAL5 BCD*10.6 Labour Calculated Cost 5
  SLABCAL1 BCD*10.6
  SLABCAL2 BCD*10.6
  SLABCAL3 BCD*10.6
  SLABCAL4 BCD*10.6
  SLABCAL5 BCD*10.6
  RLABCAL1 BCD*10.6
  RLABCAL2 BCD*10.6
  RLABCAL3 BCD*10.6
  RLABCAL4 BCD*10.6
  RLABCAL5 BCD*10.6
  OVHCAL1 BCD*10.6 Overhead Calculated Cost 1
  OVHCAL2 BCD*10.6 Overhead Calculated Cost 2
  OVHCAL3 BCD*10.6 Overhead Calculated Cost 3
  OVHCAL4 BCD*10.6 Overhead Calculated Cost 4
  OVHCAL5 BCD*10.6 Overhead Calculated Cost 5
  SUBCAL1 BCD*10.6 Subcontract Calculated Cost 1
  SUBCAL2 BCD*10.6 Subcontract Calculated Cost 2
  SUBCAL3 BCD*10.6 Subcontract Calculated Cost 3
  SUBCAL4 BCD*10.6 Subcontract Calculated Cost 4
  SUBCAL5 BCD*10.6 Subcontract Calculated Cost 5
  TOTALCAL1 BCD*10.3 Total Calculated Cost 1
  TOTALCAL2 BCD*10.3 Total Calculated Cost 2
  TOTALCAL3 BCD*10.3 Total Calculated Cost 3
  TOTALCAL4 BCD*10.3 Total Calculated Cost 4
  TOTALCAL5 BCD*10.3 Total Calculated Cost 5
  UNITCAL1 BCD*10.6 Unit Calculated Cost 1
  UNITCAL2 BCD*10.6 Unit Calculated Cost 2
  UNITCAL3 BCD*10.6 Unit Calculated Cost 3
  UNITCAL4 BCD*10.6 Unit Calculated Cost 4
  UNITCAL5 BCD*10.6 Unit Calculated Cost 5
  MATPER1 BCD*3.3 Material 1 - Margin %
  MATPER2 BCD*3.3 Material 2 - Margin %
  MATPER3 BCD*3.3 Material 3 - Margin %
  MATPER4 BCD*3.3 Material 4 - Margin %
  MATPER5 BCD*3.3 Material 5 - Margin %
  LABPER1 BCD*3.3 Labor 1 - Margin %
  LABPER2 BCD*3.3 Labor 2 - Margin %
  LABPER3 BCD*3.3 Labor 3 - Margin %
  LABPER4 BCD*3.3 Labor 4 - Margin %
  LABPER5 BCD*3.3 Labor 5 - Margin %
  OVHPER1 BCD*3.3 Overhead 1 - Margin %
  OVHPER2 BCD*3.3 Overhead 2 - Margin %
  OVHPER3 BCD*3.3 Overhead 3 - Margin %
  OVHPER4 BCD*3.3 Overhead 4 - Margin %
  OVHPER5 BCD*3.3 Overhead 5 - Margin %
  SUBCONPER1 BCD*3.3 Subcontract 1 - Margin %
  SUBCONPER2 BCD*3.3 Subcontract 2 - Margin %
  SUBCONPER3 BCD*3.3 Subcontract 3 - Margin %
  SUBCONPER4 BCD*3.3 Subcontract 4 - Margin %
  SUBCONPER5 BCD*3.3 Subcontract 5 - Margin %
  TOTCOST1 BCD*10.3 Quotation Total 1
  TOTCOST2 BCD*10.3 Quotation Total 2
  TOTCOST3 BCD*10.3 Quotation Total 3
  TOTCOST4 BCD*10.3 Quotation Total 4
  TOTCOST5 BCD*10.3 Quotation Total 5
  PERUNIT1 BCD*10.6 Quote Per unit 1
  PERUNIT2 BCD*10.6 Quote Per unit 2
  PERUNIT3 BCD*10.6 Quote Per unit 3
  PERUNIT4 BCD*10.6 Quote Per unit 4
  PERUNIT5 BCD*10.6 Quote Per unit 5
  GROSSMGIN1 BCD*3.3 Gross Margin 1 %
  GROSSMGIN2 BCD*3.3 Gross Margin 2 %
  GROSSMGIN3 BCD*3.3 Gross Margin 3 %
  GROSSMGIN4 BCD*3.3 Gross Margin 4 %
  GROSSMGIN5 BCD*3.3 Gross Margin 5 %

## MFQTEIN - Manufacturing Quotation Instructions (view MF0085)
Keys (first = PK; D=dups allowed, M=modifiable): QTUNIQ+LINENUM
Fields (NAME type description [values]):
  QTUNIQ BCD*10.0 Mfg Quotation Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  INSTR String*250 Instructions

## MFQTEOP - Manufacturing Quotation Operations (view MF0082)
Keys (first = PK; D=dups allowed, M=modifiable): QTUNIQ+LINENUM; QTUNIQ+OPERNO [D]
Fields (NAME type description [values]):
  QTUNIQ BCD*10.0 Mfg Quotation Uniquifier
  LINENUM Integer Line Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  OPERNO String*5 Operation No.
  DESC String*40 Description
  OPERTY Boolean Type [0=Internal,1=Subcontract]
  WCCD String*10 Work Center
  SETUPTIME BCD*10.6 Setup Time
  RUNTIME BCD*10.6 Run Time
  CLEANTIME BCD*10.6 Cleanup Time
  WAITTIME BCD*10.6 Wait Time
  SETUPUOM Integer Setup UOM [1=Hour,2=Minute]
  RUNUOM Integer Run UOM [1=Hour,2=Minute]
  CLEANUOM Integer Clean UOM [1=Hour,2=Minute]
  WAITUOM Integer Wait UOM [1=Hour,2=Minute]
  EXTCOST BCD*10.6 Extended Cost
  COMMENTS String*250 Comments
  SLSCOST BCD*10.6 SL Std Cost
  SLACOST BCD*10.3 SL Actual Cost
  RLSCOST BCD*10.6 RL Std Cost
  RLACOST BCD*10.3 RL Actual Cost
  OVHSCOST BCD*10.6 Overhead Std Cost
  OVHACOST BCD*10.3 Overhead Actual Cost
  TLSCOST BCD*10.6 Tool Std Cost
  TLACOST BCD*10.3 Tool Actual Cost

## MFQTERC - Manufacturing Quotation Resources (view MF0084)
Keys (first = PK; D=dups allowed, M=modifiable): QTUNIQ+LINENUM+RESRCENO; RESRCENO [D]
Fields (NAME type description [values]):
  QTUNIQ BCD*10.0 Mfg Quotation Uniquifier
  LINENUM Integer Line Number
  RESRCENO String*10 Resource Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*40 Description
  OPERNO String*5 Operation No.
  RSCTYPE Integer Resource Type [1=Setup Labor,2=Run Labor,3=Overhead]
  BASIS Integer Basis [0=Variable,1=Fixed]
  UOMTYPE Integer UOM [1=Hour,2=Minute,3=Others]
  REQQTY BCD*10.4 Required Qty
  UNITCOST BCD*10.6 Unit Cost
  ACTUALCOST BCD*10.3 Actual Cost

## MFQTETL - Manufacturing Quotation Tools (view MF0083)
Keys (first = PK; D=dups allowed, M=modifiable): QTUNIQ+LINENUM+TOOLCODE; TOOLCODE [D]
Fields (NAME type description [values]):
  QTUNIQ BCD*10.0 Mfg Quotation Uniquifier
  LINENUM Integer Line Number
  TOOLCODE String*10 Tool Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*40 Description
  OPERNO String*5 Operation No.
  BASIS Integer Basis [0=Variable,1=Fixed]
  REQQTY BCD*10.4 Required Qty
  UNIT String*10 Unit
  UNITCOST BCD*10.6 Unit Cost
  ACTUALCOST BCD*10.3 Actual Cost

## MFQTHT - Manufacturing Quotation History (view MF0086)
Keys (first = PK; D=dups allowed, M=modifiable): QTNUM+REVNO
Fields (NAME type description [values]):
  QTNUM String*19 Quotation No.
  REVNO String*3 Revision No.
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  APPBY String*8 Approved By
  APPDT Date Approved Date

## MFRECPD - Receipt Detail (view MF0034)
Keys (first = PK; D=dups allowed, M=modifiable): RECPUNIQ+LINENUM
Fields (NAME type description [values]):
  RECPUNIQ BCD*10.0 Receipt Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ASEMCODE String*24 Assembly Code
  ASEMDESC String*60 Assembly Description
  MOUNIQ BCD*10.0 MO Uniquifier
  MONUM String*16 MO No.
  MOSERIES String*2 MO Series
  MODESC String*60 MO Description
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  RECPQTY BCD*10.4 Receipt Qty
  RECPUOM String*10 UOM
  LOCATION String*6 Location
  SUBCON String*12 Subcontractor Code
  SUBCONDESC String*60 Subcontractor Description
  RECPDESC String*60 Receipt Description
  REF String*40 Reference
  SHIPLINE Integer Shipment line no.
  DETAILNUM Integer Detail line
  CLOSED Boolean Closed
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]
  ITEMLINE Integer Item Line
  PRODTYPE Integer Product Type [1=Main Product,2=Co-product]
  STOCKUNIT String*10 SKU
  ORDQTYUM BCD*10.4 Receipt Qty in SKU
  CONVERSION BCD*10.6 Conversion

## MFRECPH - Receipts (view MF0033)
Keys (first = PK; D=dups allowed, M=modifiable): RECPUNIQ; RECPNO
Fields (NAME type description [values]):
  RECPUNIQ BCD*10.0 Receipt Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RECPNO String*19 Receipt Number
  RECPDT Date Date
  LOCATION String*6 Location
  AREACD String*10 Production Area
  AREADESC String*60 Area Description
  RCPDESC String*60 Description
  RCPREF String*40 Reference
  VALUES Long Optional Field
  POSTED Boolean Posted [0=No,1=Yes]

## MFRECPO - Receipts Optional Field (view MF0511)
Keys (first = PK; D=dups allowed, M=modifiable): RECPUNIQ+OPTFIELD; OPTFIELD+RECPUNIQ
Fields (NAME type description [values]):
  RECPUNIQ BCD*10.0 Receipt Uniquifier
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

## MFRESMAS - Resource Master (view MF0001)
Keys (first = PK; D=dups allowed, M=modifiable): RESRCENO
Fields (NAME type description [values]):
  RESRCENO String*10 Resource Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  STATUS Integer Status [1=Active,2=Inactive,3=Discontinued]
  TYPE Integer Cost Type [1=Setup Labor,2=Run Labor,3=Overhead]
  UNITCOST BCD*10.6 Cost
  UOMTYPE Integer UOM [1=Hour,2=Minute,3=Others]
  UNIT String*10 UOM
  RSCACCT String*45 G/L Account
  ACCTDESC String*60
  LASTMAINDT Date Last Maintained
  MAINBY String*8 Maintained By
  CONSUMED BCD*10.4 Consumed
  COMMENTS String*250 Comments
  BASIS Integer Cost Basis [0=Run Time,1=Setup Time,2=Order Quantity]

## MFRETND - Return Detail (view MF0032)
Keys (first = PK; D=dups allowed, M=modifiable): RETNUNIQ+LINENUM
Fields (NAME type description [values]):
  RETNUNIQ BCD*10.0 Return Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE Integer Item Line
  COMPID String*24 Component
  COMPDESC String*60 Description
  MOUNIQ BCD*10.0 MO Uniquifier
  MONUM String*16 MO No.
  MOSERIES String*2 MO Series
  MODESC String*60 MO Description
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  COMPUOM String*10 UOM
  COMPTYPE Integer Component Type [1=Direct,2=Packaging]
  RETNQTY BCD*10.4 Qty to Return
  RETNUOM String*10 UOM
  LOCATION String*6 Location
  OPERNO String*5 Oper No.
  SUBCON String*12 Subcontractor Code
  SUBCONDESC String*60 Subcontractor Description
  REASON String*60 Reason
  RETNDESC String*60 Return Description
  REF String*40 Reference
  SHIPLINE Integer Shipment line no.
  DETAILNUM Integer Detail line
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]
  STOCKUNIT String*10 SKU
  SKUQTY BCD*10.4 Qty in SKU
  CONVERSION BCD*10.6 Conversion

## MFRETNH - Returns (view MF0031)
Keys (first = PK; D=dups allowed, M=modifiable): RETNUNIQ; RETNNO
Fields (NAME type description [values]):
  RETNUNIQ BCD*10.0 Return Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  RETNNO String*19 Return Number
  RETNDT Date Date
  LOCATION String*6 Location
  AREACD String*10 Production Area
  AREADESC String*60 Area Description
  RTNDESC String*60 Description
  RTNREF String*40 Reference
  VALUES Long Optional Field
  POSTED Boolean Posted [0=No,1=Yes]

## MFRETNO - Return Optional Field (view MF0509)
Keys (first = PK; D=dups allowed, M=modifiable): RETNUNIQ+OPTFIELD; OPTFIELD+RETNUNIQ
Fields (NAME type description [values]):
  RETNUNIQ BCD*10.0 Return Uniquifier
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

## MFRST - Restart Maintenance (view MF0062)
Keys (first = PK; D=dups allowed, M=modifiable): RSTNUM
Fields (NAME type description [values]):
  RSTNUM Integer Restart Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DOCUNIQ BCD*10.0 Document Number
  DOCNUM String*19 Document Uniquifier
  SCREENNUM String*10 Screen Number
  PROCESSTBL String*10 Processing Table
  RSTSTATUS Integer Status [0=,1=]
  RSTMSG String*250 Message

## MFSCRPD - Scrap Details (view MF0038)
Keys (first = PK; D=dups allowed, M=modifiable): SCRPUNIQ+LINENUM
Fields (NAME type description [values]):
  SCRPUNIQ BCD*10.0 Scrap Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE Integer Item Line
  COMPID String*24 Component
  COMPDESC String*60 Description
  MOUNIQ BCD*10.0 MO Uniquifier
  MONUM String*16 MO No.
  MOSERIES String*2 MO Series
  MODESC String*60 MO Description
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  SCRPQTY BCD*10.4 Scrap Qty
  SCRPUOM String*10 UOM
  SUBCON String*12 Subcontractor Code
  SUBCONDESC String*60 Subcontractor Description
  SCRPDESC String*60 Scrap Description
  REF String*40 Reference

## MFSCRPH - Scraps (view MF0037)
Keys (first = PK; D=dups allowed, M=modifiable): SCRPUNIQ; SCRPNO
Fields (NAME type description [values]):
  SCRPUNIQ BCD*10.0 Scrap Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SCRPNO String*19 Scrap Number
  SCRPDT Date Date
  AREACD String*10 Production Area
  AREADESC String*60 Area Description
  SCRPDESC String*60 Description
  SCRPREF String*40 Reference
  VALUES Long Optional Field
  POSTED Boolean Posted [0=No,1=Yes]

## MFSCRPO - Scrap Optional Field (view MF0515)
Keys (first = PK; D=dups allowed, M=modifiable): SCRPUNIQ+OPTFIELD; OPTFIELD+SCRPUNIQ
Fields (NAME type description [values]):
  SCRPUNIQ BCD*10.0 Scrap Uniquifier
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

## MFSTATUS - MO Status (view MF0997)
Keys (first = PK; D=dups allowed, M=modifiable): DUMMY
Fields (NAME type description [values]):
  DUMMY Integer Dummy
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  MOIMPORT Boolean MO Import? [0=No,1=Yes]
  NEXTMOUNIQ BCD*10.0 Next MO UNIQ

## MFSUBSD - Substitute Items (view MF0021)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO+SUBST; SUBST [D]
Fields (NAME type description [values]):
  ITEMNO String*24 Item Code
  SUBST String*24 Substitute Item
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  SUBSTDESC String*60 Description
  QTY BCD*10.4 Qty Per
  UOM String*10 UOM
  PRIORITY BCD*3.2 Priority
  COMMENTS String*40 Comments

## MFSUBSH - Items (view MF0020)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMNO
Fields (NAME type description [values]):
  ITEMNO String*24 Item Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMDESC String*60 Description

## MFTFD - MF Transfer Detail (view MF0074)
Keys (first = PK; D=dups allowed, M=modifiable): TFUNIQ+LINENUM
Fields (NAME type description [values]):
  TFUNIQ BCD*10.0 Transfer Uniquifier
  LINENUM Integer Line
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITEMLINE Integer Item Line
  COMPID String*24 Component
  COMPDESC String*60 Description
  MOUNIQ BCD*10.0 MO Uniquifier
  MONUM String*16 MO No.
  MOSERIES String*2 MO Series
  MODESC String*60 MO Description
  MOTYPE Boolean MO Type [0=Internal,1=Subcontract]
  COMPUOM String*10 UOM
  COMPTYPE Integer Component Type [1=Direct,2=Packaging]
  REQQTY BCD*10.4 Req. Qty
  QTYONHAND BCD*10.4 On Hand Qty
  TFQTY BCD*10.4 Transfer Qty.
  TFUOM String*10 UOM
  LOCFR String*6 Location From
  OPERNO String*5 Oper No.
  TFDESC String*60 Transfer Description
  REF String*40 Reference
  COMMENTS String*60 Comments
  TRANSLINE Integer Transfer line no.
  DETAILNUM Integer Detail line
  ISLOTITEM Boolean Lot Item [0=No,1=Yes]
  ISSNITEM Boolean S/N Item [0=No,1=Yes]

## MFTFH - MF Transfer Header (view MF0073)
Keys (first = PK; D=dups allowed, M=modifiable): TFUNIQ; TFNUM
Fields (NAME type description [values]):
  TFUNIQ BCD*10.0 Transfer Uniquifier
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  TFNUM String*19 Transfer Number
  TFDT Date Date
  AREACD String*10 Production Area
  AREADESC String*60 Area Description
  TFDESC String*60 Description
  TFREF String*40 Reference
  FRMLOC String*6 Location From
  TOLOC String*6 Location To
  MLACT Boolean ML Active [0=No,1=Yes]
  VALUES Long Optional Field
  POSTED Boolean Posted [0=No,1=Yes]

## MFTFO - MF Transfer Optional Field (view MF0513)
Keys (first = PK; D=dups allowed, M=modifiable): TFUNIQ+OPTFIELD; OPTFIELD+TFUNIQ
Fields (NAME type description [values]):
  TFUNIQ BCD*10.0 Transfer Uniquifier
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

## MFTOOL - Tool Master (view MF0003)
Keys (first = PK; D=dups allowed, M=modifiable): TOOLCODE
Fields (NAME type description [values]):
  TOOLCODE String*10 Tool Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  STATUS Integer Status [1=Active,2=Inactive,3=Discontinued]
  TOOLTYNO String*10 Tool Type
  RECEIPTDT Date Receipt Date
  RECEIVEBY String*15 Received By
  SUPPLIER String*12 Supplier
  RECEIPTNO String*15 Receipt Number
  PONO String*15 PO Number
  SERIALNO String*15 Serial Number
  CUSTODIAN String*15 Custodian
  EXPREPLDT Date Replacement Date
  LASTMAINDT Date Last Maintained
  MAINBY String*8 Maintained By
  UNITCOST BCD*10.6 Cost per Unit
  UNIT String*10 UOM
  ORIGQTY BCD*10.4 Original Quantity
  CONSUMED BCD*10.4 Consumed
  COMMENTS String*250 Comments

## MFTOOLTY - Tool Type (view MF0002)
Keys (first = PK; D=dups allowed, M=modifiable): TOOLTYNO
Fields (NAME type description [values]):
  TOOLTYNO String*10 Tool Type
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  STATUS Integer Status [1=Active,2=Inactive,3=Discontinued]
  UNITCOST BCD*10.6 Cost per Unit
  UNIT String*10 UOM
  LASTMAINDT Date Last Maintained
  MAINBY String*8 Maintained By
  CONSUMED BCD*10.4 Consumed
  COMMENTS String*250 Comments

## MFWCRSC - Work Center Resource (view MF0008)
Keys (first = PK; D=dups allowed, M=modifiable): WCCD+RESRCENO; RESRCENO [D]
Fields (NAME type description [values]):
  WCCD String*10 Work Center
  RESRCENO String*10 Resource Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  RSCTYPE Integer Type [1=Setup Labor,2=Run Labor,3=Overhead]
  COMPUBAS Integer Basis [0=Fixed,1=Variable]
  UOMTYPE Integer UOM [1=Hour,2=Minute,3=Others]
  UNIT String*10 UOM
  REQQTY BCD*10.4 Quantity
  UNITCOST BCD*10.6 Unit Cost

## MFWCSHF - Work Center Shift (view MF0007)
Keys (first = PK; D=dups allowed, M=modifiable): WCCD+SHIFTNUM; SHIFTNUM [D]
Fields (NAME type description [values]):
  WCCD String*10 Work Center
  SHIFTNUM Integer Shift
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  REGULAR BCD*5.3 Regular Hours
  OVERTIME BCD*5.3 Overtime Hours
  STATINUSE Integer Stations in Use

## MFWCTL - Work Center Tool (view MF0009)
Keys (first = PK; D=dups allowed, M=modifiable): WCCD+TOOLTYNO; TOOLTYNO [D]
Fields (NAME type description [values]):
  WCCD String*10 Work Center
  TOOLTYNO String*10 Tool Type Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  COMPUBAS Integer Basis [0=Fixed,1=Variable]
  UNIT String*10 UOM
  REQQTY BCD*10.4 Quantity
  UNITCOST BCD*10.6 Unit Cost

## MFWORK - Work Center Master (view MF0006)
Keys (first = PK; D=dups allowed, M=modifiable): WCCD
Fields (NAME type description [values]):
  WCCD String*10 Work Center
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*60 Description
  WCTY Integer Work Center Type [1=Normal,2=Fixed]
  SETUPTIME BCD*5.3 Setup Time
  RUNTIME BCD*5.3 Run Time
  CLEANTIME BCD*5.3 Cleanup Time
  WAITTIME BCD*5.3 Wait Time
  SETUPUOM Integer Setup UOM [1=Hour,2=Minute]
  RUNUOM Integer Run UOM [1=Hour,2=Minute]
  CLEANUOM Integer Cleanup UOM [1=Hour,2=Minute]
  WAITUOM Integer Wait UOM [1=Hour,2=Minute]
  WORKAREA String*40 Work Area
  STATCOUNT Long No. of Stations
  STDSETLAB BCD*5.3 Std Setup Labor
  STDRUNLAB BCD*5.3 Std Run Labor
  LASTMAINDT Date Last Changed
  MAINBY String*8 Changed By
  STDEFF BCD*3.2 Std Efficiency
  STDUTL BCD*3.2 Std Utilization
  COMMENTS String*250 Comments
  TOTRSCCOST BCD*10.6 Total Resource Cost
  TOTTLCOST BCD*10.6 Total Tool Cost
