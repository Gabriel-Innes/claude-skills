<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Manufacturing module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## ATEXMOD (ATM) - Text sequence number by module
Keys (first = PK; D = duplicates allowed): ATM0 MODULE
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[ATM]CREUSR (AUTILIS) !Other
  MODULE M*15 Module [menu 14: 20 values, see local-menus.md]
  TEXSEQ L*8 Text sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[ATM]UPDUSR (AUTILIS) !Other

## CALIBRAT (CBT) - Calibration
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): CBT0 FCY+SLE+CBTDAT+MVTSEQ
Fields:
  AUUID AUUID Single identifier
  BOX A*8 Weighing booth
  CBTDAT D Calibration date
  CBTRES M*15 Calibration results [menu 2333: 1=Correct,2=Incorrect]
  CGD CGD Calibration guide -> [CGD]CGD0 =CGD;1 (CALIGUIDES) !Block
  CGDLIG C*4 Line
  CGDNUM C*2 Number of scale
  CGDTYP M*15 Weighing type [menu 2325: 1=Center,2=Top right corner,3=Top left corner,4=Bottom right corner,5=Bottom left corner]
  CGDWEU UOM Weight unit -> [TUN]TUN0 =[CBT]CGDWEU (TABUNIT) !Block
  CGDWGG DCB*11.6 Standard weight
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM HM Time
  CREUSR A*5 Creation user
  EXCNUM L*2 Exchange number
  EXPNUM L*8 Export number
  FCY FCY Manufacturing site -> [FCY]FCY0 =[CBT]FCY (FACILITY) !Block
  LBEPRNCOD M*15 Label printout [menu 2334: 1=No printing,2=Not printed,3=Printed,4=Re-printed]
  MAXDEV DCB*11.6 Maximum error
  MVTSEQ C*4 Sequence
  SLE A*8 Weighing scale
  STI A*8 Weighing location
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEIWEI DCB*11.6 Weight recorded

## CALIGUIDES (CGD) - Calibration guides
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): CGD0 CGD+CGDLIG
Fields:
  AUUID AUUID Single identifier
  CGD A*8 Calibration guides
  CGDDES DES Description
  CGDDESAXX AX3 Description
  CGDLIG C*4 Line
  CGDNBR C*2 Amount weighed
  CGDSHO SHO Short description
  CGDSHOAXX AX1 Short description
  CGDTOL COE Standard tolerance %
  CGDTYP M*15 Weighing type [menu 2325: 1=Center,2=Top right corner,3=Top left corner,4=Bottom right corner,5=Bottom left corner]
  CGDWEU UOM Weight unit -> [TUN]TUN0 =[CGD]CGDWEU (TABUNIT) !Block
  CGDWGG DCB*11.6 Standard weight
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## CAPVAR (CPV) - Capacity variation
Keys (first = PK; D = duplicates allowed): CPV0 WST+WCRFCY
Fields:
  AUUID AUUID Single identifier
  CODVAR ADI(25) Reason -> [ADI]CODE =801;CODVAR (ATABDIV) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDDAT D(25) End date
  EXPNUM L*8 Export number
  STRDAT D(25) Start date
  TWD TWD(25) Weekly structure -> [TWD]TWD0 =[CPV]TWD (TABWEEDIA) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VARTEX TXC(25) Text
  WCRFCY FCY Manufacturing site -> [FCY]FCY0 =[CPV]WCRFCY (FACILITY) !Block
  WST WST Work center
  WSTNBR C*2(25) Number of resources

## CONTAINERS (CTN) - Containers
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): CTN0 CTN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTN A*8 Containers
  CTNDES DES Description
  CTNDESAXX AX3 Description
  CTNLBEFMT A*7 Label format
  CTNMODTAR M*4 Modifiable tare [menu 1: 1=No,2=Yes]
  CTNPRCTOL COE % tare tolerance
  CTNSAIMAN M*4 Manual weight entry [menu 1: 1=No,2=Yes]
  CTNSHO SHO Short description
  CTNSHOAXX AX1 Short description
  CTNTHETAR WEI Calculated tare
  CTNTYP M*15 Type [menu 2318: 1=Internal,2=Supplier]
  CTNUGD UGD User guides -> [UGD]UGD0 =[CTN]CTNUGD (USERGUIDES) !Block
  CTNWEU UOM Weight unit -> [TUN]TUN0 =[CTN]CTNWEU (TABUNIT) !Block
  EXPNUM L*8 Export number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## HANDLING (HSH) - Stock process instruction
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): HSH0 HSH
Fields:
  AUUID AUUID Single identifier
  CLECTNAUT COE Close packaging %
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESAXX AX3 Description
  ENMRSY RSY(4) Environment sentence -> [RSY]RSY0 =[HSH]ENMRSY (SENTENCES) !Block
  EXPNUM L*8 Export number
  HSH A*8 SHI record
  ITMTOL COE Product tolerance %
  ITMTOLNEG COE Product tolerance- %
  LBECTS A*7 Label content
  LOTSEV M*4 Lot mix [menu 1: 1=No,2=Yes]
  MAL M*4 Alterable material [menu 1: 1=No,2=Yes]
  MANREDFLG M*4 Manual adjustment [menu 9154: 1=Automatic,2=Manual,3=No]
  MCP M*4 Consumable material [menu 1: 1=No,2=Yes]
  OBL M*4 Compulsory message [menu 1: 1=No,2=Yes]
  PCK M*15 Packaging [menu 2323: 1=Internal packaging,2=Supplier packaging,3=Mixed]
  PCN ADI(8) Precautions -> [ADI]CODE =381;PCN(indice) (ATABDIV) !Block
  PLACTL M*4 Weight control [menu 1: 1=No,2=Yes]
  QLYCTL M*4 Quality operation control [menu 1: 1=No,2=Yes]
  RSKRSY RSY(4) Risk sentences -> [RSY]RSY0 =[HSH]RSKRSY (SENTENCES) !Block
  SAVRSY RSY(4) Safety sentences -> [RSY]RSY0 =[HSH]SAVRSY (SENTENCES) !Block
  SHO SHO Short description
  SHOAXX AX1 Short description
  SVRITMWEI M*4 Multi-product weighing [menu 1: 1=No,2=Yes]
  TEX TXC Text
  TXC ADI(4) Toxicity codes -> [ADI]CODE =382;TXC(indice) (ATABDIV) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEIMOD M*15 Weighing method [menu 2319: 1=By variance,2=Accumulated]

## HANDLINGR (HSR) - Container instruction
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): HSR0 HSH+WEU+WEIMAW+CTN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CTN CTN Containers -> [CTN]CTN0 =[HSR]CTN (CONTAINERS) !Block
  EXPNUM L*8 Export number
  HSH A*8 SHI record
  LBEFMT A*7 Label format
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WEIMAW WEI Max authorized weight
  WEU UOM Weight unit -> [TUN]TUN0 =[HSR]WEU (TABUNIT) !Block

## ILOGIMG (ILO) - Ilog images
Keys (first = PK; D = duplicates allowed): ILO0 NOMFIC
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  IMG AB0*9 Image
  NOMFIC A*30 File name
  TIMESTAMP A*14
  TYPBLB AT
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user

## MESPAR (MPA) - MES setup
Keys (first = PK; D = duplicates allowed): MPA0 ID
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DEFSTA A*3 Default status
  DRTSTO A*250 Storage directory
  DRTWRK A*250 Work directory
  ID A*10 Identifier
  INTIT DES Description
  MFGFOR FOR Selection formula -> [TFO]TFO0 =44;MFGFOR (TABFOR) !Block
  MFIFOR FOR Selection formula -> [TFO]TFO0 =38;MFIFOR (TABFOR) !Block
  MFITPL AOE Work orders -> [AOE]AOE0 =[MPA]MFITPL (AOBJEXT) !Block
  MFMFOR FOR Selection formula -> [TFO]TFO0 =40;MFMFOR (TABFOR) !Block
  MFMTPL AOE Materials -> [AOE]AOE0 =[MPA]MFMTPL (AOBJEXT) !Block
  MFOFOR FOR Selection formula -> [TFO]TFO0 =39;MFOFOR (TABFOR) !Block
  MFOTPL AOE Operations -> [AOE]AOE0 =[MPA]MFOTPL (AOBJEXT) !Block
  MKITPL AOE Production reporting -> [AOE]AOE0 =[MPA]MKITPL (AOBJEXT) !Block
  MKMTPL AOE Tracking of materials -> [AOE]AOE0 =[MPA]MKMTPL (AOBJEXT) !Block
  MKOTPL AOE Operation tracking -> [AOE]AOE0 =[MPA]MKOTPL (AOBJEXT) !Block
  MWSFOR FOR Selection formula -> [TFO]TFO0 =37;MWSFOR (TABFOR) !Block
  MWSTPL AOE Work centers -> [AOE]AOE0 =[MPA]MWSTPL (AOBJEXT) !Block
  TMATPL AOE Employee IDs -> [AOE]AOE0 =[MPA]TMATPL (AOBJEXT) !Block
  TSRTPL AOE Rejection reasons -> [AOE]AOE0 =[MPA]TSRTPL (AOBJEXT) !Block
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VOLFILSTO ASTO*250 Storage directory
  VOLFILWRK ASTO*250 Work directory

## MFCSCRAP (MCS) - Scrap cost
Keys (first = PK; D = duplicates allowed): MCS0 STOFCY+ITMREF+VCRTYP+VCRNUM+VCRLIN+MFCTYP+UID
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTTOT MD8 Total cost
  EXPNUM L*8 Export number
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;STOFCY (ITMFACILIT) !Block
  LABCPNCST MD8 Component labor cst act:LAB
  LABCST MD8 Labor cost act:LAB
  LABTOT MD8 Total labor cost
  MACCPNCST MD8 Component machine cost act:MAC
  MACCST MD8 Machine cost act:MAC
  MACTOT MD8 Total machine
  MATCPNCST MD8 Component material costs act:MAT
  MATCST MD8 Material cost act:MAT
  MATTOT MD8 Total material
  MFCTYP M*20 Cost type [menu 2355: 1=Theoretical,2=Release,3=Expected,4=Actual,5=Real cost price for planned quantity,6=Provisional production for achieved quantity]
  OVECPNCST MD8 Component overhead cost
  OVELABCPN MD8 Cost level OH lab
  OVELABCST MD8 Labor overh
  OVEMACCPN MD8 Cost level OH mch
  OVEMACCST MD8 Machine OH cost
  OVEMATCPN MD8 Cost level OH mat
  OVEMATCST MD8 Material overhead cost
  OVESCOCPN MD8 Cost level OH sub-con
  OVESCOCST MD8 Subcontract
  OVETOT MD8 Total overhead
  QTYSTU QTY STK quantity
  SCOCPNCST MD8 Component sub-contract cost
  SCOCST MD8 Subcontract cost
  SCOTOT MD8 Total subcontracted
  STOFCY FCY Storage site -> [FCY]FCY0 =[MCS]STOFCY (FACILITY) !Block
  UID L*8 Process
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## MFGANL (MFA) - WO analysis
Keys (first = PK; D = duplicates allowed): MFA0 MFGFCY+MFGNUM+PEREND
Fields:
  AUUID AUUID Single identifier
  CPLSHR DCB*3.3 Actual loss percentage
  CPLTIMSUM DCB*9.2 Total actual time
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DELDAYNBR DCB*9.2 Early - late
  EXPNUM L*8 Export number
  EXTTIMSUM DCB*9.2 Total expected time
  ITMREF ITM Parent product -> [ITM]ITM0 =[MFA]ITMREF (ITMMASTER) !Block
  MATNBR C*4 Number of materials requisitions
  MATQTYEFF DCB*9.2 Avg mat yield
  MFGCPLLTI DCB*9.2 Actual cycle
  MFGFCY FCY Production site -> [FCY]FCY0 =[MFA]MFGFCY (FACILITY) !Block
  MFGLIN L*8 Line no.
  MFGLTI LTI Production lead time
  MFGNUM VCR Order no.
  MFGSCDLTI DCB*9.2 Schedule cycle
  OPENBR C*4 Number of actual operations
  OPEQTYEFF DCB*9.2 Avg qty yield
  OPETIMEFF DCB*9.2 Avg time yield
  PERDAYNBR C*4 No. of period days
  PEREND D Period end
  PERSTR D Period start
  SHR DCB*3.3 Shrinkage percent
  STDTIMSUM DCB*9.2 Std time total
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MFGHEAD (MFG) - Work order - header
Notes: differs in V9.0 P12 (diff: AT3_MFGHEAD.htm); differs in V10 P1 (diff: ATD_MFGHEAD.htm)
Keys (first = PK; D = duplicates allowed): MFG0 MFGNUM; MFG1 MFGFCY+MFGTRKFLG (D); MFG2 MTOREF (D)
Fields:
  ALLSTA M*15 Allocation status [menu 336: 1=Not allocated,2=Partial,3=Complete,4=Partial/Shortage,5=Complete/Shortage]
  AUUID AUUID Single identifier
  AVAMFGQTY QTY Producible quantity
  CFMFLG M*4 Validated [menu 1: 1=No,2=Yes]
  CLCSCDLTI DCB*9.2 Calculation schedule cycle
  CLODAT D Closing date
  CPLQTY QTY Total completed qty.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DETALLNBR L*8 Number of detail allocations
  EARSTRDAT D Earliest start date act:POPS
  ENDDAT D End date
  EXPNUM L*8 Export number
  EXTQTY QTY Planned quantity
  FITCAPEND D End finite capacity
  FITCAPSTR D Finite capacity start
  INFCAPEND D End date
  INFCAPSTR D Start date
  ITMCLENBR L*8 Number of products closed
  ITMLINNBR L*8 Number of products
  LATENDDAT D Latest end date act:POPS
  LTIREDCOE DCB*3.2 LT reduction coef
  MATCLENBR L*8 Number of materials closed
  MATLINNBR L*8 Number of materials
  MFGFCY FCY Production site -> [FCY]FCY0 =[MFG]MFGFCY (FACILITY) !Block
  MFGMOD M*15 Release mode [menu 333: 1=Complete,2=Materials only,3=Operations only]
  MFGNUM VCR Order no.
  MFGPIO M*2 Priority [menu 365: 1=Normal,2=Urgent,3=Very urgent]
  MFGSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  MFGTEX TXC Production text
  MFGTRKFLG M*15 Tracking flag [menu 339: 1=Pending,2=Being optimized,3=Printed,4=In progress,5=Completed,6=Closed + Costed]
  MTOREF MTO MTO network -> [MTO]MTO0 =MTOREF (MTOHEAD) !RTZ
  OBJDAT D Initial objective
  OPECLENBR L*8 No. of operations closed
  OPELINNBR L*8 Number of operations
  OPTFLG M*4 Optimization flag [menu 1: 1=No,2=Yes]
  OPTUSR A*5 Operation optimization
  OVRALLNBR L*8 Number of global allocations
  PLNFCY FCY Planning site -> [FCY]FCY0 =[MFG]PLNFCY (FACILITY) !Block
  PRPMATNBR L*8 No. of prepared mat
  PRPSTA M*15 Picking status [menu 338: 1=Not prepared,2=Partial,3=Full]
  QUACPLQTY QTY Actual QC quantity
  REJCPLQTY QTY Actual rejected qty.
  RMNEXTQTY QTY Remaining quantity
  ROUALT TRO Routing code -> [TRO]TRO0 =[MFG]ROUALT (TABROUALT) !Block
  ROUECCMAJ ICVVAL Major version act:RVM
  ROUECCMIN ICVVAL Minor version act:RVM
  ROUNUM ROH Released routing -> [ROH]ROH0 =ROUNUM;ROUALT;MFGFCY (ROUTING) !Block
  SCDFLG M*15 Scheduling status [menu 335: 1=Not scheduled,2=Scheduled,3=Reschedule,4=Optimized]
  SCDMOD M*10 Scheduling mode [menu 334: 1=Backward,2=Forward]
  SHTMATNBR L*8 Number short
  SINUM A*1 Integrale part no. act:SMI
  STRDAT D Start date
  STU UOM Stock unit -> [TUN]TUN0 =[MFG]STU (TABUNIT) !Block
  SUSFLG M*4 WO suspended flag [menu 1: 1=No,2=Yes]
  TRKFIRST D First tracking date
  TRKFIRSTC D First tracking date
  TRKLAST D Last tracking date
  TRKLASTC D Last tracking date
  TYPMOD M*15 Mode type [menu 371: 1=To be completed,2=Complete]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WGGFLG M*15 Weighing flag [menu 2329: 1=No,2=To weigh,3=Weighing plan,4=Being weighed,5=Weighed,6=Reconciled,7=Committed,8=Weighing under progress by product] act:MWM
  WGGSTA M*15 Weighing situation [menu 2321: 11 values, see local-menus.md] act:MWM

