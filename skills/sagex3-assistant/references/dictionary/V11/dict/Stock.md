<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Stock module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## BENCHTRS (BTS) - Plan transaction
Notes: differs in V9.0 P12 (diff: AT3_BENCHTRS.htm); differs in V10 P1 (diff: ATD_BENCHTRS.htm)
Keys (first = PK; D = duplicates allowed): BTS0 BTSTYP+BTSNUM; BTS1 BTSNUM+BTSTYP
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[BTS]ACSCOD (ACCCOD) !Block
  ALLO M*4 WO not alloc. [menu 1: 1=No,2=Yes] act:MWM
  APPBUY M*4 External repl [menu 1: 1=No,2=Yes]
  APPINT M*4 Internal supply [menu 1: 1=No,2=Yes]
  APPLAN M*4 Order [menu 1: 1=No,2=Yes]
  APPPLN M*4 Request [menu 1: 1=No,2=Yes]
  APPSUG M*4 Suggestion [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  AVSTOCOD1 M*15 Available stock [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AVSTOSCR1 M*15 Available stock [menu 99: 1=Form and table,2=Form,3=Table]
  BOMFLG M*4 BOM tracking [menu 1: 1=No,2=Yes]
  BTSDES A*35 Description
  BTSNUM TRS Transaction
  BTSTYP C*2 Transaction type
  BTSTYPCAR A*2 Alpha no.
  BUYER M*4 Buyer [menu 1: 1=No,2=Yes]
  CCECOD M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCECODS M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCESCR M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table] act:ANA
  CONSMAT M*15 Material consumption [menu 354: 1=For expected quantity on first track,2=By quantity produced (limited),3=By quantity produced (unlimited)]
  CPLUPDFLG M*4 Preloading [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRIT M*4(12) Critical [menu 1: 1=No,2=Yes]
  CRIT1 M*15 Criteria 1 [menu 2302: 1=Expected completion date,2=Work order,3=Released product,4=Work center]
  CRIT2 M*15 Criteria 2 [menu 2302: 1=Expected completion date,2=Work order,3=Released product,4=Work center]
  DAC C*4(70) Order
  DBENCHTRS TRS Planning workbench
  DEFFOR A*3 Formula
  DESAXX AX3 Description
  DETALL M*4 Detailed allocations [menu 1: 1=No,2=Yes] act:MWM
  DIVFLG M*4 Work center tracking [menu 1: 1=No,2=Yes]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENTCOD GAU Automatic journal -> [GAU]GAU0 =[BTS]ENTCOD (GAUTACE) !Block
  ENTCODS GAU Auto journal code -> [GAU]GAU0 =[BTS]ENTCODS (GAUTACE) !Block
  EXPNUM L*8 Export number
  FILTDEF M*15 Filter default value [menu 355: 1=Not closed,2=Closed,3=All]
  FILTFLG M*15 Filter [menu 35: 1=Entered,2=Displayed,3=Hidden]
  FLD AVA(70) Field
  FMI M*4 Mfg request [menu 1: 1=No,2=Yes]
  GAMFLG M*4 Routing tracking [menu 1: 1=No,2=Yes]
  GESAFF M*15 User [menu 35: 1=Entered,2=Displayed,3=Hidden]
  GFY AGF Group -> [AGF]AGF0 =[BTS]GFY (AGRPFCY) !Block
  HORDEM M*4 Forecast offset [menu 1: 1=No,2=Yes]
  ICPYFLG M*3 Intercompany [menu 2744: 1=Display all,2=Only display intercompany orders,3=Do not display intercompany orders]
  IDECOD1 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD2 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDESCR1 M*18 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR2 M*18 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  INTBUY M*4 Inter-site transfer [menu 1: 1=No,2=Yes]
  INTLAN M*4 Firm [menu 1: 1=No,2=Yes]
  INTPLN M*4 Planning [menu 1: 1=No,2=Yes]
  INTSUG M*4 Suggestion [menu 1: 1=No,2=Yes]
  ITMFLG M*4 Prod reporting [menu 1: 1=No,2=Yes]
  ITMFLTFLG M*15 Filter [menu 355: 1=Not closed,2=Closed,3=All]
  LAN M*4(12) Firm [menu 1: 1=No,2=Yes]
  LOCCOD M*15 Location [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOCSCR M*15 Location [menu 99: 1=Form and table,2=Form,3=Table]
  LOTCOD M*15 Lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOTSCR M*15 Lot [menu 99: 1=Form and table,2=Form,3=Table]
  MATFLG M*4 Material consumption [menu 1: 1=No,2=Yes]
  MATFLTFLG M*15 Filter [menu 355: 1=Not closed,2=Closed,3=All]
  MATRICULE M*4 Employee ID entry [menu 1: 1=No,2=Yes]
  MCLFLG M*4 Technical sheet plan [menu 1: 1=No,2=Yes]
  MCLTRS TRS Technical sheet plan
  MFGMODFLT M*15 Release method [menu 2371: 1=Full,2=Materials only,3=Operations only,4=All]
  MFGTRS TRS Startup
  MILFLG M*4 Production plan [menu 1: 1=No,2=Yes]
  MILTRS TRS Production plan
  MMLFLG M*4 Consumption plan [menu 1: 1=No,2=Yes]
  MMLTRS TRS Consumption plan
  MODALL M*15 Allocation method [menu 398: 1=Manual,2=Automatic (global),3=Automatic (detailed)] act:MWM
  MOLFLG M*4 Time tracking schedule [menu 1: 1=No,2=Yes]
  MOLTRS TRS Time tracking schedule
  MREFLG M*4 Reintegration plan [menu 1: 1=No,2=Yes]
  MRETRS TRS Reintegration plan
  MRPFLG M*15 Suggestions origin [menu 2312: 1=MPS,2=MRP,3=All]
  MVTDESCOD M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESCOD1 M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESSCR M*15 Movement description [menu 99: 1=Form and table,2=Form,3=Table]
  NBRCOL C*2 No. of fixed columns
  NBRFLD C*2 Field nb
  NBRLIG C*4 Number of lines
  NBSLOFLG M*4 Sub-lot no. [menu 1: 1=No,2=Yes]
  NCRIT M*4(12) Not critical [menu 1: 1=No,2=Yes]
  OFFLG M*4 WO tracking [menu 1: 1=No,2=Yes]
  OPEUOMMOD M*4 Unit can be modified [menu 1: 1=No,2=Yes]
  OPEUOMTYP M*15 Default unit [menu 2314: 1=Unit of operation,2=Unit of stock]
  OVRALL M*4 Global allocations [menu 1: 1=No,2=Yes] act:MWM
  PICKTRS TRS Grouping
  PLANNER M*4 Planner [menu 1: 1=No,2=Yes]
  PLN M*4(12) Planned [menu 1: 1=No,2=Yes]
  PLNLAN M*4 Startup [menu 1: 1=No,2=Yes]
  PLNPLN M*4 Planning [menu 1: 1=No,2=Yes]
  PLNSUG M*4 Suggestion [menu 1: 1=No,2=Yes]
  PRNCOD1 M*15 Printing [menu 708: 1=No print,2=Labels,3=.,4=Transfer document,5=Analysis document]
  PRNNBFLG1 M*4 No. prints [menu 1: 1=No,2=Yes]
  PRNNBSCR1 M*15 No. prints [menu 99: 1=Form and table,2=Form,3=Table]
  PRNSCR1 M*15 Printing [menu 99: 1=Form and table,2=Form,3=Table]
  QTYSAI M*15 Release quantity [menu 377: 1=None,2=Technical lot,3=Economic lot]
  REBUT M*4 Reject entry [menu 1: 1=No,2=Yes]
  REM M*4 With message [menu 1: 1=No,2=Yes]
  RES M*4 To re-plan [menu 1: 1=No,2=Yes]
  RET M*4 Late [menu 1: 1=No,2=Yes]
  RUP M*4 Shortage [menu 1: 1=No,2=Yes]
  SCOLAN M*4 Release STR [menu 1: 1=No,2=Yes]
  SCOPLN M*4 Planning STR [menu 1: 1=No,2=Yes]
  SCOSUG M*4 Suggestion STR [menu 1: 1=No,2=Yes]
  SCOTRS TRS EO auto transaction
  SERCOD M*15 Starting serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD1 M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERESCR M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERESCR1 M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERSCR M*15 Starting serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SLOCOD M*15 Sublot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SLOSCR M*15 Sublot [menu 99: 1=Form and table,2=Form,3=Table]
  SPERFLG M*4 Expiration [menu 1: 1=No,2=Yes]
  SPOTFLG M*4 Potency [menu 1: 1=No,2=Yes]
  SRGWAIFLG M*4 Receipt at dock [menu 1: 1=No,2=Yes]
  SRUB1FLG M*4 Heading 1 [menu 1: 1=No,2=Yes]
  SRUB2FLG M*4 Section 2 [menu 1: 1=No,2=Yes]
  SRUB3FLG M*4 Section 3 [menu 1: 1=No,2=Yes]
  SRUB4FLG M*4 Section 4 [menu 1: 1=No,2=Yes]
  STACOD M*15 Status [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STASCR M*15 Status [menu 99: 1=Form and table,2=Form,3=Table]
  STKFLG M*4 Automatic issue [menu 1: 1=No,2=Yes]
  STOCODDEF M*15 Stock withdrawal [menu 227: 1=Immediate,2=Backflush,3=All]
  STOCODMAN M*4 Manual only [menu 1: 1=No,2=Yes]
  SUG M*4(12) Suggested [menu 1: 1=No,2=Yes]
  TECMODSAI M*15 Entry mode [menu 2342: 1=By tracking number,2=By tracking date,3=By work order number,4=By work center]
  TRACE M*4 Linked trace file [menu 1: 1=No,2=Yes]
  TRSCNL M*4 Inquiry transaction [menu 1: 1=No,2=Yes]
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSCODS ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  TRSFAMS ADI Transaction group -> [ADI]CODE =9;TRSFAMS (ATABDIV) !Block
  TYPQTY M*15 Quantity type [menu 2311: 1=Active,2=Physical]
  UOMSAI M*4 Entry in PAC [menu 1: 1=No,2=Yes]
  UOMSAIFLG M*4 UOM entry [menu 1: 1=No,2=Yes]
  UOMSAIFLG1 M*4 Enter PAC [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRHCOD M*15 Warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHOBY M*15 Single warehouse [menu 1: 1=No,2=Yes]

## CBNDET (CBD) - MRP detail
Notes: differs in V9.0 P12 (diff: AT3_CBNDET.htm)
Keys (first = PK; D = duplicates allowed): CBD0 STOFCY+ITMREF+BUC+REQDAT+WIPTYP+WIPNUM; CBD1 STOFCY+SUGTYP+SUGSTA+SUGNUM (D); CBD2 STOFCY+ITMREF+WIPTYP+WIPSTA (D); CBD3 ITMREF+STOFCY+BUC+REQDAT+WIPTYP+WIPNUM; CBD4 ITMREFORI+STOFCY+WIPTYP+WIPSTA (D)
Fields:
  ALLQTY QTY Allocated quantity
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Delete
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMOFS C*4 Operation lead time
  BOMOPE OPE Operation number
  BPRNUM BPR Source BP -> [BPR]BPR0 =[CBD]BPRNUM (BPARTNER) !Other
  BUC C*4 Period
  COVQTY QTY Coverage quantity
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEMBUC L*8 Demand period
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  ENDDAT D End date
  EXPNUM L*8 Export number
  EXTQTY QTY Planned quantity
  ITMREF ITM Product -> [ITM]ITM0 =[CBD]ITMREF (ITMMASTER) !BSRA
  ITMREFORI ITM Source product -> [ITM]ITM0 =[CBD]ITMREFORI (ITMMASTER) !BSRA
  MRPDAT D MRP date
  MRPMES M*15 MRP message [menu 318: 1=No action,2=Advance,3=Delay,4=Increase,5=Reduce,6=Cancel,7=Advance/Increase,8=Advance/Reduce,9=Delay/Increase,10=Delay/Reduce,11=Delay firm horizon,12=Obsolete product (end of life),13=Overstock,14=Invalid routing version]
  MRPQTY QTY MRP quantity
  MTOQTY QTY Quantity assigned
  MTOREF MTO MTO network -> [MTO]MTO0 =MTOREF (MTOHEAD) !RTZ
  PJT PJT Source project -> [PIM]PIM0 =[CBD]PJT (PIMPL) !BSRA
  REQDAT D Requirement date
  REQQTY QTY Demand/Supply
  RMNEXTQTY QTY Remaining quantity
  RPLFLG M*4 Re-planning flag [menu 1: 1=No,2=Yes]
  STOFCY FCY Storage site -> [FCY]FCY0 =[CBD]STOFCY (FACILITY) !Block
  STOQTY QTY Available stock
  STRDAT D Start date
  SUGNUM VCR Order no.
  SUGSTA M*1 WIP status [menu 342: 1=F,2=P,3=S,4=C]
  SUGTYP M*2 Order type [menu 341: 1=SO,2=PO,3=MS,4=SC,5=WO,6=MW,7=TR,8=TP,9=BW,10=VD,11=VR,12=CR,13=EO,14=MT]
  TRCFLG M*4 Log [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CBD]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WIP M*4 In progress [menu 1: 1=No,2=Yes]
  WIPLINORI L*8 Source line
  WIPNUM VCR Order no.
  WIPNUMORI VCR Source order no.
  WIPSEQORI L*8 Source sequence
  WIPSTA M*1 WIP status [menu 342: 1=F,2=P,3=S,4=C]
  WIPSTAORI M*1 Source status in progress [menu 342: 1=F,2=P,3=S,4=C]
  WIPTYP M*2 Order type [menu 341: 1=SO,2=PO,3=MS,4=SC,5=WO,6=MW,7=TR,8=TP,9=BW,10=VD,11=VR,12=CR,13=EO,14=MT]
  WIPTYPORI M*2 Source order type [menu 341: 1=SO,2=PO,3=MS,4=SC,5=WO,6=MW,7=TR,8=TP,9=BW,10=VD,11=VR,12=CR,13=EO,14=MT]

## CBNHEA (CBH) - MRP processing
Keys (first = PK; D = duplicates allowed): CBH0 STOFCY+ITMREF; CBH1 STOFCY+LLC+ITMREF
Fields:
  ALLSTO QTY Total allocated
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Delete
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BPRSTO QTY Total loan stock
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTLSTO QTY Internal 'Q'
  DAYCOV COV Coverage
  DETSHT QTY Detail shortage
  DLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  ECCSTO M*20 Stock version [menu 2777: 1=No,2=Major,3=Major and minor] act:ECC
  EXPNUM L*8 Export number
  EXYSTOFLG M*4 Obsolete stock [menu 1: 1=No,2=Yes]
  FOHENDDAT D Demand horizon
  FOHUOT M*10 Firm horizon time un [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  GENFLG M*4 Generic [menu 1: 1=No,2=Yes]
  GLOALL QTY Global allocated
  GLOSHT QTY Global shortage
  INTFLG M*4 Intermediary [menu 1: 1=No,2=Yes]
  INTSTO QTY Total internal stock
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[CBH]ITMREF (ITMMASTER) !BSRA
  LIFENDDAT D Service life end
  LIFSTRDAT D Service life start
  LLC C*2 Lowest level code
  MFGFLG M*4 Manufactured [menu 1: 1=No,2=Yes]
  ORDFLG M*4 Optimization flag [menu 1: 1=No,2=Yes]
  ORDSTO QTY Stock on order
  ORDVER M*4 Exclusive version [menu 1: 1=No,2=Yes] act:ECC
  PHAFLG M*4 Phantom [menu 1: 1=No,2=Yes]
  PHYSTO QTY Internal 'A'
  PLFSTO QTY Total dock stock
  PLHENDDAT D Firm horizon
  PLNANYCOD M*4 Replanning analysis [menu 1: 1=No,2=Yes]
  PURFLG M*4 Bought [menu 1: 1=No,2=Yes]
  QUAFLG M*25 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  QUALTI LTI Quality ctrl. lead time
  REJSTO QTY Internal 'R'
  REOCOD M*15 Suggestion type [menu 250: 1=No suggestion,2=Purchase,3=Manufacturing,4=Intersite,5=Subcontracting]
  REOFCY FCY Reorder site -> [FCY]FCY0 =[CBH]REOFCY (FACILITY) !Block
  REOMGTCOD M*15 Reorder mode [menu 727: 1=Not managed,2=By MRP,3=By MPS,4=By ROP,5=By period]
  REOPOL A*3 Reorder policy
  REOQTYCOD M*30 Reorder quantity [menu 258: 1=Net quantity,2=Minimum quantity without rounding,3=Minimum quantity with rounding]
  SAFSTOCOD M*4 Safety stock [menu 1: 1=No,2=Yes]
  SALFLG M*4 Sold [menu 1: 1=No,2=Yes]
  SALSTO QTY On sales orders
  SCOSTO QTY Total subcon. stock
  SCPFLG M*4 Subcontracted [menu 1: 1=No,2=Yes]
  SCSFLG M*4 Subcontract [menu 1: 1=No,2=Yes]
  SHR DCB*3.3 Shrinkage percent
  SPLCOD M*30 Splitting [menu 739: 1=None,2=Parallel,3=Successive]
  STDFLG M*15 Management mode [menu 297: 1=Not managed,2=By project,3=Available stock,4=By order]
  STOFCY FCY Storage site -> [FCY]FCY0 =[CBH]STOFCY (FACILITY) !Block
  STOTIAFLG M*4 Include available stock [menu 1: 1=No,2=Yes]
  STRSTO QTY Starting stock
  STU UOM Stock unit -> [TUN]TUN0 =[CBH]STU (TABUNIT) !Block
  STUDEC C*1 Decimals
  SUGTYP M*30 Suggestion type [menu 218: 1=No processing,2=With MRP pegging,3=Wthout MRP pegging,4=MRP pegging only]
  TOOFLG M*4 Tools [menu 1: 1=No,2=Yes]
  TRASTO QTY Transferred stock
  TRFSTO QTY In-transit stock
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CBH]UPDUSR (AUTILIS) !Other
  WAISTO QTY Pending issues
  WIPPRO M*4 WIP protect. [menu 1: 1=No,2=Yes]

## CBNWRK (CBW) - MRP workfile
Keys (first = PK; D = duplicates allowed): CBW0 STOFCY+ITMREF+RECCOD+DAT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CBW]CREUSR (AUTILIS) !Other
  DAT D Date
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Delete
  QTYSTU QTY STK quantity
  RECCOD C*4 Code
  STOFCY FCY Storage site -> [FCY]FCY0 =[CBW]STOFCY (FACILITY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CBW]UPDUSR (AUTILIS) !Other

## CFGABQ (CAB) - Simple calculation tables
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CAB0 ABQNUM+ABQLIN; CAB1 ABQNUM+ALPENDVAL+NUMENDVAL+DATENDVAL (D); CAB2 ABQNUM+ALPSTRVAL+NUMSTRVAL+DATSTRVAL+ALPSTRVALY+NUMSTRVALY+DATSTRVALY (D)
Fields:
  AABQLIN A*10 Line
  ABQAXX AX3 Description
  ABQCHA M*15 Entry characters [menu 650: 1=Uppercase letter,2=Lowercase letter,3=Uppercase and lowercase letter]
  ABQCHAY M*15 Entry characters [menu 650: 1=Uppercase letter,2=Lowercase letter,3=Uppercase and lowercase letter]
  ABQCOD M*4 Calc. table type [menu 784: 1=Simple calculation table,2=Conversion table,3=Double entry table]
  ABQDES DES Description
  ABQLIN C*4 Line
  ABQNUM CAB Calc. table -> [CAB]CAB0 =ABQNUM;ABQLIN (CFGABQ) !Delete
  ABQTYP M*15 Range format [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  ABQTYPY M*15 Y-value format [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  ABSAXX AX2 Vert axis title
  ABSCOD M*4 Range of values [menu 1: 1=No,2=Yes]
  ABSDES A*15 Vert axis title
  ALPENDVAL A*20 End date
  ALPENDVALY A*20 End date
  ALPRESVAL A*20 Result
  ALPSTRVAL A*20 Start range
  ALPSTRVALY A*20 Start range
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATENDVAL D End date
  DATENDVALY D End date
  DATRESVAL D Result
  DATSTRVAL D Start range
  DATSTRVALY D Start range
  EXPNUM L*8 Export number
  NUMENDVAL DCB*20 End date
  NUMENDVALY DCB*20 End date
  NUMRESVAL DCB*20 Result
  NUMSTRVAL DCB*20 Start range
  NUMSTRVALY DCB*20 Start range
  ORDAXX AX2 Horiz axis title
  ORDCOD M*4 Range of values [menu 1: 1=No,2=Yes]
  ORDDES A*15 Horiz axis title
  RESAXX AX2 Result title
  RESCHA M*15 Entry characters [menu 650: 1=Uppercase letter,2=Lowercase letter,3=Uppercase and lowercase letter]
  RESDES A*15 Result title
  RESFLG M*4 Block not found [menu 1: 1=No,2=Yes]
  RESTYP M*15 Result format [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CFGHIS (CFH) - Configuration history
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CFH0 SCENUM+CFGVCRNUM+SYMNUM+SYMSEQ; CFH1 CFGVCRNUM+SCENUM+SYMNUM+SYMSEQ; CFH2 SCENUM+SYMSEQ+SYMNUM+CFGVCRNUM
Fields:
  AUUID AUUID Single identifier
  CFGVCRNUM VCR Journal number config
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  SCENUM CFG Scenario -> [CSC]CSC0 =[CFH]SCENUM (CFGSCE) !Block
  SYMNAT M*15 Response type [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  SYMNUM CQU Symbol -> [CQU]CQU0 =[CFH]SYMNUM (CFGQST) !Delete
  SYMORI M*15 Source [menu 771: 1=User,2=System(2),3=System(3),4=System(4)]
  SYMSEQ C*4 Sequence no.
  SYMTYP M*15 Symbol type [menu 752: 30 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CFH]UPDUSR (AUTILIS) !Other
  VALALP A*250 Symbol value
  VALBLB AB0*4 Symbol value
  VALCLB AC0*4 Symbol value
  VALDAT D Symbol value
  VALNUM DCB*20 Symbol value

## CFGHISHEA (CHH) - Configuration history header
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CHH0 CFGVCRNUM; CHH1 SCENUM+CFGVCRNUM; CHH2 SCENUM+CFGBPRNUM+CFGBPRREF (D)
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  CFGBPRNUM BPR BP -> [BPR]BPR0 =[CHH]CFGBPRNUM (BPARTNER) !RTZ
  CFGBPRREF A*20 BP reference
  CFGDELDAT D Config purge date
  CFGVCRNUM VCR Journal number config
  CPNCRE M*4 BOM creation [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[CHH]FCY (FACILITY) !Block
  ITMCRE M*4 Parent product creates [menu 1: 1=No,2=Yes]
  ITMREF ITM Product -> [ITM]ITM0 =[CHH]ITMREF (ITMMASTER) !Other
  QTYSTU QTY STK quantity
  ROUALT TRO Routing code -> [TRO]TRO0 =[CHH]ROUALT (TABROUALT) !Block
  ROUCRE M*4 Routing created [menu 1: 1=No,2=Yes]
  ROUNUM ITM Routing -> [ITM]ITM0 =[CHH]ROUNUM (ITMMASTER) !Other
  SCENUM CFG Scenario -> [CSC]CSC0 =[CHH]SCENUM (CFGSCE) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CHH]UPDUSR (AUTILIS) !Other

## CFGLNK (CLN) - Configurator symbol links
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CLN0 SYMTYPWUS+SYMNUMWUS+SYMTYP+SYMNUM; CLN1 SYMTYP+SYMNUM+SYMTYPWUS+SYMNUMWUS
Fields:
  AUUID AUUID Single identifier
  CLE1 ID1 Identifier
  CLE2 ID2 Identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  FLD A*10 Field
  SYMAXXWUS AX3 Title symbol
  SYMNUM SYM Symbol
  SYMNUMWUS SYM Symbol
  SYMTYP M*20 Symbol type [menu 752: 30 values, see local-menus.md]
  SYMTYPWUS M*15 Symbol type [menu 752: 30 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CLN]UPDUSR (AUTILIS) !Other

## CFGMAC (CFM) - Standard processes
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CFM0 MACNUM+MACLIN; CFM1 SYMTYP+SYMNUM+MACNUM (D)
Fields:
  ABQNUM CAB Calc. table -> [CAB]CAB0 =ABQNUM;1 (CFGABQ) !Other
  ABQVAL CQU Table X-value -> [CQU]CQU0 =[CFM]ABQVAL (CFGQST) !Block
  ABQVALY CQU Table Y-value -> [CQU]CQU0 =[CFM]ABQVALY (CFGQST) !Block
  AUUID AUUID Single identifier
  CNDFOR AFF*250 Condition
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FORFOR AFF*250 Formula
  MACAXX AX3 Description
  MACCOD M*20 Usage code [menu 768: 1=For selections,2=For scenarios,3=Master scenario]
  MACDES DES Description
  MACLIN C*4 Line
  MACNUM CFM Standard process -> [CFM]CFM0 =MACNUM;MACLIN (CFGMAC) !Delete
  SCETXT DES Comment
  SYMDIS M*4 Deactivate [menu 1: 1=No,2=Yes]
  SYMIND C*3 Index
  SYMNUM SYM Symbol
  SYMTYP M*20 Symbol type [menu 752: 30 values, see local-menus.md]
  TXTAXX AX3 Comment
  UPDCOD M*15 Parameter [menu 763: 1=No action,2=No selection,3=Select 0 or 1 line,4=Select 1 line,5=Select 0 to n lines,6=Select 1 to n lines,7=Re work,8=Information,9=Blocking]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WINAUT M*4 Assisted entry [menu 789: 1=Standard,2=Assisted,3=Question by question]

## CFGMEMO (CME) - Configurator memo
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CME0 RECCOD+SCENUM+CREUSR+CFGBPRNUM+CFGBPRREF+QSTNUM+SELSEQ; CME1 RECCOD+PRONUM+SCENUM+QSTNUM (D)
Fields:
  AUUID AUUID Single identifier
  BLOB AB0*4 Image file
  CFGBPRNUM BPR BP -> [BPR]BPR0 =[CME]CFGBPRNUM (BPARTNER) !RTZ
  CFGBPRREF A*20 BP reference
  CLOB AC0*4 Text file (clob)
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  PRONUM L*8 Process number
  QSTNUM CQU Question -> [CQU]CQU0 =[CME]QSTNUM (CFGQST) !Delete
  QTYSAU QTY SAL quantity
  QTYSTU QTY STK quantity
  RECCOD C*4 Code
  SCENUM CFG Scenario -> [CSC]CSC0 =[CME]SCENUM (CFGSCE) !Delete
  SELSEQ C*4 Line no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CME]UPDUSR (AUTILIS) !Other
  VALALP A*250 Symbol value
  VALDAT D Symbol value
  VALNUM DCB*20 Symbol value

## CFGMENLOC (CML) - Local menus
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CLE LANCHP+LANNUM+LAN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  LAN A*3 Language
  LANCHP C*4 Chapter
  LANMES A*123 Message
  LANNUM C*4 Number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CFGOPTVAR (COV) - Options / variants
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): COV0 SELNUM+SELSEQ
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMOPVAXX AX1 Option/Variant
  ITMREFCAL AFF*250 Quantity formula
  ITMREFFOR AFF*250 Expression
  ITMREFLOA ITM Product -> [ITM]ITM0 =[COV]ITMREFLOA (ITMMASTER) !Delete
  ITMREFOPV A*20 Option/Variant
  ITMREFQTY M*15 Entry quantity [menu 766: 1=Enter 0 or 1,2=Free entry,3=No entry]
  ITMREFSEQ C*4 Option
  SELNUM CSE Selection -> [CSE]CSE0 =[COV]SELNUM (CFGSEL) !Delete
  SELSEQ C*4 Line no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[COV]UPDUSR (AUTILIS) !Other

## CFGQST (CQU) - Configurator symbols
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CQU0 QSTNUM; CQU1 QSTORI+QSTTYP+QSTNUM; CQU2 QSTLEN+QSTNUM
Fields:
  ALPDEFVAL A*20 Default value
  ALPENDVAL A*20 End date
  ALPSTRVAL A*20 Start range
  ASWCHA M*15 Character [menu 650: 1=Uppercase letter,2=Lowercase letter,3=Uppercase and lowercase letter]
  ASWTYP M*15 Response type [menu 252: 1=Alphanumeric,2=Numeric,3=Date,4=Boolean,5=Text,6=Photo (image file),7=Text file]
  AUUID AUUID Single identifier
  CODFIC ATB Table code -> [ATB]CODFIC =[CQU]CODFIC (ATABLE) !Block
  CODFLD AVA Returned field
  CODNUM ANM Sequence number -> [ANM]ANM0 =[CQU]CODNUM (ACODNUM) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTLBLO M*15 Blocking type [menu 549: 1=Not blocking,2=Blocking]
  CTLTYP M*15 Control type [menu 770: 1=No control,2=List of values,3=Table,4=Forms/templates,5=Ranges,6=Miscellaneous table]
  DATDEFVAL D Default value
  DATENDVAL D End date
  DATSTRVAL D Start range
  EVADEFVAL A*60 Evaluate def value
  EXPNUM L*8 Export number
  FCYFLD AVA Site field
  FILFIC FOR Filter formula -> [TFO]TFO0 =7;FILFIC (TABFOR) !Block
  HISFLG M*4 History [menu 1: 1=No,2=Yes]
  MOTCLE A*10 Help key-word
  NUMDEFVAL DCB*20 Default value
  NUMENDVAL DCB*20 End date
  NUMSTRVAL DCB*20 Start range
  OBJET A*8 Object
  ORDFLG M*4 Orders [menu 1: 1=No,2=Yes]
  QSTAXX AX3 Description
  QSTDES DES Description
  QSTDIM C*4 Dimension
  QSTLAN A*3(10) Language
  QSTLEN C*2 Length
  QSTNUM CQU Symbol -> [CQU]CQU0 =[CQU]QSTNUM (CFGQST) !Delete
  QSTORI M*15 Source [menu 771: 1=User,2=System(2),3=System(3),4=System(4)]
  QSTPIC A*40 Image
  QSTSHO DES(10) Screen title
  QSTSHONBR C*4 Number of descriptions
  QSTTYP M*15 Symbol type [menu 752: 30 values, see local-menus.md]
  QUOFLG M*4 Quotes [menu 1: 1=No,2=Yes]
  SALTXT AX3 Sales text
  SEAFLG M*4 Search criterion [menu 1: 1=No,2=Yes]
  SHACAT A*2 Family
  TCT TCT Control table -> [TCT]TCT0 =TCT;1 (TABCTL) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CFGSCE (CSC) - Configurator scenarios
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CSC0 SCENUM
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[CSC]ACSCOD (ACCCOD) !Block
  ALTTYPREF M*15 Alt reference typ [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  AUUID AUUID Single identifier
  BLONBR C*1 Block act:CFQ
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Block
  BOMALTREF TBO Ref. BOM code -> [TBO]TBO0 =ALTTYPREF;BOMALTREF (TABBOMALT) !Block
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMDSY M*4 Display multi-level [menu 1: 1=No,2=Yes]
  CMPFLG M*4 Component creation [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTCOD M*20 Valuation option [menu 774: 1=No calculation,2=Formula,3=Base price,4=Price list,5=Standard cost,6=Revised standard cost,7=Last price,8=Calculated by scenario,9=Budget]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FCY FCY Exclusive site -> [FCY]FCY0 =[CSC]FCY (FACILITY) !RTZ
  FCYFLG M*4 Multisite creation [menu 1: 1=No,2=Yes]
  HISFLG M*4 History search [menu 1: 1=No,2=Yes]
  ITMFLG M*4 Item creation [menu 1: 1=No,2=Yes]
  LINNBR C*2 Line act:CFQ
  NBRCOL C*3 Number of columns
  NBRLIG C*3 Number of lines
  PARITM ITM Reference item -> [ITM]ITM0 =[CSC]PARITM (ITMMASTER) !Block
  QSTNBR C*4 Number of questions
  QSTNUM CQU Question -> [CQU]CQU0 =[CSC]QSTNUM (CFGQST) !Block act:CFQ
  ROUALT TRO Routing code -> [TRO]TRO0 =[CSC]ROUALT (TABROUALT) !Block
  ROUALTREF TRO Ref. routing code -> [TRO]TRO0 =[CSC]ROUALTREF (TABROUALT) !Block
  ROUFLG M*4 Routings [menu 1: 1=No,2=Yes]
  ROUREF ITM Reference routing -> [ITM]ITM0 =[CSC]ROUREF (ITMMASTER) !Block
  SCEAXX AX3 Description
  SCEDES DES Description
  SCEFLG M*4 Sub-scenarios [menu 1: 1=No,2=Yes]
  SCENUM CFG Scenario -> [CSC]CSC0 =[CSC]SCENUM (CFGSCE) !Delete
  SEAPARITM M*20 Equivalence search [menu 775: 1=No search,2=Search equivalence,3=Always create,4=Search + automatic selection]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALDSY M*4 Quick validation [menu 1: 1=No,2=Yes]
  WINAUT M*4 Assisted entry [menu 789: 1=Standard,2=Assisted,3=Question by question]

## CFGSCELIN (CSL) - Configurator scenario lines
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CSL0 SCENUM+SCENUMTYP+SCENUMSEQ+SCENUMLIN; CSL1 SYMTYP+SYMNUM+SCENUM (D)
Fields:
  ABQNUM A*8 Calc. table
  ABQVAL CQU Table X-value -> [CQU]CQU0 =[CSL]ABQVAL (CFGQST) !Block
  ABQVALY CQU Table Y-value -> [CQU]CQU0 =[CSL]ABQVALY (CFGQST) !Block
  AUUID AUUID Single identifier
  CAD DCB*6.4 Rate
  CNDFOR AFF*250 Condition
  CNDFORLIN AFF*250 Condition
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FORFOR AFF*250 Formula
  ITMREF ITM Product -> [ITM]ITM0 =[CSL]ITMREF (ITMMASTER) !Block
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  OPENUM OPE Operation
  OPETIM TIH Run time
  ORICOD C*1 Source
  PRPTIM TIH Preparation time
  ROODES DES Ope description
  ROOTIMCOD M*15 Run time code [menu 312: 1=Proportional,2=Rate,3=Fixed]
  RPLIND C*3 Alternate index
  SCENUM CFG Scenario -> [CSC]CSC0 =SCENUM (CFGSCE) !Delete
  SCENUMLIN L*8 Line
  SCENUMSEQ L*8 Sequence number
  SCENUMTYP M*15 Line type [menu 764: 1=Select parent product,2=Create parent product,3=Select components,4=List components,5=Create components,6=Unused,7=List operations,8=Create operations,9=Final controls]
  SCETXT DES Comment
  SEAITMREF M*4 Equivalence search [menu 775: 1=No search,2=Search equivalence,3=Always create,4=Search + automatic selection]
  SETTIM TIH Setup time
  STDOPENUM ROT Standard operation
  SUBSCENUM CFG Sub-procedure -> [CSC]CSC0 =[CSL]SUBSCENUM (CFGSCE) !Block
  SYMDIS M*4 Deactivate [menu 1: 1=No,2=Yes]
  SYMIND C*3 Index
  SYMNUM A*10 Symbol
  SYMTYP M*15 Symbol type [menu 752: 30 values, see local-menus.md]
  TIMCOD M*15 Management unit [menu 303: 1=Time for 1,2=Time for 100,3=Time for 1000,4=Time per lot]
  UPDCOD M*15 Parameter [menu 763: 1=No action,2=No selection,3=Select 0 or 1 line,4=Select 1 line,5=Select 0 to n lines,6=Select 1 to n lines,7=Re work,8=Information,9=Blocking]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CSL]UPDUSR (AUTILIS) !Other
  WST WST Main work center

## CFGSEL (CSE) - Configurator selections
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CSE0 SELNUM
Fields:
  AUUID AUUID Single identifier
  CFGLIN TLP Product line -> [TLP]TLP0 =[CSE]CFGLIN (TABLINCFG) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  MACNUM CFM Standard process -> [CFM]CFM0 =MACNUM;1 (CFGMAC) !Other
  PRIFOR AFF*250 Formula
  QTYFOR AFF*250 Quantity formula
  RUL M*15(20) Rule [menu 773: 1=Mandatory choice,2=Linked with,3=Not allowed with]
  RULCND AFF*60(20) Condition
  RULNBR C*4 No. of constraints
  RULOPT1 C*4(20) Option / variant
  RULOPT2 C*4(20) Option / variant
  SELAXX AX3 Description
  SELBOO M*4(12) And / or [menu 56: 1=And,2=Or]
  SELDES DES Description
  SELFIL AFF*250 Main filter
  SELFLD A*10(30) Fields
  SELFLDNBR C*2 Field nb
  SELFOR AFF*60(12) Formula
  SELFORNBR C*2 Number of filters
  SELINT A*25(12) Description
  SELKEY M*15 Classification [menu 761: 1=Product number,2=Product description,3=Search key,4=Product line,5=Cfg document number]
  SELKEYFLD A*10 Field
  SELLINNBR C*4 Number of lines
  SELMOD M*4 Stand-alone mode [menu 1: 1=No,2=Yes]
  SELMUL M*25 Selection code [menu 763: 1=No action,2=No selection,3=Select 0 or 1 line,4=Select 1 line,5=Select 0 to n lines,6=Select 1 to n lines,7=Re work,8=Information,9=Blocking]
  SELNUM CSE Selection -> [CSE]CSE0 =[CSE]SELNUM (CFGSEL) !Delete
  SELPRI M*15 Price column [menu 774: 1=No calculation,2=Formula,3=Base price,4=Price list,5=Standard cost,6=Revised standard cost,7=Last price,8=Calculated by scenario,9=Budget]
  SELQTY M*15 Column quantity [menu 767: 1=No,2=Stock unit column,3=Sales unit column]
  SELSTR M*4(12) Active from [menu 1: 1=No,2=Yes]
  SELTBL ATB(30) Table -> [ATB]CODFIC =[CSE]SELTBL (ATABLE) !Block
  SELTYP M*15 Selection type [menu 765: 1=Select products,2=Select options/variants]
  SYMNBR C*4 No. of symbols
  SYMNUM CQU(40) Symbol -> [CQU]CQU0 =[CSE]SYMNUM (CFGQST) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CFGSHA (CSH) - Shapes and patterns
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CSH0 SHACAT+SHANUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  SHACAT A*2 Family
  SHACATAXX AX3 Description
  SHACATDES A*20 Description
  SHAFLG C*1 Flag
  SHANUM A*3 Shape/pattern para
  SHANUMAXX AX3 Description
  SHANUMDES A*20 Description
  SHAPCT A*80 Image
  SHATYP M*4 Questions window [menu 1: 1=No,2=Yes]
  SYMCND AFF*100(15) Condition
  SYMNBR C*4 No. of symbols
  SYMNUM CQU(15) Symbol -> [CQU]CQU0 =[CSH]SYMNUM (CFGQST) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VARFOR AFF*100(5) Expression
  VARNBR C*4 No. of variables
  VARNUM CQU(5) Variable -> [CQU]CQU0 =[CSH]VARNUM (CFGQST) !Block

## CFGTEX (CFT) - Configurator work file
Notes: activity code CFG
Keys (first = PK; D = duplicates allowed): CFT0 PRONUM+RECCOD+CODFIC+CODZON+CLE+CLE1
Fields:
  AUUID AUUID Single identifier
  CLE A*30 Identifier
  CLE1 A*30 Identifier
  CLOB ACB Text file (clob)
  CODFIC ATB Table code -> [ATB]CODFIC =[CFT]CODFIC (ATABLE) !Other
  CODZON AVA Field code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CST MD8 Total cost
  PROFLG C*1 Processing flag
  PRONUM L*8 Process number
  RECCOD L*8 Code
  TXT A*250 Text
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CFT]UPDUSR (AUTILIS) !Other

## CUNLISDET (CUD) - Counts
Notes: differs in V9.0 P12 (diff: AT3_CUNLISDET.htm)
Keys (first = PK; D = duplicates allowed): CUD0 CUNSSSNUM+CUNLISNUM+ITMLISNUM; CUD1 STOFCY+ITMREF+CUNLISNUM (D); CUD2 STOFCY+ITMREF+LOC (D); CUD3 STOFCY+CUNSSSNUM+CUNLISNUM+ITMREF (D)
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  CUNCST MD8 Unit val.
  CUNCSTCOD M*15 Costing mode [menu 705: 1=Entered,2=Standard cost,3=Revised standard cost,4=Last cost,5=Historical AUC,6=FIFO cost,7=Lot average cost,8=Order cost,9=LIFO cost,10=Last purchase price]
  CUNDAT D Count date
  CUNLISNUM VCR Count worksheet
  CUNLISSTA M*15 Status [menu 2729: 1=To be counted,2=Counted,3=Abandoned,4=Validated]
  CUNLOKFLG M*15 Blocked stock [menu 2724: 1=No,2=Yes,3=Partial]
  CUNSSSNUM VCR Stock count session
  CUR CUR Currency -> [TCU]TCU0 =[CUD]CUR (TABCUR) !Block
  DEPAMT MD1 Revaluation amt
  DEPRAT RAT Revaluation rate
  DIE DIE Dimension type code -> [DIE]DIE0 =[CUD]DIE (GDIE) !Block act:ANA
  DLUDAT D Use-by date
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  INVDTACST MD7 Invoicing element act:SPD
  IPTDAT D Allocation date
  ITMLISNUM L*8 Product rank
  ITMREF ITM Product -> [ITM]ITM0 =[CUD]ITMREF (ITMMASTER) !Block
  LABCST MD7 Labor cost act:LAB
  LINFLG M*15 Notes [menu 715: 1=New line,2=Old line,3=Changed unit,4=Not controlled,5=Controlled,6=Analysis requested,7=Suspended]
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Other
  LOT LOT Lot
  MACCST MD7 Machine cost act:MAC
  MATCST MD7 Material cost act:MAT
  NETCUNCST MD8 Net unit value
  NEWLTIDAT D Recontrol date
  OVELABCST MD7 Labor OH act:SPD
  OVEMACCST MD7 Machine OH act:SPD
  OVEMATCST MD7 Mat. OH act:SPD
  OVESCOCST MD7 Sub-con OH act:SPD
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Unit -> [TUN]TUN0 =[CUD]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  POT DCB*5.4 Potency
  PRIORD MD5 Order price
  QLYCTLDEM VCR Analysis request
  QTYPCU QTY PAC quantity
  QTYPCUNEW QTY Counted stock PAC
  QTYPCUNEW1 QTY Counted stock PAC 1
  QTYPCUNEW2 QTY Counted stock PAC 2
  QTYSTU QTY STK quantity
  QTYSTUNEW QTY Counted STK stock
  QTYSTUNEW1 QTY Counted stock STK 1
  QTYSTUNEW2 QTY Counted stock STK 2
  REFPER D Expiration reference
  SCOCST MD7 Total subcontracted act:SPD
  SERNUM SER Serial number
  SHLDAT D Expiration date
  SLO SLO Sublot
  STA A*3 Stock status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[CUD]STOFCY (FACILITY) !Block
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Block act:WRH
  ZERSTOFLG M*4 Zero stock [menu 1: 1=No,2=Yes]
  ZERSTOFLG1 M*4 Null stock 1 [menu 1: 1=No,2=Yes]
  ZERSTOFLG2 M*4 Null stock 2 [menu 1: 1=No,2=Yes]

## CUNLISTE (CUL) - Count worksheets
Notes: differs in V9.0 P12 (diff: AT3_CUNLISTE.htm)
Keys (first = PK; D = duplicates allowed): CUL0 CUNSSSNUM+CUNLISNUM; CUL1 STOFCY+CUNSSSNUM+CUNLISNUM
Fields:
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTGUSR AX3 Count manager
  CTGUSR1 AX3 Count manager 1
  CTGUSR2 AX3 Count manager 2
  CUNLISDAT D Count date
  CUNLISDES DES Description
  CUNLISNUM VCR Count worksheet
  CUNLISSTA M*15 Status [menu 2723: 1=To be counted,2=Cancelled,3=Counted,4=Partial validation,5=Validated,6=Closed]
  CUNLOKFLG M*15 Blocked stock [menu 2724: 1=No,2=Yes,3=Partial]
  CUNSSSNUM VCR Stock count session
  CUNSTADAT D Status date
  DIE DIE Dimension type code -> [DIE]DIE0 =[CUL]DIE (GDIE) !Block act:ANA
  EXPNUM L*8 Export number
  IPTDAT D Allocation date
  LASIPTDAT D Last allocation
  MVTDES DES Movement description
  NBRLIG C*4 Number of lines
  STOFCY FCY Storage site -> [FCY]FCY0 =[CUL]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USR A*5 Operator
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## CUNSESSION (CUN) - Stock count session
Notes: differs in V9.0 P12 (diff: AT3_CUNSESSION.htm)
Keys (first = PK; D = duplicates allowed): CUN0 CUNSSSNUM; CUN1 STOFCY+CUNSSSNUM
Fields:
  ABCCLSA M*4 Class 'A' [menu 1: 1=No,2=Yes]
  ABCCLSB M*4 Class 'B' [menu 1: 1=No,2=Yes]
  ABCCLSC M*4 Class 'C' [menu 1: 1=No,2=Yes]
  ABCCLSD M*4 Class 'D' [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPRNUMEND BPR To BP -> [BPR]BPR0 =[CUN]BPRNUMEND (BPARTNER) !Other
  BPRNUMSTR BPR From BP -> [BPR]BPR0 =[CUN]BPRNUMSTR (BPARTNER) !Other
  BUYEND AUS To buyer -> [AUS]CODUSR =[CUN]BUYEND (AUTILIS) !Other
  BUYSTR AUS From buyer -> [AUS]CODUSR =[CUN]BUYSTR (AUTILIS) !Other
  CPLCUNNBRA L*8 A product physical counts
  CPLCUNNBRB L*8 B product physical counts
  CPLCUNNBRC L*8 C product physical counts
  CPLCUNNBRD L*8 D product stock cts
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUNITMWRH M*4 Products-warehouses [menu 1: 1=No,2=Yes]
  CUNLASFLG M*4 Global [menu 1: 1=No,2=Yes]
  CUNNBRA L*8 A requested physical count
  CUNNBRB L*8 B requested physical count
  CUNNBRC L*8 C requested physical counts
  CUNNBRD L*8 D req stock count
  CUNNULSTK M*4 Products without stock [menu 1: 1=No,2=Yes]
  CUNSRTCOD M*15 Count sort [menu 796: 1=Product location,2=Location product]
  CUNSSSDAT D Count date
  CUNSSSDES DES Description
  CUNSSSMOD M*15 Processing selection [menu 756: 1=Manual selection,2=Cycle stock count,3=Annual stock count]
  CUNSSSNUM VCR Stock count session
  CUNSSSSTA M*15 Status [menu 2722: 1=In creation,2=To be counted,3=Closed]
  CUNSSSTYP M*20 Stock count type [menu 2717: 1=Product,2=Locations]
  EXPNUM L*8 Export number
  ITMNBR C*4 Number of products
  ITMREFEND ITM To product -> [ITM]ITM0 =[CUN]ITMREFEND (ITMMASTER) !Other
  ITMREFSTR ITM From product -> [ITM]ITM0 =[CUN]ITMREFSTR (ITMMASTER) !Other
  ITMSTA006 M*4 Usable [menu 1: 1=No,2=Yes]
  LOCEND LOC To location -> [STC]STC0 =STOFCY;LOCEND (STOLOC) !Other
  LOCPOS C*2 Location position
  LOCSTR LOC From location -> [STC]STC0 =STOFCY;LOCSTR (STOLOC) !Other
  LOCTYPEND TLO To locn type -> [TLO]TLO0 =STOFCY;LOCTYPEND (TABLOCTYP) !Other
  LOCTYPSTR TLO From locn type -> [TLO]TLO0 =STOFCY;LOCTYPSTR (TABLOCTYP) !Other
  LOTEND LOT To lot
  LOTSTR LOT From lot
  MAGLOCFLG M*4 Shop location [menu 1: 1=No,2=Yes]
  MAXLIG C*4 Maximum lines
  MULCTGFLG M*4 Multiple counts [menu 1: 1=No,2=Yes]
  MULLISFLG M*4 Multilists [menu 1: 1=No,2=Yes]
  PICLOCFLG M*4 Picking location [menu 1: 1=No,2=Yes]
  PRCLIG C*4 % limit
  QUALOCFLG M*4 Dock location [menu 1: 1=No,2=Yes]
  RCPLOCFLG M*4 Receipt loc. [menu 1: 1=No,2=Yes]
  RETLOCFLG M*4 Return location [menu 1: 1=No,2=Yes]
  SELFOR FOR Product formula -> [TFO]TFO0 =18;SELFOR (TABFOR) !Block
  SELFOR0 FOR Product formula -> [TFO]TFO0 =29;SELFOR0 (TABFOR) !Block
  SELFOR00 FOR Prod-whs for. -> [TFO]TFO0 =42;SELFOR00 (TABFOR) !Block
  SELFOR1 FOR Stock formula -> [TFO]TFO0 =27;SELFOR1 (TABFOR) !Block
  SELFOR2 FOR Location formula -> [TFO]TFO0 =28;SELFOR2 (TABFOR) !Block
  SELFOR3 FOR Warehouse formula -> [TFO]TFO0 =43;SELFOR3 (TABFOR) !Block
  STOFCY FCY Storage site -> [FCY]FCY0 =[CUN]STOFCY (FACILITY) !Block
  STOLOCFLG M*4 Storage location [menu 1: 1=No,2=Yes]
  TCLCODEND ITG Last category -> [ITG]ITG0 =STOFCY;TCLCODEND (ITMCATEG) !Other
  TCLCODSTR ITG First category -> [ITG]ITG0 =STOFCY;TCLCODSTR (ITMCATEG) !Other
  TRALOCFLG M*4 Work station locn [menu 1: 1=No,2=Yes]
  TSICODEND ADI To stat grp -> [ADI]CODE =indice+40;TSICODEND(indice) (ATABDIV) !Other act:STI
  TSICODSTR ADI From stat grp -> [ADI]CODE =indice+40;TSICODSTR(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRHEND WRH To warehouse -> [WRH]WRH0 =[CUN]WRHEND (WAREHOUSE) !Other
  WRHSTR WRH From warehouse -> [WRH]WRH0 =[CUN]WRHSTR (WAREHOUSE) !Other

## INVENTD (INVD) - Counts
Notes: activity code KPO
Keys (first = PK; D = duplicates allowed): INVD0 CPY+REFDAT+NUMLIN; INVD1 CPY+REFDAT+ITMREF (D); INVD2 CPY+CUNSSSNUM+CUNLISNUM (D); INVD3 CPY+REFDAT+CUNSSSNUM (D)
Fields:
  AMT DCB*9.4 Amount
  AMTITM DCB*9.4 Amount
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[INVD]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[INVD]CREUSR (AUTILIS) !Other
  CTRNUM CTR Identifier 2
  CUNLISDES DES Description
  CUNLISNUM VCR Count in progress
  CUNSSSDES DES Description
  CUNSSSNUM VCR Stock count session
  ISSVLTCOD M*20(2) Issue costing [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  ITMLISNUM L*8 Product rank
  ITMREF ITM Product -> [ITM]ITM0 =[INVD]ITMREF (ITMMASTER) !Block
  LOC EMP Location
  LOT LOT Lot
  NUMLIN L*8 Line
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Packing unit -> [TUN]TUN0 =[INVD]PCU (TABUNIT) !Other
  PCUSTUCOE COE Coefficient
  QLYCTLDEM VCR Analysis request
  QTY QTY Quantity
  REFDAT D Reference date
  SERNUM SER Serial number
  SLO SLO Sublot
  STA A*3 Status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[INVD]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[INVD]STU (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[INVD]UPDUSR (AUTILIS) !Other
  WIP M*4 In progress [menu 1: 1=No,2=Yes]

## INVENTH (INV) - Counts
Notes: activity code KPO
Keys (first = PK; D = duplicates allowed): INV0 CPY+REFDAT
Fields:
  AUUID AUUID Single identifier
  CALCDAT D Calculation period
  CPY CPY Company -> [CPY]CPY0 =[INV]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[INV]CREUSR (AUTILIS) !Other
  DES DES Description
  ENDDAT D End date
  EXPDAT D Export date
  EXPSTA M*4 Exported [menu 1: 1=No,2=Yes]
  ORIGIN M*10 Origin [menu 2052: 1=Counts,2=Stock by date]
  REFDAT D Reference date
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[INV]UPDUSR (AUTILIS) !Other
  WIPFLG M*4 WIP [menu 1: 1=No,2=Yes]

## ITMABCWRK (ITK) - ABC Class calculation
Keys (first = PK; D = duplicates allowed): ITK0 STOFCY+ITMREF; ITK1 STOFCY-ABCBAS+ITMREF
Fields:
  ABCBAS DCB*16.2 Calculated basis
  ABCBASPRC DCB*3.3 Percentage
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  ABCCLSNEW M*15 ABC Class simulation [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FORERR C*4 Error
  ITMREF ITM Product -> [ITM]ITM0 =[ITK]ITMREF (ITMMASTER) !Block
  STOFCY FCY Storage site -> [FCY]FCY0 =[ITK]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## LABELPRN (LBP) - Label printing
Keys (first = PK; D = duplicates allowed): LBP0 NUMREQ+USR+RPTCOD+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[LBP]ITMREF (ITMMASTER) !Block
  MVTIND L*8 Index
  MVTSEQ L*8 Sequence
  NUMLIG L*8 Line no.
  NUMREQ L*8 Query no.
  PACNUM PCN Package no.
  PACSEQ C*4 Sequence no.
  PCKSTKFLG M*4 Stock detail [menu 1: 1=No,2=Yes]
  RPTCOD ARP Report code -> [ARP]ARP0 =[LBP]RPTCOD (AREPORT) !Delete
  STOFCY FCY Storage site -> [FCY]FCY0 =STOFCY (FACILITY) !Delete
  UPDCOD M*4 Update [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LBP]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[LBP]USR (AUTILIS) !Delete
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## ORDCOV (ORC) - WIP consideration history
Notes: differs in V9.0 P12 (diff: AT3_ORDCOV.htm); differs in V10 P1 (diff: ATD_ORDCOV.htm)
Keys (first = PK; D = duplicates allowed): ORC0 VCRTYPDST+VCRNUMDST+VCRLINDST+VCRSEQDST+WIPSTADST (D); ORC1 VCRTYP+VCRNUM+VCRLIN+VCRSEQ (D)
Fields:
  ABBFIL A*3 File abbreviation
  AUUID AUUID Single identifier
  BOMALT C*2 BOM code
  BOMOPE OPE Operation number
  BPRNUM BPR BP -> [BPR]BPR0 =[ORC]BPRNUM (BPARTNER) !RTZ
  COVQTY QTY Quantity covered
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ORC]CREUSR (AUTILIS) !Other
  ENDDAT D End date
  EXTQTY QTY Planned quantity
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Other
  ITMREFORI ITM Source product -> [ITM]ITM0 =[ORC]ITMREFORI (ITMMASTER) !Other
  ORI M*15 Source [menu 298: 1=Purchasing,2=Sales,3=Stock,4=Production,5=MPS,6=MRP,7=Projet]
  ORIFCY FCY Original site -> [FCY]FCY0 =[ORC]ORIFCY (FACILITY) !Other
  PIO M*15 Priority [menu 410: 1=Normal,2=Urgent,3=Critical]
  PJT PJT Project -> [PIM]PIM0 =[ORC]PJT (PIMPL) !Block
  ROUALT C*2 Routing code
  ROUNUM A*20 Released routing
  STOFCY FCY Storage site -> [FCY]FCY0 =[ORC]STOFCY (FACILITY) !Other
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ORC]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRLINDST L*8 Receiving line
  VCRLINORI L*8 Origin line
  VCRNUM VCR Entry
  VCRNUMDST VCR Receipt document
  VCRNUMORI VCR Original document
  VCRSEQ L*8 Document sequence no.
  VCRSEQDST L*8 Receiving seq.
  VCRSEQORI L*8 Source sequence
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPDST M*15 Rcpt journal type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPSTADST M*10 Receipt status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]
  WIPTYPDST M*15 Ship-to type [menu 306: 14 values, see local-menus.md]

## PARMRP (PCB) - Requirements parameters
Notes: differs in V9.0 P12 (diff: AT3_PARMRP.htm); differs in V10 P1 (diff: ATD_PARMRP.htm)
Keys (first = PK; D = duplicates allowed): PCB0 STOFCY
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  MPSALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  MPSANYLTI C*4 Replanning analysis
  MPSBOMALT TBO BOM code -> [TBO]TBO0 =MPSALTTYP;MPSBOMALT (TABBOMALT) !Block
  MPSBUCCOR M*4 Automatic adjustment [menu 1: 1=No,2=Yes]
  MPSCAPFCT M*4 Capacity factor [menu 1: 1=No,2=Yes]
  MPSCAPLTI C*4 Load calculation
  MPSCOV M*4 Ignore coverage [menu 1: 1=No,2=Yes]
  MPSCOVRES M*4 Resources in coverage [menu 1: 1=No,2=Yes]
  MPSCTLSTO M*15 Quality control stock [menu 785: 1=No,2=Yes in starting stock,3=Yes at date end control]
  MPSDAYNBR C*4 No. of day groupings
  MPSEOFFLG M*4 EO firm [menu 1: 1=No,2=Yes]
  MPSEOPFLG M*4 EO planned [menu 1: 1=No,2=Yes]
  MPSEOSFCY M*4 Gen. subcon. sugg. [menu 1: 1=No,2=Yes]
  MPSGHOSTO M*4 Phantoms [menu 1: 1=No,2=Yes]
  MPSHORDEM M*4 Forecast offset [menu 1: 1=No,2=Yes]
  MPSITM M*4 MPS and MRP products [menu 1: 1=No,2=Yes]
  MPSITMCOD M*4 Exclusive selection [menu 1: 1=No,2=Yes]
  MPSLASDAT D Last calculation date
  MPSLASLTI L*8 Time in minutes
  MPSMAXANY M*4 Maximum stock analysis [menu 1: 1=No,2=Yes]
  MPSMFGLTI M*15 Production lead time [menu 747: 1=Product lead times,2=Routing/product lead times,3=Always routing lead times]
  MPSMONNBR C*4 No. of month grouping
  MPSMTFFLG M*4 Project task firm [menu 1: 1=No,2=Yes]
  MPSMTPFLG M*4 Project task planned [menu 1: 1=No,2=Yes]
  MPSMWRPLN M*4 Replan material [menu 1: 1=No,2=Yes]
  MPSPHYSTO M*4 Physical stock [menu 1: 1=No,2=Yes]
  MPSPLHDAT M*4 Ignore firm horizon [menu 1: 1=No,2=Yes]
  MPSPOFFLG M*4 POs firm [menu 1: 1=No,2=Yes]
  MPSPOPFLG M*4 POs planned [menu 1: 1=No,2=Yes]
  MPSPOSFCY M*4 Purchase orders [menu 1: 1=No,2=Yes]
  MPSPOSFCYI M*4 Gen. inter. pur. sugg. [menu 1: 1=No,2=Yes]
  MPSPRNFLG M*4 Print calculation report [menu 1: 1=No,2=Yes]
  MPSREJSTO M*4 Rejected stock [menu 1: 1=No,2=Yes]
  MPSSAFCOV M*15 Rebuild safety stock [menu 2741: 1=Always,2=At first requirement]
  MPSSAFSTO M*4 Ignore safety stock [menu 1: 1=No,2=Yes]
  MPSSHRPRC M*4 Ignore link scrap % [menu 1: 1=No,2=Yes]
  MPSSOFFLG M*4 Sales orders firm [menu 1: 1=No,2=Yes]
  MPSSOPFLG M*4 Sales orders planned [menu 1: 1=No,2=Yes]
  MPSSOSFLG M*4 Sales orders suggested [menu 1: 1=No,2=Yes]
  MPSSPEPAR A*10 Specific parameter
  MPSTPFFLG M*4 Transfers firm [menu 1: 1=No,2=Yes]
  MPSTPPFLG M*4 Transfers planned [menu 1: 1=No,2=Yes]
  MPSTPSFLG M*4 Transfers suggested [menu 1: 1=No,2=Yes]
  MPSTRDFLG M*4 Transfer requests [menu 1: 1=No,2=Yes]
  MPSTRFFLG M*4 Transfers firm [menu 1: 1=No,2=Yes]
  MPSTRFSTO M*4 Transfers [menu 1: 1=No,2=Yes]
  MPSTRPFLG M*4 Transfers planned [menu 1: 1=No,2=Yes]
  MPSTWD TWD Weekly structure -> [TWD]TWD0 =[PCB]MPSTWD (TABWEEDIA) !Block
  MPSWAISTO M*4 Pending issues [menu 1: 1=No,2=Yes]
  MPSWEENBR C*4 Number of week groupings
  MPSWOFFLG M*4 Work orders released [menu 1: 1=No,2=Yes]
  MPSWOPFLG M*4 Work orders planned [menu 1: 1=No,2=Yes]
  MPSWOSFCY M*4 Gen. WO sugg. [menu 1: 1=No,2=Yes]
  MPSWOSFCYI M*4 Gen. intersite sugg. [menu 1: 1=No,2=Yes]
  MRPALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  MRPANYLTI C*4 Replanning analysis
  MRPBOMALT TBO BOM code -> [TBO]TBO0 =MRPALTTYP;MRPBOMALT (TABBOMALT) !Block
  MRPBUCCOR M*4 Automatic adjustment [menu 1: 1=No,2=Yes]
  MRPCAPFCT M*4 Capacity factor [menu 1: 1=No,2=Yes]
  MRPCAPLTI C*4 Load calculation
  MRPCOV M*4 Ignore coverage [menu 1: 1=No,2=Yes]
  MRPCOVRES M*4 Resources in coverage [menu 1: 1=No,2=Yes]
  MRPCTLSTO M*15 Quality control stock [menu 785: 1=No,2=Yes in starting stock,3=Yes at date end control]
  MRPDAYNBR C*4 No. of day groupings
  MRPEOFFLG M*4 EO firm [menu 1: 1=No,2=Yes]
  MRPEOPFLG M*4 EO planned [menu 1: 1=No,2=Yes]
  MRPEOSFCY M*4 Gen. subcon. sugg. [menu 1: 1=No,2=Yes]
  MRPGHOSTO M*4 Phantoms [menu 1: 1=No,2=Yes]
  MRPHORDEM M*4 Forecast offset [menu 1: 1=No,2=Yes]
  MRPITM M*4 MPS and MRP products [menu 1: 1=No,2=Yes]
  MRPITMCOD M*4 Exclusive selection [menu 1: 1=No,2=Yes]
  MRPLASDAT D Last calculation date
  MRPLASLTI L*8 Time in minutes
  MRPMAXANY M*4 Maximum stock analysis [menu 1: 1=No,2=Yes]
  MRPMFGLTI M*15 Production lead time [menu 747: 1=Product lead times,2=Routing/product lead times,3=Always routing lead times]
  MRPMONNBR C*4 No. of month grouping
  MRPMTFFLG M*4 Project task firm [menu 1: 1=No,2=Yes]
  MRPMTPFLG M*4 Project task planned [menu 1: 1=No,2=Yes]
  MRPMWRPLN M*4 Replan material [menu 1: 1=No,2=Yes]
  MRPPHYSTO M*4 Physical stock [menu 1: 1=No,2=Yes]
  MRPPLHDAT M*4 Ignore firm horizon [menu 1: 1=No,2=Yes]
  MRPPOFFLG M*4 POs firm [menu 1: 1=No,2=Yes]
  MRPPOPFLG M*4 POs planned [menu 1: 1=No,2=Yes]
  MRPPOSFCY M*4 Purchase orders [menu 1: 1=No,2=Yes]
  MRPPOSFCYI M*4 Gen. inter. pur. sugg. [menu 1: 1=No,2=Yes]
  MRPPOSFLG M*4 Suggested supplier orders [menu 1: 1=No,2=Yes]
  MRPPRNFLG M*4 Print calculation report [menu 1: 1=No,2=Yes]
  MRPREJSTO M*4 Rejected stock [menu 1: 1=No,2=Yes]
  MRPSAFCOV M*15 Rebuild safety stock [menu 2741: 1=Always,2=At first requirement]
  MRPSAFSTO M*4 Ignore safety stock [menu 1: 1=No,2=Yes]
  MRPSHRPRC M*4 Ignore link scrap % [menu 1: 1=No,2=Yes]
  MRPSOFFLG M*4 Sales orders firm [menu 1: 1=No,2=Yes]
  MRPSOPFLG M*4 Sales orders planned [menu 1: 1=No,2=Yes]
  MRPSOSFLG M*4 Sales orders suggested [menu 1: 1=No,2=Yes]
  MRPSPEPAR A*10 Specific parameter
  MRPTPFFLG M*4 Transfers firm [menu 1: 1=No,2=Yes]
  MRPTPPFLG M*4 Transfers planned [menu 1: 1=No,2=Yes]
  MRPTPSFLG M*4 Transfers suggested [menu 1: 1=No,2=Yes]
  MRPTRDFLG M*4 Transfer requests [menu 1: 1=No,2=Yes]
  MRPTRFFLG M*4 Transfers firm [menu 1: 1=No,2=Yes]
  MRPTRFSTO M*4 Transfers [menu 1: 1=No,2=Yes]
  MRPTRPFLG M*4 Transfers planned [menu 1: 1=No,2=Yes]
  MRPTWD TWD Weekly structure -> [TWD]TWD0 =[PCB]MRPTWD (TABWEEDIA) !Block
  MRPWAISTO M*4 Pending issues [menu 1: 1=No,2=Yes]
  MRPWEENBR C*4 Number of week groupings
  MRPWOFFLG M*4 Work orders released [menu 1: 1=No,2=Yes]
  MRPWOPFLG M*4 Work orders planned [menu 1: 1=No,2=Yes]
  MRPWOSFCY M*4 Gen. WO sugg. [menu 1: 1=No,2=Yes]
  MRPWOSFCYI M*4 Gen. intersite sugg. [menu 1: 1=No,2=Yes]
  MRPWOSFLG M*4 Suggested production orders [menu 1: 1=No,2=Yes]
  REOPOLDIS M*4 Ignore policy [menu 1: 1=No,2=Yes]
  REOPOLDISS M*4 Ignore policy [menu 1: 1=No,2=Yes]
  RESBLWLOT M*4 Resource [menu 1: 1=No,2=Yes]
  RESBLWLOTS M*4 Resource [menu 1: 1=No,2=Yes]
  RPLBWDLTI C*3(8) Backward lead time
  RPLBWDLTIS C*3(8) Backward lead time
  RPLFRWLTI C*3(8) Forward lead time
  RPLFRWLTIS C*3(8) Forward lead time
  RPLMOD M*15(8) Replan. mode [menu 738: 1=No processing,2=Messages only,3=Simulation]
  RPLMODS M*15(8) Replan. mode [menu 738: 1=No processing,2=Messages only,3=Simulation]
  RPLTYP M*15(8) Order type [menu 2734: 1=WOF,2=WOP,3=POF,4=POP,5=TRF,6=TRP,7=EOF,8=EOP]
  RPLTYPS M*15(8) Order type [menu 2734: 1=WOF,2=WOP,3=POF,4=POP,5=TRF,6=TRP,7=EOF,8=EOP]
  RPLUPDDAT M*15(8) Replan. date [menu 2736: 1=None,2=Early,3=Late,4=Early/late]
  RPLUPDDATS M*15(8) Replan. date [menu 2736: 1=None,2=Early,3=Late,4=Early/late]
  RPLUPDQTY M*15(8) Replan. qty [menu 2735: 1=None,2=Decrease,3=Increase,4=Decrease/increase]
  RPLUPDQTYS M*15(8) Replan. qty [menu 2735: 1=None,2=Decrease,3=Increase,4=Decrease/increase]
  STOFCY FCY Storage site -> [FCY]FCY0 =[PCB]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WIPPRO M*4 WIP protect. [menu 2740: 1=No,2=Always,3=According to product]
  WIPPROS M*4 WIP protect. [menu 2740: 1=No,2=Always,3=According to product]

## PARSTOACC (PAS) - Stock interface setup
Keys (first = PK; D = duplicates allowed): PAS0 LEG+CPY+TRSTYP
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[PAS]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  KEY1 A*50 Key
  KEY2 A*50 Key
  KEY3 A*50 Key
  KEY4 A*50 Key
  KEY5 A*50 Key
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SCHGD (SGD) - Stock change line
Keys (first = PK; D = duplicates allowed): SGD0 VCRNUM+VCRLIN
Fields:
  AUUID AUUID Single identifier
  COEDES COE PAC-STK factor
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  EXPNUM L*8 Export number
  IMPNUMLIG L*8 Import line
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[SGD]ITMREF (ITMMASTER) !Block
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Other
  LOCTYP TLO Location type -> [TLO]TLO0 =STOFCY;LOCTYP (TABLOCTYP) !Other
  LOT LOT Lot
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Unit -> [TUN]TUN0 =[SGD]PCU (TABUNIT) !Block
  PCUDES A*5 Destination unit
  PCUSTUCOE COE PAC-STK conversion
  PRI MD8 Net price - tax
  QLYCTLDEM VCR Quality control
  QLYCTLFLG M*4 Analysis request [menu 1: 1=No,2=Yes]
  QTYPCU QTY Quantity
  QTYPCUDES QTY PAC quantity
  QTYSTUDES QTY STK quantity
  SERNUM SER Serial number
  SERNUMF SER Ending serial number
  SLO SLO Sublot
  STA A*3 Status
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  STU UOM Stock unit -> [TUN]TUN0 =[SGD]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SCHGH (SGH) - Stock change header
Notes: differs in V9.0 P12 (diff: AT3_SCHGH.htm); differs in V10 P1 (diff: ATD_SCHGH.htm)
Keys (first = PK; D = duplicates allowed): SGH0 VCRNUM; SGH1 SIHNUM+VCRNUM
Fields:
  ARVDAT D Arrival date
  ATDTCOD A*100 AT code act:KPO
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCYCOD M*15 Destination [menu 792: 1=Internal,2=Intersite,3=Customer,4=Subcontract transfer,5=Subcontract return]
  BPCNUM BPR Customer -> [BPR]BPR0 =[SGH]BPCNUM (BPARTNER) !Block
  BPSADD ADR Address
  BPSNUM BPR Subcontractor -> [BPR]BPR0 =[SGH]BPSNUM (BPARTNER) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFMFLG M*4 Signed [menu 1: 1=No,2=Yes] act:KPO
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Customer currency -> [TCU]TCU0 =[SGH]CUR (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[SGH]DIE (GDIE) !Block act:ANA
  DPEDAT D Departure date
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[SGH]ENTCOD (GAUTACE) !Block
  ETA HM Arrival time
  ETD HM Departure time
  EXPNUM L*8 Export number
  FCYADD ADR Receipt address
  FCYDES FCY Destination site -> [FCY]FCY0 =[SGH]FCYDES (FACILITY) !Block
  IMPNUMLIG L*8 Import line
  INVFLG M*4 Invoiced [menu 1: 1=No,2=Yes]
  INVSGH M*4 To be invoiced [menu 1: 1=No,2=Yes]
  IPTDAT D Allocation date
  LICPLATE REGLIC Registration
  MANDOC DOC Manual document act:KPO
  PJT PJT Project -> [PIM]PIM0 =[SGH]PJT (PIMPL) !Block
  PURFCY FCY Purchase site -> [FCY]FCY0 =[SGH]PURFCY (FACILITY) !Block
  SALFCY FCY Sales site -> [FCY]FCY0 =[SGH]SALFCY (FACILITY) !Block
  SCOLOC LOC Subcontract loc. -> [STC]STC0 =STOFCY;SCOLOC (STOLOC) !Block
  SGHTYP TSG Doc type -> [TSG]TSG0 =SGHTYP;[V]GSUPCLE (TABSGHTYP) !Block act:TRSNE
  SIHNUM VCR Invoice no.
  STOFCY FCY Storage site -> [FCY]FCY0 =[SGH]STOFCY (FACILITY) !Block
  TMPSGHNUM VCR Doc no. act:TRSNE
  TRLLICPLATE REGLIC Trailer license plate
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRDES DES Description
  VCRNUM VCR Entry
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SCMAPAR (SZP) - APS Forecast setup
Keys (first = PK; D = duplicates allowed): SZP0 ID
Fields:
  AUUID AUUID Single identifier
  BCGCODFLG M*4 Category [menu 1: 1=No,2=Yes]
  BPCGRUFLG M*4 Group customer [menu 1: 1=No,2=Yes]
  BPCINVFLG M*4 Bill-to customer [menu 1: 1=No,2=Yes]
  CFGLINFLG M*4 Product line [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CRYFLG M*4 Country [menu 1: 1=No,2=Yes]
  DRTSTO A*250 Storage directory
  DRTWRK A*250 Work directory
  FCYCRIPIT PIT Sites/criteria -> [PIT]PIT0 =FCYCRIPIT (PIVOTS) !Block
  FCYCRITYP M*20 Code type [menu 2248: 1=Code only,2=Description only,3=Code and description]
  FCYPIT PIT Sites -> [PIT]PIT0 =FCYPIT (PIVOTS) !Block
  HISSDHFLG M*4 Deliveries/invoices [menu 1: 1=No,2=Yes]
  HISSOHFLG M*4 Closed orders [menu 1: 1=No,2=Yes]
  HISSOHPIT PIT Sales history -> [PIT]PIT0 =HISSOHPIT (PIVOTS) !Block
  ID A*10 Identifier
  INTIT DES Description
  ITMCRIPIT PIT Products/criteria -> [PIT]PIT0 =ITMCRIPIT (PIVOTS) !Block
  ITMCRITYP M*20 Code type [menu 2248: 1=Code only,2=Description only,3=Code and description]
  ITMFOR FOR Selection formula -> [TFO]TFO0 =41;ITMFOR (TABFOR) !Block
  ITMPIT PIT Products -> [PIT]PIT0 =ITMPIT (PIVOTS) !Block
  ITMTCOPIT PIT Products/conversions -> [PIT]PIT0 =ITMTCOPIT (PIVOTS) !Block
  PCU0FLG M*4 PAC unit [menu 1: 1=No,2=Yes]
  PCU1FLG M*4 PAC unit [menu 1: 1=No,2=Yes]
  PCU2FLG M*4 PAC unit [menu 1: 1=No,2=Yes]
  PCU3FLG M*4 PAC unit [menu 1: 1=No,2=Yes]
  PLANNERFLG M*4 User [menu 1: 1=No,2=Yes]
  SDHFOR FOR Selection formula -> [TFO]TFO0 =46;SDHFOR (TABFOR) !Block
  SOHFOR FOR Selection formula -> [TFO]TFO0 =45;SOHFOR (TABFOR) !Block
  SOHGRU M*15 Aggregation level [menu 2247: 1=Detail,2=Date,3=Week,4=Month]
  SOHPIT PIT Orders in progress -> [PIT]PIT0 =SOHPIT (PIVOTS) !Block
  SOSDLTFLG M*4 Product deletion [menu 1: 1=No,2=Yes]
  SOSPIT PIT Sales forecasts -> [PIT]PIT0 =SOSPIT (PIVOTS) !Block
  SOSRAZFLG M*4 Forecast rtz [menu 1: 1=No,2=Yes]
  TCLCODFLG M*4 Category [menu 1: 1=No,2=Yes]
  TSCCOD0FLG M*4 Statistical group 1 [menu 1: 1=No,2=Yes]
  TSCCOD1FLG M*4 Statistical group 2 [menu 1: 1=No,2=Yes]
  TSCCOD2FLG M*4 Statistical group 3 [menu 1: 1=No,2=Yes]
  TSCCOD3FLG M*4 Statistical group 4 [menu 1: 1=No,2=Yes]
  TSCCOD4FLG M*4 Statistical group 5 [menu 1: 1=No,2=Yes]
  TSICOD0FLG M*4 Statistical group 1 [menu 1: 1=No,2=Yes]
  TSICOD1FLG M*4 Statistical group 2 [menu 1: 1=No,2=Yes]
  TSICOD2FLG M*4 Statistical group 3 [menu 1: 1=No,2=Yes]
  TSICOD3FLG M*4 Statistical group 4 [menu 1: 1=No,2=Yes]
  TSICOD4FLG M*4 Statistical group 5 [menu 1: 1=No,2=Yes]
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VOLFILSTO ASTO*250 Storage directory
  VOLFILWRK ASTO*250 Work directory

## SCMDPAR (SDP) - SCM n.skep setup
Keys (first = PK; D = duplicates allowed): SDP0 ID
Fields:
  AUUID AUUID Single identifier
  BPCPIT PIT Customers -> [PIT]PIT0 =BPCPIT (PIVOTS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DRTISS A*250 Index destination
  DRTRCP A*250 Directory to be scanned
  DRTSTO A*250 Storage directory
  FCYPIT PIT Sites -> [PIT]PIT0 =FCYPIT (PIVOTS) !Block
  HISSDHFLG M*4 Deliveries/invoices [menu 1: 1=No,2=Yes]
  HISSOHFLG M*4 Closed orders [menu 1: 1=No,2=Yes]
  HISSOHPIT PIT Sales history -> [PIT]PIT0 =HISSOHPIT (PIVOTS) !Block
  ID A*10 Identifier
  INTIT DES Description
  ITMFCYPIT PIT Products/sites -> [PIT]PIT0 =ITMFCYPIT (PIVOTS) !Block
  ITMFOR FOR Selection formula -> [TFO]TFO0 =41;ITMFOR (TABFOR) !Block
  ITMPIT PIT Products -> [PIT]PIT0 =ITMPIT (PIVOTS) !Block
  SDHFOR FOR Selection formula -> [TFO]TFO0 =46;SDHFOR (TABFOR) !Block
  SOHFOR FOR Selection formula -> [TFO]TFO0 =45;SOHFOR (TABFOR) !Block
  SOHGRU M*15 Aggregation level [menu 2247: 1=Detail,2=Date,3=Week,4=Month]
  SOHPIT PIT Orders in progress -> [PIT]PIT0 =SOHPIT (PIVOTS) !Block
  SOSDLTFLG M*4 Product deletion [menu 1: 1=No,2=Yes]
  SOSPIT PIT Sales forecasts -> [PIT]PIT0 =SOSPIT (PIVOTS) !Block
  SOSRAZFLG M*4 Forecast rtz [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## SLOTMD (SLD) - Lot modification line
Keys (first = PK; D = duplicates allowed): SLD0 VCRNUM+VCRLIN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  EXPNUM L*8 Export number
  IMPNUMLIG L*8 Import line
  LBEFMT ARP Label format -> [ARP]ARP0 =[SLD]LBEFMT (AREPORT) !Block
  LBENBR C*4 Number of labels
  LOC EMP Location
  LOCTYP TEM Location type
  LOT LOT Lot
  PALNUM PAL Identifier 1
  PCU UOM Unit -> [TUN]TUN0 =[SLD]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conversion
  QTYPCU QTY Quantity
  QTYSTU QTY STK quantity
  SERNUM SER Serial number
  SLO SLO Sublot
  STA A*3 Status
  STU UOM Stock unit -> [TUN]TUN0 =[SLD]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry

## SLOTMH (SLH) - Lot modification header
Notes: differs in V9.0 P12 (diff: AT3_SLOTMH.htm); differs in V10 P1 (diff: ATD_SLOTMH.htm)
Keys (first = PK; D = duplicates allowed): SLH0 VCRNUM
Fields:
  AUUID AUUID Single identifier
  BPSLOT LOT Supplier lot
  BPSLOTOLD LOT Supplier lot
  CHANGECOD M*4 Lot mod type [menu 2739: 1=Lot characteristics modification,2=Renumbering, mixing and splitting]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DLU COE UBD coefficient
  DLUDAT D Use-by date
  DLUDATOLD D Use-by date
  DLUOLD COE Coefficient
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMAJOLD ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  ECCVALMINOLD EVL Minor version act:ECC
  EXPNUM L*8 Export number
  IMPNUMLIG L*8 Import line
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[SLH]ITMREF (ITMMASTER) !Block
  LOT LOT Lot
  LOTDES LOT Ship-to lot
  MODCOD M*4 Lot modif. code [menu 2745: 1=Renumbering,2=Mixing]
  MVTDES DES Movement description
  NEWLTIDAT D Recontrol date
  NEWLTIDATO D Recontrol date
  PJT PJT Project -> [PIM]PIM0 =[SLH]PJT (PIMPL) !Block
  POT DCB*5.4 Potency
  POTOLD DCB*5.4 Potency
  REFPER D Expiration reference
  REFPEROLD D Expiration reference
  SHL C*4 Shelf life
  SHLDAT D Expiration date
  SHLDATOLD D Expiration date
  SHLLTI C*4 Recontrol lead time
  SHLLTIOLD C*4 Recontrol lead time
  SHLLTIUOM M*15 Rectrl time unit [menu 2759: 1=Calendar days,2=Month]
  SHLLTIUOMO M*15 Time unit [menu 2759: 1=Calendar days,2=Month]
  SHLOLD C*4 Shelf life
  SHLUOM M*15 Expir t unit [menu 2759: 1=Calendar days,2=Month]
  SHLUOMOLD M*15 Time unit [menu 2759: 1=Calendar days,2=Month]
  SLO SLO Sublot
  SLODES SLO Ship-to sub-lot
  STOFCY FCY Storage site -> [FCY]FCY0 =[SLH]STOFCY (FACILITY) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLD1 A*20 Stock custom field 1
  USRFLD1OLD A*20 Stock custom field 1
  USRFLD2 A*10 Stock custom field 2
  USRFLD2OLD A*10 Custom field
  USRFLD3 DCB*10 Stock custom field 3
  USRFLD3OLD DCB*10 Custom field
  USRFLD4 D Stock custom field 4
  USRFLD4OLD D Custom field
  VCRDES DES Description
  VCRNUM VCR Entry

## SMVTD (SMD) - Stock movement detail
Keys (first = PK; D = duplicates allowed): SMD0 VCRTYP+VCRNUM+VCRLIN
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Other
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  IMPNUMLIG L*8 Import line
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[SMD]ITMREF (ITMMASTER) !Block
  LINTYP M*15 Line type [menu 2731: 1=Parent product,2=Component]
  PCU UOM Unit -> [TUN]TUN0 =[SMD]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conversion
  PNTMVTCOD M*4 Rec/ iss product [menu 1: 1=No,2=Yes]
  PRI MD5 Price
  PRIORD MD5 Order price
  QTYPCU QTY Quantity
  QTYPCUORI QTY Original PAC quant.
  QTYSTU QTY STK quantity
  QTYSTUORI QTY Original quantity STK
  STU UOM Stock unit -> [TUN]TUN0 =[SMD]STU (TABUNIT) !Block
  UPDCOD M*4 Stock update [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDPRI M*15 Price type [menu 220: 1=Calculated,2=Entered]
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRLINORI L*8 Source document line
  VCRLINPNT L*8 Compound line
  VCRNUM VCR Entry
  VCRNUMORI VCR Original document
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SMVTDVAL (SMV) - Movement price
Keys (first = PK; D = duplicates allowed): SMV0 VCRTYP+VCRNUM+VCRLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SMV]CREUSR (AUTILIS) !Other
  INVDTACST DCB*9.6 Invoicing element
  LABCST DCB*9.6 Labor cost act:LAB
  MACCST DCB*9.6 Machine cost act:MAC
  MATCST DCB*9.6 Material cost act:MAT
  OVELABCST DCB*9.6 Labor OH
  OVEMACCST DCB*9.6 Machine OH
  OVEMATCST DCB*9.6 Mat. OH
  OVESCOCST DCB*9.6 Sub-con OH
  SCOTOT DCB*9.6 Total subcontracted
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SMV]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## SMVTH (SMH) - Movement header
Notes: differs in V9.0 P12 (diff: AT3_SMVTH.htm); differs in V10 P1 (diff: ATD_SMVTH.htm)
Keys (first = PK; D = duplicates allowed): SMH0 VCRTYP+VCRNUM; SMH1 VCRTYP+IPTDAT+VCRNUM
Fields:
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFMCOD M*4 Validate entry [menu 1: 1=No,2=Yes]
  CFMFLG M*4 Validated [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DBYDEV MD5 Disassembly closing
  DBYFLG M*4 Disassembly [menu 1: 1=No,2=Yes]
  DIE DIE Dimension type code -> [DIE]DIE0 =[SMH]DIE (GDIE) !Block act:ANA
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[SMH]ENTCOD (GAUTACE) !Block
  EXPNUM L*8 Export number
  IMPNUMLIG L*8 Import line
  IPTDAT D Allocation date
  PJT PJT Project -> [PIM]PIM0 =[SMH]PJT (PIMPL) !Block
  STOFCY FCY Storage site -> [FCY]FCY0 =[SMH]STOFCY (FACILITY) !Block
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRDES DES Description
  VCRNUM VCR Entry
  VCRNUMORI VCR Original document
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SPACK (SPH) - Delivery package
Keys (first = PK; D = duplicates allowed): SPH0 VCRTYP+VCRNUM+PACNUM+PACSEQ; SPH1 VCRTYP+VCRNUM+SCCCOD (D)
Fields:
  AUUID AUUID Single identifier
  BPCORD BPR Sold-to -> [BPR]BPR0 =[SPH]BPCORD (BPARTNER) !Block
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CPY CPY Company -> [CPY]CPY0 =[SPH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SPH]CUR (TABCUR) !Other
  EXPNUM L*8 Export number
  LBLFMT ARP Label format -> [ARP]ARP0 =[SPH]LBLFMT (AREPORT) !Block
  NETWEI WEI Net weight
  ONEITMFLG M*4 Uniqueness of contents [menu 1: 1=No,2=Yes]
  PACNUM PCN Package no.
  PACSEQ C*4 Sequence no.
  PCK PCK Packaging -> [TPA]TPA0 =[SPH]PCK (TABPACKAGE) !Block
  PCKPRI MD1 Packaging price
  PCKWEI WEI Tare weight
  PKGTYP M*15 Packing type [menu 2753: 1=Declarative,2=Postpacking]
  PREUSR A*5 Picker
  SCCCOD A*20 SSCC code
  SPHTEX TXC Packing texts
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SPH]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VOL VOL Volume
  VOU UOM Volume unit -> [TUN]TUN0 =[SPH]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[SPH]WEU (TABUNIT) !Block

## SPACKD (SPD) - Delivery package detail
Keys (first = PK; D = duplicates allowed): SPD0 VCRTYP+VCRNUM+VCRLIN+PACNUM+PACIND+PACSEQ+VCRSEQ; SPD1 VCRTYP+VCRNUM+PACSEQ+VCRLIN+PACNUM+PACIND+VCRSEQ; SPD2 VCRTYP+VCRNUM+VCRLIN+PACNUM+PACIND+VCRSEQ+PACSEQ; SPD3 VCRTYP+VCRNUM+PACNUM+PACSEQ (D)
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[SPD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  EXPNUM L*8 Export number
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[SPD]ITMREF (ITMMASTER) !Block
  ITMWEI WEI Item weight
  LOT LOT Lot
  NETWEI WEI Net weight
  PACIND L*8 Index
  PACNUM PCN Package no.
  PACSEQ C*4 Sequence no.
  PALNUM PAL Identifier 1
  PCK PCK Packaging -> [TPA]TPA0 =[SPD]PCK (TABPACKAGE) !Block
  PCKSTKFLG M*4 Stock detail [menu 1: 1=No,2=Yes]
  PCU UOM Unit -> [TUN]TUN0 =[SPD]PCU (TABUNIT) !Block
  PCUSTUCOE COE Coefficient
  QTY QTY Quantity
  QTYPCU QTY Quantity
  SAU UOM SAL -> [TUN]TUN0 =[SPD]SAU (TABUNIT) !Block
  SERNUM SER Serial number
  SLO SLO Sublot
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SPD]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WEU UOM Weight unit -> [TUN]TUN0 =[SPD]WEU (TABUNIT) !Block
  WSTOCOU M*4 Chronological stock [menu 1: 1=No,2=Yes]

## STJTMP (SJT) - Interface - stock journal
Keys (first = PK; D = duplicates allowed): SJT0 ENTCOD+CPY+KEY1+KEY2+KEY3+KEY4+KEY5+STOFCY+UPDCOD+ITMREF+IPTDAT-MVTSEQ-MVTIND
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[SJT]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SJT]CREUSR (AUTILIS) !Other
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[SJT]ENTCOD (GAUTACE) !Block
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[SJT]ITMREF (ITMMASTER) !Block
  KEY1 A*30 Key
  KEY2 A*30 Key
  KEY3 A*30 Key
  KEY4 A*30 Key
  KEY5 A*30 Key
  MVTIND L*8 Index
  MVTSEQ L*8 Sequence
  PSTOJOU L*8 Sequence no.
  STOFCY FCY -> [FCY]FCY0 =[SJT]STOFCY (FACILITY) !Block
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDCOD M*4 Update [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SJT]UPDUSR (AUTILIS) !Other
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## STKMVTADJ (SMA) - Cost adjustment
Keys (first = PK; D = duplicates allowed): SMA0 VCRNUM+VCRLIN+VCRTYP+STOFCY+VCRNUMREG+VCRLINREG+VCRTYPREG+ITMREF+LOT+SLO; SMA1 LLC+NUM
Fields:
  AMT MS1 Amount
  AUUID AUUID Single identifier
  AVCAMT MS1 AUC base amount
  AVCQTY QTY AUC base quantity
  CPY CPY Company -> [CPY]CPY0 =[SMA]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREMVTSEQ L*8 Source sequence
  CRETIM HS Time
  CREUSR AUS User -> [AUS]CODUSR =[SMA]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[SMA]ITMREF (ITMMASTER) !Block
  LLC C*2 Lowest level code
  LOT LOT Lot
  NUM L*8 Sequence no.
  QTY QTY Quantity
  SLO SLO Sublot
  STOFCY FCY Storage site -> [FCY]FCY0 =[SMA]STOFCY (FACILITY) !Block
  TCLCOD ITG Category -> [ITG]ITG0 ="";TCLCOD (ITMCATEG) !Block
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SMA]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRLINREG L*8 Journal line no. adjusted
  VCRNUM VCR Entry
  VCRNUMREG VCR Journal adjustment
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPREG M*15 Journal adjustm type [menu 701: 40 values, see local-menus.md]

## STKREGWRK (SRW) - Cost adjustment
Keys (first = PK; D = duplicates allowed): SRW0 VCRNUM+VCRLIN+VCRTYP+CREMVTSEQ+CPY+ITMREF+LOT+SLO
Fields:
  AMT MS1 Amount
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[SRW]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREMVTSEQ L*8 Source sequence
  CRETIM HS Time
  CREUSR AUS User -> [AUS]CODUSR =[SRW]CREUSR (AUTILIS) !Other
  INVDTACST MD7 Invoicing element
  ITMREF ITM Product -> [ITM]ITM0 =[SRW]ITMREF (ITMMASTER) !Block
  LABCST MD7 Labor cost act:LAB
  LOT LOT Lot
  MACCST MD7 Machine cost act:MAC
  MATCST MD7 Material cost act:MAT
  OVELABCST MD7 Labor OH
  OVEMACCST MD7 Machine OH
  OVEMATCST MD7 Mat. OH
  OVESCOCST MD7 Sub-con OH
  QTY QTY Quantity
  SCOCST MD7 Total subcontracted
  SLO SLO Sublot
  STOFCY FCY Storage site -> [FCY]FCY0 =[SRW]STOFCY (FACILITY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SRW]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## STOACCPAR (SAC) - Actng. interface parameter
Keys (first = PK; D = duplicates allowed): SAC0 PRODAT
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FINFCY FCY Financial site -> [FCY]FCY0 =[SAC]FINFCY (FACILITY) !RTZ
  IFAFLG M*4 Posting [menu 1: 1=No,2=Yes]
  NUMEXP L*8 Current sequence number
  PRODAT D Processing date
  STOFCY FCY Storage site -> [FCY]FCY0 =[SAC]STOFCY (FACILITY) !RTZ
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SAC]UPDUSR (AUTILIS) !Other

## STOALL (STA) - Allocations
Keys (first = PK; D = duplicates allowed): STA0 STOFCY+ITMREF+STOCOU+SEQ; STA1 VCRTYP+VCRNUM+VCRLIN+VCRSEQ+STOCOU (D); STA2 ITMREF+VCRTYP+VCRNUM+VCRLIN+VCRSEQ+ALLTYP+STOFCY (D)
Fields:
  ALLDAT D Reservation ends
  ALLTYP M*15 Allocation type [menu 294: 1=Global,2=Detailed,3=Not used,4=Shortages/Detailed,5=Shortages/Global,6=Not used]
  AUUID AUUID Single identifier
  BESDAT D Requirement date
  BPAADD ADR Delivery address
  BPRNUM BPR BP -> [BPR]BPR0 =[STA]BPRNUM (BPARTNER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEFLOC EMP Def consump. locn.
  DEFLOCTYP A*5 Default consump locn type
  DEFWRH DEP Default conso whouse
  ECCVALMAJ ECS Major version act:ECC
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[STA]ITMREF (ITMMASTER) !Block
  LOC EMP Location shortage
  LOT LOT Lot shortage
  MVTDES DES Movement description
  PRECOD PRC Preparation code
  PRENUM VCR Picking no.
  QTYSTU QTY STK quantity
  QTYSTUACT QTY Active quantity STK
  SCOFLG M*30 Type of supply [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  SEQ L*8 Sequence
  SERNUM SER Serial number in shortage
  SLO SLO Sublot shortage
  SRGLIN L*8 No. list lines
  SRGLOC EMP Consumption location
  SRGNUM VCR Storage list no.
  SRGQTYSTU QTY Storage quantity STK
  STA A*3 Shortage status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[STA]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WRH DEP Shortage warehouse

## STOCK (STO) - Stock
Notes: differs in V9.0 P12 (diff: AT3_STOCK.htm); differs in V10 P1 (diff: ATD_STOCK.htm)
Keys (first = PK; D = duplicates allowed): STO0 STOFCY+STOCOU; STO1 STOFCY+PALNUM+ITMREF (D); STO3 ITMREF+STOFCY+LOT+SLO+LOC (D); STO4 STOFCY+LOC (D); STO5 ITMREF+SERNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPSLOT LOT Supplier lot
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  CUMALLQTA QTY Allocated active qty
  CUMALLQTY QTY Allocated qty.
  CUMWIPQTA QTY Act qty in process
  CUMWIPQTY QTY Qty. in process
  CUNLISNUM VCR Count worksheet
  CUNLOKFLG M*4 Count in progress [menu 1: 1=No,2=Yes]
  ECCVALMAJ ECS Major version act:ECC
  EDTFLG C*1 Edit flag
  EXPNUM L*8 Export number
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  LASCUNDAT D Last count
  LASISSDAT D Last issue date
  LASRCPDAT D Last receipt date
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOCCAT M*15 Location category [menu 2710: 1=Internal,2=Dock,3=Customer,4=Subcontract]
  LOCTYP TLO Location type -> [TLO]TLO0 =STOFCY;LOCTYP (TABLOCTYP) !Block
  LOT LOT Lot
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Packing unit -> [TUN]TUN0 =[STO]PCU (TABUNIT) !Block
  PCUORI UOM Original packing -> [TUN]TUN0 =[STO]PCUORI (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PJT PJT Project -> [PIM]PIM0 =[STO]PJT (PIMPL) !BSRA
  QLYCTLDEM VCR Analysis request
  QTYPCU QTY PAC quantity
  QTYPCUORI QTY Original PAC quant.
  QTYSTU QTY STK quantity
  QTYSTUACT QTY Active quantity STK
  QTYSTUORI QTY Original quantity STK
  RCPDAT D Date entry series
  SERNUM SER Serial number
  SLO SLO Sublot
  STA A*3 Status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Stock site -> [FCY]FCY0 =[STO]STOFCY (FACILITY) !Block
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Block act:WRH

## STOCOST (STP) - Stock FIFO cost
Keys (first = PK; D = duplicates allowed): STP0 ITMREF+STOFCY+CSTDAT+CSTTIM+CSTCOU; STP1 ITMREF+STOFCY+VCRTYP+VCRNUM+VCRLIN (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CST MD7 Value
  CSTCOU DCB*10 Chronological FIFO costs
  CSTDAT D Allocation date
  CSTTIM HS Time
  EXPNUM L*8 Export number
  INVDTACST MD7 Invoicing element act:SPD
  ITMREF ITM Product -> [ITM]ITM0 =[STP]ITMREF (ITMMASTER) !Block
  LABCST MD7 Labor cost act:LABD
  MACCST MD7 Machine cost act:MACD
  MATCST MD7 Material cost act:MATD
  OVELABCST MD7 Labor OH act:SPD
  OVEMACCST MD7 Machine OH act:SPD
  OVEMATCST MD7 Mat. OH act:SPD
  OVESCOCST MD7 Sub-con OH act:SPD
  QTYSTUACT QTY Active quantity STK
  SCOCST MD7 Total subcontracted act:SPD
  STOFCY FCY Storage site -> [FCY]FCY0 =[STP]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## STOJOU (STJ) - Stock journal
Notes: differs in V9.0 P12 (diff: AT3_STOJOU.htm); differs in V10 P1 (diff: ATD_STOJOU.htm)
Keys (first = PK; D = duplicates allowed): STJ0 STOFCY+UPDCOD+ITMREF-IPTDAT+MVTSEQ+MVTIND; STJ1 STOFCY+VCRTYP+VCRNUM+VCRLIN (D); STJ2 UPDCOD+ITMREF-IPTDAT+MVTSEQ+MVTIND (D); STJ3 UPDCOD-CREDAT-CRETIM+ITMREF (D); STJ4 ITMREF+IPTDAT+CREMVTDAT+CREMVTTIM+CREMVTSEQ (D)
Fields:
  ACCDAT D Accounting date
  ACT DCB*5.4 IU potency
  ACTQTY QTY Active quantity
  AGGIFAFLG M*4 Interface aggregation [menu 1: 1=No,2=Yes]
  AMTDEV MD1 Variance not absorbed
  AMTDEV2 MD1 Variance not absorbed act:VLT
  AMTORD MD5 Order amount
  AMTVAL MD5 Movement value
  AMTVAL2 MD5 Movement value act:VLT
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BPRNUM BPR BP -> [BPR]BPR0 =[STJ]BPRNUM (BPARTNER) !Block
  BPSLOT LOT Supplier lot
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREMVTDAT D Date created
  CREMVTSEQ L*8 Source sequence
  CREMVTTIM HS Time
  CRETIM HM Time
  CREUSR A*5 Creation user
  CSTCOU DCB*10 Chronological FIFO costs
  CSTDAT D FIFO date
  CSTTIM HS FIFO time
  CTRNUM CTR Identifier 2
  DIE DIE Dimension type code -> [DIE]DIE0 =[STJ]DIE (GDIE) !Block act:ANA
  DLUDAT D UBD
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[STJ]ENTCOD (GAUTACE) !Block
  EXPNUM L*8 Export number
  FINRSPFCY FCY Financial site -> [FCY]FCY0 =[STJ]FINRSPFCY (FACILITY) !Block
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[STJ]ITMREF (ITMMASTER) !Block
  LBEFMT ARP Label format -> [ARP]ARP0 =[STJ]LBEFMT (AREPORT) !Block
  LBENBR C*4 Number of labels
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Other
  LOT LOT Lot
  MVTDES DES Movement description
  MVTIND L*8 Index
  MVTSEQ L*8 Sequence
  NEWLTIDAT D Recontrol date
  NUMVCR VCR Accounting document
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Unit -> [TUN]TUN0 =[STJ]PCU (TABUNIT) !Block
  PCUORI UOM Original PAC -> [TUN]TUN0 =[STJ]PCUORI (TABUNIT) !Block
  PCUSTUCOE COE Coefficient
  PCUSTUORI COE Original coef.
  PJT PJT Project -> [PIM]PIM0 =[STJ]PJT (PIMPL) !Block
  POT DCB*5.4 Potency
  PRINAT M*15 Cost source [menu 705: 1=Entered,2=Standard cost,3=Revised standard cost,4=Last cost,5=Historical AUC,6=FIFO cost,7=Lot average cost,8=Order cost,9=LIFO cost,10=Last purchase price]
  PRINAT2 M*15 Cost source [menu 705: 1=Entered,2=Standard cost,3=Revised standard cost,4=Last cost,5=Historical AUC,6=FIFO cost,7=Lot average cost,8=Order cost,9=LIFO cost,10=Last purchase price] act:VLT
  PRIORD MD5 Order price
  PRIREGFLG M*4 Adjustment flag [menu 1: 1=No,2=Yes]
  PRIVAL MD5 Valued price
  PRIVAL2 MD5 Valued price act:VLT
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PRONUM L*8 Process number
  QLYCTLDEM VCR Analysis request
  QTYPCU QTY Quantity
  QTYSTU QTY STK quantity
  REGFLG M*4 Adjusted movement [menu 1: 1=No,2=Yes]
  SERNUM SER Serial number
  SHLDAT D Expiration date
  SLO SLO Sublot
  STA A*3 Status
  STOFCY FCY Storage site -> [FCY]FCY0 =[STJ]STOFCY (FACILITY) !Block
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  STU UOM Stock unit -> [TUN]TUN0 =[STJ]STU (TABUNIT) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !Block
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDCOD M*4 Update [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLD1 A*20 Stock custom field 1
  USRFLD2 A*10 Stock custom field 2
  USRFLD3 DCB*10 Stock custom field 3
  USRFLD4 D Stock custom field 4
  VARORD MD5 Order variance
  VARVAL MD5 Movement variance
  VARVAL2 MD5 Movement variance act:VLT
  VCRLIN L*8 Entry line no.
  VCRLINORI L*8 Source document line
  VCRLINREG L*8 Journal line no. adjusted
  VCRNUM VCR Entry
  VCRNUMORI VCR Original document
  VCRNUMREG VCR Journal adjustment
  VCRSEQORI L*8 Source document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  VCRTYPREG M*15 Journal adjustm type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## STOJOUOVE (SJO) - Ovhds stock movements
Keys (first = PK; D = duplicates allowed): SJV0 STOFCY+UPDCOD+ITMREF-IPTDAT+MVTSEQ+MVTIND+OVENAT
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  IPTDAT D Allocation date
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  MVTIND L*8 Index
  MVTSEQ L*8 Sequence
  ONAAMT MD1 Account amount
  OVENAT A*3 Nature
  STOFCY FCY Storage site -> [FCY]FCY0 =[SJO]STOFCY (FACILITY) !Block
  TYPCST M*15 Cost type [menu 2384: 1=As per context,2=Material,3=Machine,4=Labor,5=Subcontracting]
  UPDCOD M*4 Update [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## STOJOUVAL (SJV) - Stock movement values
Keys (first = PK; D = duplicates allowed): SJV0 STOFCY+UPDCOD+ITMREF-IPTDAT+MVTSEQ+MVTIND
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEVINVDTA MD1 Variance not absorbed
  DEVINVDTA2 MD1 Variance not absorbed act:VLT
  DEVLABCST MD1 Variance not absorbed act:LAB
  DEVLABCST2 MD1 Variance not absorbed act:LAB2
  DEVMACCST MD1 Variance not absorbed act:MAC
  DEVMACCST2 MD1 Variance not absorbed act:MAC2
  DEVMATCST MD1 Variance not absorbed act:MAT
  DEVMATCST2 MD1 Variance not absorbed act:MAT2
  DEVOVELAB MD1 Variance not absorbed
  DEVOVELAB2 MD1 Variance not absorbed act:VLT
  DEVOVEMAC MD1 Variance not absorbed
  DEVOVEMAC2 MD1 Variance not absorbed act:VLT
  DEVOVEMAT MD1 Variance not absorbed
  DEVOVEMAT2 MD1 Variance not absorbed act:VLT
  DEVOVESCO MD1 Variance not absorbed
  DEVOVESCO2 MD1 Variance not absorbed act:VLT
  DEVSCOCST MD1 Variance not absorbed
  DEVSCOCST2 MD1 Variance not absorbed act:VLT
  DOINVDTA MD1 Invoicing element
  DOLABCST MD1 Labor cost act:LAB
  DOLABTOT MD1 Total labor
  DOMACCST MD1 Machine cost act:MAC
  DOMACTOT MD1 Total machine
  DOMATCST MD1 Material cost act:MAT
  DOMATTOT MD1 Total material
  DOOVELAB MD1 Labor OH
  DOOVEMAC MD1 Machine OH
  DOOVEMAT MD1 Mat. OH
  DOOVESCO MD1 Sub-con OH
  DOSCOTOT MD1 Total subcontracted
  DV2INVDTA MD1 Invoicing element act:VLT
  DV2LABCST MD1 Labor cost act:LAB2
  DV2LABTOT MD1 Total labor act:VLT
  DV2MACCST MD1 Machine cost act:MAC2
  DV2MACTOT MD1 Total machine act:VLT
  DV2MATCST MD1 Material cost act:MAT2
  DV2MATTOT MD1 Total material act:VLT
  DV2OVELAB MD1 Labor OH act:VLT
  DV2OVEMAC MD1 Machine OH act:VLT
  DV2OVEMAT MD1 Mat. OH act:VLT
  DV2OVESCO MD1 Sub-con OH act:VLT
  DV2SCOTOT MD1 Total subcontracted act:VLT
  DVINVDTA MD1 Invoicing element
  DVLABCST MD1 Labor cost act:LAB
  DVLABTOT MD1 Total labor
  DVMACCST MD1 Machine cost act:MAC
  DVMACTOT MD1 Total machine
  DVMATCST MD1 Material cost act:MAT
  DVMATTOT MD1 Total material
  DVOVELAB MD1 Labor OH
  DVOVEMAC MD1 Machine OH
  DVOVEMAT MD1 Mat. OH
  DVOVESCO MD1 Sub-con OH
  DVSCOTOT MD1 Total subcontracted
  IPTDAT D Allocation date
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  MVTIND L*8 Index
  MVTSEQ L*8 Sequence
  OINVDTATOT MD1 Invoicing element
  OLABCST MD1 Labor cost act:LAB
  OLABTOT MD1 Total labor
  OMACCST MD1 Machine cost act:MAC
  OMACTOT MD1 Total machine
  OMATCST MD1 Material cost act:MAT
  OMATTOT MD1 Total material
  OOVELABTOT MD1 Labor OH
  OOVEMACTOT MD1 Machine OH
  OOVEMATTOT MD1 Mat. OH
  OOVESCOTOT MD1 Sub-con OH
  OSCOTOT MD1 Total subcontracted
  STOFCY FCY Storage site -> [FCY]FCY0 =[SJV]STOFCY (FACILITY) !Block
  UPDCOD M*4 Update [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  V2INVDTA MD1 Invoicing element act:VLT
  V2LABCST MD1 Labor cost act:LAB2
  V2LABTOT MD1 Total labor act:VLT
  V2MACCST MD1 Machine cost act:MAC2
  V2MACTOT MD1 Total machine act:VLT
  V2MATCST MD1 Material cost act:MAT2
  V2MATTOT MD1 Total material act:VLT
  V2OVELAB MD1 Labor OH act:VLT
  V2OVEMAC MD1 Machine OH act:VLT
  V2OVEMAT MD1 Mat. OH act:VLT
  V2OVESCO MD1 Sub-con OH act:VLT
  V2SCOTOT MD1 Total subcontracted act:VLT
  VINVDTATOT MD1 Invoicing element
  VLABCST MD1 Labor cost act:LAB
  VLABTOT MD1 Total labor
  VMACCST MD1 Machine cost act:MAC
  VMACTOT MD1 Total machine
  VMATCST MD1 Material cost act:MAT
  VMATTOT MD1 Total material
  VOVELABTOT MD1 Labor OH
  VOVEMACTOT MD1 Machine OH
  VOVEMATTOT MD1 Mat. OH
  VOVESCOTOT MD1 Sub-con OH
  VSCOTOT MD1 Total subcontracted

## STOLOC (STC) - Locations
Keys (first = PK; D = duplicates allowed): STC0 STOFCY+LOC; STC1 STOFCY+OCPCOD+LOCTYP+PPSSEQ; STC2 STOFCY+LOCTYP+PPSSEQ; STC3 STOFCY+LOCTYP+LOC; STC4 STOFCY+LOCCAT+LOCTYP+LOC; STC5 STOFCY+WRH+LOC
Fields:
  ALLDAT D Reservation date
  ALLHOU HM Reservation time
  ALLUSR A*5 Reservation user
  AUUID AUUID Single identifier
  AUZSST A*20 Authorized substatuses
  AVADAT D Available date
  AVAHOU HM Available time
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUNLOKFLG M*4 Count in progress [menu 1: 1=No,2=Yes]
  DEDFLG M*4 Dedicated [menu 1: 1=No,2=Yes]
  DTH C*4 Depth
  EXPNUM L*8 Export number
  FILMGTFLG M*4 Capacity managed [menu 1: 1=No,2=Yes]
  FRGMGTMOD M*15 Release mode [menu 711: 1=Immediately,2=Temporarily blocked,3=Blocked]
  HEI C*4 Height
  LOC EMP Location
  LOCCAT M*15 Location category [menu 2710: 1=Internal,2=Dock,3=Customer,4=Subcontract]
  LOCNUMFMT EMP Location format
  LOCTYP TLO Location type -> [TLO]TLO0 =STOFCY;LOCTYP (TABLOCTYP) !Block
  LOKSTA M*4 Blocked [menu 1: 1=No,2=Yes]
  MAXAUZWEI WEI Maximum weight
  MAXQTYPCU QTY Max quantity PAC
  MONITMFLG M*4 Single-product [menu 1: 1=No,2=Yes]
  OCPCOD M*15 Storage location [menu 757: 1=Empty,2=Occupied,3=Full]
  PCU UOM Packing unit -> [TUN]TUN0 =[STC]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PPSSEQ EMP Proposal sequence
  QTYPCU QTY PAC quantity
  REAFLG M*4 Replenish [menu 1: 1=No,2=Yes]
  STOFCY FCY Stock site -> [FCY]FCY0 =[STC]STOFCY (FACILITY) !Block
  TEMLTI C*3 Time delay
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WID C*4 Width
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Block act:WRH

## STOLOCAFF (STF) - Bin assignment
Keys (first = PK; D = duplicates allowed): STF0 STOFCY+LOC+ITMREF; STF1 STOFCY+ITMREF+LOC
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[STF]ITMREF (ITMMASTER) !Delete
  LOC EMP Location
  MAXSTO QTY Maximum reorder qty
  PCU UOM Reorder unit -> [TUN]TUN0 =[STF]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  QTYPCU QTY Eco reorder qty
  REOTSD QTY Reorder threshold
  STOFCY FCY Storage site -> [FCY]FCY0 =[STF]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## STOLOCRES (SWL) - Location work
Keys (first = PK; D = duplicates allowed): SWL0 PRONUM+LINNUM; SWL1 STOFCY+LOC (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ITMREF ITM Product -> [ITM]ITM0 =[SWL]ITMREF (ITMMASTER) !Delete
  LINNUM L*8 Line number
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Delete
  LOKDAT D Reservation date
  LOKHOU HM Reservation time
  MAXQTYPCU QTY Max quantity PAC
  PCU UOM Packing unit -> [TUN]TUN0 =[SWL]PCU (TABUNIT) !Delete
  PRONUM L*8 Process number
  QTYPCU QTY PAC quantity
  STA A*3 Status
  STOFCY FCY Storage site -> [FCY]FCY0 =[SWL]STOFCY (FACILITY) !Delete
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWL]UPDUSR (AUTILIS) !Other

## STOLOT (STL) - Lot numbers
Keys (first = PK; D = duplicates allowed): STL0 ITMREF+LOT+SLO; STL1 ITMREF+LOTCREDAT+LOT+SLO; STL2 ITMREF+SHLDAT+LOTCREDAT+LOT+SLO; STL3 SHLDAT+ITMREF+LOT+SLO
Fields:
  ACT DCB*5.4 IU potency
  AUUID AUUID Single identifier
  BPSLOT LOT Supplier lot
  BPSNUM BPS Supplier -> [BPS]BPS0 =[STL]BPSNUM (BPSUPPLIER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DLU COE UBD coefficient
  DLUDAT D Use-by date
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[STL]ITMREF (ITMMASTER) !Block
  LOT LOT Lot
  LOTCREDAT D Lot created
  LTIDAT D Control date
  NEWLTIDAT D Recontrol date
  POT DCB*5.4 Potency
  REFPER D Expiration reference
  SHL C*4 Shelf life
  SHLDAT D Expiration date
  SHLLTI C*4 Recontrol lead time
  SHLLTIUOM M*15 Rectrl time unit [menu 2759: 1=Calendar days,2=Month]
  SHLUOM M*15 Expir t unit [menu 2759: 1=Calendar days,2=Month]
  SLO SLO Sublot
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLD1 A*20 Stock custom field 1
  USRFLD2 A*10 Stock custom field 2
  USRFLD3 DCB*10 Stock custom field 3
  USRFLD4 D Stock custom field 4
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## STOLOTFCY (SLF) - Lots - sites
Keys (first = PK; D = duplicates allowed): SLF0 ITMREF+LOT+SLO+STOFCY
Fields:
  AAACUMQTY QTY Accepted quantity
  AINVDTAAVC MD7 Invoicing element act:SPD
  AINVDTACST MD7 Invoicing element act:SPD
  ALABAVC MD7 MAP labor cost act:LABD
  ALABCST MD7 MAP labor cost act:LABD
  AMACAVC MD7 MAP machine cost act:MACD
  AMACCST MD7 MAP machine cost act:MACD
  AMATAVC MD7 MAP material cost act:MATD
  AMATCST MD7 MAP material cost act:MATD
  AOVELABAVC MD7 MAP labor OH act:SPD
  AOVELABCST MD7 MAP labor OH act:SPD
  AOVEMACAVC MD7 MAP machine OH act:SPD
  AOVEMACCST MD7 MAP machine OH act:SPD
  AOVEMATAVC MD7 MAP material OH act:SPD
  AOVEMATCST MD7 MAP material OH act:SPD
  AOVESCOAVC MD7 MAP sub-con OH act:SPD
  AOVESCOCST MD7 MAP sub-con OH act:SPD
  ASCOAVC MD7 MAP sub-con cost act:SPD
  ASCOCST MD7 MAP sub-con cost act:SPD
  AUUID AUUID Single identifier
  AVC MD7 Average cost
  AVCBASAMT MD7 AUC base amount
  AVCBASQTY QTY AUC base quantity
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SLF]CUR (TABCUR) !Block
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[SLF]ITMREF (ITMMASTER) !Block
  LASCUNDAT D Last count
  LASISSDAT D Last issue date
  LASRCPDAT D Last receipt date
  LOT LOT Lot
  QQQCUMQTY QTY Quantity to be controlled
  RRRCUMQTY QTY Rejected quantity
  SLO SLO Sublot
  STOFCY FCY Storage site -> [FCY]FCY0 =[SLF]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## STOMVTCOST (SMC) - Link documents / FIFO stack
Keys (first = PK; D = duplicates allowed): SMC0 CSTCOU+CSTTIM+CSTDAT+VCRNUM+VCRLIN+VCRTYP; SMC1 CSTCOU+CSTTIM+CSTDAT (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SMC]CREUSR (AUTILIS) !Other
  CST MD7 Value
  CSTCOU DCB*10 Chronological FIFO costs
  CSTDAT D Allocation date
  CSTTIM HS Time
  INVDTACST MD7 Invoicing element act:SPD
  ITMREF ITM Product -> [ITM]ITM0 =[SMC]ITMREF (ITMMASTER) !Block
  LABCST MD7 Labor cost act:LABD
  MACCST MD7 Machine cost act:MACD
  MATCST MD7 Material cost act:MATD
  OVELABCST MD7 Labor OH act:SPD
  OVEMACCST MD7 Machine OH act:SPD
  OVEMATCST MD7 Mat. OH act:SPD
  OVESCOCST MD7 Sub-con OH act:SPD
  QTYSTU QTY STK quantity
  SCOCST MD7 Total subcontracted act:SPD
  STOFCY FCY Storage site -> [FCY]FCY0 =[SMC]STOFCY (FACILITY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SMC]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## STOPAR (STE) - Stock parameters
Keys (first = PK; D = duplicates allowed): STE0 STOFCY+TCLCOD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUNACCA RAT Precision Class A
  CUNACCB RAT Precision Class B
  CUNACCC RAT Precision Class C
  CUNACCD RAT Accuracy class D
  CUNCSTCOD M*15 Costing mode [menu 705: 1=Entered,2=Standard cost,3=Revised standard cost,4=Last cost,5=Historical AUC,6=FIFO cost,7=Lot average cost,8=Order cost,9=LIFO cost,10=Last purchase price]
  CUNCSTFLG M*4 Changeable [menu 1: 1=No,2=Yes]
  CUNNBRA L*8 Act counts cls A
  CUNNBRB L*8 Act counts cls B
  CUNNBRC L*8 Act counts cls C
  CUNNBRD L*8 Counts done cls D
  CYCCUNDAT D Count start date
  DAYGAPCLSA C*3 Class A interval
  DAYGAPCLSB C*3 Class B interval
  DAYGAPCLSC C*3 Class C interval
  DAYGAPCLSD C*3 Interval class D
  EOQMAXHIS C*2 Maximum history
  EOQMINHIS C*2 Minimum history
  EXPNUM L*8 Export number
  FILNAM A*100 File name
  FLDLIM A*1 Field delimiter
  FLG130 C*1 Flag
  ITMIMP A*10(20) Stock import
  LASCUNDATA D Last count Class A
  LASCUNDATB D Last count Class B
  LASCUNDATC D Last count Class C
  LASCUNDATD D Last count cls D
  LOCCARFLG M*4 Adjust. auto loc abs [menu 1: 1=No,2=Yes]
  MAXMAXHIS C*2 Max stk max hist
  MAXMINHIS C*2 Max stk min hist
  OPTDAT C*1 Date format
  ORDCST MS1 Ordering cost
  SAFMAXHIS C*2 Safety stk max hist
  SAFMINHIS C*2 Safety stk min hist
  SAFSTOFLG M*4 Include safety stock [menu 1: 1=No,2=Yes]
  SEPDEC A*1 Decimal separator
  SEPFLD A*30 Field separator
  SEPREC A*30 Record separator
  SERIMP A*10(10) Import serial numbers
  SHTAUTFLG M*4 Automatic processing [menu 1: 1=No,2=Yes]
  SHTCAT1 M*15 Document category [menu 790: 1=No,2=Sales,3=Production,4=Internal]
  SHTCAT2 M*15 Document category [menu 790: 1=No,2=Sales,3=Production,4=Internal]
  SHTCAT3 M*15 Document category [menu 790: 1=No,2=Sales,3=Production,4=Internal]
  SHTPAR1 M*15 Process backorders [menu 791: 1=No processing,2=Suspended transactions,3=Shortages on non-validated issues,4=Shortages on order & WO]
  SHTPAR2 M*15 Process backorders [menu 791: 1=No processing,2=Suspended transactions,3=Shortages on non-validated issues,4=Shortages on order & WO]
  SHTPAR3 M*15 Process backorders [menu 791: 1=No processing,2=Suspended transactions,3=Shortages on non-validated issues,4=Shortages on order & WO]
  SPEPAR A*10 Specific parameter
  SRVRATA TSA Service level Class A -> [TSA]TSA0 =[STE]SRVRATA (TABSAFSTO) !Block
  SRVRATB TSA Service level Class B -> [TSA]TSA0 =[STE]SRVRATB (TABSAFSTO) !Block
  SRVRATC TSA Service level Class C -> [TSA]TSA0 =[STE]SRVRATC (TABSAFSTO) !Block
  STACARFLG M*4 Adjust auto sta abs [menu 1: 1=No,2=Yes]
  STOCSTRAT RAT Carrying cost %
  STOFCY FCY Storage site -> [FCY]FCY0 =[STE]STOFCY (FACILITY) !Block
  TCLCOD ITG Category -> [ITG]ITG0 ="";TCLCOD (ITMCATEG) !Delete
  TSDMAXHIS C*2 Maximum history
  TSDMINHIS C*2 Reorder thresh min hist
  TYPFIL M*15 File type [menu 94: 1=ASCII (1),2=ASCII (2),3=Delimited,4=Fixed length,5=XML,6=Flat,7=With header]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  YEACUNNBRA L*8 Annual counts Class A
  YEACUNNBRB L*8 Annual counts Class B
  YEACUNNBRC L*8 Annual counts Class C
  YEACUNNBRD L*8 Ann counts cls D

## STOPRED (PRE) - Pick ticket detail
Keys (first = PK; D = duplicates allowed): PRE0 PRHNUM+PRELIN; PRE1 ORINUM+ORILIN+ORISEQ (D)
Fields:
  ALLQTY QTY Allocated qty.
  ALLTYP M*15 Allocation type [menu 294: 1=Global,2=Detailed,3=Not used,4=Shortages/Detailed,5=Shortages/Global,6=Not used]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FLGANN C*4 Cancelled line
  FLGVT C*4 VT picked line
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[PRE]ITMREF (ITMMASTER) !Block
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  LOCDES EMP Target location
  LOCTYPDES TEM Dstn. loc. type
  OALQTYSTU QTY Order qty alloc. STU
  ORILIN L*8 Line no.
  ORINUM VCR Document no.
  ORISEQ L*8 Sequence no.
  ORITYP M*20 Source [menu 2747: 1=Order,2=Loan order,3=Subcontract repl.,4=Subcontract shortage]
  ORITYPSCO C*4 Sub-contract type
  PACQTYSTU QTY Qty packed SAL
  PCK PCK Packaging -> [TPA]TPA0 =[PRE]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PCKFLG M*4 Packing [menu 1: 1=No,2=Yes]
  PCU UOM Packing unit -> [TUN]TUN0 =[PRE]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PRELIN L*8 Preparation line
  PRHNUM VCR Pick ticket
  PRPTEX TXC Picking ticket line text
  QTYSTU QTY Qty. prepared
  REOLOC EMP Subcontract loc.
  SEQ L*8 Allocation sequence
  SHTQTY QTY Shortage
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[PRE]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## STOPREH (PRH) - Pick ticket header
Keys (first = PK; D = duplicates allowed): PRH0 PRHNUM; PRH1 STOFCY+DLVFLG+PRHNUM; PRH2 STOFCY+PRLNUM+DLVFLG+PRHNUM; PRH3 SDHNUM+PRHNUM
Fields:
  AUUID AUUID Single identifier
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPCORD BPR Sold-to -> [BPR]BPR0 =[PRH]BPCORD (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PRH]BPTNUM (BPCARRIER) !Other
  CPY CPY Company -> [CPY]CPY0 =[PRH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DLVDAT D Delivery date
  DLVFLG M*10 Status [menu 2754: 1=In process,2=Deliverable,3=Delivered,4=Canceled]
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  EXPNUM L*8 Export number
  GROWEI WEI Gross weight
  NETWEI WEI Net weight
  ORIPRH M*20 Origin of note [menu 2751: 1=Order,2=Loan order,3=Subcontract requirement]
  PACFLG M*4 Packing completed [menu 1: 1=No,2=Yes]
  PACNBR C*4 Number of packages
  PRECOD PRC Preparation code
  PREUSR AUS Picker -> [AUS]CODUSR =[PRH]PREUSR (AUTILIS) !Other
  PRHNUM VCR Pick ticket
  PRLNUM VCR List no.
  PRNNPR M*4 Printed pick ticket [menu 1: 1=No,2=Yes]
  PRPTEX1 TXC PT header text
  PRPTEX2 TXC PT footer text
  SDHNUM VCR Delivery no.
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;[V]GSUPCLE (TABSDHTYP) !Block
  SHIDAT D Shipment date
  STOFCY FCY Storage site -> [FCY]FCY0 =[PRH]STOFCY (FACILITY) !Block
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !RTZ
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEU UOM Weight unit -> [TUN]TUN0 =[PRH]WEU (TABUNIT) !Block

## STOPRELIS (PRL) - Shipment preparation list
Keys (first = PK; D = duplicates allowed): PRL0 PRLNUM+PRLSEQ; PRL1 ORITYP+ORINUM+ORILIN+ORISEQ (D); PRL2 PRHNUM+PRELIN+PRLNUM+PRLSEQ (D)
Fields:
  AUUID AUUID Single identifier
  BESDAT D Requirement date
  BPAADD ADR Delivery address
  BPCORD BPR Sold-to -> [BPR]BPR0 =[PRL]BPCORD (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PRL]BPTNUM (BPCARRIER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DLVDAT D Delivery date
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[PRL]ITMREF (ITMMASTER) !Block
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  ORILIN L*8 Line no.
  ORINUM VCR Document no.
  ORISEQ L*8 Sequence no.
  ORITYP M*20 Source [menu 2747: 1=Order,2=Loan order,3=Subcontract repl.,4=Subcontract shortage]
  PCK PCK Packaging -> [TPA]TPA0 =[PRL]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PCKFLG M*4 Packing [menu 1: 1=No,2=Yes]
  PCU UOM Packing unit -> [TUN]TUN0 =[PRL]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PRECOD PRC Preparation code
  PRELIN L*8 Preparation line
  PREUSR AUS Picker -> [AUS]CODUSR =[PRL]PREUSR (AUTILIS) !Other
  PRHNUM VCR Pick ticket
  PRLNUM VCR List no.
  PRLSEQ L*8 Sequence no.
  QTYSTU QTY STK quantity
  REOLOC EMP Subcontract loc.
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;[V]GSUPCLE (TABSDHTYP) !Block
  SEQ L*8 Allocation sequence
  STOFCY FCY Storage site -> [FCY]FCY0 =[PRL]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[PRL]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## STOPRELISW (PLW) - Work preparation lists
Notes: differs in V10 P1 (diff: ATD_STOPRELISW.htm)
Keys (first = PK; D = duplicates allowed): PLW0 PRONUM+WKEY+ORITYP+ORI1+ORI2+ORI3
Fields:
  AUUID AUUID Single identifier
  BESDAT D Requirement date
  BPAADD ADR Delivery address
  BPCORD BPR Sold-to -> [BPR]BPR0 =[PLW]BPCORD (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PLW]BPTNUM (BPCARRIER) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PLW]CREUSR (AUTILIS) !Other
  DLVDAT D Delivery date
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  ITMREF ITM Product -> [ITM]ITM0 =[PLW]ITMREF (ITMMASTER) !Block
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  LOC EMP Subcontract loc.
  ORI1 A*30 Source
  ORI2 A*10 Source
  ORI3 L*8 Source
  ORITYP M*20 Source [menu 2747: 1=Order,2=Loan order,3=Subcontract repl.,4=Subcontract shortage]
  PCK PCK Packaging -> [TPA]TPA0 =[PLW]PCK (TABPACKAGE) !Other
  PCKCAP COE Packaging capacity
  PCU UOM Packing unit -> [TUN]TUN0 =[PLW]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PRECOD PRC Preparation code
  PRONUM L*8 Process number
  QTYSTU QTY Qty to prepare US
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;[V]GSUPCLE (TABSDHTYP) !Block
  STOFCY FCY Storage site -> [FCY]FCY0 =[PLW]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[PLW]STU (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PLW]UPDUSR (AUTILIS) !Other
  WKEY A*40 Data

## STOPREW (PRW) - Work preparation sheet
Keys (first = PK; D = duplicates allowed): PRW0 PRONUM+WKEY+ORITYP+ORI1+ORI2+ORI3; PRW1 PRONUM+WKEY+WKEYD+ORITYP+ORI1+ORI2+ORI3
Fields:
  AUUID AUUID Single identifier
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[PRW]BPCINV (BPARTNER) !Block
  BPCORD BPR Sold-to -> [BPR]BPR0 =[PRW]BPCORD (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PRW]BPTNUM (BPCARRIER) !Other
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PRW]CREUSR (AUTILIS) !Other
  DLVDAT D Delivery date
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  IME M*15 Invoicing mode [menu 408: 1=One/slip,2=One/closed order,3=One/order,4=One/ship-to,5=One/period,6=Manual]
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[PRW]ITMREF (ITMMASTER) !Block
  LINSCO L*8 Order line
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  MDL MDL Delivery mode -> [TMD]TMD0 =[PRW]MDL (TABMODELIV) !Block
  NUMSCO VCR Mfg./subcon. order no.
  ODL M*4 One order per delivery [menu 1: 1=No,2=Yes]
  ORI1 A*30 Source
  ORI2 A*10 Source
  ORI3 L*8 Source
  ORITYP M*20 Source [menu 2747: 1=Order,2=Loan order,3=Subcontract repl.,4=Subcontract shortage]
  PCU UOM Packing unit -> [TUN]TUN0 =[PRW]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PRECOD PRC Preparation code
  PREUSR AUS Picker -> [AUS]CODUSR =[PRW]PREUSR (AUTILIS) !Other
  PRLNUM VCR List no.
  PRLSEQ L*8 Sequence no.
  PRONUM L*8 Process number
  QTYSTU QTY Qty to prepare US
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;[V]GSUPCLE (TABSDHTYP) !Block
  SEQSCO L*8 Order sequence
  SHIDAT D Shipment date
  STOFCY FCY Storage site -> [FCY]FCY0 =[PRW]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[PRW]STU (TABUNIT) !Block
  TYPSCO C*4 Sub-contract type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PRW]UPDUSR (AUTILIS) !Other
  WDATA A*250 Data
  WDATA2 A*250 Data
  WKEY A*120 Data
  WKEYD L*8 Break key

## STOQLYD (QLD) - Quality control detail
Notes: differs in V9.0 P12 (diff: AT3_STOQLYD.htm)
Keys (first = PK; D = duplicates allowed): QLD0 VCRTYP+VCRNUM+VCRLIN; QLD1 ITMREF+STOFCY+VCRTYP+VCRNUM+VCRLIN; QLD2 VCRTYP+VCRNUM+LOT+SLO+SERNUM (D); QLD3 VCRTYP+VCRNUM+VCRLINORI+SERNUM (D)
Fields:
  AUUID AUUID Single identifier
  CRDFLG M*4 Tracking record [menu 1: 1=No,2=Yes]
  CRDSEQ L*8 Seq no. analysis file
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  ECCVALMAJ ECS Major version
  ECCVALMIN EVL Minor version
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[QLD]ITMREF (ITMMASTER) !Block
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOCTYP TLO Location type -> [TLO]TLO0 =STOFCY;LOCTYP (TABLOCTYP) !Block
  LOT LOT Lot
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Packing unit -> [TUN]TUN0 =[QLD]PCU (TABUNIT) !Block
  PCUSTUCOE COE Coefficient
  QLYCRD QLC Technical sheet -> [QLC]QLC0 =QLYCRD;1 (QLYCRD) !Block
  QTYPCU QTY PAC quantity
  QTYSTU QTY STK quantity
  SERNUM SER Serial number
  SLO SLO Sublot
  STA A*3 Status
  STOFCY FCY Storage site -> [FCY]FCY0 =[QLD]STOFCY (FACILITY) !Block
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*5 Line no. analyzed
  VCRLINORI L*8 Source document line
  VCRNUM VCR Analysis request
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Block act:WRH

## STOQLYH (QLH) - Quality control header
Notes: differs in V9.0 P12 (diff: AT3_STOQLYH.htm); differs in V10 P1 (diff: ATD_STOQLYH.htm)
Keys (first = PK; D = duplicates allowed): QLH0 VCRTYP+VCRNUM; QLH1 STOFCY+ITMREF+VCRNUM; QLH2 VALFLG+VCRTYP+VCRNUM; QLH3 VCRTYPORI+VCRNUMORI+ITMREF (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDCTLDAT D Control end date
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[QLH]ITMREF (ITMMASTER) !Block
  PJT PJT Project -> [PIM]PIM0 =[QLH]PJT (PIMPL) !Block
  QLYCRD A*8 Technical sheet
  STOFCY FCY Storage site -> [FCY]FCY0 =[QLH]STOFCY (FACILITY) !Block
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALFLG M*4 Validation flag [menu 1: 1=No,2=Yes]
  VCRNUM VCR Analysis request
  VCRNUMORI VCR Original document
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]

## STOQUAL (STQ) - Quality control
Notes: differs in V9.0 P12 (diff: AT3_STOQUAL.htm); differs in V10 P1 (diff: ATD_STOQUAL.htm)
Keys (first = PK; D = duplicates allowed): STQ0 QLYCTLDEM; STQ1 ITMREF+LOT+QLYCTLDEM
Fields:
  AAAORIQTY QTY Original accepted qty
  AAAQTY QTY Accepted qty.
  ACT DCB*5.4 IU potency
  ACTFLG M*4 IU control potency [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[STQ]BPRNUM (BPARTNER) !Block
  CRDFLG M*4 Tracking record [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDCTLDAT D Control end date
  EXPNUM L*8 Export number
  EXYFLG M*4 Expiration controlled [menu 1: 1=No,2=Yes]
  ITMREF ITM Product -> [ITM]ITM0 =[STQ]ITMREF (ITMMASTER) !Block
  LOT LOT Lot
  MVTDES DES Movement description
  MVTSEQ C*4 Sequence
  PJT PJT Project -> [PIM]PIM0 =[STQ]PJT (PIMPL) !Block
  POT DCB*5.4 Potency
  POTFLG M*4 Potency controlled [menu 1: 1=No,2=Yes]
  PRNFLG M*4 Printed document [menu 1: 1=No,2=Yes]
  QLYCRD A*8 Technical sheet
  QLYCTLDEM VCR Analysis request
  QQQORIQTY QTY Original control qty
  QQQQTY QTY QC quantity
  RRRORIQTY QTY Original rejected qty
  RRRQTY QTY Rejected qty.
  SHLDAT D Expiration date
  STAFLG M*4 Control status [menu 1: 1=No,2=Yes]
  STOFCY FCY Storage site -> [FCY]FCY0 =[STQ]STOFCY (FACILITY) !Block
  TRSNUM A*3 Transaction
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Analysis request
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## STOREO (REO) - Reorder
Keys (first = PK; D = duplicates allowed): REO0 STOFCY+LOC+ITMREF; REO1 VCRTYP+VCRNUM+VCRLIN (D)
Fields:
  AUUID AUUID Single identifier
  BESDAT D Requirement date
  BPAADD ADR Address
  BPRNUM BPR BP -> [BPR]BPR0 =[REO]BPRNUM (BPARTNER) !Block
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEFPOT DCB*5.4 Default potency %
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[REO]ITMREF (ITMMASTER) !Block
  LOC EMP Location
  LOCCAT M*15 Location category [menu 2710: 1=Internal,2=Dock,3=Customer,4=Subcontract]
  MVTDES DES Movement description
  PCU UOM Packing unit -> [TUN]TUN0 =[REO]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PRECOD PRC Preparation code
  PROTIM HM Processing time
  QTYPCU QTY PAC quantity
  QTYSTU QTY STK quantity
  QTYSTUACT QTY Active quantity STK
  QTYSTUORIA QTY Issued STK
  STAFLG M*15 Status [menu 2737: 1=Waiting reorder,2=Reorder plan]
  STOFCY FCY Storage site -> [FCY]FCY0 =[REO]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[REO]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Block act:WRH

## STOSER (STS) - Serial numbers
Keys (first = PK; D = duplicates allowed): STS0 ITMREF+SERNUM; STS2 ITMREF+SDHTYP+SDHNUM+SDDLIN+SERNUM
Fields:
  AUUID AUUID Single identifier
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCNUM;BPAADD (BPDLVCUST) !Other
  BPCNUM BPC Customer -> [BPC]BPC0 =[STS]BPCNUM (BPCUSTOMER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  GUAENDDAT D Warranty end date
  ISSDAT D Issue date
  ITMREF ITM Product -> [ITM]ITM0 =[STS]ITMREF (ITMMASTER) !Block
  RCPDAT D Receipt date
  RCPFCY FCY Receipt site -> [FCY]FCY0 =[STS]RCPFCY (FACILITY) !Block
  RCPVCRLIN L*8 Receipt document line
  RCPVCRNUM VCR Receiving document
  RCPVCRTYP M*15 Receipt document type [menu 701: 40 values, see local-menus.md]
  SDDLIN L*8 Shipment line
  SDHNUM VCR Shipment number
  SDHTYP M*15 Shipment type [menu 701: 40 values, see local-menus.md]
  SERNUM SER Serial number
  STOFCY FCY Storage site -> [FCY]FCY0 =[STS]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Line no. creation
  VCRNUM VCR Doc no. creation
  VCRTYP M*15 Doc type creation [menu 701: 40 values, see local-menus.md]

## STOSRG (SRG) - Storage
Notes: differs in V9.0 P12 (diff: AT3_STOSRG.htm); differs in V10 P1 (diff: ATD_STOSRG.htm)
Keys (first = PK; D = duplicates allowed): SRG0 STOCOU+VCRTYP+VCRNUM+VCRLIN; SRG1 STOFCY+ITMREF (D); SRG2 STOFCY+LOC (D); SRG3 STOFCY+VCRTYP+VCRNUM+VCRLIN (D); SRG4 STOFCY+SRGPPS (D); SRG5 STOFCY+VCRNUM+VCRLIN (D)
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[SRG]BPRNUM (BPARTNER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREPPS D List date
  CRETIM HM Time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[SRG]ITMREF (ITMMASTER) !Block
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  MVTDES DES Movement description
  ORICOD M*15 Source [menu 2720: 1=Awaiting put-away,2=Replenishment]
  PCU UOM Packing unit -> [TUN]TUN0 =[SRG]PCU (TABUNIT) !Block
  PCUSTUCOE COE PAC-STK conv.
  PJT PJT Project -> [PIM]PIM0 =[SRG]PJT (PIMPL) !Block
  QTYPCU QTY PAC quantity
  QTYSTU QTY STK quantity
  QTYSTUACT QTY Active quantity STK
  QUAFLG M*25 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  QUAFRE C*1 Frequency
  SRGPPS SRG List number
  STA A*3 Status
  STAFLG M*15 Status [menu 2716: 1=Awaiting put-away,2=Put-away plan]
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[SRG]STOFCY (FACILITY) !Block
  TRFFCY FCY Transfer site -> [FCY]FCY0 =[SRG]TRFFCY (FACILITY) !Other
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRLINORI L*8 Source document line
  VCRNUM VCR Entry
  VCRNUMORI VCR Original document
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Block act:WRH

## STOSRGW (SGW) - Storage (details)
Keys (first = PK; D = duplicates allowed): SGW0 STOCOU+VCRTYP+VCRNUM+VCRLIN+SRGSEQ
Fields:
  ACT DCB*5.4 IU potency
  ACTQTY QTY Active quantity
  AUUID AUUID Single identifier
  BPSLOT LOT Supplier lot
  CREDATTIM ADATIM Date time
  CREPPS D List date
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  ECCVALMAJ ECS Major version
  ECCVALMIN EVL Minor version
  EXPNUM L*8 Export number
  GESLOT A*1 Lot source
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOCTYP TLO Location type -> [TLO]TLO0 =STOFCY;LOCTYP (TABLOCTYP) !Block
  LOT LOT Lot
  ORICOD M*15 Source [menu 2720: 1=Awaiting put-away,2=Replenishment]
  PALNUM PAL Identifier 1
  PCU UOM Unit -> [TUN]TUN0 =[SGW]PCU (TABUNIT) !Block
  PCUSTUCOE COE Coefficient
  POT DCB*5.4 Potency
  QTYPCU QTY Quantity
  QTYSTU QTY STK quantity
  REFPER D Expiration reference
  SERNUM SER Serial number
  SERNUMF SER Ending serial number
  SHL C*4 Shelf life
  SHLDAT D Expiration date
  SLO SLO Sublot
  SRGPPS SRG List number
  SRGSEQ L*8 Sequence number
  STA A*3 Status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[SGW]STOFCY (FACILITY) !Block
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  STOSEQTWS C*4 TWS sequence no.
  STU UOM Stock unit -> [TUN]TUN0 =[SGW]STU (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SGW]UPDUSR (AUTILIS) !Other
  USRFLD1 A*20 Stock custom field 1
  USRFLD2 A*10 Stock custom field 2
  USRFLD3 DCB*10 Stock custom field 3
  USRFLD4 D Stock custom field 4
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Block act:WRH
  WSTOFLG C*4 Entry OK indicator

## STOSYNW (SYW) - Stock resynch work
Keys (first = PK; D = duplicates allowed): SYW0 CUNLISNUM+STOFCY+ITMREF+SEQ; SYW1 STOFCY+ITMREF+LOT+SLO+LOC+STA (D); SYW2 STOFCY+ITMREF+SERNUM (D)
Fields:
  ACT DCB*5.4 IU potency
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[SYW]BPRNUM (BPARTNER) !Other
  BPSLOT LOT Supplier lot
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  CUNLISNUM VCR Count worksheet
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[SYW]ITMREF (ITMMASTER) !Other
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Other
  LOT LOT Lot
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Unit -> [TUN]TUN0 =[SYW]PCU (TABUNIT) !Other
  PCUSTUCOE COE PAC-STK conv.
  POT DCB*5.4 Potency
  QLYCTLDEM VCR Analysis request
  QTYPCUNEW QTY Counted stock PAC
  QTYPCUSTO QTY Stock PAC
  QTYSTUNEW QTY Counted STK stock
  QTYSTUSTO QTY Stock STK
  SEQ L*8 Sequence
  SERNUM SER Serial number
  SHLDAT D Expiration date
  SLO SLO Sublot
  STA A*3 Stock status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[SYW]STOFCY (FACILITY) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRFLD1 A*20 Stock custom field 1
  USRFLD2 A*10 Stock custom field 2
  USRFLD3 DCB*10 Stock custom field 3
  USRFLD4 D Stock custom field 4

## STOTRK (STR) - Traceability
Keys (first = PK; D = duplicates allowed): STR0 ITMREF+LOT+SLO-IPTDAT+MVTSEQ+STOFCY; STR1 VCRTYP+VCRNUM+VCRLIN (D); STR2 ITMREF+SERNUM-IPTDAT+MVTSEQ+STOFCY (D)
Fields:
  ACT DCB*5.4 IU potency
  AUUID AUUID Single identifier
  BPRNUM BPR BP -> [BPR]BPR0 =[STR]BPRNUM (BPARTNER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[STR]ITMREF (ITMMASTER) !Block
  LOT LOT Lot
  MVTIND L*8 Index
  MVTSEQ L*8 Sequence
  PALNUM PAL Identifier 1
  POT DCB*5.4 Potency
  QLYCTLDEM VCR Analysis request
  QTYSTU QTY STK quantity
  REGFLG M*4 Adjusted movement [menu 1: 1=No,2=Yes]
  SERNUM SER Serial number
  SHLDAT D Expiration date
  SLO SLO Sublot
  STA A*3 Status
  STOFCY FCY Storage site -> [FCY]FCY0 =[STR]STOFCY (FACILITY) !Block
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  STU UOM Stock unit -> [TUN]TUN0 =[STR]STU (TABUNIT) !Block
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRLINORI L*8 Source document line
  VCRNUM VCR Entry
  VCRNUMORI VCR Original document
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]

## STOTRKWRK (SKW) - Traceability workfile
Keys (first = PK; D = duplicates allowed): SKW0 PRONUM+LEV; SKW1 CREUSR+CREDAT+PRONUM+LEV
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  IPTDAT D Allocation date
  ITMDESSEL DES Description 1
  ITMREF A*20 Product
  ITMREFSEL ITM Product -> [ITM]ITM0 =[SKW]ITMREFSEL (ITMMASTER) !Block
  LEV A*60 Level
  LEVALP A*20 Level
  LEVNUM C*2 Level
  LOT LOT Lot
  LOTSEL LOT Lot
  MVTSEQ L*8 Sequence
  PALNUM PAL Identifier 1
  PRONUM A*20 Process number
  REGFLG M*4 Adjusted movement [menu 1: 1=No,2=Yes]
  SEL A*20 Sign
  SERNUM SER Serial number
  SERNUMSEL SER Serial number
  SLO SLO Sublot
  SLOSEL SLO Sublot
  STOFCY FCY Storage site -> [FCY]FCY0 =[SKW]STOFCY (FACILITY) !Other
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  TRSNUM A*3 Transaction
  TRSTYP M*15 Transaction type [menu 704: 35 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SKW]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRLINORI L*8 Source document line
  VCRNUM VCR Entry
  VCRNUMORI VCR Original document
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]

## STOVALCUM (SVC) - Valuated stock totals report
Keys (first = PK; D = duplicates allowed): SVC0 PRONUM+STOFCY+TCLCOD+TSINUM+TSICOD+BUY
Fields:
  AMT MD1 Amount
  AMTDEV MD1 Variance not absorbed
  AMTDEVDAT D Calculated start date
  AUUID AUUID Single identifier
  BUY AUS Buyer -> [AUS]CODUSR =[SVC]BUY (AUTILIS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SVC]CUR (TABCUR) !Other
  PRONUM A*10 Process number
  STOFCY FCY Storage site -> [FCY]FCY0 =[SVC]STOFCY (FACILITY) !Other
  TCLCOD A*5 Category
  TSICOD ADI Statistical group -> [ADI]CODE =TSINUM;TSICOD (ATABDIV) !Block
  TSINUM C*4
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SVC]UPDUSR (AUTILIS) !Other

## STOVALWRK (STV) - Stock valuation report
Keys (first = PK; D = duplicates allowed): STV0 CREUSR+PRONUM+ITMREF+STOFCY+LOT+STOCOU
Fields:
  ACT DCB*5.4 IU potency
  AMT MD1 Amount
  AMTDEV MD1 Variance not absorbed
  AMTDEVDAT D Calculated start date
  AMTISS MD1 Issues value
  AMTRCP MD1 Receipt source
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CST MD1 Value
  CSTCOD M*15 Costing mode [menu 263: 1=Standard cost,2=Revised standard,3=Last cost,4=Cumulative AUC,5=FIFO cost,6=Lot AUC,7=Order cost,8=LIFO cost,9=Last purchase price]
  CUR CUR Currency -> [TCU]TCU0 =[STV]CUR (TABCUR) !Other
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[STV]ITMREF (ITMMASTER) !Other
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Other
  LOT LOT Lot
  PCU UOM Packing unit -> [TUN]TUN0 =[STV]PCU (TABUNIT) !Other
  PCUDEC C*1 Decimals
  POT DCB*5.4 Potency
  PRONUM A*10 Process number
  QTYPCU QTY PAC quantity
  QTYSTU QTY STK quantity
  QTYSTUISS QTY Issues
  QTYSTURCP QTY Receipts
  REFDAT D Reference date
  SLO SLO Sublot
  STA A*3 Status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[STV]STOFCY (FACILITY) !Other
  STU UOM Stock unit -> [TUN]TUN0 =[STV]STU (TABUNIT) !Other
  STUDEC C*1 Decimals
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[STV]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other

## STOWIPW (SWW) - Stock being processed
Keys (first = PK; D = duplicates allowed): SWW0 STOCOU+PRONUM+SEQ
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  PRONUM L*8 Process number
  SEQ L*8 Sequence
  STOCOU DCB*10 Chronological stock
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWW]UPDUSR (AUTILIS) !Other
  WIPQTA QTY Act qty in process
  WIPQTY QTY Qty. in process

## TABLOCTYP (TLO) - Location type table
Keys (first = PK; D = duplicates allowed): TLO0 STOFCY+LOCTYP; TLO1 STOFCY+LOCCAT+LOCTYP
Fields:
  ANYDAT D Analysis date
  ANYTIM HM Analysis time
  AUUID AUUID Single identifier
  AUZSST A*20 Authorized substatuses
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEDFLG M*4 Dedicated [menu 1: 1=No,2=Yes]
  DTH C*4 Depth
  EXPNUM L*8 Export number
  FILMGTFLG M*4 Capacity managed [menu 1: 1=No,2=Yes]
  FRGLOC L*8 Free locations
  FRGMGTMOD M*15 Release mode [menu 711: 1=Immediately,2=Temporarily blocked,3=Blocked]
  FULLOC L*8 Locations full
  HEI C*4 Height
  LOCCAT M*15 Location category [menu 2710: 1=Internal,2=Dock,3=Customer,4=Subcontract]
  LOCNUMFMT EMP Location format
  LOCTYP TEM Location type
  LOKLOC L*8 Blocked locations
  MAXAUZWEI WEI Maximum weight
  MAXQTYPCU QTY(9) Max quantity PAC
  MONITMFLG M*4 Single-product [menu 1: 1=No,2=Yes]
  OCPLOC L*8 Occupied locations
  PCU UOM(9) Packing unit -> [TUN]TUN0 =[TLO]PCU (TABUNIT) !Block
  PCUNBR C*2 Number PAC
  PERLOA DCB*3.2 Occupied %
  PPSSEQ EMP Proposal sequence
  REAFLG M*4 Replenish [menu 1: 1=No,2=Yes]
  RPLLOCTYP TEM(9) Alternate loc type
  RPLNBR C*2
  STOFCY FCY Stock site -> [FCY]FCY0 =[TLO]STOFCY (FACILITY) !Block
  TEMLTI C*3 Time delay
  TYPDES DES Description
  TYPDESAXX AX3 Description
  TYPSHO SHO Short description
  TYPSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WID C*4 Width

## TABPRECOD (PRC) - Preparation code
Keys (first = PK; D = duplicates allowed): PRC0 STOFCY+NUMCRIT+PRECOD; PRC1 STOFCY+PRECOD (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRIT A*250 Criteria
  DESAXX AX3 Description
  EXPNUM L*8 Export number
  FOR1 A*250 Formula
  FOR2 A*250 Formula
  FOR3 A*250 Formula
  FOR4 A*250 Formula
  FOR5 A*250 Formula
  NUMCRIT C*1 No. criteria
  PRECOD A*5 Preparation code
  PREDES A*30 Description
  STOFCY FCY Storage site -> [FCY]FCY0 =[PRC]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSAFSTO (TSA) - Safety stock coefficients
Keys (first = PK; D = duplicates allowed): TSA0 SRVRAT
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TSA]CREUSR (AUTILIS) !Other
  SRVRAT C*3 Service rate
  SRVRATAXX AX3 Description
  SRVRATCOE DCB*1.3 Safety stock factors
  SRVRATDES SHO Description
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TSA]UPDUSR (AUTILIS) !Other

## TABWIPSTO (TWS) - Blocked stock quantities
Keys (first = PK; D = duplicates allowed): TWS0 STOCOU+STOSEQ; TWS1 STOFCY+ITMREF (D); TWS2 VCRTYP+VCRNUM+VCRLIN (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[TWS]ITMREF (ITMMASTER) !Other
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[TWS]STOFCY (FACILITY) !Other
  STOSEQ C*4 Sequence no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WIPQTA QTY Active quantity
  WIPQTY QTY Quantity

## TMPKRPT (TKRPT) - Temporary print key table
Notes: differs in V10 P1 (diff: ATD_TMPKRPT.htm)
Keys (first = PK; D = duplicates allowed): TKRPT0 NUMREQ+USR+RPTCOD+VCRNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TKRPT]CREUSR (AUTILIS) !Other
  NUMREQ L*8 Query no.
  PTATCOD A*50 AT code
  PTCPYADDLIG A*35(3) Address line
  PTCPYCTY A*30 City
  PTCPYNAM A*40 Company
  PTCPYPOSCOD POS Postal code
  PTCPYSAT SAT County
  PTMENTION01 A*100 Legal mention
  PTMENTION02 A*100 Legal mention
  PTMENTION03 A*100 Legal mention
  PTMENTION04 A*100 Legal mention
  PTMENTION05 A*100 Legal mention
  PTMENTION06 A*100 Legal mention
  PTMENTION07 A*60 Legal mention
  RPTCOD ARP Report code -> [ARP]ARP0 =[TKRPT]RPTCOD (AREPORT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TKRPT]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TKRPT]USR (AUTILIS) !Other
  VCRNUM VCR Document no.

## WCUNLISDET (WCU) - Print stock count
Keys (first = PK; D = duplicates allowed): WCU0 NUMREQ+USR+CUNSSSNUM+CUNLISNUM+ITMLISNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  CUNCST MD8 Unit val.
  CUNLISNUM VCR Count worksheet
  CUNSSSNUM VCR Stock count session
  CUR CUR Currency -> [TCU]TCU0 =[WCU]CUR (TABCUR) !Other
  ECCVALMAJ ECS Major version act:ECC
  ITMLISNUM L*8 Product rank
  ITMREF ITM Product -> [ITM]ITM0 =[WCU]ITMREF (ITMMASTER) !Other
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Other
  LOT LOT Lot
  NUMREQ L*8 Query no.
  PALNUM PAL Identifier 1
  PCU UOM Unit -> [TUN]TUN0 =[WCU]PCU (TABUNIT) !Other
  PCUSTUCOE COE PAC-STK conv.
  QTYPCU QTY PAC quantity
  QTYPCUNEW QTY Counted stock PAC
  QTYSTU QTY STK quantity
  QTYSTUNEW QTY Counted STK stock
  SERNUM SER Serial number
  SLO SLO Sublot
  STA A*3 Stock status
  STOFLD1 SF1 Custom field 1 act:SFD
  STOFLD2 SF2 Custom field 2 act:SFD
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  USR AUS Operator -> [AUS]CODUSR =[WCU]USR (AUTILIS) !Other
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## WRKSTOCNS (WCN) - Transfer stock inquiry
Keys (first = PK; D = duplicates allowed): WCN0 NUMREQ+USR+NUMLIG
Fields:
  AUUID AUUID Single identifier
  BPSLOT LOT Supplier lot
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[WCN]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[WCN]ITMREF (ITMMASTER) !Block
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOT LOT Lot
  NUMLIG L*8 Line no.
  NUMREQ L*8 Query no.
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[WCN]PRHFCY (FACILITY) !Block
  QTYSTU QTY STK quantity
  SERNUM SER Serial number
  SLO SLO Sublot
  STA A*3 Status
  STOFCY FCY Storage site -> [FCY]FCY0 =[WCN]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[WCN]STU (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[WCN]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[WCN]USR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## WRKSTOPER (WSP) - Stock by date inquiry
Keys (first = PK; D = duplicates allowed): WSP0 STOFCY+ITMREF+IPTDAT
Fields:
  AMTVAL MD1 Value
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[WSP]CREUSR (AUTILIS) !Other
  FIYNUM C*2 Fiscal year
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[WSP]ITMREF (ITMMASTER) !Block
  PERNUM C*2 Period number
  QTYSTU QTY STK quantity
  STOFCY FCY Storage site -> [FCY]FCY0 =[WSP]STOFCY (FACILITY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[WSP]UPDUSR (AUTILIS) !Other

## WSTOALL (WSTA) - Allocations
Keys (first = PK; D = duplicates allowed): WSTA0 NUMREQ+USR+STOFCY+ITMREF+STOCOU+SEQ
Fields:
  ALLDAT D Reservation ends
  ALLTYP M*15 Allocation type [menu 294: 1=Global,2=Detailed,3=Not used,4=Shortages/Detailed,5=Shortages/Global,6=Not used]
  AUUID AUUID Single identifier
  BESDAT D Requirement date
  BPAADD ADR Delivery address
  BPRNUM BPR BP -> [BPR]BPR0 =[WSTA]BPRNUM (BPARTNER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEFLOC EMP Def consump. locn.
  DEFLOCTYP A*3 Default consump locn type
  DEFWRH DEP Default conso whouse
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[WSTA]ITMREF (ITMMASTER) !Other
  LOC EMP Location shortage
  LOT LOT Lot shortage
  MVTDES DES Movement description
  NUMREQ L*8 Query no.
  PRECOD PRC Preparation code
  PRENUM VCR Picking no.
  QTYSTU QTY STK quantity
  QTYSTUACT QTY Active quantity STK
  SCOFLG M*30 Type of supply [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  SEQ L*8 Sequence
  SERNUM SER Serial number in shortage
  SLO SLO Sublot shortage
  SRGLIN L*8 No. list lines
  SRGLOC EMP Consumption location
  SRGNUM VCR Storage list no.
  SRGQTYSTU QTY Storage quantity STK
  STA A*3 Shortage status
  STOCOU DCB*10 Chronological stock
  STOFCY FCY Storage site -> [FCY]FCY0 =[WSTA]STOFCY (FACILITY) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USR AUS User code -> [AUS]CODUSR =[WSTA]USR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WRH DEP Shortage warehouse

## WSTOLOTFCY (WSL) - Lots - sites
Keys (first = PK; D = duplicates allowed): WSL0 NUMREQ+USR+ITMREF+LOT+SLO+STOFCY
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[WSL]ITMREF (ITMMASTER) !Other
  LOT LOT Lot
  NUMREQ L*8 Query no.
  SLO SLO Sublot
  STOFCY FCY Storage site -> [FCY]FCY0 =[WSL]STOFCY (FACILITY) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USR AUS Operator -> [AUS]CODUSR =[WSL]USR (AUTILIS) !Other
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 2771: 1=Delivery,2=Analysis request]

## WSTOQLYD (WQL) - Quality control detail
Keys (first = PK; D = duplicates allowed): WQL0 NUMREQ+USR+VCRTYP+VCRNUM+ITMREF+LOT
Fields:
  AUUID AUUID Single identifier
  CODSMP A*3 Sampling code
  CRDSEQ L*8 Seq no. analysis file
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTRNUM CTR Identifier 2
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[WQL]ITMREF (ITMMASTER) !Other
  LOT LOT Lot
  NUMREQ L*8 Query no.
  OWNER BPF Owner
  PALNUM PAL Identifier 1
  PCU UOM Packing unit -> [TUN]TUN0 =[WQL]PCU (TABUNIT) !Other
  PCUSTUCOE COE Coefficient
  QLYCRD A*8 Technical sheet
  QTYACP L*6 Acceptance
  QTYPCU QTY PAC quantity
  QTYSMP L*6 Sampling size
  QTYSMPACP L*6 Accepted quantity
  QTYSMPREF L*6 Refused quantity
  QTYSTU QTY STK quantity
  RENSMP ADI Reason -> [ADI]CODE =104;RENSMP (ATABDIV) !Other
  SAICOD A*1 Sampling
  SERNUM SER Serial number
  SLO SLO Sublot
  STA A*3 Status
  STASMP A*3 Status
  STASMPCAL A*3 Initial status
  STOFCY FCY Storage site -> [FCY]FCY0 =[WQL]STOFCY (FACILITY) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USR AUS Operator -> [AUS]CODUSR =[WQL]USR (AUTILIS) !Other
  VCRLIN L*5 Line no. analyzed
  VCRNUM VCR Analysis request
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## WSTOREO (WREO) - Reorder
Keys (first = PK; D = duplicates allowed): WREO0 NUMREQ+USR+ORIREO+STOFCY+LOC+ITMREF+SEQ
Fields:
  AUUID AUUID Single identifier
  BESDAT D Requirement date
  BPAADD ADR Address
  BPRNUM BPR BP -> [BPR]BPR0 =[WREO]BPRNUM (BPARTNER) !Other
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEFLOC A*15 Consump. locn
  DEFPOT DCB*5.4 Default potency %
  DEFTYPLOC A*3 Consump. type
  EXPNUM L*8 Export number
  ITMREF ITM Product -> [ITM]ITM0 =[WREO]ITMREF (ITMMASTER) !Other
  LOC EMP Location
  LOCCAT M*15 Location category [menu 2710: 1=Internal,2=Dock,3=Customer,4=Subcontract]
  MVTDES DES Movement description
  NUMREQ L*8 Query no.
  ORIREO M*15 Source [menu 2750: 1=Replenishment,2=Consumption,3=Shortage]
  PCU UOM Packing unit -> [TUN]TUN0 =[WREO]PCU (TABUNIT) !Other
  PCUSTUCOE COE PAC-STK conv.
  PRECOD PRC Preparation code
  PROTIM HM Processing time
  QTYPCU QTY PAC quantity
  QTYSTU QTY STK quantity
  QTYSTUACT QTY Active quantity STK
  QTYSTUORIA QTY Issued STK
  SEQ L*8 Sequence
  STAFLG M*15 Status [menu 2737: 1=Waiting reorder,2=Reorder plan]
  STOFCY FCY Storage site -> [FCY]FCY0 =[WREO]STOFCY (FACILITY) !Other
  STU UOM Stock unit -> [TUN]TUN0 =[WREO]STU (TABUNIT) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USR AUS Operator -> [AUS]CODUSR =[WREO]USR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