## MFGHEADTRK (MTK) - Manufacture tracking - header
Keys (first = PK; D = duplicates allowed): MTK0 MFGTRKNUM; MTK1 MFGNUM+MFGTRKNUM; MTK2 PTHNUM+PTDLIN (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENTCOD GAU Stock auto journal -> [GAU]GAU0 =[MTK]ENTCOD (GAUTACE) !Block
  EXPNUM L*8 Export number
  ITMTRKFLG M*4 Prod reporting [menu 1: 1=No,2=Yes]
  MATTRKFLG M*4 Material tracking [menu 1: 1=No,2=Yes]
  MFGFCY FCY Production site -> [FCY]FCY0 =[MTK]MFGFCY (FACILITY) !Block
  MFGMOD M*15 Release mode [menu 333: 1=Complete,2=Materials only,3=Operations only]
  MFGNUM VCR Order no.
  MFGTRKDAT D Tracking date
  MFGTRKNUM VCR Tracking number
  MTKTEX TXC Text
  NBRITM C*4 Number of released products
  NBRMAT C*4 Number of materials
  NBROPE C*4 Number of operations
  OPETRKFLG M*4 Operation tracking [menu 1: 1=No,2=Yes]
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Other
  TRSCODS ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## MFGITM (MFI) - Work orders - products
Notes: differs in V9.0 P12 (diff: AT3_MFGITM.htm); differs in V10 P1 (diff: ATD_MFGITM.htm)
Keys (first = PK; D = duplicates allowed): MFI0 MFGNUM+MFGLIN; MFI1 MFGFCY+STRDAT (D); MFI2 MFGNUM (D); PJMPJT1 PJT (D)
Fields:
  ABCCLS M*15 ABC class [menu 212: 1=Class A,2=Class B,3=Class C,4=Class D]
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BOMALT TBO BOM code -> [TBO]TBO0 =2;BOMALT (TABBOMALT) !Block
  BOMOFS C*4 Operation lead time
  BOMOPE OPE Operation number
  BPCNUM BPR Destination -> [BPR]BPR0 =BPCNUM (BPARTNER) !Block
  BPCTYPDEN M*15 Ship-to type [menu 722: 1=Site,2=Customer,3=Supplier]
  CLODAT D Closing date
  CPLQTY QTY Total completed qty.
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTFLG M*4 Valuation [menu 1: 1=No,2=Yes]
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  ENDDAT D End date
  EXPNUM L*8 Export number
  EXTQTY QTY Planned quantity
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  ITMLIN L*8 WO line
  ITMREF ITM Product -> [ITM]ITM0 =[MFI]ITMREF (ITMMASTER) !Block
  ITMSTA M*15 Line status [menu 363: 1=Pending,2=In process,3=Completed,4=Cancelled]
  ITMTYP M*15 Revenue type [menu 2301: 1=Product,2=By-product]
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  LOT LOT Lot
  MFGDES DES WO description
  MFGFCY FCY Production site -> [FCY]FCY0 =[MFI]MFGFCY (FACILITY) !Block
  MFGLIN L*8 Line no.
  MFGNUM VCR Order no.
  MFGPIO M*2 Priority [menu 365: 1=Normal,2=Urgent,3=Very urgent]
  MFGSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  MFITRKFLG M*15 Tracking flag [menu 339: 1=Pending,2=Being optimized,3=Printed,4=In progress,5=Completed,6=Closed + Costed]
  PJT PJT Project -> [PIM]PIM0 =[MFI]PJT (PIMPL) !Block
  PLANNER AUS Planner -> [AUS]CODUSR =[MFI]PLANNER (AUTILIS) !Block
  PLNFCY FCY Planning site -> [FCY]FCY0 =[MFI]PLNFCY (FACILITY) !Block
  QTYRND M*15 Quantity rounding [menu 293: 1=Round to the nearest,2=Greater than,3=Less than]
  QUACPLQTY QTY Actual QC quantity
  REJCPLQTY QTY Actual rejected qty.
  RMNEXTQTY QTY Remaining quantity
  STRDAT D Start date
  STU UOM Stock unit -> [TUN]TUN0 =[MFI]STU (TABUNIT) !Block
  TCLCOD ITG Category -> [ITG]ITG0 ="";TCLCOD (ITMCATEG) !Block
  TRKFIRST D First tracking date
  TRKFIRSTC D First tracking date
  TRKLAST D Last tracking date
  TRKLASTC D Last tracking date
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UOM UOM Release unit -> [TUN]TUN0 =[MFI]UOM (TABUNIT) !Block
  UOMEXTQTY QTY Rel quantity
  UOMSTUCOE COE STK conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WIPNUM VCR WIP order no.

## MFGITMTRK (MKI) - Manufacture tracking - products
Notes: differs in V9.0 P12 (diff: AT3_MFGITMTRK.htm); differs in V10 P1 (diff: ATD_MFGITMTRK.htm)
Keys (first = PK; D = duplicates allowed): MKI0 MFGTRKNUM+ITMTRKLIN; MKI1 MFGNUM+MFGTRKNUM+ITMTRKLIN
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =2;BOMALT (TABBOMALT) !Block
  CPLQTY QTY Actual accepted qty
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTFLG M*4 Valuation [menu 1: 1=No,2=Yes]
  EXPNUM L*8 Export number
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[MKI]ITMREF (ITMMASTER) !Block
  ITMTRKLIN L*8 Line
  ITMTYP M*15 Revenue type [menu 2301: 1=Product,2=By-product]
  LOT LOT Lot
  MFGFCY FCY Production site -> [FCY]FCY0 =[MKI]MFGFCY (FACILITY) !Block
  MFGLIN L*8 WO line
  MFGNUM VCR Order no.
  MFGTRKNUM VCR Tracking number
  PJT PJT Project -> [PIM]PIM0 =[MKI]PJT (PIMPL) !Block
  PRODTYP M*15 Tracking type [menu 2306: 1=WO,2=BOM,3=WO reintegration,4=BOM reintegration]
  QUAFLG M*15 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  QUARTNFLG M*4 Return from QC [menu 1: 1=No,2=Yes]
  STA A*3 Status
  STU UOM Stock unit -> [TUN]TUN0 =[MKI]STU (TABUNIT) !Block
  UOM UOM Release unit -> [TUN]TUN0 =[MKI]UOM (TABUNIT) !Block
  UOMCPLQTY QTY Actual quantity OK
  UOMSTUCOE COE STK conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## MFGMAT (MFM) - Work order - materials
Keys (first = PK; D = duplicates allowed): MFM0 MFGNUM+MFGLIN+BOMSEQ+ITMREF; MFM1 MFGFCY+RETDAT (D); MFM2 MFGFCY+MFGPIO+RETDAT (D); MFM3 MFGNUM+BOMOPE+ITMREF (D)
Fields:
  ALLQTY QTY Allocated quantity
  ALLSTA M*15 Allocation status [menu 340: 1=None,2=Global with shortage,3=Global,4=Detailed with shortage,5=Detailed]
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BOMOFS C*4 Operation lead time
  BOMOPE OPE Operation number
  BOMQTY QTY UOM link quantity
  BOMSEQ C*4 BOM sequence
  BOMSEQORI C*4 Source sequence act:MWM
  BOMSHO DES Link description
  BOMSTUCOE COE UOM-STK factor
  BOMUOM UOM UOM -> [TUN]TUN0 =[MFM]BOMUOM (TABUNIT) !Block
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUMFLG M*4 Cumulated requirement [menu 1: 1=No,2=Yes]
  CUMFXDQTY QTY Cumul total qty
  DEFPOT DCB*5.4 Default potency %
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  ISSMGTCOD M*15 Stock issuing method [menu 724: 1=By lot,2=FIFO,3=FEFO]
  ITMREF ITM Product -> [ITM]ITM0 =[MFM]ITMREF (ITMMASTER) !Block
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  LOC LOC Location -> [STC]STC0 =mfgfcy;loc (STOLOC) !Other
  LOT LOT Preferred lot
  MATSTA M*15 Material status [menu 363: 1=Pending,2=In process,3=Completed,4=Cancelled]
  MFGFCY FCY Production site -> [FCY]FCY0 =[MFM]MFGFCY (FACILITY) !Block
  MFGLIN L*8 Line no.
  MFGNUM VCR Order no.
  MFGPIO M*2 Priority [menu 365: 1=Normal,2=Urgent,3=Very urgent]
  MFGSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  MFMTEX TXC Link text
  MFMTRKFLG M*15 Tracking flag [menu 339: 1=Pending,2=Being optimized,3=Printed,4=In progress,5=Completed,6=Closed + Costed]
  PICPRN M*4 Materials requisition printing [menu 1: 1=No,2=Yes]
  PKC M*15 Pick list code [menu 2328: 10 values, see local-menus.md] act:MWM
  PLANNER AUS Planner -> [AUS]CODUSR =[MFM]PLANNER (AUTILIS) !Block
  PLNFCY FCY Planning site -> [FCY]FCY0 =[MFM]PLNFCY (FACILITY) !Block
  PRPSTA M*15 Picking status [menu 338: 1=Not prepared,2=Partial,3=Full]
  QTYCOD M*15 Management unit [menu 225: 1=One,2=Per hundred,3=Per thousand,4=Percentage,5=By lot]
  QTYRND M*15 Quantity rounding [menu 293: 1=Round to the nearest,2=Greater than,3=Less than]
  RELSCATIA M*4 Shrink with release [menu 1: 1=No,2=Yes]
  RETDAT D Requirement date
  RETQTY QTY Requirement quantity
  RETQTYORI QTY Source quantity act:MWM
  SCA DCB*3.3 Scrap factor %
  SCOFLG M*30 Type of supply [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  SHTQTY QTY Shortage
  STA A*12 Preferential status
  STDQTY QTY Standard quantity
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[MFM]STU (TABUNIT) !Block
  TRKFIRST D First tracking date
  TRKFIRSTC D First tracking date
  TRKLAST D Last tracking date
  TRKLASTC D Last tracking date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEQTY QTY Consumed quantity
  WGGBOX M*4 Weighing... [menu 1: 1=No,2=Yes] act:MWM
  WGGSTA M*15 Weighing situation [menu 2322: 1=Not weighed,2=In weighing process,3=Weighing,4=Reconciliation control,5=Reconciled,6=Process start control,7=Process started,8=Consumed] act:MWM
  WGGSTAAVS M*15 Weighing situation before completion [menu 2322: 1=Not weighed,2=In weighing process,3=Weighing,4=Reconciliation control,5=Reconciled,6=Process start control,7=Process started,8=Consumed] act:MWM
  WIPNUM VCR Order no.

## MFGMATTRK (MKM) - Manufacture tracking - materia
Notes: differs in V9.0 P12 (diff: AT3_MFGMATTRK.htm); differs in V10 P1 (diff: ATD_MFGMATTRK.htm)
Keys (first = PK; D = duplicates allowed): MKM0 MFGTRKNUM+MATTRKLIN; MKM1 MFGNUM+MFGTRKNUM+MATTRKLIN
Fields:
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =2;BOMALT (TABBOMALT) !Block
  BOMNUM ITM BOM -> [ITM]ITM0 =[MKM]BOMNUM (ITMMASTER) !Block
  BOMSEQ C*4 BOM sequence
  CPLWST WST Actual work center
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUMMATSUI C*1 Total
  EXPNUM L*8 Export number
  IPTDAT D Allocation date
  ITMREF ITF Product -> [ITF]ITF0 =ITMREF;MFGFCY (ITMFACILIT) !Block
  LOCPREF LOC Storage location -> [STC]STC0 =MFGFCY;LOCPREF (STOLOC) !Block
  LOTPREF LOT Preferred lot
  MATTRKLIN L*8 Line
  MATTYP M*15 Material type [menu 2306: 1=WO,2=BOM,3=WO reintegration,4=BOM reintegration]
  MFGFCY FCY Production site -> [FCY]FCY0 =[MKM]MFGFCY (FACILITY) !Block
  MFGLIN L*8 Line no.
  MFGNUM VCR Order no.
  MFGTRKNUM VCR Tracking number
  MFMEXTQTY QTY Quantity
  MFMITMREF ITM Component -> [ITM]ITM0 =[MKM]MFMITMREF (ITMMASTER) !Block
  MKMTEX TXC Text
  OPENUM OPE Operation
  PJT PJT Project -> [PIM]PIM0 =[MKM]PJT (PIMPL) !Block
  STAPREF A*12 Preferential status
  STU UOM Stock unit -> [TUN]TUN0 =[MKM]STU (TABUNIT) !Block
  TYPQTY M*15 Quantity type [menu 2311: 1=Active,2=Physical]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEQTY QTY Consumed quantity
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## MFGOPE (MFO) - Work order - operations
Keys (first = PK; D = duplicates allowed): MFO0 MFGNUM+OPENUM+OPESPLNUM; MFO1 POHNUM+POPLIN+POPSEQ (D); MFO2 MFGFCY+EXTWST+SCHSBB+MFGNUM (D)
Fields:
  ALTOPECOD M*4 Routing code ope. [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BPAADD ADR Address
  BPRNUM BPR BP -> [BPR]BPR0 =[MFO]BPRNUM (BPARTNER) !Other
  CAD DCB*6.4 Rate
  CPLCRG MD8 Actual charge
  CPLLAB WST Actual labor W/C
  CPLLABNBR C*2 Act. no. labor
  CPLOPETIM TIH Actual run time
  CPLPRI MD8 Actual price
  CPLQTY QTY Total completed qty.
  CPLSETTIM TIH Actual stp. time
  CPLUNTTIM TIH Actual unit time
  CPLWST WST Actual work center
  CPLWSTNBR C*2 Actual resources
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EFF DCB*3.3 % efficiency
  EQUNUM ITM Tools -> [ITM]ITM0 =[MFO]EQUNUM (ITMMASTER) !Block
  EXPNUM L*8 Export number
  EXTLAB WST Expected labor work center
  EXTLABNBR C*2 Exp. no. labor
  EXTOPETIM TIH Exp. run time
  EXTPRI MD8 Expected price
  EXTQTY QTY Planned quantity
  EXTSETTIM TIH Expected stp. time
  EXTSTRQTY QTY Sub-contract quantity
  EXTSTUQTY QTY Expected STK quantity
  EXTUNTTIM TIH Expected unit time
  EXTWST WST Expected W/C
  EXTWSTNBR C*2 Expected resources
  FITCAPEND D End finite capacity
  FITCAPSTR D Finite capacity start
  FRCSTRDAT D Sched forced scheduling
  FRCSTRHOU HM Forced scheduling time
  FXGNUM A*20 Fixture
  GRPSETTIM TIH Group setup time
  INFCAPEND D End date
  INFCAPSTR D Start date
  INVQTY QTY Invoiced qty.
  MFGFCY FCY Production site -> [FCY]FCY0 =[MFO]MFGFCY (FACILITY) !Block
  MFGNUM VCR Order no.
  MFGPIO M*15 Priority [menu 365: 1=Normal,2=Urgent,3=Very urgent]
  MFGSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  MFOTEX TXC Text
  MFOTRKFLG M*15 Tracking flag [menu 339: 1=Pending,2=Being optimized,3=Printed,4=In progress,5=Completed,6=Closed + Costed]
  OPEEND D End date
  OPELABCOE DCB*3.3 Labor r-time fact
  OPENUM OPE Operation
  OPENUMLEV C*1 Operation suffix
  OPEPLNNUM A*20 Operation plan
  OPEROUPCT A*20 Operation image
  OPESPLNUM C*4 Operation split
  OPESTA M*15 Operation status [menu 308: 1=Pending,2=Previous operation in process,3=Previous operation closed,4=In process,5=Closed,6=Excluded,7=Ordered]
  OPESTR D Start date
  OPESTRCOE COE SUSCU/OU factor
  OPESTUCOE COE STK-OPE conversion
  OPEUOM UOM Operation UOM -> [TUN]TUN0 =[MFO]OPEUOM (TABUNIT) !Block
  OPSNUM VCR Load no.
  PLNFCY FCY Planning site -> [FCY]FCY0 =[MFO]PLNFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  PRGNUM A*20 Program
  PRPTIM TIH Preparation time
  PSPTIM TIH Post-run time
  QUACPLQTY QTY Actual QC quantity
  REFPRI MD8 Reference price
  REJCPLQTY QTY Actual rejected qty.
  ROODES DES Ope description
  ROOTIMCOD M*15 Run time code [menu 312: 1=Proportional,2=Rate,3=Fixed]
  ROUOPENUM OPE Operation no.
  RPLIND C*3 Alternate index
  RSTMAC A*5 Machine restriction
  SCHGRP A*15 Grouping criterion
  SCHSBB A*15 Distinction criteria
  SCOCOD M*15 Subcontract [menu 311: 1=No,2=Normal,3=By exception]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[MFO]SCOITMREF (ITMMASTER) !Block
  SCOLTI LTI Subcontract LT
  SCOPUU UOM Purchase unit -> [TUN]TUN0 =[MFO]SCOPUU (TABUNIT) !Block
  SCOWST WST Subcontract work C
  SETLABCOE DCB*3.3 Labor time set fac
  SHR DCB*3.3 Shrinkage in %
  SPLCOD M*15 Splitting [menu 304: 1=None,2=Equal quantities,3=Equal run times,4=Equal run times / 1 rule,5=Equal quantities + efficiency]
  SPLMAXNBR C*4 Max splits
  STDLAB WST Standard labor
  STDLABNBR C*2 Std no. labor
  STDOPETIM TIH Standard run time
  STDQTY QTY Standard quantity
  STDSETTIM TIH Standard stp. time
  STDUNTTIM TIH Standard unit time
  STDWST WST Standard position
  STDWSTNBR C*2 Std no. workcenters
  TECCRD A*8 Technical sheet
  TIMCOD M*15 Management unit [menu 303: 1=Time for 1,2=Time for 100,3=Time for 1000,4=Time per lot]
  TIMUOMCOD M*15 Time unit [menu 301: 1=Hours,2=Minutes]
  TRKFIRST D First tracking date
  TRKFIRSTC D First tracking date
  TRKLAST D Last tracking date
  TRKLASTC D Last tracking date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WAITIM TIH Waiting time
  WIPNUM VCR WIP no.
  WSTEFF DCB*3.3 Post efficiency

## MFGOPETRK (MKO) - Manufacture tracking - operati
Notes: differs in V9.0 P12 (diff: AT3_MFGOPETRK.htm); differs in V10 P1 (diff: ATD_MFGOPETRK.htm)
Keys (first = PK; D = duplicates allowed): MKO0 MFGTRKNUM+OPETRKLIN; MKO1 MFGNUM+MFGTRKNUM+OPETRKLIN
Fields:
  AUUID AUUID Single identifier
  BPSNUM BPS Supplier -> [BPS]BPS0 =[MKO]BPSNUM (BPSUPPLIER) !Other
  CPLCRG MD8 Actual charge
  CPLLAB WST Actual labor W/C
  CPLOPETIM TIH Actual run time
  CPLPRI MD8 Actual price
  CPLQTY QTY Total completed qty.
  CPLSETTIM TIH Actual stp. time
  CPLWST WST Actual work center
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DACDAT D Entry date
  DACHOU HM Entered hour
  DACMST M*10 Milestone [menu 352: 1=None,2=Normal tracking,3=Range]
  EMPNUM C*4 Employee ID
  EXPNUM L*8 Export number
  EXTPRI MD8 Expected price
  INVQTY QTY Invoiced qty.
  IPTDAT D Allocation date
  ITMREF ITM Routing -> [ITM]ITM0 =[MKO]ITMREF (ITMMASTER) !Block
  MFGFCY FCY Production site -> [FCY]FCY0 =[MKO]MFGFCY (FACILITY) !Block
  MFGNUM VCR Order no.
  MFGTRKNUM VCR Tracking number
  MKOTEX TXC Text
  MSGNUM C*4 Message
  OPEBORNE OPE Operation range
  OPELABCOE DCB*3.3 Labor r-time fact
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  OPETRKLIN L*8 Line
  OPEUOM UOM Entry unit -> [TUN]TUN0 =[MKO]OPEUOM (TABUNIT) !Block
  OPEWORCOE COE U-OPE conversion
  PJT PJT Project -> [PIM]PIM0 =[MKO]PJT (PIMPL) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  QUACPLQTY QTY Actual QC quantity
  REJCPLQTY QTY Actual rejected qty.
  ROUALT C*2 Routing code
  ROUOPENUM OPE Operation no.
  RPLIND C*3 Alternate index
  SCANUM C*4(15) Rejection
  SETLABCOE DCB*3.3 Labor time set fac
  STDOPENUM ROT Standard operation
  TABREJQTY QTY(15) Rejection quantity
  TECCRD A*8 Technical sheet
  TIMTYP M*10 Time type [menu 399: 1=Work order,2=Product,3=Miscellaneous]
  TIMUOMCOD M*15 Time unit [menu 301: 1=Hours,2=Minutes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MFGPRN (MFP) - Work orders - documents
Keys (first = PK; D = duplicates allowed): MFP0 MFGNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ENDDAT D End date
  EXPNUM L*8 Export number
  EXTMFGFDR C*2 Expected folder
  LABTIKFLG M*4 Job ticket flag [menu 1: 1=No,2=Yes]
  LBEFMT ARP Label format -> [ARP]ARP0 =[MFP]LBEFMT (AREPORT) !Block act:NUC
  LBEMOD M*15 Labeling [menu 391: 1=Manual,2=Automatic]
  MFGFCY FCY Production site -> [FCY]FCY0 =[MFP]MFGFCY (FACILITY) !Block
  MFGFDRFLG M*4 Folder flag [menu 1: 1=No,2=Yes]
  MFGNUM VCR Order no.
  MFGTIKFLG M*4 Production slip flag [menu 1: 1=No,2=Yes]
  PCU UOM Packing unit -> [TUN]TUN0 =[MFP]PCU (TABUNIT) !Block act:NUC
  PCUNBR L*8 Number PAC act:NUC
  PCUSTUCOE COE PAC-STK conv. act:NUC
  PICLISFLG M*4 PL flag [menu 1: 1=No,2=Yes]
  PLNFCY FCY Planning site -> [FCY]FCY0 =[MFP]PLNFCY (FACILITY) !Block
  ROUNUM ITM Released routing -> [ITM]ITM0 =[MFP]ROUNUM (ITMMASTER) !Block
  ROUSHEFLG M*4 Tracking record flag [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  TECCRDFLG M*4 Technical sheet flag [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MFGTRS (MTS) - Production entry transaction
Notes: differs in V9.0 P12 (diff: AT3_MFGTRS.htm); differs in V10 P1 (diff: ATD_MFGTRS.htm)
Keys (first = PK; D = duplicates allowed): MTS0 MTSTYP+MTSNUM; MTS1 MTSNUM+MTSTYP
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[MTS]ACSCOD (ACCCOD) !Block
  ADJPRIFLG M*4 Adjusted movement [menu 1: 1=No,2=Yes]
  AQRCODS M*15 Status issued [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AQRSCRS M*15 Status [menu 99: 1=Form and table,2=Form,3=Table]
  AUUID AUUID Single identifier
  AVSTOCOD1 M*15 Available stock [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AVSTOSCR1 M*15 Available stock [menu 99: 1=Form and table,2=Form,3=Table]
  CCECOD M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ANA
  CCECODS M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCESCR M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table] act:ANA
  CONFFLG M*4 Confirmations [menu 1: 1=No,2=Yes]
  CONSMAT M*15 Material consumption [menu 354: 1=For expected quantity on first track,2=By quantity produced (limited),3=By quantity produced (unlimited)]
  CRAFF M*15 Change request [menu 60: 1=Displayed,2=Hidden] act:CCM
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[MTS]CREUSR (AUTILIS) !Block
  DENAFF M*15 Destination [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DESAFF M*15 Description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DESAXX AX3 Description
  DOCFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  DOCNAM ARP Document -> [ARP]ARP0 =[MTS]DOCNAM (AREPORT) !Block
  ECCCOD M*15 Major version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCCODMIN M*15 Minor version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCFLG M*4 Version [menu 1: 1=No,2=Yes] act:ECC
  ECCSCR M*15 Major version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  ECCSCRMIN M*15 Minor version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  EMPFLG M*15 Location modif [menu 4: 1=Decimal,2=Octal,3=Hexadecimal]
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[MTS]ENTCOD (GAUTACE) !Block
  ENTCODS GAU Auto journal code -> [GAU]GAU0 =[MTS]ENTCODS (GAUTACE) !Other
  EXPNUM L*8 Export number
  FDMA M*15 First availability [menu 60: 1=Displayed,2=Hidden]
  FILTDEF M*15 Filter default value [menu 355: 1=Not closed,2=Closed,3=All]
  FILTFLG M*15 Filter [menu 35: 1=Entered,2=Displayed,3=Hidden]
  GFY AGF Group -> [AGF]AGF0 =[MTS]GFY (AGRPFCY) !Block
  IDECOD01 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD02 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD1 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD2 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECODS1 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECODS2 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDESCR01 M*15 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR02 M*15 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR1 M*18 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR2 M*18 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCRS1 M*15 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCRS2 M*15 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  ITMECCMAJ M*10 Major version [menu 60: 1=Displayed,2=Hidden] act:ECC
  ITMECCMIN M*10 Minor version [menu 60: 1=Displayed,2=Hidden] act:ECC
  ITMMULT M*4 Multi-product [menu 1: 1=No,2=Yes]
  ITMTRKFLG M*4 Prod reporting [menu 1: 1=No,2=Yes]
  LABTIK M*4 Job ticket [menu 1: 1=No,2=Yes]
  LABTIKNAM ARP Document -> [ARP]ARP0 =[MTS]LABTIKNAM (AREPORT) !Block
  LABTIKNBR FOR Number -> [TFO]TFO0 =8;LABTIKNBR (TABFOR) !Block
  LBEMOD M*15 Labeling [menu 391: 1=Manual,2=Automatic]
  LOCCOD M*15 Location [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOCCODS M*15 Location issued [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOCFOU M*4 Supplier location [menu 1: 1=No,2=Yes]
  LOCSCR M*18 Location [menu 99: 1=Form and table,2=Form,3=Table]
  LOCSCRS M*15 Location [menu 99: 1=Form and table,2=Form,3=Table]
  LOTAFF M*15 Lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOTCOD M*15 Lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOTCODS M*15 Lot issued [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOTSCR M*18 Lot [menu 99: 1=Form and table,2=Form,3=Table]
  LOTSCRS M*15 Lot [menu 99: 1=Form and table,2=Form,3=Table]
  MATCCECOD M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ANA
  MATCCESCR M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table] act:ANA
  MATECCCOD M*15 Major version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  MATECCCODMIN M*15 Minor version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  MATECCSCR M*15 Major version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  MATECCSCRMIN M*15 Minor version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  MATRICULE M*4 Employee ID entry [menu 2303: 1=Mandatory,2=Optional,3=Prohibited]
  MATTRKFLG M*4 Material tracking [menu 1: 1=No,2=Yes]
  MCCIMPMOD M*15 Provisional cost [menu 2366: 1=No,2=Report,3=Trace,4=Report and trace]
  MFGMODC M*4 Full [menu 1: 1=No,2=Yes]
  MFGMODM M*4 Materials only [menu 1: 1=No,2=Yes]
  MFGMODO M*4 Operations only [menu 1: 1=No,2=Yes]
  MFGSTA M*15 Authorized statuses [menu 370: 1=Planned,2=Firm,3=By selection]
  MFGTIK M*4 Production slip [menu 1: 1=No,2=Yes]
  MFGTIKNAM ARP Document -> [ARP]ARP0 =[MTS]MFGTIKNAM (AREPORT) !Block
  MFGTIKNBR FOR Number -> [TFO]TFO0 =8;MFGTIKNBR (TABFOR) !Block
  MODALL M*15 Allocation method [menu 398: 1=Manual,2=Automatic (global),3=Automatic (detailed)]
  MODDOS M*15 Folder report mode [menu 372: 1=Manual,2=Automatic]
  MODJAL M*15 Scheduling mode [menu 372: 1=Manual,2=Automatic]
  MODOPT M*15 Production Scheduler [menu 372: 1=Manual,2=Automatic] act:POPS
  MTSDES A*35 Description
  MTSNUM TRS Transaction
  MTSTYP M*20 Transaction type [menu 353: 1=Manufacturing release,2=Production tracking]
  MTSTYPCAR A*2 Alpha no.
  MVTDESCOD M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESCOD1 M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESCODS M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESSCR M*18 Movement description [menu 99: 1=Form and table,2=Form,3=Table]
  MVTDESSCRS M*15 Movement description [menu 99: 1=Form and table,2=Form,3=Table]
  MWLFLG M*4 Weighing plan [menu 1: 1=No,2=Yes] act:MWM
  NBSLOFLG M*4 Sub-lot no. [menu 1: 1=No,2=Yes]
  OPECCECOD M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ANA
  OPECCESCR M*18 Analytical dimension [menu 99: 1=Form and table,2=Form,3=Table] act:ANA
  OPETRKFLG M*4 Operation tracking [menu 1: 1=No,2=Yes]
  OPEUOMMOD M*4 Unit can be modified [menu 1: 1=No,2=Yes]
  OPEUOMTYP M*15 Default unit [menu 2314: 1=Unit of operation,2=Unit of stock]
  PICLIS M*4 Pick list [menu 1: 1=No,2=Yes]
  PICLISNAM ARP Document -> [ARP]ARP0 =[MTS]PICLISNAM (AREPORT) !Block
  PICLISNBR FOR Number -> [TFO]TFO0 =8;PICLISNBR (TABFOR) !Block
  PIOAFF M*15 Priority code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PJTAFF M*15 Project [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PRNCOD1 M*15 Printing [menu 708: 1=No print,2=Labels,3=.,4=Transfer document,5=Analysis document]
  PRNNBFLG1 M*4 No. prints [menu 1: 1=No,2=Yes]
  PRNNBSCR1 M*15 No. prints [menu 99: 1=Form and table,2=Form,3=Table]
  PRNSCR1 M*15 Printing [menu 99: 1=Form and table,2=Form,3=Table]
  QTYSAI M*15 Release quantity [menu 377: 1=None,2=Technical lot,3=Economic lot]
  REBUT M*4 Reject entry [menu 1: 1=No,2=Yes]
  REDAFF M*15 % LT reduction [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REM M*4 Message [menu 1: 1=No,2=Yes]
  ROUSAI M*4 Routing entry [menu 1: 1=No,2=Yes]
  ROUSHE M*4 Routing sheet [menu 1: 1=No,2=Yes]
  ROUSHENAM ARP Document -> [ARP]ARP0 =[MTS]ROUSHENAM (AREPORT) !Block
  ROUSHENBR FOR Number -> [TFO]TFO0 =8;ROUSHENBR (TABFOR) !Block
  SCDMODSAI M*15 Scheduling mode [menu 2348: 1=Backward,2=Forward,3=By selection]
  SERCOD M*15 Starting serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERCODS M*15 Start serial issued [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD1 M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECODS M*15 End serial issued [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERESCR M*18 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERESCR1 M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERESCRS M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERSCR M*18 Starting serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERSCRS M*15 Starting serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SLOCOD M*15 Sublot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SLOCODS M*15 Sub-lot issued [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SLOSCR M*18 Sublot [menu 99: 1=Form and table,2=Form,3=Table]
  SLOSCRS M*15 Sublot [menu 99: 1=Form and table,2=Form,3=Table]
  SORTITM M*15 Sort [menu 362: 1=By product,2=By operation/product,3=By reservation date/product,4=By sequence/product]
  SPERFLG M*4 Expiration [menu 1: 1=No,2=Yes]
  SPOTFLG M*4 Potency [menu 1: 1=No,2=Yes]
  SRGWAIFLG M*4 Receipt at dock [menu 1: 1=No,2=Yes]
  SRUB1FLG M*4 Heading 1 [menu 1: 1=No,2=Yes]
  SRUB2FLG M*4 Section 2 [menu 1: 1=No,2=Yes]
  SRUB3FLG M*4 Section 3 [menu 1: 1=No,2=Yes]
  SRUB4FLG M*4 Section 4 [menu 1: 1=No,2=Yes]
  STACOD M*15 Status [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STASCR M*18 Status [menu 99: 1=Form and table,2=Form,3=Table]
  STKFLG M*4 Automatic issue [menu 1: 1=No,2=Yes]
  STOCODDEF M*15 Stock withdrawal [menu 227: 1=Immediate,2=Backflush,3=All]
  STOCODMAN M*4 Manual only [menu 1: 1=No,2=Yes]
  TECCRD M*4 Technical sheet [menu 1: 1=No,2=Yes]
  TECCRDNAM ARP Document -> [ARP]ARP0 =[MTS]TECCRDNAM (AREPORT) !Block
  TECCRDNBR FOR Number -> [TFO]TFO0 =8;TECCRDNBR (TABFOR) !Block
  TRSAUTO M*4 Automtc. transaction [menu 1: 1=No,2=Yes]
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Other
  TRSCODS ADI Movement code -> [ADI]CODE =14;TRSCODS (ATABDIV) !Other
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  TRSFAMS ADI Transaction group -> [ADI]CODE =9;TRSFAMS (ATABDIV) !RTZ
  TYPART M*10 Product type [menu 60: 1=Displayed,2=Hidden]
  TYPMAT M*10 Material type [menu 60: 1=Displayed,2=Hidden]
  TYPMODM M*15 Material mode type [menu 371: 1=To be completed,2=Complete]
  TYPMODO M*15 Operations mode type [menu 371: 1=To be completed,2=Complete]
  TYPQTY M*15 Quantity type [menu 2311: 1=Active,2=Physical]
  TYPTPS M*10 Time type [menu 60: 1=Displayed,2=Hidden]
  UOMSAI M*4 Entry in PAC [menu 1: 1=No,2=Yes]
  UOMSAIFLG M*4 UOM entry [menu 1: 1=No,2=Yes]
  UOMSAIFLG1 M*4 Enter PAC [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[MTS]UPDUSR (AUTILIS) !Block
  WRHCOD M*15 Warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHCOD1 M*15 Warehouse receipt [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHCOD2 M*15 Warehouse issue [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHOBY M*15 Single warehouse [menu 1: 1=No,2=Yes]
  WRHSCR M*15 Warehouse [menu 99: 1=Form and table,2=Form,3=Table]
  WRHSCR1 M*15 Warehouse receipt [menu 99: 1=Form and table,2=Form,3=Table]
  WRHSCR2 M*15 Warehouse issue [menu 99: 1=Form and table,2=Form,3=Table]

## MFGVERSION (MFV) - MFG version change
Keys (first = PK; D = duplicates allowed): MFV0 TABLE+VERSION+CLE
Fields:
  AUUID AUUID Single identifier
  CLE A*30 Key
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MFV]CREUSR (AUTILIS) !Other
  DATA A*30(10) Data
  TABLE A*10 Table
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MFV]UPDUSR (AUTILIS) !Other
  VERSION A*10 Version

## MODSCALE (MODL) - Weighing scale templates
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): MOD1 MODSCALE
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MODL]CREUSR (AUTILIS) !Other
  DES DES Description
  MODSCALE MOD Template -> [MODL]MOD1 =[MODL]MODSCALE (MODSCALE) !Delete
  RAZERO C*4 RTZ key code
  TARE C*4 Tare weight key code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MODL]UPDUSR (AUTILIS) !Other

## MTKCRDASW (MTA) - Technical sheets - responses
Keys (first = PK; D = duplicates allowed): MTA0 MFGTRKNUM+OPETRKLIN+QSTNUM
Fields:
  ALPASW A*50 Answer
  ASW A*50 Answer
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DATASW D Answer
  EXPNUM L*8 Export number
  FLGASW M*4 Answer [menu 1: 1=No,2=Yes]
  GPG ADI Grouping -> [ADI]CODE =102;GPG (ATABDIV) !Block
  IPTDAT D Allocation date
  MFGNUM VCR Order no.
  MFGTRKNUM VCR Tracking number
  NUMASW DCB*13 Answer
  OPENUM OPE Operation
  OPETRKLIN L*8 Line
  OSDASW M*4 Non-standard response [menu 1: 1=No,2=Yes]
  PRNCOD M*4 Printing [menu 1: 1=No,2=Yes]
  QLYCRD QLC Quality record -> [QLC]QLC0 =QLYCRD;1 (QLYCRD) !Other
  QSTNUM QST Question -> [QLQ]QLQ0 =[MTA]QSTNUM (QLYCRDQST) !Block
  RPLQLYCRD A*8 New record
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## MWMCRDASW (MWA) - Booth procedures - Responses
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): MWA0 MFGNUM+BOMOPE+ITMREF+IPTDAT+MVTSEQ+QSTNUM
Fields:
  ALPASW A*50 Answer
  ASW A*50 Answer
  AUUID AUUID Single identifier
  BOMOPE OPE Operation number
  BOX A*8 Weighing booth
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM HM Time
  CREUSR A*5 Creation user
  DATASW D Answer
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[MWA]FCY (FACILITY) !Block
  FLGASW M*4 Answer [menu 1: 1=No,2=Yes]
  GPG ADI Grouping -> [ADI]CODE =102;GPG (ATABDIV) !Block
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[MWA]ITMREF (ITMMASTER) !BSRA
  MFGNUM VCR Order no.
  MVTSEQ C*4 Sequence
  NUMASW DCB*13 Answer
  OBYPCR M*4 Mandatory [menu 1: 1=No,2=Yes]
  OSDASW M*4 Non-standard response [menu 1: 1=No,2=Yes]
  PCRTYP M*15 Procedure type [menu 2336: 1=Opening of box,2=Empty box at end of work order,3=Empty box at end of phase]
  PRNCOD M*4 Printing [menu 1: 1=No,2=Yes]
  QLYCRD QLC Quality record -> [QLC]QLC0 =QLYCRD;MVTSEQ (QLYCRD) !Block
  QSTNUM QST Question -> [QLQ]QLQ0 =[MWA]QSTNUM (QLYCRDQST) !Block
  RPLQLYCRD A*8 New record
  STI STX Weighing location -> [STX]STX0 =[MWA]STI (STATION) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## OPERATIONS (OPS) - Load in progress
Notes: differs in V9.0 P12 (diff: AT3_OPERATIONS.htm); differs in V10 P1 (diff: ATD_OPERATIONS.htm)
Keys (first = PK; D = duplicates allowed): OPS0 OPSNUM; OPS1 MFGNUM+OPENUM+OPESPLNUM; OPS2 POHNUM+POPLIN+POPSEQ (D); OPS3 MFGFCY+OPESTR+MFGNUM (D)
Fields:
  ABBFIL A*3 File abbreviation
  AUUID AUUID Single identifier
  BPSNUM BPS Supplier -> [BPS]BPS0 =[OPS]BPSNUM (BPSUPPLIER) !Other
  CPLLAB WST Actual labor W/C
  CPLLABNBR C*2 Act. no. labor
  CPLOPETIM TIH Actual run time
  CPLQTY QTY Total completed qty.
  CPLSETTIM TIH Actual stp. time
  CPLWST WST Actual work center
  CPLWSTNBR C*2 Actual resources
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  EXTLAB WST Expected labor work center
  EXTLABNBR C*2 Exp. no. labor
  EXTOPETIM TIH Exp. run time
  EXTQTY QTY Planned quantity
  EXTSETTIM TIH Expected stp. time
  EXTWST WST Expected W/C
  EXTWSTNBR C*2 Expected resources
  EXTWSTTYP M*15 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]
  FITCAPEND D End finite capacity
  FITCAPSTR D Finite capacity start
  FORPLA C*4 Forced placement act:POPS
  INFCAPEND D End date
  INFCAPSTR D Start date
  MFGFCY FCY Production site -> [FCY]FCY0 =[OPS]MFGFCY (FACILITY) !Block
  MFGNUM VCR Order no.
  OPEEND D End date
  OPELABCOE DCB*3.3 Labor r-time fact
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  OPESTA M*15 Operation status [menu 308: 1=Pending,2=Previous operation in process,3=Previous operation closed,4=In process,5=Closed,6=Excluded,7=Ordered]
  OPESTR D Start date
  OPESTUCOE COE STK-OPE conversion
  OPEUOM UOM Operation UOM -> [TUN]TUN0 =[OPS]OPEUOM (TABUNIT) !Block
  OPSNUM VCR Load no.
  OPSSTA M*15 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  OPSTYP M*15 Charge type [menu 350: 1=Manufacturing operation,2=Macro-operation]
  ORI M*15 Source [menu 298: 1=Purchasing,2=Sales,3=Stock,4=Production,5=MPS,6=MRP,7=Projet]
  PJT PJT Project -> [PIM]PIM0 =[OPS]PJT (PIMPL) !Block
  PLNFCY FCY Planning site -> [FCY]FCY0 =[OPS]PLNFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  PRPTIM TIH Preparation time
  PSPTIM TIH Post-run time
  QUACPLQTY QTY Actual QC quantity
  REJCPLQTY QTY Actual rejected qty.
  ROOTIMCOD M*15 Run time code [menu 312: 1=Proportional,2=Rate,3=Fixed]
  ROUOPENUM OPE Operation no.
  SCHGRP A*15 Grouping criterion
  SCHSBB A*15 Distinction criteria
  SCOFLG M*4 Subcon code [menu 1: 1=No,2=Yes]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[OPS]SCOITMREF (ITMMASTER) !Block
  SCOLTI LTI Subcontract LT
  SCOWST WST Subcontract work C
  SEQORD C*4 Sequence order act:POPS
  SETLABCOE DCB*3.3 Labor time set fac
  TIMUOMCOD M*15 Time unit [menu 301: 1=Hours,2=Minutes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WAITIM TIH Waiting time
  WIPNUM VCR Order no.

## ORDOOPAR (ORO) - APS setup
Keys (first = PK; D = duplicates allowed): ORO0 ID
Fields:
  AUUID AUUID Single identifier
  BOMPIT PIT BOM set (pivot) -> [PIT]PIT0 =BOMPIT (PIVOTS) !Block
  BPCPIT PIT Customer pivot -> [PIT]PIT0 =BPCPIT (PIVOTS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DRTISS A*250 Index destination
  DRTRCP A*250 Directory to be scanned
  DRTSTO A*250 Storage directory
  GRUBOMFLG M*4 Grouping [menu 1: 1=No,2=Yes]
  ID A*10 Identifier
  INTIT DES Description
  ITMPIT PIT Product set (pivot) -> [PIT]PIT0 =ITMPIT (PIVOTS) !Block
  MWSPIT PIT Work center pivot -> [PIT]PIT0 =MWSPIT (PIVOTS) !Block
  OPEPIT PIT Operation pivot -> [PIT]PIT0 =OPEPIT (PIVOTS) !Block
  ORDPIT PIT Order pivot -> [PIT]PIT0 =ORDPIT (PIVOTS) !Block
  ORTCLIBIN A*250 Client directory
  ORTDRTBIN A*250 Directory
  ORTENM A*50 Environment
  ORTFLG M*4 APS integration [menu 1: 1=No,2=Yes]
  ORTLTI C*4 Planning leadtime
  ORTPLNFLG M*4 Open planning [menu 1: 1=No,2=Yes]
  PJTPIT PIT Project pivot -> [PIT]PIT0 =PJTPIT (PIVOTS) !Block
  POFPIT PIT Purchase pivot -> [PIT]PIT0 =POFPIT (PIVOTS) !Block
  RPLPIT PIT Repl wrk center pivot -> [PIT]PIT0 =RPLPIT (PIVOTS) !Block
  RSSPIT PIT Sec resources pivot -> [PIT]PIT0 =RSSPIT (PIVOTS) !Block
  STOPIT PIT Stock pivot -> [PIT]PIT0 =STOPIT (PIVOTS) !Block
  TWCPIT PIT Wrk center grp pivot -> [PIT]PIT0 =TWCPIT (PIVOTS) !Block
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VOLFILISS ASTO*250 Index destination
  VOLFILRCP ASTO*250 Directory to be scanned
  VOLFILSTO ASTO*250 Storage directory
  WOMAR C*2 Release margin
  WSTPIT PIT Wrk center/grp pivot -> [PIT]PIT0 =WSTPIT (PIVOTS) !Block

## ORDOPPAR (ORP) - PREACTOR parameters
Keys (first = PK; D = duplicates allowed): ORP0 ID
Fields:
  AUUID AUUID Single identifier
  BOMPIT PIT BOM set (pivot) -> [PIT]PIT0 =BOMPIT (PIVOTS) !Block
  BPCPIT PIT Customer pivot -> [PIT]PIT0 =BPCPIT (PIVOTS) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  DRTISS A*250 Index destination
  DRTRCP A*250 Directory to be scanned
  DRTSTO A*250 Storage directory
  GRUBOMFLG M*4 Grouping [menu 1: 1=No,2=Yes]
  ID A*10 Identifier
  INTIT DES Description
  ITMPIT PIT Product set (pivot) -> [PIT]PIT0 =ITMPIT (PIVOTS) !Block
  MWSPIT PIT Work center pivot -> [PIT]PIT0 =MWSPIT (PIVOTS) !Block
  OPEPIT PIT Operation pivot -> [PIT]PIT0 =OPEPIT (PIVOTS) !Block
  ORDPIT PIT Order pivot -> [PIT]PIT0 =ORDPIT (PIVOTS) !Block
  PJTPIT PIT Project pivot -> [PIT]PIT0 =PJTPIT (PIVOTS) !Block
  POFPIT PIT Purchase pivot -> [PIT]PIT0 =POFPIT (PIVOTS) !Block
  RPLPIT PIT Repl wrk center pivot -> [PIT]PIT0 =RPLPIT (PIVOTS) !Block
  RSSPIT PIT Sec resources pivot -> [PIT]PIT0 =RSSPIT (PIVOTS) !Block
  STOPIT PIT Stock pivot -> [PIT]PIT0 =STOPIT (PIVOTS) !Block
  TWCPIT PIT Wrk center grp pivot -> [PIT]PIT0 =TWCPIT (PIVOTS) !Block
  TYPEXP M*15 Destination type [menu 921: 1=Client,2=Server]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDTIM L*8 Time
  UPDUSR A*5 Change user
  VOLFILISS ASTO*250 Index destination
  VOLFILRCP ASTO*250 Directory to be scanned
  VOLFILSTO ASTO*250 Storage directory
  WSTPIT PIT Wrk center/grp pivot -> [PIT]PIT0 =WSTPIT (PIVOTS) !Block

## PARJAL (PJA) - Scheduling parameters
Keys (first = PK; D = duplicates allowed): PJA0 MFGFCY
Fields:
  AUTFRCSCD M*4 Automatic forced rescheduling [menu 1: 1=No,2=Yes]
  AUTFRWSCD M*4 Automatic reschedule of arrears [menu 1: 1=No,2=Yes]
  AUTWIPSCD M*4 WIP rescheduling [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUTSTRDAT D First cutoff
  MAXPERNBR C*4 Maximum periods
  MFGFCY FCY Production site -> [FCY]FCY0 =[PJA]MFGFCY (FACILITY) !Block
  STRTEAM1 HM Start activity 1
  STRTEAM2 HM Start activity 2
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WKLBUCCOR M*4 Automatic adjustment [menu 1: 1=No,2=Yes]
  WKLDAYNBR C*4 Day periods
  WKLMONNBR C*4 No. periods months
  WKLWEENBR C*4 No. per. weeks

## PARWIPACC (PWA) - Wipcost-interface parameter
Keys (first = PK; D = duplicates allowed): PWA0 LEG+CPY+TXNTYP
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[PWA]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  KEY1 A*50 Key
  KEY2 A*50 Key
  KEY3 A*50 Key
  KEY4 A*50 Key
  KEY5 A*50 Key
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  TXNTYP M*15 Transaction type [menu 2358: 20 values, see local-menus.md]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PDPDET (PDD) - MPS calculation detail
Notes: differs in V9.0 P12 (diff: AT3_PDPDET.htm)
Keys (first = PK; D = duplicates allowed): CBD0 STOFCY+ITMREF+BUC+REQDAT+WIPTYP+WIPNUM; CBD1 STOFCY+SUGTYP+SUGSTA+SUGNUM (D); CBD2 STOFCY+ITMREF+WIPTYP+WIPSTA (D); CBD3 ITMREF+STOFCY+BUC+REQDAT+WIPTYP+WIPNUM; CBD4 ITMREFORI+STOFCY+WIPTYP+WIPSTA (D)
Fields:
  ALLQTY QTY Allocated quantity
  AUUID AUUID Single identifier
  BOMALT TBO BOM code -> [TBO]TBO0 =BOMALTTYP;BOMALT (TABBOMALT) !Delete
  BOMALTTYP M*15 BOM type [menu 224: 1=Sales (Kit),2=Manufacturing,3=Subcontracting]
  BOMOFS C*4 Operation lead time
  BOMOPE OPE Operation number
  BPRNUM BPR Source BP -> [BPR]BPR0 =[PDD]BPRNUM (BPARTNER) !Other
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
  ITMREF ITM Product -> [ITM]ITM0 =[PDD]ITMREF (ITMMASTER) !Block
  ITMREFORI ITM Source product -> [ITM]ITM0 =[PDD]ITMREFORI (ITMMASTER) !Other
  MRPDAT D MRP date
  MRPMES M*15 MRP message [menu 318: 1=No action,2=Advance,3=Delay,4=Increase,5=Reduce,6=Cancel,7=Advance/Increase,8=Advance/Reduce,9=Delay/Increase,10=Delay/Reduce,11=Delay firm horizon,12=Obsolete product (end of life),13=Overstock,14=Invalid routing version]
  MRPQTY QTY MRP quantity
  MTOQTY QTY Quantity assigned
  PJT PJT Source project -> [PIM]PIM0 =[PDD]PJT (PIMPL) !BSRA
  REQDAT D Requirement date
  REQQTY QTY Demand/Supply
  RMNEXTQTY QTY Remaining quantity
  RPLFLG M*4 Re-planning flag [menu 1: 1=No,2=Yes]
  STOFCY FCY Storage site -> [FCY]FCY0 =[PDD]STOFCY (FACILITY) !Block
  STOQTY QTY Available stock
  STRDAT D Start date
  SUGNUM VCR Order no.
  SUGSTA M*1 WIP status [menu 342: 1=F,2=P,3=S,4=C]
  SUGTYP M*2 Order type [menu 341: 1=SO,2=PO,3=MS,4=SC,5=WO,6=MW,7=TR,8=TP,9=BW,10=VD,11=VR,12=CR,13=EO,14=MT]
  TRCFLG M*4 Log [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PDD]UPDUSR (AUTILIS) !Other
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

## PDPHEA (PDH) - MPS calculation header
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
  ITMREF ITM Product -> [ITM]ITM0 =[PDH]ITMREF (ITMMASTER) !Block
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
  PROFLG C*1 Processing flag
  PURFLG M*4 Bought [menu 1: 1=No,2=Yes]
  QUAFLG M*25 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  QUALTI LTI Quality ctrl. lead time
  REJSTO QTY Internal 'R'
  REOCOD M*15 Suggestion type [menu 250: 1=No suggestion,2=Purchase,3=Manufacturing,4=Intersite,5=Subcontracting]
  REOFCY FCY Reorder site -> [FCY]FCY0 =[PDH]REOFCY (FACILITY) !Block
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
  STOFCY FCY Storage site -> [FCY]FCY0 =[PDH]STOFCY (FACILITY) !Block
  STOTIAFLG M*4 Include available stock [menu 1: 1=No,2=Yes]
  STRSTO QTY Starting stock
  STU UOM Stock unit -> [TUN]TUN0 =[PDH]STU (TABUNIT) !Block
  STUDEC C*1 Decimals
  SUGTYP M*30 Suggestion type [menu 218: 1=No processing,2=With MRP pegging,3=Wthout MRP pegging,4=MRP pegging only]
  TOOFLG M*4 Tools [menu 1: 1=No,2=Yes]
  TRASTO QTY Transferred stock
  TRFSTO QTY In-transit stock
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PDH]UPDUSR (AUTILIS) !Other
  WAISTO QTY Pending issues
  WIPPRO M*4 WIP protect. [menu 1: 1=No,2=Yes]

## POPSCALEXP (CEP) - Calendar exception
Notes: activity code POPS; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): CEP0 WSTFCY+WST+STRDAT+ENDDAT
Fields:
  AUUID AUUID Single identifier
  COMMENT A*240 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CEP]CREUSR (AUTILIS) !Other
  EDITABLE C*2 Exception editable
  ENDDAT D End date
  OPENED C*2 Is period open
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CEP]UPDUSR (AUTILIS) !Other
  WST WST Work center
  WSTFCY FCY Site -> [FCY]FCY0 =[CEP]WSTFCY (FACILITY) !Block

## POPSCUSFLDS (PSCF) - Prod. Sched. custom fields
Notes: activity code POPS; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PSCF0 MENNUM+MESNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSCF]CREUSR (AUTILIS) !Other
  ENTTYP A*10 Entity type
  FLDORD C*4 Numerical order
  FLDTYP A*20 Field type
  FORMULE AFF*250 Formula
  MENNUM C*4 Chapter
  MESNUM C*4 Message
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSCF]UPDUSR (AUTILIS) !Other

## POPSCUSVALS (PSCV) - Prod. Sched. custom values
Notes: activity code POPS; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PSCV0 FCY
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSCV]CREUSR (AUTILIS) !Other
  DEFFLG M*4 Default [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[PSCV]FCY (FACILITY) !Block
  OPCUSFLD C*4(2) OP custom field
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSCV]UPDUSR (AUTILIS) !Other
  WOCUSFLD C*4(2) WO custom field

## POPSMRK (MRK) - Planner One marker
Notes: activity code POPS; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): MRK0 MFGNUM+OPENUM+MRKID
Fields:
  AUUID AUUID Single identifier
  COMMENT A*240 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MRK]CREUSR (AUTILIS) !Other
  MFGNUM VCR Order no.
  MRKID A*20 Marker ID
  OPENUM OPE Operation
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MRK]UPDUSR (AUTILIS) !Other

## POPSOBJ (PSOBJ) - Objects in PS
Notes: activity code POPS; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PSOBJ0 FCY+TYP+IDENT1+IDENT2
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[PSOBJ]CREUSR (AUTILIS) !Other
  FCY FCY Site -> [FCY]FCY0 =[PSOBJ]FCY (FACILITY) !Delete
  IDENT1 ID1 Identifier 1
  IDENT2 ID2 Identifier 2
  INF1 INF Information 1
  INF2 INF Information 2
  INF3 INF Information 3
  INF4 INF Information 4
  TYP A*10 Object
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSOBJ]UPDUSR (AUTILIS) !Other

## POPSPIN (PIN) - Operation pin type
Notes: activity code POPS; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): PIN0 MFGNUM+OPENUM+OPESPLNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PIN]CREUSR (AUTILIS) !Other
  MFGNUM VCR Order no.
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  PINTYP C*2 Operation pin type
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PIN]UPDUSR (AUTILIS) !Other

## POPSTAG (TAG) - Planner One tag
Notes: activity code POPS; not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): TAG0 TAGID
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TAG]CREUSR (AUTILIS) !Other
  DELETED C*2 Whether deleted
  TAGICON A*20 Icon name
  TAGID A*20 Tag ID
  TAGORD C*4 Numerical order
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TAG]UPDUSR (AUTILIS) !Other

## ROUOPE (ROO) - Routing - operations
Keys (first = PK; D = duplicates allowed): ROO0 FCY+ITMREF+ROUALT+OPENUM+RPLIND; ROO1 FCY+VALENDDAT (D); ROO2 FCY+WST (D); ROO3 FCY+LABWST (D); ROO4 FCY+STDOPENUM (D)
Fields:
  ALTOPECOD M*4 Routing code ope. [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BPAADD ADR Address
  BPRNUM BPR BP -> [BPR]BPR0 =[ROO]BPRNUM (BPARTNER) !Other
  CAD DCB*6.4 Rate
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EFF DCB*3.3 % efficiency
  EQUNUM ITM Tools -> [ITM]ITM0 =[ROO]EQUNUM (ITMMASTER) !Block
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[ROO]FCY (FACILITY) !Block
  FXGNUM A*20 Fixture
  GRPSETTIM TIH Group setup time
  ITMREF ITM Routing -> [ITM]ITM0 =[ROO]ITMREF (ITMMASTER) !Block
  LABNBR C*2 Number labor res.
  LABWST WST Labor work center
  OPELABCOE DCB*3.3 Labor r-time fact
  OPENUM OPE Operation
  OPENUMLEV C*1 Operation suffix
  OPEPLNNUM A*20 Operation plan
  OPEROUPCT A*20 Operation image
  OPESTUCOE COE STK-OPE conversion
  OPESTUFOR FOR STK-OPE formula -> [TFO]TFO0 =2;OPESTUFOR (TABFOR) !Block
  OPETIM TIH Run time
  OPEUOM UOM Operation UOM -> [TUN]TUN0 =OPEUOM (TABUNIT) !Block
  PRGNUM A*20 Program
  PRPTIM TIH Preparation time
  PSPTIM TIH Post-run time
  REFPRI MD8 Reference price
  ROODES DES Ope description
  ROOTEX TXC Operation text
  ROOTIMCOD M*15 Run time code [menu 312: 1=Proportional,2=Rate,3=Fixed]
  ROUALT C*2 Routing code
  RPLIND C*3 Alternate index
  RSTMAC A*5 Machine restriction
  SCHGRP A*15 Grouping criterion
  SCHGRPFOR FOR Grouping formula -> [TFO]TFO0 =9;SCHGRPFOR (TABFOR) !Other
  SCHSBB A*15 Distinction criteria
  SCHSBBFOR FOR Distinction formula -> [TFO]TFO0 =9;SCHGRPFOR (TABFOR) !Other
  SCOCOD M*15 Subcontract [menu 311: 1=No,2=Normal,3=By exception]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[ROO]SCOITMREF (ITMMASTER) !Block
  SCOWST WST Subcontract work C
  SETLABCOE DCB*3.3 Labor time set fac
  SETTIM TIH Setup time
  SHR DCB*3.3 Shrinkage in %
  SPLCOD M*15 Splitting [menu 304: 1=None,2=Equal quantities,3=Equal run times,4=Equal run times / 1 rule,5=Equal quantities + efficiency]
  SPLMAXNBR C*4 Max splits
  STDOPENUM ROT Standard operation
  TECCRD A*8 Technical sheet
  TIMCOD M*15 Management unit [menu 303: 1=Time for 1,2=Time for 100,3=Time for 1000,4=Time per lot]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VALENDDAT D End date
  VALSTRDAT D Start date
  WAITIM TIH Waiting time
  WST WST Main work center
  WSTNBR C*2 Number of resources

## ROUOPESTD (ROT) - Standard operations
Keys (first = PK; D = duplicates allowed): ROT0 STDOPENUM+FCY; ROT1 FCY+STDOPENUM
Fields:
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BPAADD ADR Address
  BPRNUM BPR BP -> [BPR]BPR0 =[ROT]BPRNUM (BPARTNER) !Other
  CAD DCB*6.4 Rate
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EFF DCB*3.3 % efficiency
  EQUNUM ITM Tools -> [ITM]ITM0 =[ROT]EQUNUM (ITMMASTER) !Block
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[ROT]FCY (FACILITY) !Block
  FXGNUM A*20 Fixture
  GRPSETTIM TIH Group setup time
  LABNBR C*2 Number labor res.
  LABWCR WCR Labor work center group -> [TWC]TWC0 =[ROT]LABWCR (TABWRKCTR) !Block
  LABWST WST Labor work center
  LABWSTTYP M*20 Labor W/C type [menu 313: 1=MAC,2=LBR,3=SUB]
  OPELABCOE DCB*3.3 Labor r-time fact
  OPEPLNNUM A*20 Operation plan
  OPEROUPCT A*20 Operation image
  OPETEXNUM TXC Operation text
  OPETIM TIH Run time
  OPEUOM UOM Operation UOM -> [TUN]TUN0 =[ROT]OPEUOM (TABUNIT) !Block
  PRGNUM A*20 Program
  PRPTIM TIH Preparation time
  PSPTIM TIH Post-run time
  REFPRI MD8 Reference price
  ROOTIMCOD M*15 Run time code [menu 312: 1=Proportional,2=Rate,3=Fixed]
  RSTMAC A*5 Machine restriction
  SCHGRP A*15 Grouping criterion
  SCHGRPFOR FOR Grouping formula -> [TFO]TFO0 =9;SCHGRPFOR (TABFOR) !Other
  SCOCOD M*15 Subcontract [menu 311: 1=No,2=Normal,3=By exception]
  SCOITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[ROT]SCOITMREF (ITMMASTER) !Block
  SCOWCR WCR Subcontractor work center -> [TWC]TWC0 =[ROT]SCOWCR (TABWRKCTR) !Block
  SCOWST WST Subcontract work C
  SETLABCOE DCB*3.3 Labor time set fac
  SETTIM TIH Setup time
  SHR DCB*3.3 Shrinkage in %
  SPLCOD M*15 Splitting [menu 304: 1=None,2=Equal quantities,3=Equal run times,4=Equal run times / 1 rule,5=Equal quantities + efficiency]
  SPLMAXNBR C*4 Max splits
  STDOPEDES DES Std oper title
  STDOPEDESAXX AX3 Std oper title
  STDOPENUM ROT Standard operation
  TECCRD QLC Technical sheet -> [QLC]QLC0 =TECCRD;1 (QLYCRD) !Block
  TIMCOD M*15 Management unit [menu 303: 1=Time for 1,2=Time for 100,3=Time for 1000,4=Time per lot]
  TIMUOMCOD M*15 Time unit [menu 301: 1=Hours,2=Minutes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WAITIM TIM Waiting time
  WCR WCR Work center group -> [TWC]TWC0 =[ROT]WCR (TABWRKCTR) !Block
  WST WST Main work center
  WSTNBR C*2 Number of resources
  WSTTYP M*20 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]

## ROUSCD (ROS) - Routing - scheduling operation
Keys (first = PK; D = duplicates allowed): ROS0 FCY+ITMREF+ROUALT+OPENUM; ROS1 FCY+ITMREF+ROUALT+NEXOPENUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DACMST M*10 Milestone [menu 352: 1=None,2=Normal tracking,3=Range]
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[ROS]FCY (FACILITY) !Block
  ITMREF ITM Routing -> [ITM]ITM0 =[ROS]ITMREF (ITMMASTER) !Block
  MFGMST M*4 Production step [menu 1: 1=No,2=Yes]
  NEXOPENUM OPE Downstream operation
  OPENUM OPE Operation
  ROUALT C*2 Routing code
  SCDCOD M*30 Scheduling [menu 305: 1=Absolute successor,2=Overlapping wait = lots,3=Overlapping wait = time,4=Overlapping wait = quantity,5=Start synchronization,6=End synchronization,7=All order operations parallel,8=Subcontract synchronization,9=Simple successor]
  SCDLOT DCB*5.2 No. of overlap lots
  SCDQTY QTY Overlapping qty
  SCDTIM TIH Overlapping time
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## ROUTING (ROH) - Routings - header
Keys (first = PK; D = duplicates allowed): ROH0 ITMREF+ROUALT+FCY; ROH1 FCY+ITMREF+ROUALT
Fields:
  ACSCOD ACS Access code -> [ACS]ACS0 =[ROH]ACSCOD (ACCCOD) !Block
  AUUID AUUID Single identifier
  CFGVCRNUM VCR Journal number config act:CFG
  CFMFLG M*4 Validated [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[ROH]FCY (FACILITY) !Block
  IDENT1 ID1 Identifier 1
  ITMREF ITM Routing -> [ITM]ITM0 =[ROH]ITMREF (ITMMASTER) !Block
  LASWORDAT D Last release date
  LASWORQTY QTY Last release qty
  PLNNUM A*20 Routing header plan
  ROUALT TRO Routing code -> [TRO]TRO0 =[ROH]ROUALT (TABROUALT) !Block
  ROUDES DES Header title
  ROUDESAXX AX3 Header title
  ROUENDDAT D Valid to
  ROUPCT A*20 Routing header image
  ROUSTRDAT D Valid from
  TEXNUM TXC Routing header text
  TIMUOMCOD M*15 Time unit [menu 301: 1=Hours,2=Minutes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USESTA M*15 Use status [menu 240: 1=In development,2=Available to use]
  WORMAXQTY QTY Max release qty
  WORMINQTY QTY Mini release qty
  WORTYP M*30 WO management mode [menu 302: 1=No change,2=Materials change,3=Operation change,4=Change materials and operations]

## RPLWST (RPW) - Alternate work centers
Notes: differs in V9.0 P12 (diff: AT3_RPLWST.htm); differs in V10 P1 (diff: ATD_RPLWST.htm)
Keys (first = PK; D = duplicates allowed): RPW0 WST+WCRFCY
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  PIO C*2(25) Priority
  RPLWST WST(25) Alternate work center
  RPLWSTDES DES(25) Work center title
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WCR WCR(25) Work center group -> [TWC]TWC0 =[RPW]WCR (TABWRKCTR) !Block
  WCRFCY FCY Manufacturing site -> [FCY]FCY0 =[RPW]WCRFCY (FACILITY) !Block
  WST WST Work center
  WSTTYP M*20(25) Work center type [menu 313: 1=MAC,2=LBR,3=SUB]

## RVMVAL (RVV) - Routing versions
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): RVV1 ITMREF+FCY+ECCVALMAJ+ECCVALMIN; RVV0 ITMREF+FCY+ECCSEQ
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[RVV]CREUSR (AUTILIS) !Other
  ECCSEQ C*4 Sequence
  ECCVALMAJ ICVVAL Major version
  ECCVALMIN ICVVAL Minor version
  ENDDAT D End date
  EXNDAT D Excp. date
  EXNFLG M*4 Derogation [menu 1: 1=No,2=Yes]
  FCY FCY Site -> [FCY]FCY0 =[RVV]FCY (FACILITY) !Delete
  ITMREF ROH Product -> [ROH]ROH0 =ITMREF;ROUALT;FCY (ROUTING) !Delete
  ROUALT TRO Routing code -> [TRO]TRO0 =[RVV]ROUALT (TABROUALT) !BSRA
  STRDAT D Start date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[RVV]UPDUSR (AUTILIS) !Other
  USESTA M*15 Use status [menu 240: 1=In development,2=Available to use]

## SCALES (SLE) - Weighing scales
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): SLE0 SLE+FCY; SLE1 FCY+SLE
Fields:
  AUTO M*4 Auto [menu 1: 1=No,2=Yes]
  AUUID AUUID Single identifier
  AVACOD M*15 Availability [menu 2331: 1=Available,2=Unavailable,3=Being weighed,4=Being calibrated,5=Defective]
  BAURAT C*4 Speed in bauds
  BOX A*8 Weighing booth
  CAG C*1 Port number
  CBTCOD M*15 Calibration code [menu 2317: 1=No calibration,2=Number of days,3=Number of weighings,4=Number of days and weighings,5=Each weighing]
  CBTLBE ARP Calibration label -> [ARP]ARP0 =[SLE]CBTLBE (AREPORT) !Block
  CGD CGD Calibration guide -> [CGD]CGD0 =CGD;1 (CALIGUIDES) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DECNBR C*1 Number of decimals
  DES DES Description
  DESAXX AX3 Description
  EXPNUM L*8 Export number
  FCY FCY Manufacturing site -> [FCY]FCY0 =[SLE]FCY (FACILITY) !Block
  ITGNBR C*1 Whole numbers
  LASCBTDAT D Calibration date
  MAXRGE DCB*11.6 Maximum reach
  MAXTAR DCB*11.6 Maximum tare
  MINRGE DCB*11.6 Minimum reach
  MODSCALE MOD Template -> [MODL]MOD1 =[SLE]MODSCALE (MODSCALE) !Block
  NBRDAY C*4 Number of days
  NBRWGG C*4 Number of weighings
  NBRWGGCBT C*4 No. scales cal.
  PILNAM ADI Pilot name -> [ADI]CODE =380;PILNAM (ATABDIV) !Block
  PLATEFORME C*4 No. platform
  PRY M*15 Parity [menu 2316: 1=No parity,2=Odd parity,3=Even parity]
  SEP M*15 Decimal separator [menu 2326: 1=Point,2=Comma]
  SERIALNUM A*20 Serial number
  SHO SHO Short description
  SHOAXX AX1 Short description
  SLE A*8 Weighing scale
  SRVCOD M*15 Use status [menu 2332: 1=In service,2=Not in service]
  STI A*8 Weighing location
  STPBYT M*15 Stop bit [menu 2315: 1=1 stop bit,2=2 stop bits]
  SYZBYT C*1 Format of the data
  TEMIND C*4 Waiting time
  TEX TXC Text
  TOL COE Tolerance
  UGD UGD User guides -> [UGD]UGD0 =[SLE]UGD (USERGUIDES) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USRUSR A*5 Operator user
  WEICNG M*4 Locker weight [menu 1: 1=No,2=Yes]
  WEU UOM Weight unit -> [TUN]TUN0 =[SLE]WEU (TABUNIT) !Block

## SCHEDULING (SCH) - Work order scheduling
Notes: differs in V9.0 P12 (diff: AT3_SCHEDULING.htm)
Keys (first = PK; D = duplicates allowed): SCH0 MFGNUM+OPENUM+OPESPLNUM
Fields:
  AUUID AUUID Single identifier
  CLCAFTDUR DCB*9.2 Calc time after prod
  CLCEXTTIM DCB*9.2 Calc exp time
  CLCLAB WST Expected labor work center
  CLCOPEDUR DCB*9.2 Calculated run-time
  CLCPRPDUR DCB*9.2 Calculated prep time
  CLCPSTDUR DCB*9.2 Calc post-op time
  CLCSETDUR DCB*9.2 Calculated setup time
  CLCWAIDUR DCB*9.2 Calculated wait time
  CLCWORDUR DCB*9.2 Calc prod time
  CLCWST WST Expected W/C
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DACMST M*15 Milestone [menu 352: 1=None,2=Normal tracking,3=Range]
  EXPNUM L*8 Export number
  FITCAPEND D End finite capacity
  FITCAPENF DCB*1.4 Last split
  FITCAPSTF DCB*1.4 First split
  FITCAPSTR D Finite capacity start
  FITDELAY DCB*9.2 Early/Late
  FITOPEEND D Operation end
  FITOPEENF DCB*1.4 Last operation split
  FITPRPDUR DCB*9.2 Prep time
  FITPSTDUR DCB*9.2 Cal p/op tm
  FITWORDUR DCB*9.2 Calc prod tm
  INFCAPEND D End date
  INFCAPENF DCB*1.4 Last split
  INFCAPSTF DCB*1.4 First split
  INFCAPSTR D Start date
  LOTQTY QTY Lot quantity
  MFGFCY FCY Production site -> [FCY]FCY0 =[SCH]MFGFCY (FACILITY) !Block
  MFGMST M*4 Production step [menu 1: 1=No,2=Yes]
  MFGNUM VCR Order no.
  NEXOPENUM OPE Downstream operation
  OPEENDDAT D Operation end
  OPEENDFRD DCB*1.4 Last operation split
  OPEFITSTD D Prep start
  OPEFITSTF DCB*1.4 Prep start offset
  OPELABCOE DCB*3.3 Labor r-time fact
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  OPESTRDAT D Operation start
  OPESTRFRD DCB*1.4 First ope split
  PLNFCY FCY Planning site -> [FCY]FCY0 =[SCH]PLNFCY (FACILITY) !Block
  ROUALT C*2 Routing code
  ROUECCMAJ ICVVAL Major version act:RVM
  ROUECCMIN ICVVAL Minor version act:RVM
  ROUNUM ITM Released routing -> [ITM]ITM0 =[SCH]ROUNUM (ITMMASTER) !Block
  SCDCOD M*30 Scheduling [menu 305: 1=Absolute successor,2=Overlapping wait = lots,3=Overlapping wait = time,4=Overlapping wait = quantity,5=Start synchronization,6=End synchronization,7=All order operations parallel,8=Subcontract synchronization,9=Simple successor]
  SCDLOT DCB*5.2 No. of overlap lots
  SCDQTY QTY Overlapping qty
  SCDTIM TIH Overlapping time
  SETENDDAT D Setup end da
  SETENDFRD DCB*1.4 Adjust split
  SETLABCOE DCB*3.3 Labor time set fac
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SENTENCES (RSY) - Safety risk sentences
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): RSY0 RSY
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  EXPNUM L*8 Export number
  PGM A*10 Pictogram
  RSY A*15 Safety risk sentences
  RSYDES DES Description
  RSYSHO SHO Short description
  RSYTEX A*250 Definition
  RSYTYP M*15 Type [menu 2320: 1=Risk,2=Security,3=Environment]
  SHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SFTTXN (SFTX) - Shop floor transactions
Notes: not in V9.0 P12 (new table); differs in V10 P1 (diff: ATD_SFTTXN.htm)
Keys (first = PK; D = duplicates allowed): SFT0 EMPNUM+SFTTYP+VCRNUM+SFTSEQ
Fields:
  ACTENDDATTIM ADATIM End
  ACTSTRDATTIM ADATIM Start
  AUUID AUUID Single identifier
  BRKTXN AUUID Break code
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CPLQTY QTY Completed qty.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SFTX]CREUSR (AUTILIS) !Other
  DURATION DCB*9.2 Duration
  EMPNUM TMA*4 Employee ID -> [TMA]TMA0 =[SFTX]EMPNUM (TABMAT) !Block
  ERRFLG M*4 Error [menu 1: 1=No,2=Yes]
  ERRMSG A*200 Error msg
  FCY FCY Site -> [FCY]FCY0 =[SFTX]FCY (FACILITY) !Block
  INDREF A*3 Indirect references
  INDTYP M*15 Category type [menu 2417: 1=Time off,2=Break,3=Non-exclusive labor,4=Exclusive labor,5=Auto break]
  LCENTER WST Labor center
  MACFLG M*4 Machine [menu 1: 1=No,2=Yes]
  NUMJOBS L*8 Number of activities
  NUMMAC M*4 Machine included [menu 1: 1=No,2=Yes]
  OPENUM OPE Operation number
  OPEUOM UOM Entry unit -> [TUN]TUN0 =[SFTX]OPEUOM (TABUNIT) !Block
  REJCPLQTY QTY Rejected qty.
  SCANUM C*4 Rejection
  SETUPSTOP C*1 Setup stop
  SFTSEQ L*4 Sequence
  SFTTYP M*4 Type [menu 2416: 1=Clock in/out,2=Indirect,3=Break,4=Setup,5=Run]
  SHIFT SHFT Shift code -> [SFTS]SHF0 =[SFTX]SHIFT (SFTSHIFT) !Block
  SHIFTDAT D Shift date
  STRTXNUUID AUUID Transaction code
  SUMEMP L*8 Number of employees
  TEAMNUM TMA Team -> [TMA]TMA0 =[SFTX]TEAMNUM (TABMAT) !Block
  TXNUUID AUUID Transaction code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SFTX]UPDUSR (AUTILIS) !Other
  UTCENDDATTIM ADATIM End
  UTCOFFSET DCB*9.2 Time zone difference
  UTCSTRDATTIM ADATIM Start
  VCRNUM VCR Document
  WCENTER WST Work center

## SFTTXNH (SFTH) - Shop floor trans. history
Notes: not in V9.0 P12 (new table); differs in V10 P1 (diff: ATD_SFTTXNH.htm)
Keys (first = PK; D = duplicates allowed): SFT0 EMPNUM+SFTTYP+VCRNUM+SFTSEQ+HISSEQ
Fields:
  ACTENDDATTIM ADATIM End
  ACTSTRDATTIM ADATIM Start
  AUUID AUUID Single identifier
  CHGRAT DCB*12.2 Labor rate
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CPLLAB WST Actual labor W/C
  CPLQTY QTY Completed qty.
  CPLWST WST Actual work center
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SFTH]CREUSR (AUTILIS) !Other
  DURATION DCB*9.2 Duration
  EMPNUM TMA*4 Employee ID -> [TMA]TMA0 =[SFTH]EMPNUM (TABMAT) !Block
  HISSEQ L*8 History sequence
  INDREF INDREF Indirect references -> [SFTIR]SFTAG0 =[SFTH]INDREF (SFTINDREF) !Block
  INDTYP M*15 Category type [menu 2417: 1=Time off,2=Break,3=Non-exclusive labor,4=Exclusive labor,5=Auto break]
  LABCOE DCB*3.3 Labor factor
  LCENTER WST Labor center
  MACFLG M*4 Machine [menu 1: 1=No,2=Yes]
  MFGCREDAT D Date created
  MFGFCY FCY Production site -> [FCY]FCY0 =[SFTH]MFGFCY (FACILITY) !Block
  MFGTRKNUM VCR Tracking number
  NUMJOBS L*8 Number of activities
  NUMMAC M*4 Machine included [menu 1: 1=No,2=Yes]
  OPENUM OPE Operation number
  OPEUOM UOM Entry unit -> [TUN]TUN0 =[SFTH]OPEUOM (TABUNIT) !Block
  REJCPLQTY QTY Actual rejected qty.
  SCANUM C*4 Rejection
  SFTSEQ L*4 Sequence
  SFTTYP M*4 Type [menu 2416: 1=Clock in/out,2=Indirect,3=Break,4=Setup,5=Run]
  SFTWSTTYP M*3 Work center type [menu 2423: 1=Labor only,2=Machine only,3=Labor and machine]
  SHIFT SHFT Shift code -> [SFTS]SHF0 =[SFTH]SHIFT (SFTSHIFT) !Block
  SHIFTDAT D Shift date
  STRTXNUUID AUUID Transaction code
  SUMEMP L*8 Number of employees
  TEAMNUM TMA Team -> [TMA]TMA0 =[SFTH]TEAMNUM (TABMAT) !Block
  TIMMAC DCB*19.8 Machine duration act:FAL
  TXNUUID AUUID Transaction code
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SFTH]UPDUSR (AUTILIS) !Other
  UTCENDDATTIM ADATIM End
  UTCOFFSET DCB*9.2 Time zone difference
  UTCSTRDATTIM ADATIM Start
  VCRNUM VCR Document
  WCENTER WST Work center

## STATION (STX) - Weighing location
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): STX0 STI
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  STI A*8 Weighing location
  STXDES DES Description
  STXDESAXX AX3 Description
  STXSHO SHO Short description
  STXSHOAXX AX1 Short description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## STATIONBOX (SBX) - Location/booth configuration
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): SBX0 BOX+FCY; SBX1 STI+BOX (D)
Fields:
  AUUID AUUID Single identifier
  BOX A*8 Weighing booth
  BOXOPGFLG M*4 Mandatory [menu 1: 1=No,2=Yes]
  BOXOPGPCR QLC Open booth -> [QLC]QLC0 =BOXOPGPCR;1 (QLYCRD) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DES DES Description
  DESAXX AX3 Description
  DESKCNX A*80 Connection station
  EXPNUM L*8 Export number
  FCY FCY Manufacturing site -> [FCY]FCY0 =[SBX]FCY (FACILITY) !Block
  LOC EMP Location act:EMP
  MATEPYFLG M*4 Mandatory [menu 1: 1=No,2=Yes]
  MATEPYPCR QLC Empty booth end of material -> [QLC]QLC0 =MATEPYPCR;1 (QLYCRD) !Block
  PHAEPYFLG M*4 Mandatory [menu 1: 1=No,2=Yes]
  PHAEPYPCR QLC Empty booth end of phase -> [QLC]QLC0 =PHAEPYPCR;1 (QLYCRD) !Block
  PRTALL A*50 Default printer
  PRTCBT A*50 Default printer
  PRTDESALL A*250(2) Description
  PRTDESCBT A*250(2) Description
  PRTDESETI A*250(2) Description
  PRTDESOF A*250(2) Description
  PRTDESPHA A*250(2) Description
  PRTDRVALL A*30 Driver
  PRTDRVCBT A*30 Driver
  PRTDRVETI A*30 Driver
  PRTDRVOF A*30 Driver
  PRTDRVPHA A*30 Driver
  PRTETI A*50 Default printer
  PRTOF A*50 Default printer
  PRTPHA A*50 Default printer
  PRTPORALL A*30 Port
  PRTPORCBT A*30 Port
  PRTPORETI A*30 Port
  PRTPOROF A*30 Port
  PRTPORPHA A*30 Port
  PRTSRV A*30 Server
  SHO SHO Short description
  SHOAXX AX1 Short description
  STI STX Weighing location -> [STX]STX0 =[SBX]STI (STATION) !Block
  STIBOXTEX TXC Location / booth text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WOREPYFLG M*4 Mandatory [menu 1: 1=No,2=Yes]
  WOREPYPCR QLC Empty WO booth -> [QLC]QLC0 =WOREPYPCR;1 (QLYCRD) !Block
  WRH WRH Warehouse -> [WRH]WRH0 =[SBX]WRH (WAREHOUSE) !BSRA act:WRH

## TABCABCUT (CUT) - BC division rules
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): CUT0 FCY
Fields:
  AUUID AUUID Single identifier
  CREDAT D Change date
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUTAXX AX3 Description
  CUTCOD A*6 Rule
  FCY FCY Site -> [FCY]FCY0 =[CUT]FCY (FACILITY) !Block
  ITMDEB C*4 Start position
  ITMFIN C*4 End position
  ITMLON C*4 Field length
  ITMSET A*1 Separating character
  LOTDEB C*4 Start position
  LOTFIN C*4 End position
  LOTLON C*4 Field length
  LOTSET A*1 Separating character
  NUMITM C*4 Item field no.
  NUMLOT C*4 Lot field no.
  NUMSLO C*4 Sublot field no.
  SLODEB C*4 Start position
  SLOFIN C*4 End position
  SLOLON C*4 Field length
  SLOSET A*1 Separating character
  SUPBLC M*4 Blank deletion [menu 1: 1=No,2=Yes]
  TYPCAB M*15 BC type [menu 2395: 1=Field separator,2=Fixed length]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABWRKCTR (TWC) - Work center groups
Notes: differs in V10 P1 (diff: ATD_TABWRKCTR.htm)
Keys (first = PK; D = duplicates allowed): TWC0 WCR; TWC1 WCRDES (D)
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DSPLEV M*15 Display level [menu 2327: 1=Level 1,2=Level 2,3=Level 3]
  EXPNUM L*8 Export number
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WCR A*5 Work center group
  WCRDES DES W/C title
  WCRDESAXX AX3 W/C title

## TANKS (TKS) - Tanks
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): TKS0 TKS+FCY
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[TKS]FCY (FACILITY) !Block
  TKS A*8 Tanks
  TKSDES DES Description
  TKSDESAXX AX3 Description
  TKSEMP LOC Location -> [STC]STC0 =FCY;TKSEMP (STOLOC) !Block
  TKSITM ITM Product -> [ITM]ITM0 =[TKS]TKSITM (ITMMASTER) !Block
  TKSSHO SHO Short description
  TKSSHOAXX AX1 Short description
  TKSUGD UGD User guides -> [UGD]UGD0 =[TKS]TKSUGD (USERGUIDES) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TANKSGATES (TGT) - Gate tank assignments
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): TGT0 TGTTKS+FCY+TGTLIN; TGT1 TGTTKS+FCY+TGTGTS
Fields:
  AUUID AUUID Single identifier
  BOX A*8 Weighing booth
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  FCY FCY Site -> [FCY]FCY0 =[TGT]FCY (FACILITY) !Block
  STI A*8 Weighing location
  TGTGTS A*8 Gates
  TGTLIN L*8 Line number
  TGTTKS A*8 Tanks
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TDUPDCLC (TUC) - Serial No. - calculation modification
Keys (first = PK; D = duplicates allowed): TUC0 MFGNUM
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TUC]CREUSR (AUTILIS) !Other
  MFGNUM VCR Order no.
  SCDFLG M*15 Scheduling status [menu 335: 1=Not scheduled,2=Scheduled,3=Reschedule,4=Optimized]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TUC]UPDUSR (AUTILIS) !Other

## USERGUIDES (UGD) - User guides
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): UGD0 UGD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  UGD A*8 User guides
  UGDDES DES Description
  UGDDESAXX AX3 Description
  UGDSHO SHO Short description
  UGDSHOAXX AX1 Short description
  UGDTEX A*20 Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## WEIGHING (WGG) - Weighing
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): WGG0 MFGNUM+BOMOPE+ITMREF+MFGLIN+BOMSEQ+CBTDAT+MVTSEQ
Fields:
  AUUID AUUID Single identifier
  BOMOPE OPE Operation number
  BOMSEQ C*4 BOM sequence
  BOX A*8 Weighing booth
  CBTDAT D Date weighed
  CCLDAT D Cancellation date
  CCLUSR A*5 Cancellation operator
  CCLWGGOPT M*15 Cancellation mode [menu 2345: 1=With return,2=Without return]
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CONNECFLG M*4 Connected scale flag [menu 1: 1=No,2=Yes]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM HM Time
  CREUSR A*5 Creation user
  CTNTAR WEI Container tare
  DEFPOT DCB*5.4 Default potency %
  ENGCOD M*4 Committed [menu 1: 1=No,2=Yes]
  ENGDAT D Commitment date
  ENGDATSUP D Commit canc date
  ENGTIM HM Com time
  ENGTIMSUP HM Commitment canc hour
  ENGUSR A*5 Commitment operator
  ENGUSRSUP A*5 Commit canc operator
  EXC DCB*11.6 Tolerance+ exceeded
  EXCNUM L*2 Exchange number
  EXPNUM L*8 Export number
  EXTCTN A*8 Container exp.
  EXTSLE A*8 Balance expected
  FCY FCY Manufacturing site -> [FCY]FCY0 =[WGG]FCY (FACILITY) !Block
  ISM HSH SHI record -> [HSH]HSH0 =[WGG]ISM (HANDLING) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[WGG]ITMREF (ITMMASTER) !Block
  ITMREFMNU ITM Manufactured product -> [ITM]ITM0 =[WGG]ITMREFMNU (ITMMASTER) !Block
  LBEPRNCOD M*15 Label printout [menu 2334: 1=No printing,2=Not printed,3=Printed,4=Re-printed]
  LOC LOC Location -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOT LOT Lot
  MFGLIN L*8 Line no.
  MFGNUM VCR Order no.
  MFGTRKNUM VCR Tracking number
  MLTITMFLG M*4 Multi-product flag [menu 1: 1=No,2=Yes]
  MVTSEQ C*4 Sequence
  PKC M*15 Pick list code [menu 2328: 10 values, see local-menus.md]
  POT DCB*5.4 Potency of lot
  RCLCOD M*4 Reconciliation [menu 1: 1=No,2=Yes]
  RCLDAT D Reconciliation date
  RCLDATSUP D Recon canc date
  RCLTIM HM Rcncltn time
  RCLTIMSUP HM Recon canc hour
  RCLUSR A*5 Reconciliation operator
  RCLUSRSUP A*5 Reconc canc oper
  SLO SLO Sublot
  STA A*3 Status
  STI A*8 Weighing location
  STOCOU DCB*10 Chronological stock
  STU UOM Stock unit -> [TUN]TUN0 =[WGG]STU (TABUNIT) !Block
  TGTGTS A*8 Gates
  TKS A*8 Tanks
  TRKNUMPRV VCR Previous tracking no.
  TRSNUM A*3 Transaction
  UOM UOM Release unit -> [TUN]TUN0 =[WGG]UOM (TABUNIT) !Block
  UOMEXTQTY QTY Rel quantity
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USECTN A*8 Container used
  USESLE A*8 Balance used
  WEI DCB*11.6 Weight to record
  WEIFLG M*15 Weighing [menu 2344: 1=None,2=Partial,3=Complete,4=Close packaging,5=Stock count]
  WEIWEI DCB*11.6 Weight recorded
  WEU UOM Weight unit -> [TUN]TUN0 =[WGG]WEU (TABUNIT) !Block
  WGGOPT M*15 Weighing option [menu 2335: 1=Weighed by work order,2=Weighed by product,3=Weighed in production]

## WEIGHPRT (WGP) - Label printing
Notes: activity code MWM
Keys (first = PK; D = duplicates allowed): WGP0 MFGNUM+BOMOPE+ITMREF+MFGLIN+BOMSEQ+CBTDAT+MVTSEQ+PRTSEQ
Fields:
  AUUID AUUID Single identifier
  BOMOPE OPE Operation number
  BOMSEQ C*4 BOM sequence
  CBTDAT D Date weighed
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CRETIM L*8 Time
  CREUSR A*5 Creation user
  ITMREF ITM Product -> [ITM]ITM0 =[WGP]ITMREF (ITMMASTER) !Block
  MFGLIN L*8 Line no.
  MFGNUM VCR Order no.
  MVTSEQ C*4 Sequence
  NBPRINT C*4 Number of copies
  PRT AIM Destination -> [AIM]AIM0 =[WGP]PRT (APRINTER) !Delete
  PRTREASON M*15 Reason for re-print [menu 2398: 1=Printer unavailable,2=End of roller,3=Format error,4=Label illegible]
  PRTSEQ C*4 Print sequence
  RPTCOD ARP Label format -> [ARP]ARP0 =[WGP]RPTCOD (AREPORT) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## WIPSCPM (MSM) - Rejects temporary material
Keys (first = PK; D = duplicates allowed): MSM0 MFGNUM+MFGLIN+BOMSEQ+ITMREF+TXNTYP+PRONUM
Fields:
  AMOUNT DCB*11.4 Amount
  AUUID AUUID Single identifier
  BOMSEQ C*4 BOM sequence
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MSM]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[MSM]ITMREF (ITMMASTER) !Block
  MFGLIN L*8 Line no.
  MFGNUM VCR Order no.
  PRONUM L*8 Process number
  TXNTYP M*15 Transaction type [menu 2358: 20 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MSM]UPDUSR (AUTILIS) !Other

## WIPSCPO (MSO) - Rejects temporary operation
Keys (first = PK; D = duplicates allowed): MSO0 MFGNUM+OPENUM+OPESPLNUM+TXNTYP+PRONUM
Fields:
  AMOUNT DCB*11.4 Amount
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MSO]CREUSR (AUTILIS) !Other
  MFGNUM VCR Order no.
  OPENUM OPE Operation
  OPESPLNUM C*4 Operation split
  PRONUM L*8 Process number
  TXNTYP M*15 Transaction type [menu 2358: 20 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MSO]UPDUSR (AUTILIS) !Other

## WIPTMP (MWT) - Wipcost-interface
Keys (first = PK; D = duplicates allowed): MWT0 ENTCOD+CPY+KEY1+KEY2+KEY3+KEY4+KEY5+VCRTYP+VCRNUM+WIPSEQ
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[MWT]CPY (COMPANY) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MWT]CREUSR (AUTILIS) !Other
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[MWT]ENTCOD (GAUTACE) !Block
  KEY1 A*30 Key
  KEY2 A*30 Key
  KEY3 A*30 Key
  KEY4 A*30 Key
  KEY5 A*30 Key
  PWIPCOST L*8 Sequence no.
  TXNTYP M*15 Transaction type [menu 2358: 20 values, see local-menus.md]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MWT]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Order no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WIPSEQ L*8 Sequence

## WORKCOST (MWC) - Costing dimension
Keys (first = PK; D = duplicates allowed): WCT0 VLTCCE+VLTFCY; WCT1 VLTFCY+VLTCCE
Fields:
  ACCCOD CAC Accounting code -> [CAC]CAC0 =18;ACCCOD;[V]GSUPCLE (GACCCODE) !Block
  AUUID AUUID Single identifier
  BRDCOD M*15 Cost group [menu 316: 1=Subtotal 1,2=Subtotal 2,3=Subtotal 3,4=Subtotal 4,5=Subtotal 5,6=Subtotal 6,7=Subtotal 7,8=Subtotal 8,9=Subtotal 9,10=Subtotal 10,11=Subtotal 11,12=Subtotal 12,13=Subtotal 13,14=Subtotal 14,15=Subtotal 15]
  BUDOPECST MS1 Budgeted run
  BUDSETCST MS1 Budgeted setup
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CCECOD M*15 Method [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ANA
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTTYP M*15 Rate type [menu 314: 1=Unit,2=Fixed]
  CUTOPECST MS1 Revised run
  CUTSETCST MS1 Revised setup
  DIE DIE Dimension type code -> [DIE]DIE0 =[MWC]DIE (GDIE) !Block act:ANA
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[MWC]ENTCOD (GAUTACE) !Block
  EXPNUM L*8 Export number
  OVECOD OVE Overhead -> [OVE]OVE0 =[MWC]OVECOD (OVERHEAD) !Block
  SIMOPECST MS1 Operation rate simulation
  SIMSETCST MS1 Adjust rate simul
  STDOPECST MS1 Standard run
  STDSETCST MS1 Standard setup
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VLTCCE A*20 Costing dimension
  VLTFCY FCY Site -> [FCY]FCY0 =[MWC]VLTFCY (FACILITY) !Block
  WCTDES DES Description
  WCTDESAXX AX3 Description
  WCTSHO SHO Short description
  WCTSHOAXX AX1 Short description

## WORKLOAD (WKL) - Production load
Keys (first = PK; D = duplicates allowed): WKL0 MFGFCY+WST+PEREND; WKL1 MFGFCY+WCR+WST+PEREND
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  MFGFCY FCY Production site -> [FCY]FCY0 =[WKL]MFGFCY (FACILITY) !Delete
  ORSLOD DCB*9.2 MPS load
  OWFLOD DCB*9.2 Firm load
  OWPLOD DCB*9.2 Planned load
  OWSLOD DCB*9.2 MRP load
  PERAVA DCB*9.2 Adjusted availability
  PERDAYNBR C*4 No. of period days
  PEREND D Period end
  PERLOD DCB*9.2 Total load per
  PERNUM C*3 Period number
  PERSTR D Period start
  PERTHEAVA DCB*9.2 Capacity
  PERWRKNBR C*4 Number of period workdays
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WCR WCR Work center group -> [TWC]TWC0 =[WKL]WCR (TABWRKCTR) !Delete
  WST WST Work center

## WSTANL (WSA) - Workstation analysis
Keys (first = PK; D = duplicates allowed): WSA0 WCRFCY+WST+PEREND
Fields:
  AUUID AUUID Single identifier
  AVEQTYEFF DCB*9.2 Average yield in quantity
  AVEQTYSCA DCB*9.2 Average loss
  CPLOPELOD DCB*9.2 Total actual functional time
  CPLOPENBR C*4 Number of actual operations
  CPLQTYSUM QTY Total produced qties
  CPLSETLOD DCB*9.2 Total actual setup time
  CPLTOTLOD DCB*9.2 Total load time
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  EXTCPLTIM DCB*9.2 Total expected time
  EXTOPELOD DCB*9.2 Total expected operation time
  EXTQTYSUM QTY Tot expected qty
  EXTSETLOD DCB*9.2 Total expected setup time
  PERAVA DCB*9.2 Adjusted availability
  PERDAYNBR C*4 No. of period days
  PEREND D Period end
  PERSTR D Period start
  PERTHEAVA DCB*9.2 Capacity
  PERWRKNBR C*4 Number of period workdays
  REJQTYSUM QTY Tot scrapped qty
  STDOPELOD DCB*9.2 Std func time total
  STDSETLOD DCB*9.2 Std setup time total
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WCR WCR Work center group -> [TWC]TWC0 =[WSA]WCR (TABWRKCTR) !Block
  WCRFCY FCY Manufacturing site -> [FCY]FCY0 =[WSA]WCRFCY (FACILITY) !Block
  WST WST Work center
  WSTTYP M*20 Work center type [menu 313: 1=MAC,2=LBR,3=SUB]

