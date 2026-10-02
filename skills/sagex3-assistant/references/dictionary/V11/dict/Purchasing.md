<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Purchasing module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## BITMPPORDERP (BIPOP) - POs price
Keys (first = PK; D = duplicates allowed): BIPOP0 BIPOPADXUID+POHNUM+POPLIN+POPSEQ
Fields:
  AUUID AUUID Single identifier
  BIPOPADXUID L*8 Identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BIPOP]CREUSR (AUTILIS) !Other
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BIPOP]UPDUSR (AUTILIS) !Other

## BITMPPORDERQ (BIPOQ) - POs quantities
Keys (first = PK; D = duplicates allowed): BIPOQ0 BIPOQADXUID+POHNUM+POPLIN+POQSEQ
Fields:
  AUUID AUUID Single identifier
  BIPOQADXUID L*8 Identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BIPOQ]CREUSR (AUTILIS) !Other
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  POQSEQ L*8 Sequence number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BIPOQ]UPDUSR (AUTILIS) !Other

## CONTAINER (CTRH) - Container
Notes: differs in V9.0 P12 (diff: AT3_CONTAINER.htm); differs in V10 P1 (diff: ATD_CONTAINER.htm)
Keys (first = PK; D = duplicates allowed): CTRH0 CTRNUM
Fields:
  AUUID AUUID Single identifier
  AVAVOL QTY Available volume
  AVAWEI QTY Avail. weight
  BPSNUM BPS Supplier -> [BPS]BPS0 =[CTRH]BPSNUM (BPSUPPLIER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CTRH]CREUSR (AUTILIS) !Other
  CRRWEI QTY Container total wgt.
  CTRNUM VCR Container no.
  CTRUID A*20 Container ID
  CUR CUR Currency -> [TCU]TCU0 =[CTRH]CUR (TABCUR) !Block
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[CTRH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[CTRH]DSPWEU (TABUNIT) !Block
  FCY FCY Site -> [FCY]FCY0 =[CTRH]FCY (FACILITY) !Block
  FULFLG M*4 Full [menu 1: 1=No,2=Yes]
  SEANUM1 A*30 Seal number 1
  SEANUM2 A*30 Seal number 2
  SEANUM3 A*30 Seal number 3
  SHIPNUM VCR Shipment number
  TCTRNUM TCTR Freight container -> [TCTR]TCTR0 =[CTRH]TCTRNUM (TABCONTAINER) !Block
  TOTLINAMT MD1 Invoice lines excluding tax
  TOTLINVOU QTY Line volume total
  TOTLINWEU QTY Line weight total
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CTRH]UPDUSR (AUTILIS) !Other

## CONTAINERD (CTRD) - Container detail
Keys (first = PK; D = duplicates allowed): CTRD0 CTRNUM+CTRLIN; CTRD1 POHNUM+POPLIN+POQSEQ (D); CTRD2 CTRNUM+POHNUM+POPLIN+POQSEQ
Fields:
  AUUID AUUID Single identifier
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[CTRD]CREUSR (AUTILIS) !Other
  CTRLIN L*8 Line
  CTRNUM VCR Container no.
  EECICT ICT Incoterm -> [ICTH]ICT0 =[CTRD]EECICT (INCOTERM) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[CTRD]ITMREF (ITMMASTER) !Block
  LEGCPY CPY Legal company -> [CPY]CPY0 =[CTRD]LEGCPY (COMPANY) !Block
  LINAMT MD1 Line amount - tax
  LINVOU UOM Volume unit -> [TUN]TUN0 =[CTRD]LINVOU (TABUNIT) !Block
  LINWEU UOM Weight unit -> [TUN]TUN0 =[CTRD]LINWEU (TABUNIT) !Block
  NETCUR CUR Currency -> [TCU]TCU0 =[CTRD]NETCUR (TABCUR) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Sequence number
  PUU UOM Purchase unit -> [TUN]TUN0 =[CTRD]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Ordered qty.
  QTYVOU QTY Volume
  QTYWEU QTY Weight
  SHIPNUM VCR Shipment number
  STU UOM Stock unit -> [TUN]TUN0 =[CTRD]STU (TABUNIT) !Block
  UOM UOM Order unit -> [TUN]TUN0 =[CTRD]UOM (TABUNIT) !Block
  UOMPUUCOE COE STK-PUR conversion
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CTRD]UPDUSR (AUTILIS) !Other

## COSTSTCD (STCD) - Cost structure - documents
Notes: differs in V9.0 P12 (diff: AT3_COSTSTCD.htm)
Keys (first = PK; D = duplicates allowed): STCD0 VCRTYP+VCRNUM+VCRLIN+VCRSEQ+NUMSEQ; STCD1 VCRTYP+VCRNUM+VCRLIN+FCSCOD (D)
Fields:
  AUUID AUUID Single identifier
  BAS M*25 Basis [menu 2091: 1=Quantity,2=Volume,3=Weight]
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGCOE RCU Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[STCD]CUR (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[STCD]DIE (GDIE) !Block act:ANA
  DOCCHGTYP M*4 Doc rate type [menu 1: 1=No,2=Yes]
  FCSAMT MD1 Entered amount
  FCSAMTCLC MD1 Calculated amount
  FCSAMTSOC MD1 Entered amount
  FCSCOD FCS Cost -> [FCS]FCS0 =[STCD]FCSCOD (FRECST) !Block
  FCSNAT M*40 Cost nature [menu 2276: 1=Packaging,2=Loading,3=Pre-transport,4=Export customs formality,5=Main transport loading,6=Main transport,7=Main transport unloading,8=Import customs formalities,9=Post-transport,10=Unloading,11=Insurance,12=Others]
  FORFCS FOR Formula -> [TFO]TFO0 ="C";FORFCS (TABFOR) !Block
  NUMSEQ L*8 Sequence number
  PRCBUY DCB*5.4 Percentage
  PRINETPRC DCB*5.4 Percentage per net price
  QTY QTY Quantity
  STCLIN L*8 Structure line
  STCRFLG M*4 Reconciled [menu 1: 1=No,2=Yes]
  UNTPRI MD6 Unit price
  UOM UOM Unit -> [TUN]TUN0 =[STCD]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Order no.
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WEIPRC DCB*5.4 Weighting percentage:

## COSTSTCR (STCR) - Cost matching
Keys (first = PK; D = duplicates allowed): STCR0 NUM+PIDLIN; STCR1 TYPORI+NUMORI+LINORI+SEQORI+FCSCOD+CREDATTIM (D)
Fields:
  AMTNOTLIN MD1 Line amount - tax
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[STCR]CUR (TABCUR) !Block
  FCSCOD FCS Cost -> [FCS]FCS0 =[STCR]FCSCOD (FRECST) !Block
  ITMREF ITM Product -> [ITM]ITM0 =[STCR]ITMREF (ITMMASTER) !Block
  ITMREFORI ITM Source product -> [ITM]ITM0 =[STCR]ITMREFORI (ITMMASTER) !Block
  LINORI L*8 Source line
  NUM VCR Document no.
  NUMORI VCR Source number
  PIDLIN L*8 Line
  SEQORI L*8 Original sequence
  STCRFLG M*4 Reconciled [menu 1: 1=No,2=Yes]
  TYPORI M*10 Line origin [menu 511: 1=Order,2=Receipt,3=Return,4=Invoice,5=Miscellaneous,6=Shipment]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## EVENTTRNP (EVT) - Transport incident
Notes: differs in V9.0 P12 (diff: AT3_EVENTTRNP.htm)
Keys (first = PK; D = duplicates allowed): EVT0 TRNNUM+EVTNUM
Fields:
  AUUID AUUID Single identifier
  CMT A*50 Comment
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[EVT]CREUSR (AUTILIS) !Other
  DAT D Date
  EVTCOD ADI Incident -> [ADI]CODE =106;EVTCOD (ATABDIV) !Block
  EVTLTI C*4 Lead time
  EVTNUM L*8 Line
  TRNNUM VCR Transport no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[EVT]UPDUSR (AUTILIS) !Other

## MATCHTOL (MAT) - Matching tolerance
Keys (first = PK; D = duplicates allowed): MAT0 MATTOL
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[MAT]CREUSR (AUTILIS) !Other
  ERACT M*15 Early receipt action [menu 581: 1=Blocking,2=Warning,3=No control]
  ERCTL M*4 Early recpt control [menu 1: 1=No,2=Yes]
  ERDAYS C*3 Early receipt days
  IQEACT M*15 Qty exceeded action [menu 581: 1=Blocking,2=Warning,3=No control]
  IQECTL M*4 Qty exceeded control [menu 1: 1=No,2=Yes]
  IQECTLP M*4 Qty exceeded control [menu 1: 1=No,2=Yes]
  IQECTLQ M*4 Qty exceeded control [menu 1: 1=No,2=Yes]
  IQEPER DCB*3.2 Qty exceeded percent
  IQEQTY QTY Qty exceeded maximum
  IQSACT M*15 Qty shortage action [menu 581: 1=Blocking,2=Warning,3=No control]
  IQSCTL M*4 Qty shortage control [menu 1: 1=No,2=Yes]
  IQSCTLP M*4 Qty shortage control [menu 1: 1=No,2=Yes]
  IQSCTLQ M*4 Qty shortage control [menu 1: 1=No,2=Yes]
  IQSPER DCB*3.2 Qty shortage percent
  IQSQTY QTY Qty shortage maximum
  LRACT M*15 Last receipt action [menu 581: 1=Blocking,2=Warning,3=No control]
  LRCTL M*4 Last receipt control [menu 1: 1=No,2=Yes]
  LRDAYS C*4 Last receipt days
  MATTOL A*5 Matching tolerance
  OILACT M*15 Over inv line action [menu 581: 1=Blocking,2=Warning,3=No control]
  OILAMT MD8 Over inv line amount
  OILCTL M*4 Over inv line ctrl [menu 1: 1=No,2=Yes]
  OILCTLA M*4 Amt. control [menu 1: 1=No,2=Yes]
  OILCTLP M*4 Pct control [menu 1: 1=No,2=Yes]
  OILPER DCB*3.2 Over inv line perct
  OIUACT M*15 Over inv unit action [menu 581: 1=Blocking,2=Warning,3=No control]
  OIUAMT MD8 Over inv unit amnt
  OIUCTL M*4 Over inv unit ctrl [menu 1: 1=No,2=Yes]
  OIUCTLA M*4 Amt. control [menu 1: 1=No,2=Yes]
  OIUCTLP M*4 Pct control [menu 1: 1=No,2=Yes]
  OIUPER DCB*3.2 Over inv unit perct
  QEACT M*15 Qty exceeded action [menu 581: 1=Blocking,2=Warning,3=No control]
  QECTL M*4 Qty exceeded control [menu 1: 1=No,2=Yes]
  QECTLP M*4 Pct control [menu 1: 1=No,2=Yes]
  QECTLQ M*4 Qty. control [menu 1: 1=No,2=Yes]
  QEPER DCB*3.2 Qty exceeded percent
  QEQTY QTY Qty exceeded maximum
  QSACT M*15 Qty shortage action [menu 581: 1=Blocking,2=Warning,3=No control]
  QSCTL M*4 Qty shortage control [menu 1: 1=No,2=Yes]
  QSCTLP M*4 Pct control [menu 1: 1=No,2=Yes]
  QSCTLQ M*4 Qty. control [menu 1: 1=No,2=Yes]
  QSPER DCB*3.2 Qty shortage percent
  QSQTY QTY Qty shortage maximum
  TOLCUR CUR Currency -> [TCU]TCU0 =[MAT]TOLCUR (TABCUR) !Block
  TOLDES DES Description
  TOLUOM UOM Table of units of measure -> [TUN]TUN0 =[MAT]TOLUOM (TABUNIT) !Block
  UILACT M*15 Under inv line actn [menu 581: 1=Blocking,2=Warning,3=No control]
  UILAMT MD8 Under inv line amnt
  UILCTL M*4 Under inv line ctrl [menu 1: 1=No,2=Yes]
  UILCTLA M*4 Amt. control [menu 1: 1=No,2=Yes]
  UILCTLP M*4 Pct control [menu 1: 1=No,2=Yes]
  UILPER DCB*3.2 Under inv line perct
  UIUACT M*15 Under inv unit actn [menu 581: 1=Blocking,2=Warning,3=No control]
  UIUAMT MD8 Under inv unit amnt
  UIUCTL M*4 Under inv unit ctrl [menu 1: 1=No,2=Yes]
  UIUCTLA M*4 Amt. control [menu 1: 1=No,2=Yes]
  UIUCTLP M*4 Pct control [menu 1: 1=No,2=Yes]
  UIUPER DCB*3.2 Under inv unit perct
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[MAT]UPDUSR (AUTILIS) !Other

## PARWIPACCS (SWA) - Wipcost-interface parameter
Keys (first = PK; D = duplicates allowed): SWA0 LEG+CPY+TXNTYP
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[SWA]CPY (COMPANY) !Block
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

## PINVOICED (PID) - Purchase invoice detail
Notes: differs in V9.0 P12 (diff: AT3_PINVOICED.htm); differs in V10 P1 (diff: ATD_PINVOICED.htm)
Keys (first = PK; D = duplicates allowed): PID0 NUM+PIDLIN; PID1 TYPORI+NUMORI+LINORI+SEQORI+NUM+PIDLIN; PID2 ITMREF+NUM+PIDLIN; PID3 BPR+INVTYP+ITMREF+NUM+PIDLIN; PID4 POHNUM+POPLIN+POQSEQ (D); PJMPJT1 PJT (D)
Fields:
  ACCDAT D Accounting date
  AMTATILIN MD1 Line amount + tax
  AMTDEPLIN MD1 Discount amount
  AMTNOTLIN MD1 Line amount - tax
  AMTNOTLINCAL MD1 Line amount - tax
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AUUID AUUID Single identifier
  BASTAXLIN1 MD1 Tax basis 1
  BPR BPR BP -> [BPR]BPR0 =[PID]BPR (BPARTNER) !Block
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PID]BPSNUM (BPARTNER) !Block
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  CMMNUM VCR Commitment no.
  CPR DCB*10.8 Cost price
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CPRCUR CUR Currency -> [TCU]TCU0 =[PID]CPRCUR (TABCUR) !Block
  CPY CPY Company -> [CPY]CPY0 =[PID]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTMAJLIN M*4 New cost [menu 1: 1=No,2=Yes]
  CSTPUR MD8 Purchase cost per unit
  DCLEECNUM EEC VAT declaration no. act:KPO
  DDTADEP1 MD1 Dist. line inv. elmt. 1
  DDTADEP2 MD1 Dist. line inv. elmt. 2
  DDTADEP3 MD1 Dist. line inv. elmt. 3
  DDTADEP4 MD1 Dist. line inv. elmt. 4
  DDTADEP5 MD1 Dist. line inv. elmt. 5
  DDTADEP6 MD1 Dist. line inv. elmt. 6
  DDTADEP7 MD1 Dist. line inv. elmt. 7
  DDTADEP8 MD1 Dist. line inv. elmt. 8
  DDTADEP9 MD1 Dist. line inv. elmt. 9
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DISBASLIN1 MD1 Rebate tax basis 1
  DISCRGAMT1 MD1 Discount/Charge 1
  DISCRGAMT2 MD1 Discount/Charge 2
  DISCRGAMT3 MD1 Discount/Charge 3
  DISCRGAMT4 MD1 Discount/Charge 4
  DISCRGAMT5 MD1 Discount/Charge 5
  DISCRGAMT6 MD1 Discount/Charge 6
  DISCRGAMT7 MD1 Discount/Charge 7
  DISCRGAMT8 MD1 Discount/Charge 8
  DISCRGAMT9 MD1 Discount/Charge 9
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[PID]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[PID]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[PID]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECFLOPHY M*4 Physical flow [menu 1: 1=No,2=Yes] act:DEB
  ENDDAT D End date
  FASREF A*30 FA reference
  FCSCOD FCS Cost -> [FCS]FCS0 =[PID]FCSCOD (FRECST) !Block
  FCSCPR MD1 Stock cost total
  FCSCSTPUR MD1 Purchase cost total
  FCY FCY Site -> [FCY]FCY0 =[PID]FCY (FACILITY) !Block
  FCYLIN FCY Line site -> [FCY]FCY0 =[PID]FCYLIN (FACILITY) !Block
  FLG1099 M*4 1099 [menu 1: 1=No,2=Yes] act:S1099
  GLU UOM Non-financial unit -> [TUN]TUN0 =[PID]GLU (TABUNIT) !Block
  GROPRI MD8 Gross price
  INVLIN L*8 Line
  INVNUM VCR Invoice number
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PID]ITMREF (ITMMASTER) !Block
  LIKQTYCOE COE Link qty. coef.
  LINAMTCPR MD8 Stock cost
  LINCSTPUR MD8 Purchase cost
  LINEECFLG M*4 Debit line [menu 1: 1=No,2=Yes] act:DEB
  LINORI L*8 Source line
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINTEX TXC Text
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  LINVOU UOM Volume unit -> [TUN]TUN0 =[PID]LINVOU (TABUNIT) !Block
  LINWEU UOM Weight unit -> [TUN]TUN0 =[PID]LINWEU (TABUNIT) !Block
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[PID]MATTOL (MATCHTOL) !Block
  NETCUR CUR Currency -> [TCU]TCU0 =[PID]NETCUR (TABCUR) !Block
  NETPRI MD8 Net price
  NUM VCR Document no.
  NUMORI VCR Source number
  ORINETPRI MD8 Source net price
  ORIQTYPUU QTY Source quantity
  ORIQTYVOU QTY Original volume
  ORIQTYWEU QTY Original weight
  PERNBR C*4 Periodicity
  PERTYP M*15 Periodicity [menu 635: 1=Days,2=Week,3=10-day period,4=2-week period,5=Month]
  PIDLIN L*8 Line
  PIHTYP M*20 Purchase invoice cat. [menu 533: 1=Invoice,2=Additional invoice,3=Credit memo,4=Credit memo/Return]
  PIVTYP TPV Usr invoice type -> [TPV]TPV0 =PIVTYP;[V]GSUPCLE (TABPIVTYP) !Block
  PJT PJT Project -> [PIM]PIM0 =[PID]PJT (PIMPL) !Block
  PNDLIN L*8 Line
  PNHNUM VCR Return no.
  POHNUM VCR Order no.
  POPLIN L*8 PO line
  POQSEQ L*8 Sequence number
  PRIREN PPR Price reason -> [PPR]PPR0 =[PID]PRIREN (PPREASON) !Block
  PRTFLG M*4 Partial invoice [menu 1: 1=No,2=Yes]
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PID]PUU (TABUNIT) !Block
  QTYBUDLIN QTY Qty to be decommitted
  QTYGLU QTY Actual quantity
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Invoiced qty.
  QTYVOU QTY Volume
  QTYWEU QTY Weight
  RCPDAT D Receipt date
  SATISS SAT Issue region act:PTX
  SATRCP SAT Receipt region act:PTX
  SEQORI L*8 Original sequence
  SHIPLIN L*8 Line
  SHIPNUM VCR Shipment number
  SIDLIN L*8 Sales invoice line
  STCNUM VCR Cost structure
  STCRFLG M*4 Reconciled [menu 1: 1=No,2=Yes]
  STRDAT D Start date
  STU UOM Stock unit -> [TUN]TUN0 =[PID]STU (TABUNIT) !Block
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  TWMSTA M*15 Match status [menu 585: 1=Not applicable,2=Successful,3=Warning,4=Blocked,5=Unblocked]
  TYPORI M*10 Line origin [menu 511: 1=Order,2=Receipt,3=Return,4=Invoice,5=Miscellaneous,6=Shipment]
  UOM UOM Invoicing unit -> [TUN]TUN0 =[PID]UOM (TABUNIT) !Block
  UOMPUUCOE COE STK-PUR conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## PINVOICEV (PIV) - Costing purchase invoices
Keys (first = PK; D = duplicates allowed): PIV0 NUM
Fields:
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[PIV]BPCINV (BPARTNER) !Block
  BPR BPR BP -> [BPR]BPR0 =[PIV]BPR (BPARTNER) !Block
  CLCLINAMT MD1 Calculated lines -tax
  CPY CPY Company -> [CPY]CPY0 =[PIV]CPY (COMPANY) !Block
  CPYLAN LAN Company language -> [TLA]TLA0 =[PIV]CPYLAN (TABLAN) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation author
  CUR CUR Currency -> [TCU]TCU0 =[PIV]CUR (TABCUR) !Block
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[PIV]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[PIV]DSPWEU (TABUNIT) !Block
  EXPNUM L*8 Export number
  INVDTALIN1 PFI Invoice line element -> [PFI]PFI0 =[PIV]INVDTALIN1 (PFOOTINV) !Block act:PPR
  INVDTALIN2 PFI(9) Invoice line allocation elemen -> [PFI]PFI0 =[PIV]INVDTALIN2 (PFOOTINV) !Block
  INVDTAVAT1 VAT Price line tax -> [TVT]TVT0 =INVDTAVAT1(indice);[V]GSUPCLE (TABVAT) !Block act:PPR
  INVDTAVAT2 VAT(9) Distribution line tax -> [TVT]TVT0 =INVDTAVAT2(indice);[V]GSUPCLE (TABVAT) !Block
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LAN LAN Language -> [TLA]TLA0 =[PIV]LAN (TABLAN) !Block
  LINNBR C*4 Number of lines
  NUM VCR Document no.
  PIHTYP M*20 Purchase invoice cat. [menu 533: 1=Invoice,2=Additional invoice,3=Credit memo,4=Credit memo/Return]
  PIVTYP TPV Usr invoice type -> [TPV]TPV0 =PIVTYP;[V]GSUPCLE (TABPIVTYP) !Block
  PRILINNBR C*4 Number of different price line
  QTYLINNBR C*4 Number of different quantity L
  SIHNUM VCR Sales invoice no.
  TEX1 TXC Text
  TEX2 TXC Text
  TOTLINAMT MD1 Invoice lines excluding tax
  TOTLINQTY DCB*11.6 Total quantity lines
  TOTLINVOU QTY Line volume total
  TOTLINWEU QTY Line weight total
  TOTTAXAMT MD1 Tax total
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Other act:STS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author

## PORDER (POH) - POs
Notes: differs in V9.0 P12 (diff: AT3_PORDER.htm); differs in V10 P1 (diff: ATD_PORDER.htm)
Keys (first = PK; D = duplicates allowed): POH0 POHNUM; POH1 BPSNUM+ORDDAT+POHNUM; POH2 ORDDAT+POHNUM
Fields:
  APPFLG M*15 Signed [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersite [menu 1: 1=No,2=Yes]
  BPAADD ADR Address
  BPAADDLIG ADL(3) Address line
  BPAINV ADR Billing address
  BPAPAY ADR Pay-to BP address
  BPCORD BPR Sold-to -> [BPR]BPR0 =[POH]BPCORD (BPARTNER) !Block
  BPOADD ADR Ship-from address
  BPOADDLIG ADL(3) Address line
  BPOCRY CRY Country -> [TCY]TCY0 =[POH]BPOCRY (TABCOUNTRY) !Block
  BPOCRYNAM NCY Country name
  BPOCTY CTY City
  BPONAM NAM(2) Company name
  BPOPOSCOD POS Postal code
  BPOSAT SAT County
  BPRNAM NAM(2) Company name
  BPRPAY BPR Pay-to -> [BPR]BPR0 =[POH]BPRPAY (BPARTNER) !Block
  BPSINV BPR Bill-by BP -> [BPR]BPR0 =[POH]BPSINV (BPARTNER) !Block
  BPSNUM BPR Supplier -> [BPR]BPR0 =[POH]BPSNUM (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[POH]BPTNUM (BPCARRIER) !Block
  BUY AUS Buyer -> [AUS]CODUSR =[POH]BUY (AUTILIS) !Block
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGCOE RCU Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CLELINNBR C*4 No. closed lines
  COPNBR C*1 No. copies order note
  CPY CPY Company -> [CPY]CPY0 =[POH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[POH]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  CUR CUR Currency -> [TCU]TCU0 =[POH]CUR (TABCUR) !Block
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[POH]DIE (GDIE) !Block act:ANA
  DISCRGTYP M*10 Discount / charge type [menu 255: 1=Amount,2=% combined,3=% series] act:PPR
  DME M*15 Partial delivery [menu 414: 1=Authorized,2=Full delivery line,3=Full order line]
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[POH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[POH]DSPWEU (TABUNIT) !Block
  EECICT ICT Incoterm -> [ICTH]ICT0 =[POH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNUM A*20 EU identification act:DEB
  ENDDAT D Validity end date
  EXPNUM L*8 Export number
  EXTRCPDAT1 D Exp. receipt date
  FBULINNBR C*4 No. lines > budg
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[POH]FFWNUM (BPCARRIER) !Block
  FUPFLG M*4 Delivery reminders [menu 1: 1=No,2=Yes]
  GPGCOD A*20 Grouping code
  ICTCTY CTY Incoterm town
  INVDTALIN1 PFI Invoice line element -> [PFI]PFI0 =[POH]INVDTALIN1 (PFOOTINV) !Block act:PPR
  INVDTALIN2 PFI(9) Invoice line allocation elemen -> [PFI]PFI0 =[POH]INVDTALIN2 (PFOOTINV) !Block
  INVDTAVAT1 VAT Price line tax -> [TVT]TVT0 =INVDTAVAT1(indice);[V]GSUPCLE (TABVAT) !Block act:PPR
  INVDTAVAT2 VAT(9) Distribution line tax -> [TVT]TVT0 =INVDTAVAT2(indice);[V]GSUPCLE (TABVAT) !Block
  INVFCY FCY Invoicing site -> [FCY]FCY0 =[POH]INVFCY (FACILITY) !Block
  INVFLG M*15 Invoiced [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  INVLINNBR C*4 No. invoiced lines
  INVNBR L*8 Number of invoices
  LAN LAN Language -> [TLA]TLA0 =[POH]LAN (TABLAN) !Block
  LINNBR C*4 Number of lines
  MDL MDL Delivery mode -> [TMD]TMD0 =[POH]MDL (TABMODELIV) !Block
  OCNDAT D Ack. date
  OCNFLG M*4 Ack. reminder [menu 1: 1=No,2=Yes]
  OCNNUM A*20 Ack. ID
  OCNREM A*150 Ack. notes
  ORDDAT D Order date
  ORDMAXAMT MD1 Maximum order
  ORDREF A*20 Internal reference
  ORIFCY FCY Original site -> [FCY]FCY0 =[POH]ORIFCY (FACILITY) !Block
  PJTH PJT Project -> [PIM]PIM0 =[POH]PJTH (PIMPL) !Block
  POHFCY FCY Order site -> [FCY]FCY0 =[POH]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POSCOD POS Postal code
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  PURTYP M*15 Purchase type [menu 507: 1=Commercial,2=General]
  RCPFCY FCY Receiving site -> [FCY]FCY0 =[POH]RCPFCY (FACILITY) !Block
  RCPFLG M*15 Received [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  RCPLINNBR C*4 No. received lines
  RCPNBR L*8 Number of receipts
  REVNUM C*4 Revision no.
  SALFCY FCY Sales site -> [FCY]FCY0 =[POH]SALFCY (FACILITY) !Block
  SAT SAT County
  SINUM A*10 Integrale part no. act:SMI
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  STOFCY FCY Shipment site -> [FCY]FCY0 =[POH]STOFCY (FACILITY) !Block
  STRDAT D Validity start date
  TCTRNUM TCTR Freight container -> [TCTR]TCTR0 =[POH]TCTRNUM (TABCONTAINER) !Block
  TCTRQTY C*4 No. of containers
  TEX1 TXC Text
  TEX2 TXC Text
  TOTLINAMT MD1 Invoice lines excluding tax
  TOTLINATI MD1 Lines total incl-tax
  TOTLINQTY DCB*11.6 Total quantity lines
  TOTLINVOU QTY Line volume total
  TOTLINWEU QTY Line weight total
  TOTORD MD1 Total order -tax
  TOTORDL MD1 Total excl. tax (co currency)
  TOTTAXAMT MD1 Tax total
  TOTVLT MD1 Expected total -tax
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Other act:STS
  TTVORD MD1 Total order +tax
  TTVORDL MD1 Tax incl. total cy currency
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACTYP C*1 Tax rule type
  VOLCAP QTY Volume
  WEICAP QTY Weight

## PORDERC (POC) - Cumulative POs before returns
Notes: differs in V9.0 P12 (diff: AT3_PORDERC.htm); differs in V10 P1 (diff: ATD_PORDERC.htm)
Keys (first = PK; D = duplicates allowed): POC0 POHNUM+POPLIN; POC1 POHNUM+ITMREF+PRHFCY; POC2 ITMREF+BETFCY+STRDAT (D)
Fields:
  AMTVLT MD1 Costing amount
  AUUID AUUID Single identifier
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPSNUM BPR Supplier -> [BPR]BPR0 =[POC]BPSNUM (BPARTNER) !Block
  COA COA(10) Chart code -> [COA]COA0 =[POC]COA (GCOA) !RTZ
  CPY CPY Company -> [CPY]CPY0 =[POC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYDSP C*3(7) Daily distribution
  DLVREQNUM L*8 Number of delivery request pro
  EARDAT D Early/Late date
  EARHOU HM Early/late time
  EARQTY QTY Early/Late qty.
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EECICT2 ICT Incoterm -> [ICTH]ICT0 =[POC]EECICT2 (INCOTERM) !Block
  EECLOC2 M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNUM2 A*20 EU identification act:DEB
  ENDDAT D Valid to
  EXPNUM L*8 Export number
  EXTQTYPUU QTY Expected PUR quantity
  EXTQTYSTU QTY Expected STK quantity
  FCYADD ADR Receipt address
  FFWADD2 ADR Forwarding agent address
  FFWNUM2 BPT Freight agent -> [BPT]BPT0 =[POC]FFWNUM2 (BPCARRIER) !Block
  FIMHOR C*4 Firm horizon
  FRTHOR C*4 Planning horizon
  FRTHORUOM M*15 Planning horizon time unit [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  ICTCTY2 CTY Incoterm town
  INVQTYPUU QTY Invoiced PUR
  INVQTYSTU QTY Invoiced STU
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[POC]ITMREF (ITMMASTER) !Block
  ITMREFBPS A*20 Supplier product
  LINACC GAC(10) Accounts -> [GAC]GAC0 =COA(indice);LINACC(indice) (GACCOUNT) !Block
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINREVNUM C*4 Revision no.
  ORDQTYPUU QTY Ordered PUR
  ORDQTYSTU QTY Ordered STK
  PJT PJT Project -> [PIM]PIM0 =[POC]PJT (PIMPL) !Block
  PLI PLI Price list code
  POHFCY FCY Order site -> [FCY]FCY0 =[POC]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[POC]PRHFCY (FACILITY) !Block
  PRIVLT MD8 Costing price
  PUU UOM Purchase unit -> [TUN]TUN0 =[POC]PUU (TABUNIT) !Block
  RCPQTYPUU QTY Received PUR
  RCPQTYSTU QTY Received STK
  RTNQTYPUU QTY Returned PUR qty.
  RTNQTYSTU QTY Returned STK qty.
  STOFCY FCY Shipment site -> [FCY]FCY0 =[POC]STOFCY (FACILITY) !Block
  STRDAT D Valid from
  STU UOM Stock unit -> [TUN]TUN0 =[POC]STU (TABUNIT) !Block
  TEX TXC Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  WEEDSP C*3(5) Weekly distribution

## PORDERP (POP) - POs price
Notes: differs in V9.0 P12 (diff: AT3_PORDERP.htm); differs in V10 P1 (diff: ATD_PORDERP.htm)
Keys (first = PK; D = duplicates allowed): POP0 POHNUM+POPLIN+POPSEQ; POP1 POHNUM+POPLIN+POPDAT; POP2 PRHFCY+POHNUM+POPLIN (D); POP3 ITMREF+POHTYP (D); PJMPJT1 PJT (D)
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[POP]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[POP]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[POP]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[POP]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECINCRAT RAT Intrastat increase act:DEB
  EXPNUM L*8 Export number
  FCYADD ADR Receipt address
  GROPRI MD8 Gross price
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[POP]ITMREF (ITMMASTER) !Block
  LINBUY AUS Buyer -> [AUS]CODUSR =[POP]LINBUY (AUTILIS) !Block
  LINREVNUM C*4 Revision no.
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[POP]MATTOL (MATCHTOL) !Block
  NETPRI MD8 Net price
  ORICRY CRY Country of origin -> [TCY]TCY0 =[POP]ORICRY (TABCOUNTRY) !Block
  PJT PJT Project -> [PIM]PIM0 =[POP]PJT (PIMPL) !Block
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPCREFLG M*4 Creation flag [menu 1: 1=No,2=Yes]
  POPDAT D Application end date
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[POP]PRHFCY (FACILITY) !Block
  PRIREN PPR Price reason -> [PPR]PPR0 =[POP]PRIREN (PPREASON) !Block
  QUAFLG M*4 QC management [menu 1: 1=No,2=Yes]
  STRDAT D Price effectivity date
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## PORDERQ (POQ) - POs quantities
Keys (first = PK; D = duplicates allowed): POQ0 POHNUM+POPLIN+POQSEQ; POQ1 LININVFLG+WIPSTA+BPSINV+ITMREF+POHNUM (D); POQ2 LINCLEFLG+WIPSTA+PRHFCY+BPSNUM+POHNUM (D); POQ3 POHNUM+POQLNK; POQ4 VCRTYPORI+VCRNUMORI+VCRLINORI+VCRSEQORI+ITMREFORI (D)
Fields:
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AUUID AUUID Single identifier
  BASTAXLIN1 MD1 Tax basis 1
  BPAINV ADR Billing address
  BPSINV BPR Bill-by BP -> [BPR]BPR0 =[POQ]BPSINV (BPARTNER) !Block
  BPSNUM BPR Supplier -> [BPR]BPR0 =[POQ]BPSNUM (BPARTNER) !Block
  CAD M*7 Sequencing [menu 278: 1=Day,2=Week,3=Month]
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  CMMFLG C*1 Commitment indic
  CMMNUM VCR Commitment no.
  CMMTAX M*25 Commitment type [menu 578: 1=Tax-excl. amount,2=Tax-excl. amount + Non-deductible VAT]
  CPR MD8 Stock cost per unit
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CPRCUR CUR Company currency -> [TCU]TCU0 =[POQ]CPRCUR (TABCUR) !Block
  CPRPRI MD8 Production cost PUR
  CPY CPY Company -> [CPY]CPY0 =[POQ]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTPUR MD8 Purchase cost per unit
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DEMENDDAT D Requesteded end date
  DEMENDHOU C*4 Requested end time
  DEMRCPDAT D Requested receipt date
  DEMRCPHOU C*4 Requested delivery time
  DISBASLIN1 MD1 Rebate tax basis 1
  DISCRGAMT1 MD1 Discount/Charge 1
  DISCRGAMT2 MD1 Discount/Charge 2
  DISCRGAMT3 MD1 Discount/Charge 3
  DISCRGAMT4 MD1 Discount/Charge 4
  DISCRGAMT5 MD1 Discount/Charge 5
  DISCRGAMT6 MD1 Discount/Charge 6
  DISCRGAMT7 MD1 Discount/Charge 7
  DISCRGAMT8 MD1 Discount/Charge 8
  DISCRGAMT9 MD1 Discount/Charge 9
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  EXTRCPDAT D Exp. receipt date
  FBUFLG M*4 Budget overrun [menu 1: 1=No,2=Yes]
  FCSCPR MD1 Stock cost total
  FCSCSTPUR MD1 Purchase cost total
  FCYADD ADR Receipt address
  INVQTYPUU QTY Invoiced PUR
  INVQTYSTU QTY Invoiced STU
  INVRCPNBR C*4 No. of invoice receipts
  ITMREF ITM Product -> [ITM]ITM0 =[POQ]ITMREF (ITMMASTER) !Block
  ITMREFBPS A*20 Supplier product
  ITMREFORI ITM Released product -> [ITM]ITM0 =[POQ]ITMREFORI (ITMMASTER) !Block
  LASINVDAT D Last invoice date
  LASRCPDAT D Last receipt date
  LIKQTYCOE COE Link qty. coef.
  LINAMT MD1 Line amount - tax
  LINAMTCPR MD8 Stock cost
  LINATI MD1 Line amount + tax
  LINATIAMT MD1 Line amount + tax
  LINCLEFLG M*4 Line closed [menu 1: 1=No,2=Yes]
  LINCSTPUR MD8 Purchase cost
  LININVFLG M*4 Invoiced line [menu 1: 1=No,2=Yes]
  LININVNBR C*4 Number of invoices
  LINOCNDAT D Ack. date
  LINOCNFLG C*1 Acknowledgement flag
  LINOCNNUM A*20 Ack. ID
  LINPRNFLG M*4 Line printed [menu 1: 1=No,2=Yes]
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINRCPNBR C*4 Number of receipts
  LINREVNUM C*4 Revision no.
  LINSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  LINSTOFCY FCY Shipment site -> [FCY]FCY0 =[POQ]LINSTOFCY (FACILITY) !Block
  LINTEX TXC Text
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  LINVOU UOM Volume unit -> [TUN]TUN0 =[POQ]LINVOU (TABUNIT) !Block
  LINWEU UOM Weight unit -> [TUN]TUN0 =[POQ]LINWEU (TABUNIT) !Block
  MON C*2 Months
  NETCUR CUR Currency -> [TCU]TCU0 =[POQ]NETCUR (TABCUR) !Block
  OCNLIN L*8 Interco. sales line
  OCNSEQ L*8 Interco. sales seq.
  OFS LTI Reorder LT
  ORDDAT D Order date
  ORI M*15 Request source [menu 505: 1=Purchases,2=Direct order,3=Received direct order,4=Transfer,5=Production]
  POHFCY FCY Order site -> [FCY]FCY0 =[POQ]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPLIN L*8 Line
  POQLNK A*16 Line + sequence
  POQSEQ L*8 Sequence number
  PPDLIN L*8 Response line
  PQHNUM VCR RFQ no.
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[POQ]PRHFCY (FACILITY) !Block
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[POQ]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Ordered qty.
  QTYVOU QTY Volume
  QTYWEU QTY Weight
  RCPCLEFLG M*4 Closed by receipt [menu 1: 1=No,2=Yes]
  RCPQTYPUU QTY Received PUR
  RCPQTYSTU QTY Received STK
  REACSTPUR MD8 Actual purchase cost
  RETQTYPUU QTY Required PUR
  RETQTYSTU QTY Required STK
  RETRCPDAT D Requirement date
  SCOADD ADR Subcon. address
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  SHIQTYPUU QTY PUR qty. being deliv.
  SHIQTYSTU QTY STK qty. being deliv.
  SOHNUM VCR Sales order no.
  SOPLIN L*8 Sales order line
  SOQSEQ L*8 Sequence number
  STCNUM VCR Cost structure
  STU UOM Stock unit -> [TUN]TUN0 =[POQ]STU (TABUNIT) !Block
  UOM UOM Order unit -> [TUN]TUN0 =[POQ]UOM (TABUNIT) !Block
  UOMFLG M*4 Order in PAC [menu 1: 1=No,2=Yes]
  UOMPUUCOE COE STK-PUR conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WEE C*2 Week no.
  WIPNUM VCR Order no.
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]
  YEA C*4 Year

## PORDITM (POI) - Purchase orders by product
Keys (first = PK; D = duplicates allowed): POI0 USR+NOLIG; POI1 USR+POILIN
Fields:
  AUUID AUUID Single identifier
  BPSNUM BPR Supplier -> [BPR]BPR0 =[POI]BPSNUM (BPARTNER) !Block
  BUY AUS Buyer -> [AUS]CODUSR =[POI]BUY (AUTILIS) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGCOE RCU Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[POI]CUR (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[POI]DIE (GDIE) !Block act:ANA
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[POI]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[POI]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[POI]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EECINCRAT RAT Intrastat increase act:DEB
  EXPNUM L*8 Export number
  EXTRCPDAT D Exp. receipt date
  FCYADD ADR Addr.
  GROPRI MD8 Gross price
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[POI]ITMREF (ITMMASTER) !Block
  LINBUY AUS Buyer -> [AUS]CODUSR =[POI]LINBUY (AUTILIS) !Block
  NETPRI MD8 Net price
  NOLIG C*3 Line number
  ORDDAT D Order date
  ORDREF A*20 Internal reference
  ORICRY CRY Country of origin -> [TCY]TCY0 =[POI]ORICRY (TABCOUNTRY) !Block
  PJT A*20 Project
  POHFCY FCY Order site -> [FCY]FCY0 =[POI]POHFCY (FACILITY) !Block
  POICOU L*8 Line sequence number
  POILIN L*8 Order information
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[POI]PRHFCY (FACILITY) !Block
  PRIREN PPR Price reason -> [PPR]PPR0 =[POI]PRIREN (PPREASON) !Block
  PRONUM L*8 Process number
  PUU UOM Purchase unit -> [TUN]TUN0 =[POI]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Ordered qty.
  QUAFLG M*4 QC management [menu 1: 1=No,2=Yes]
  RETQTYPUU QTY Required PUR
  RETQTYSTU QTY Required STK
  RETRCPDAT D Requirement date
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[POI]STU (TABUNIT) !Block
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD (ATABDIV) !Other act:STI
  UOM UOM Order unit -> [TUN]TUN0 =[POI]UOM (TABUNIT) !Block
  UOMFLG M*4 Order in PAC [menu 1: 1=No,2=Yes]
  UOMPUUCOE COE STK-PUR conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDPSDFLG M*4 Purchase request upd [menu 1: 1=No,2=Yes]
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  USR AUS Operator -> [AUS]CODUSR =[POI]USR (AUTILIS) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## PPRICLINK (PPK) - Purchase price list search (link)
Notes: differs in V9.0 P12 (diff: AT3_PPRICLINK.htm); differs in V10 P1 (diff: ATD_PPRICLINK.htm)
Keys (first = PK; D = duplicates allowed): PPK0 CLE
Fields:
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPAADD ADR Address
  BPSNUM BPS Supplier -> [BPS]BPS0 =[PPK]BPSNUM (BPSUPPLIER) !BSRA
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PPK]BPTNUM (BPCARRIER) !BSRA
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLE A*3 Key
  CPY CPY Purchase company -> [CPY]CPY0 =[PPK]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PPK]CREUSR (AUTILIS) !Other
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  EECICT ICT Incoterm -> [ICTH]ICT0 =[PPK]EECICT (INCOTERM) !Other
  ITMREFORI ITM Released product -> [ITM]ITM0 =[PPK]ITMREFORI (ITMMASTER) !BSRA
  MDL MDL Delivery mode -> [TMD]TMD0 =[PPK]MDL (TABMODELIV) !Other
  MFGITM ITM Released product -> [ITM]ITM0 =[PPK]MFGITM (ITMMASTER) !BSRA
  OPENUM OPE Operation
  PJT PJT Project -> [PIM]PIM0 =[PPK]PJT (PIMPL) !BSRA
  PJTNUM PJT Project number -> [PIM]PIM0 =[PPK]PJTNUM (PIMPL) !Block
  PLIBPRCNR M*15 BP concerns [menu 2210: 1=Outside group,2=Group,3=All]
  POHFCY FCY Purchase site -> [FCY]FCY0 =[PPK]POHFCY (FACILITY) !Other
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[PPK]PRHFCY (FACILITY) !Other
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Other
  PURTYP M*15 Purchase type [menu 507: 1=Commercial,2=General]
  PUU UOM Purchase unit -> [TUN]TUN0 =[PPK]PUU (TABUNIT) !Other
  SALCPY CPY Sales company -> [CPY]CPY0 =[PPK]SALCPY (COMPANY) !Other
  SALFCY FCY Sales site -> [FCY]FCY0 =[PPK]SALFCY (FACILITY) !Other
  STU UOM Stock unit -> [TUN]TUN0 =[PPK]STU (TABUNIT) !Other
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Other act:STS
  UOM UOM Order unit -> [TUN]TUN0 =[PPK]UOM (TABUNIT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PPK]UPDUSR (AUTILIS) !Other
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Other
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]

## PPRIVARWRK (PPV) - Purchase price variance report
Keys (first = PK; D = duplicates allowed): PPV PID (D)
Fields:
  AUUID AUUID Single identifier
  BPSNAM NAM Company name
  BPSNUM BPS Supplier -> [BPS]BPS0 =[PPV]BPSNUM (BPSUPPLIER) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PPV]CREUSR (AUTILIS) !Other
  CSTTOT MD8 Total cost
  CUR CUR Currency -> [TCU]TCU0 =[PPV]CUR (TABCUR) !Block
  FCY FCY Site -> [FCY]FCY0 =[PPV]FCY (FACILITY) !Block
  ITMDES1 DES Description 1
  ITMREF ITM Product -> [ITM]ITM0 =[PPV]ITMREF (ITMMASTER) !Block
  NETPRI MD8 Net price
  NUM VCR Invoice number
  PID A*20 Processes
  PIDPRI MD8 Invoice price
  PLIN L*8 Line
  PNUM VCR Document no.
  POHNUM VCR Order no.
  QTYSTU QTY STK quantity
  STKVAR MD8 Stock itm variance
  STU UOM Stock unit -> [TUN]TUN0 =[PPV]STU (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PPV]UPDUSR (AUTILIS) !Other

## PQUOTAT (PQH) - RFQs
Keys (first = PK; D = duplicates allowed): PQH0 PQHNUM; PQH1 PQHDAT+PQHNUM
Fields:
  AUUID AUUID Single identifier
  BPSNBR C*4 Number of suppliers
  CPY CPY Company -> [CPY]CPY0 =[PQH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  LINNBR C*4 Number of lines
  PQHDAT D RFQ date
  PQHFCY FCY RFQ site -> [FCY]FCY0 =[PQH]PQHFCY (FACILITY) !Block
  PQHNUM VCR RFQ no.
  PQHREF A*20 Internal reference
  REQUSR AUS Requester -> [AUS]CODUSR =[PQH]REQUSR (AUTILIS) !Block
  RSPDEA D Response due date
  RSPNBR C*4 Number of responses
  TEX1 TXC Text
  TEX2 TXC Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PQUOTATD (PQD) - RFQ product detail
Keys (first = PK; D = duplicates allowed): PQD0 PQHNUM+PQDLIN; PQD1 PQHNUM+ITMREF (D)
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[PQD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF A*20 Product
  LINRSPNBR C*4 Number of responses
  LINTEX TXC Text
  LTI C*3 Lead time
  PQDLIN L*8 Line
  PQDPJT A*20 Project
  PQHFCY FCY RFQ site -> [FCY]FCY0 =[PQD]PQHFCY (FACILITY) !Block
  PQHNUM VCR RFQ no.
  PSDLIN L*8 Pur. req. line no.
  PSHNUM VCR Pur. req. no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PQD]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  RCPDAT D Receipt date
  RETQTYSTU QTY Required STK
  STU UOM Stock unit -> [TUN]TUN0 =[PQD]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PQUOTATF (PQF) - RFQ supplier detail
Keys (first = PK; D = duplicates allowed): PQF0 PQHNUM+BPSNUM; PQF1 BPSNUM+PQHNUM
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPAADDLIG ADL(3) Address line
  BPRNAM NAM(2) Company name
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PQF]BPSNUM (BPARTNER) !Block
  COPNBR C*1 No. copies request for quote
  CPY CPY Company -> [CPY]CPY0 =[PQF]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[PQF]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  FUPDAT D Last reminder date
  FUPNBR C*4 Number of relaunches
  POSCOD POS Postal code
  PQHFCY FCY RFQ site -> [FCY]FCY0 =[PQF]PQHFCY (FACILITY) !Block
  PQHNUM VCR RFQ no.
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  RSPNBR C*4 Number of responses
  SAT SAT County
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PRECEIPT (PTH) - Receipt
Notes: differs in V9.0 P12 (diff: AT3_PRECEIPT.htm); differs in V10 P1 (diff: ATD_PRECEIPT.htm)
Keys (first = PK; D = duplicates allowed): PTH0 PTHNUM; PTH1 BPSNDE (D); PTH2 BPSNUM+RCPDAT (D); PTH3 RCPDAT+PTHNUM; PTH4 CPY+EECNUMDEB+RCPDAT (D)
Fields:
  ARVDAT D Arrival date
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPAADD ADR Address
  BPAINV ADR Billing address
  BPAPAY ADR Pay-to BP address
  BPOADD ADR Ship-from address
  BPOADDLIG ADL(3) Address line
  BPOCRY CRY Country -> [TCY]TCY0 =[PTH]BPOCRY (TABCOUNTRY) !Block
  BPOCRYNAM NCY Country name
  BPOCTY CTY City
  BPONAM NAM(2) Company name
  BPOPOSCOD POS Postal code
  BPOSAT SAT County
  BPRPAY BPR Pay-to -> [BPR]BPR0 =[PTH]BPRPAY (BPARTNER) !Block
  BPSINV BPR Bill-by supplier -> [BPR]BPR0 =[PTH]BPSINV (BPARTNER) !Block
  BPSNDE A*20 Supplier packing slip no.
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PTH]BPSNUM (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PTH]BPTNUM (BPCARRIER) !Block
  CAI A*10 CAI number act:KAG
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGCOE RCU Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLSVCR A*10 Class act:KAG
  CPY CPY Company -> [CPY]CPY0 =[PTH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PTH]CUR (TABCUR) !Block
  DATVLYCAI D*1 CAI validity date act:KAG
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[PTH]DIE (GDIE) !Block act:ANA
  DPEDAT D Departure date
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[PTH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[PTH]DSPWEU (TABUNIT) !Block
  EECICT ICT Incoterm -> [ICTH]ICT0 =[PTH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block act:DEB
  EECNUM A*20 EU identification act:DEB
  EECNUMDEB C*4 EU Intrastat act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[PTH]ENTCOD (GAUTACE) !Block
  ETA HM Arrival time
  ETD HM Departure time
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[PTH]FFWNUM (BPCARRIER) !Block
  GPGCOD A*20 Grouping code
  ICTCTY CTY Incoterm town
  INVDTALIN1 PFI Invoice line element -> [PFI]PFI0 =[PTH]INVDTALIN1 (PFOOTINV) !Block act:PPR
  INVDTALIN2 PFI(9) Invoice line allocation elemen -> [PFI]PFI0 =[PTH]INVDTALIN2 (PFOOTINV) !Block
  INVDTAVAT1 VAT Price line tax -> [TVT]TVT0 =INVDTAVAT1(indice);[V]GSUPCLE (TABVAT) !Block act:PPR
  INVDTAVAT2 VAT(9) Distribution line tax -> [TVT]TVT0 =INVDTAVAT2(indice);[V]GSUPCLE (TABVAT) !Block
  INVFLG M*15 Invoiced [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  INVLINCTR C*4 No. invoiced lines
  INVLINNBR C*4 No. lines comp inv
  LICPLATE REGLIC Registration
  LINNBR C*4 Number of lines
  MDL MDL Delivery mode -> [TMD]TMD0 =[PTH]MDL (TABMODELIV) !Block
  NDEDAT D Packing slip date
  PJTH PJT Project -> [PIM]PIM0 =[PTH]PJTH (PIMPL) !Block
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[PTH]PRHFCY (FACILITY) !Block
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PSTDAT D Reversal date
  PSTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  PSTLINNBR C*4 No. of posted lines
  PTHNUM VCR Receipt no.
  PURTYP M*15 Purchase type [menu 507: 1=Commercial,2=General]
  RCPDAT D Receipt date
  SCUVCR A*10 Branch act:KAG
  SEQVCR A*10 Sequence act:KAG
  TEX1 TXC Text
  TEX2 TXC Text
  TOTAMTATI MD1 Total including tax
  TOTAMTATIL MD1 Tax incl. total cy currency
  TOTAMTNOT MD1 Total excluding tax
  TOTAMTNOTL MD1 Total excl. tax (co currency)
  TOTGROWEI DCB*11.4 Gross weight
  TOTLINAMT MD1 Invoice lines excluding tax
  TOTLINQTY DCB*11.6 Total quantity lines
  TOTLINVOU QTY Line volume total
  TOTLINWEU QTY Line weight total
  TOTNETWEI DCB*11.4 Net weight
  TOTTAXAMT MD1 Tax total
  TOTVOL DCB*11.4 Volume
  TRLLICPLATE REGLIC Trailer license plate
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Block act:STS
  TYPVCR A*10 Document type act:KAG
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACTYP C*1 Tax rule type
  VOU UOM Volume unit -> [TUN]TUN0 =[PTH]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[PTH]WEU (TABUNIT) !Block
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## PRECEIPTD (PTD) - Detail receipts
Notes: differs in V9.0 P12 (diff: AT3_PRECEIPTD.htm); differs in V10 P1 (diff: ATD_PRECEIPTD.htm)
Keys (first = PK; D = duplicates allowed): PTD0 PTHNUM+PTDLIN; PTD1 LININVFLG+BPSINV+ITMREF+PTHNUM+PTDLIN; PTD2 POHNUM+POPLIN+POQSEQ+PTHNUM+PTDLIN; PTD3 PRHFCY+BPSNUM+ITMREF+PTHNUM+PTDLIN; PJMPJT1 PJT (D)
Fields:
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AUUID AUUID Single identifier
  BASTAXLIN1 MD1 Tax basis 1
  BPAINV ADR Billing address
  BPOCRY CRY Shipping country -> [TCY]TCY0 =[PTD]BPOCRY (TABCOUNTRY) !Block
  BPSINV BPR Bill-by supplier -> [BPR]BPR0 =[PTD]BPSINV (BPARTNER) !Block
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PTD]BPSNUM (BPARTNER) !Block
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  CPR MD8 Production cost PUR
  CPRAMT MD5 Fixed cost per unit
  CPRCLC MD8 Calculated STK cost
  CPRCOE COE Landed cost coef.
  CPRCUR CUR Company currency -> [TCU]TCU0 =[PTD]CPRCUR (TABCUR) !Block
  CPRPRI MD8 Production cost PUR
  CPY CPY Company -> [CPY]CPY0 =[PTD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTPUR MD8 Purchase cost per unit
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DISBASLIN1 MD1 Rebate tax basis 1
  DISCRGAMT1 MD1 Discount/Charge 1
  DISCRGAMT2 MD1 Discount/Charge 2
  DISCRGAMT3 MD1 Discount/Charge 3
  DISCRGAMT4 MD1 Discount/Charge 4
  DISCRGAMT5 MD1 Discount/Charge 5
  DISCRGAMT6 MD1 Discount/Charge 6
  DISCRGAMT7 MD1 Discount/Charge 7
  DISCRGAMT8 MD1 Discount/Charge 8
  DISCRGAMT9 MD1 Discount/Charge 9
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[PTD]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[PTD]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[PTD]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECINCRAT RAT Intrastat increase act:DEB
  EXPNUM L*8 Export number
  FCSCPR MD1 Stock cost total
  FCSCPRCPT MD1 Posted stock costs
  FCSCSTPUR MD1 Purchase cost total
  GROPRI MD8 Gross price
  INVQTYPUU QTY Invoiced PUR
  INVQTYSTU QTY Invoiced STU
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PTD]ITMREF (ITMMASTER) !Block
  ITMREFORI ITM Released product -> [ITM]ITM0 =[PTD]ITMREFORI (ITMMASTER) !Block
  LIKQTYCOE COE Link qty. coef.
  LINAMT MD1 Line amount - tax
  LINAMTCPR MD8 Stock cost
  LINATIAMT MD1 Line amount + tax
  LINCAT M*15 Movement category [menu 574: 1=Standard,2=For subcontracting]
  LINCSTPUR MD8 Purchase cost
  LINEECFLG M*4 Debit line [menu 1: 1=No,2=Yes] act:DEB
  LININVFLG M*4 Invoiced line [menu 1: 1=No,2=Yes]
  LINPRNFLG M*4 Line printed [menu 1: 1=No,2=Yes]
  LINPSTDAT D Reversal date
  LINPSTFLG M*4 Posted line [menu 1: 1=No,2=Yes]
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINSTOFCY FCY Shipment site -> [FCY]FCY0 =[PTD]LINSTOFCY (FACILITY) !Block
  LINTEX TXC Text
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  LINVOU UOM Volume unit -> [TUN]TUN0 =[PTD]LINVOU (TABUNIT) !Block
  LINWEU UOM Weight unit -> [TUN]TUN0 =[PTD]LINWEU (TABUNIT) !Block
  MATTOL MAT Matching tolerance -> [MAT]MAT0 =[PTD]MATTOL (MATCHTOL) !Block
  NETCUR CUR Currency -> [TCU]TCU0 =[PTD]NETCUR (TABCUR) !Block
  NETPRI MD8 Net price
  NETPRIPUU MD8 Net price PUR
  ORICRY CRY Country of origin -> [TCY]TCY0 =[PTD]ORICRY (TABCOUNTRY) !Block
  PJT PJT Project -> [PIM]PIM0 =[PTD]PJT (PIMPL) !Block
  POHFCY FCY Order site -> [FCY]FCY0 =[PTD]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPLIN L*8 Order line
  POQSEQ L*8 Order seq no.
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[PTD]PRHFCY (FACILITY) !Block
  PRIREN PPR Price reason -> [PPR]PPR0 =[PTD]PRIREN (PPREASON) !Block
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PTD]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Quantity STK
  QTYVOU QTY Volume
  QTYWEU QTY Weight
  QUAFLG M*15 QC management [menu 275: 1=No control,2=Non-changeable control,3=Changeable control,4=Periodic control]
  QUARTNFLG M*4 Return from QC [menu 1: 1=No,2=Yes]
  RCPDAT D Receipt date
  RRRQTYPUU QTY Quantity R PUR
  RRRQTYSTU QTY Quantity R STK
  RTNQTYPUU QTY Returned PUR qty.
  RTNQTYSTU QTY Returned STK qty.
  SATISS SAT Issue region act:PTX
  SCOCSTCPT MD1 Posted subcon cost
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  SHIPLIN L*8 Line
  SHIPNUM VCR Shipment number
  STCNUM VCR Cost structure
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[PTD]STU (TABUNIT) !Block
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Block act:STI
  UOM UOM Receipt unit -> [TUN]TUN0 =[PTD]UOM (TABUNIT) !Block
  UOMPUUCOE COE STK-PUR conversion
  UOMSTUCOE COE STK conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  VERFLG C*3 Version flag
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## PREQUIS (PSH) - Purchase requests
Notes: differs in V9.0 P12 (diff: AT3_PREQUIS.htm); differs in V10 P1 (diff: ATD_PREQUIS.htm)
Keys (first = PK; D = duplicates allowed): PSH0 PSHNUM; PSH1 PSHFCY+PSHNUM; PSH2 PRQDAT+PSHNUM; PSH3 PSHNUMMMS+PSHNUM
Fields:
  APPFLG M*15 Signed [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  APPLINNBR C*4 No. of signed lines
  ATECORI M*15 Source [menu 7885: 1=Classic pages,2=Classes]
  AUUID AUUID Single identifier
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CLELINNBR C*4 No. closed lines
  CPY CPY Company -> [CPY]CPY0 =[PSH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DIE DIE Dimension type code -> [DIE]DIE0 =[PSH]DIE (GDIE) !Block act:ANA
  EXPNUM L*8 Export number
  FBULINNBR C*4 No. lines > budg
  LINNBR C*4 Number of lines
  MMSURL A*250 Maintenance URL
  ORDFLG M*4 Ordered [menu 1: 1=No,2=Yes]
  ORDLINNBR C*4 No. of order lines
  PJTH PJT Project -> [PIM]PIM0 =PJTH (PIMPL) !Block
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PRQDAT D Request date
  PSHFCY FCY Request site -> [FCY]FCY0 =[PSH]PSHFCY (FACILITY) !Block
  PSHNUM VCR Request no.
  PSHNUMMMS A*15 Maintenance no.
  REQUSR AUS Requester -> [AUS]CODUSR =[PSH]REQUSR (AUTILIS) !Block
  TEX1 TXC Text
  TEX2 TXC Text
  TOTPRQ MD1 Request total -tax
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PREQUISA (PSA) - Link purchase requests
Keys (first = PK; D = duplicates allowed): PSA0 PSHNUM+PSDLIN+PQHNUM+PQDLIN; PSA1 PQHNUM+PQDLIN+PSHNUM+PSDLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSA]CREUSR (AUTILIS) !Other
  PQDLIN L*8 Line
  PQHNUM VCR RFQ no.
  PSDLIN L*8 Pur. req. line no.
  PSHNUM VCR Request no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PSA]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  STU UOM Stock unit -> [TUN]TUN0 =[PSA]STU (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSA]UPDUSR (AUTILIS) !Other

## PREQUISD (PSD) - Purchase request detail
Notes: differs in V9.0 P12 (diff: AT3_PREQUISD.htm); differs in V10 P1 (diff: ATD_PREQUISD.htm)
Keys (first = PK; D = duplicates allowed): PSD0 PSHNUM+PSDLIN; PSD1 LINORDFLG+ITMREF+EXTRCPDAT+PSHNUM+PSDLIN (D); PSD2 LINORDFLG+LINBUY+EXTORDDAT (D); PSD3 PSDNUMMMS+PSHNUM+PSDLIN; PJMPJT1 PJT (D)
Fields:
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  ATECORI M*15 Source [menu 7885: 1=Classic pages,2=Classes]
  AUUID AUUID Single identifier
  BASTAXLIN1 MD1 Tax basis 1
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PSD]BPSNUM (BPARTNER) !Block
  CHGCOE RCU Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  CMMPRPFLG C*1 Pre commitment indic
  CMMPRPNUM VCR Pre-commitment no.
  CMMPRPTAX M*25 Commitment type [menu 578: 1=Tax-excl. amount,2=Tax-excl. amount + Non-deductible VAT]
  CPY CPY Company -> [CPY]CPY0 =[PSD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PSD]CUR (TABCUR) !Block
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[PSD]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[PSD]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[PSD]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXTORDDAT D Calculated order date
  EXTRCPDAT D Requested date
  FBUFLG M*4 Budget overrun [menu 1: 1=No,2=Yes]
  GROPRI MD8 Gross price
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PSD]ITMREF (ITMMASTER) !Block
  LINAMT MD1 Line amount - tax
  LINAPPFLG M*15 Signed line [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  LINATIAMT MD1 Line amount + tax
  LINBUY AUS Buyer -> [AUS]CODUSR =[PSD]LINBUY (AUTILIS) !Block
  LINCLEFLG M*4 Line closed [menu 1: 1=No,2=Yes]
  LINORDFLG M*4 Ordered line [menu 1: 1=No,2=Yes]
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINTEX TXC Text
  NBAOF L*4 No. of RFQs
  NETPRI MD8 Net price
  ORDQTYPUU QTY Ordered PUR
  ORDQTYSTU QTY Ordered STK
  ORI M*15 Request source [menu 505: 1=Purchases,2=Direct order,3=Received direct order,4=Transfer,5=Production]
  PJT PJT Project -> [PIM]PIM0 =[PSD]PJT (PIMPL) !Block
  PPDLIN L*8 Response line
  PQHNUM VCR RFQ no.
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[PSD]PRHFCY (FACILITY) !Block
  PRIREN PPR Price reason -> [PPR]PPR0 =[PSD]PRIREN (PPREASON) !Block
  PSDLIN L*8 Line
  PSDNUMMMS A*15 Maintenance line id
  PSHFCY FCY Request site -> [FCY]FCY0 =[PSD]PSHFCY (FACILITY) !Block
  PSHNUM VCR Request no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PSD]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  STU UOM Stock unit -> [TUN]TUN0 =[PSD]STU (TABUNIT) !Block
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACTYP C*1 Tax rule type
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  WIPNUM VCR Order no.

## PREQUISO (PSO) - Link purchase requests
Keys (first = PK; D = duplicates allowed): PSO0 PSHNUM+PSDLIN+POHNUM+POPLIN+POQSEQ; PSO1 POHNUM+POPLIN+POQSEQ+PSHNUM+PSDLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PSO]CREUSR (AUTILIS) !Other
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Sequence number
  PSDLIN L*8 Line
  PSHNUM VCR Request no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PSO]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  STU UOM Stock unit -> [TUN]TUN0 =[PSO]STU (TABUNIT) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PSO]UPDUSR (AUTILIS) !Other

## PRESP (PPH) - RFQ responses
Keys (first = PK; D = duplicates allowed): PPH0 BPSNUM+PQHNUM+PQDLIN; PPH1 ITMREF+BPSNUM+PQHNUM (D); PPH2 BPSNUM+ITMREF+PQHNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PPH]BPSNUM (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[PPH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EANCODBPS A*20 Supplier UPC code
  ITMDESBPS DES Supplier description
  ITMREF A*20 Product
  ITMREFBPS A*20 Supplier product
  LINNBR C*4 Number of lines
  PLISTC PRS Structure code -> [PRS]PRS0 =2;PLISTC (PRICSTRUCT) !Block
  PQDLIN L*8 Line
  PQHFCY FCY RFQ site -> [FCY]FCY0 =[PPH]PQHFCY (FACILITY) !Block
  PQHNUM VCR RFQ no.
  PRIFLG M*4 Price recorded [menu 1: 1=No,2=Yes]
  PRILINNBR C*4 Number of price lines
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  RSPDAT D Response date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PRESPD (PPD) - Detail RFQ responses
Keys (first = PK; D = duplicates allowed): PPD0 BPSNUM+PQHNUM+PQDLIN+PPDLIN; PPD1 BPSNUM+PQHNUM+ITMREF+PPDLIN (D)
Fields:
  AUUID AUUID Single identifier
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PPD]BPSNUM (BPARTNER) !Block
  CPY CPY Company -> [CPY]CPY0 =[PPD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PPD]CUR (TABCUR) !Block
  DISCRGVAL1 MD8 Discount/Charge 1
  DISCRGVAL2 MD8 Discount/Charge 2
  DISCRGVAL3 MD8 Discount/Charge 3
  DISCRGVAL4 MD8 Discount/Charge 4
  DISCRGVAL5 MD8 Discount/Charge 5
  DISCRGVAL6 MD8 Discount/Charge 6
  DISCRGVAL7 MD8 Discount/Charge 7
  DISCRGVAL8 MD8 Discount/Charge 8
  DISCRGVAL9 MD8 Discount/Charge 9
  ITMREF A*20 Product
  LTI C*3 Lead time
  MAXQTY QTY Maximum quantity
  MINQTY QTY Minimum quantity
  ORDFLG M*4 Order recorded [menu 1: 1=No,2=Yes]
  PLIENDDAT D Validity end date
  PLISTRDAT D Validity start date
  PPDLIN L*8 Response line
  PQDLIN L*8 Line
  PQHFCY FCY RFQ site -> [FCY]FCY0 =[PPD]PQHFCY (FACILITY) !Block
  PQHNUM VCR RFQ no.
  PRI MD8 Price
  PRIDIV C*4 Price factor
  PRIFLG M*4 Price recorded [menu 1: 1=No,2=Yes]
  PRIREN PPR Price reason -> [PPR]PPR0 =[PPD]PRIREN (PPREASON) !Block
  PUU UOM Purchase unit -> [TUN]TUN0 =[PPD]PUU (TABUNIT) !Block
  RCPDAT D Receipt date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PRETURN (PNH) - Returns
Notes: differs in V9.0 P12 (diff: AT3_PRETURN.htm); differs in V10 P1 (diff: ATD_PRETURN.htm)
Keys (first = PK; D = duplicates allowed): PNH0 PNHNUM; PNH1 BPSNUM+RTNDAT (D); PNH2 RTNDAT+PNHNUM; PNH3 CPY+EECNUMDEB+RTNDAT (D)
Fields:
  ARVDATR D Arrival date
  ATDTCODR A*100 AT code act:KPO
  AUUID AUUID Single identifier
  AUZNUM A*15 Authorization number
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BOLNUM VCR BOL number
  BPAADD ADR Address
  BPAADDLIG ADL(3) Address line
  BPAINV ADR Billing address
  BPAPAY ADR Pay-to BP address
  BPRNAM NAM(2) Company name
  BPRPAY BPR Pay-to -> [BPR]BPR0 =[PNH]BPRPAY (BPARTNER) !Block
  BPSINV BPR Bill-by BP -> [BPR]BPR0 =[PNH]BPSINV (BPARTNER) !Block
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PNH]BPSNUM (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PNH]BPTNUM (BPCARRIER) !Block
  BUY AUS Buyer -> [AUS]CODUSR =[PNH]BUY (AUTILIS) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFMFLG M*4 Posted [menu 1: 1=No,2=Yes]
  COPNBR C*1 No. copies return note
  CPY CPY Company -> [CPY]CPY0 =[PNH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[PNH]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  DIE DIE Dimension type code -> [DIE]DIE0 =[PNH]DIE (GDIE) !Block act:ANA
  DPEDATR D Departure date
  EECICT ICT Incoterm -> [ICTH]ICT0 =[PNH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block act:DEB
  EECNUM A*20 EU identification act:DEB
  EECNUMDEB C*4 EU Intrastat act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  ENTCOD GAU Stock auto journal -> [GAU]GAU0 =[PNH]ENTCOD (GAUTACE) !Block
  ETAR HM Arrival time
  ETDR HM Departure time
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[PNH]FFWNUM (BPCARRIER) !Block
  ICTCTY CTY Incoterm town
  INVFLG M*15 Invoiced [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  INVLINNBR C*4 No. invoiced lines
  LICPLATER REGLIC Registration
  LINNBR C*4 Number of lines
  MANDOCR DOC Manual document act:KPO
  MDL MDL Delivery mode -> [TMD]TMD0 =[PNH]MDL (TABMODELIV) !Block
  PJTH PJT Project -> [PIM]PIM0 =[PNH]PJTH (PIMPL) !Block
  PNHFCY FCY Return site -> [FCY]FCY0 =[PNH]PNHFCY (FACILITY) !Block
  PNHNUM VCR Return no.
  PNHTYP TPN Return type -> [TPN]TPN0 =PNHTYP;[V]GSUPCLE (TABPNHTYP) !Block act:TRSNE
  POSCOD POS Postal code
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PSTDAT D Reversal date
  PSTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  PSTLINNBR C*4 No. of posted lines
  PURTYP M*15 Purchase type [menu 507: 1=Commercial,2=General]
  REM A*250 Notes
  RTNDAT D Return date
  SAT SAT County
  TEX1 TXC Text
  TEX2 TXC Text
  TMPPNHNUM VCR Return no.
  TOTGROWEI DCB*11.4 Gross weight
  TOTNETWEI DCB*11.4 Net weight
  TOTVOL DCB*11.4 Volume
  TRLLICPLATER REGLIC Trailer license plate
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Other
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Block act:STS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACTYP C*1 Tax rule type
  VOU UOM Volume unit -> [TUN]TUN0 =[PNH]VOU (TABUNIT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[PNH]WEU (TABUNIT) !Block
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## PRETURND (PND) - Detail return
Notes: differs in V9.0 P12 (diff: AT3_PRETURND.htm); differs in V10 P1 (diff: ATD_PRETURND.htm)
Keys (first = PK; D = duplicates allowed): PND0 PNHNUM+PNDLIN; PND1 PTHNUM+PTDLIN (D); PND2 LININVFLG+BPSINV+ITMREF+PNHNUM+PNDLIN; PND3 POHNUM+POPLIN+POQSEQ (D); PJMPJT1 PJT (D)
Fields:
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AUUID AUUID Single identifier
  BASTAXLIN1 MD1 Tax basis 1
  BPAINV ADR Billing address
  BPOCRY CRY Shipping country -> [TCY]TCY0 =[PND]BPOCRY (TABCOUNTRY) !Block
  BPSINV BPR Bill-by BP -> [BPR]BPR0 =[PND]BPSINV (BPARTNER) !Block
  BPSNDE A*20 Supplier packing slip no.
  BPSNUM BPR Supplier -> [BPR]BPR0 =[PND]BPSNUM (BPARTNER) !Block
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  CPR MD8 Cost price
  CPRCOE COE Landed cost coef.
  CPRCUR CUR Currency -> [TCU]TCU0 =[PND]CPRCUR (TABCUR) !Block
  CPY CPY Company -> [CPY]CPY0 =[PND]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[PND]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[PND]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[PND]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECINCRAT RAT Intrastat increase act:DEB
  GROPRI MD8 Gross price
  INVQTYPUU QTY Invoiced PUR
  INVQTYSTU QTY Invoiced STU
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PND]ITMREF (ITMMASTER) !Block
  LIKQTYCOE COE Link qty. coef.
  LINAMT MD1 Line amount - tax
  LINATIAMT MD1 Line amount + tax
  LINAUTFLG M*4 Automatic flow [menu 1: 1=No,2=Yes]
  LINCAT M*15 Movement category [menu 574: 1=Standard,2=For subcontracting]
  LINEECFLG M*4 Debit line [menu 1: 1=No,2=Yes] act:DEB
  LININVFLG M*4 Invoiced line [menu 1: 1=No,2=Yes]
  LINPRNFLG M*4 Line printed [menu 1: 1=No,2=Yes]
  LINPSTDAT D Reversal date
  LINPSTFLG M*4 Posted line [menu 1: 1=No,2=Yes]
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINSTOFCY FCY Shipment site -> [FCY]FCY0 =[PND]LINSTOFCY (FACILITY) !Block
  LINTEX TXC Text
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  NETCUR CUR Currency -> [TCU]TCU0 =[PND]NETCUR (TABCUR) !Block
  NETPRI MD8 Net price
  NETPRIPUU MD8 Net price PUR
  ORDFLG M*15 Reinstatement [menu 540: 1=No,2=Yes, same Llne,3=Yes, other line,4=Yes, other order]
  ORICRY CRY Destination country -> [TCY]TCY0 =[PND]ORICRY (TABCOUNTRY) !Block
  PJT PJT Project -> [PIM]PIM0 =[PND]PJT (PIMPL) !Block
  PNDLIN L*8 Line
  PNHFCY FCY Return site -> [FCY]FCY0 =[PND]PNHFCY (FACILITY) !Block
  PNHNUM VCR Return no.
  POHFCY FCY Order site -> [FCY]FCY0 =[PND]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPLIN L*8 Line
  POQSEQ L*8 PO sequence no.
  PRIREN PPR Price reason -> [PPR]PPR0 =[PND]PRIREN (PPREASON) !Block
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PND]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Quantity
  RTNDAT D Return date
  RTNDES DES Reason description
  RTNREN SHO Return reason
  SATISS SAT Issue region act:PTX
  SRDLIN L*8 Sales return line
  SRDQTYSTU QTY Sale return qty STK
  SRHNUM VCR Sales return no.
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[PND]STU (TABUNIT) !Block
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UNTWEI WEI Unit weight
  UOM UOM Return unit -> [TUN]TUN0 =[PND]UOM (TABUNIT) !Block
  UOMFLG M*4 Return PAC [menu 1: 1=No,2=Yes]
  UOMPUUCOE COE STK-PUR conversion
  UOMSTUCOE COE STK conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  WEU UOM Weight unit -> [TUN]TUN0 =[PND]WEU (TABUNIT) !Block
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## PURTRS (PTR) - Entered purchase transactions
Notes: differs in V9.0 P12 (diff: AT3_PURTRS.htm); differs in V10 P1 (diff: ATD_PURTRS.htm)
Keys (first = PK; D = duplicates allowed): PTR0 PTRTYP+PTRNUM; PTR1 PTRNUM+PTRTYP
Fields:
  ACCCOD M*15 General account [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ACCSCR M*18 General account [menu 99: 1=Form and table,2=Form,3=Table]
  ACSCOD ACS Access code -> [ACS]ACS0 =[PTR]ACSCOD (ACCCOD) !Block
  ADDCOD M*15 Address [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ADDSCR M*18 Address [menu 99: 1=Form and table,2=Form,3=Table]
  APPFLG M*4 Signed [menu 1: 1=No,2=Yes]
  APPSCR M*18 Signed [menu 99: 1=Form and table,2=Form,3=Table]
  AUUID AUUID Single identifier
  AVSTOCOD1 M*15 Available stock [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AVSTOSCR1 M*15 Available stock [menu 99: 1=Form and table,2=Form,3=Table]
  BPRDATCOD M*15 Supplier inv date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPRSACCOD M*15 Control [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPRVCRCOD M*15 Supplier inv no. [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSCOD M*15(3) Supplier [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSLOTCOD M*15(2) Supplier lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSLOTFLG M*4 Supplier lot [menu 1: 1=No,2=Yes]
  BPSLOTSCR M*18(2) Supplier lot [menu 99: 1=Form and table,2=Form,3=Table]
  BPSLOTSCR1 M*18 Supplier lot [menu 99: 1=Form and table,2=Form,3=Table]
  BPSNDEFLG M*4 Supplier packing slip [menu 1: 1=No,2=Yes]
  BPSNDESCR M*18 Supplier packing slip [menu 99: 1=Form and table,2=Form,3=Table]
  BPSSCR M*18(3) Supplier [menu 99: 1=Form and table,2=Form,3=Table]
  BPTCOD M*15 Carrier [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BUYCOD M*15 Buyer [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BUYFLG M*4 Buyer [menu 1: 1=No,2=Yes]
  CCEDEF CDE Default dimension -> [CDE]CDE0 =CCEDEF;[V]GSUPCLE (CACCEDEF) !Block
  CLEBUT M*4 Close [menu 1: 1=No,2=Yes]
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CLESCR M*18 Closed [menu 99: 1=Form and table,2=Form,3=Table]
  CONSMAT M*15 Material consumption [menu 354: 1=For expected quantity on first track,2=By quantity produced (limited),3=By quantity produced (unlimited)]
  CONTINFOCOD M*15 Containers [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CPRCOD M*15 Stock cost [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CPRCOECOD M*15 LC coefficient [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CPRCOESCR M*18 LC coef [menu 99: 1=Form and table,2=Form,3=Table]
  CPRSCR M*18 Stock cost [menu 99: 1=Form and table,2=Form,3=Table]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTCOD M*15 Cost [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CSTMAJCOD M*15 New cost [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CSTMAJSCR M*15 New cost [menu 99: 1=Form and table,2=Form,3=Table]
  CSTPURCOD M*15 Purchase cost [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CSTPURSCR M*18 Purchase cost [menu 99: 1=Form and table,2=Form,3=Table]
  CURCOD M*15 Currency [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DAS2COD M*15 Fees declaration [menu 35: 1=Entered,2=Displayed,3=Hidden] act:FEE
  DEPCOD M*15 Settlement discount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DESAXX AX3 Description
  DESCOD M*15 Comments [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DIFPRIFLG M*4 Cost difference [menu 1: 1=No,2=Yes]
  DIFPRISCR M*18 Cost difference [menu 99: 1=Form and table,2=Form,3=Table]
  DIFQTYFLG M*4 Quantity difference [menu 1: 1=No,2=Yes]
  DIFQTYSCR M*18 Quantity difference [menu 99: 1=Form and table,2=Form,3=Table]
  DISCRGCOD M*15 Disc/charge values [menu 35: 1=Entered,2=Displayed,3=Hidden] act:PPR
  DISCRGSCR M*18 Disc/charge values [menu 99: 1=Form and table,2=Form,3=Table] act:PPR
  DOCFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  DOCNAM ARP Document -> [ARP]ARP0 =[PTR]DOCNAM (AREPORT) !Block
  ECCCOD M*15 Major version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCCODMIN M*15 Minor version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCFLG M*4 Version [menu 1: 1=No,2=Yes] act:ECC
  ECCSCR M*15 Major version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  ECCSCRMIN M*15 Minor version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  EECICTCOD M*15 Incoterm [menu 35: 1=Entered,2=Displayed,3=Hidden]
  EECINCCOD M*15 Intrastat increase [menu 35: 1=Entered,2=Displayed,3=Hidden] act:DEB
  EECINCSCR M*18 Intrastat increase [menu 99: 1=Form and table,2=Form,3=Table] act:DEB
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENTCOD GAU Automatic journal -> [GAU]GAU0 =[PTR]ENTCOD (GAUTACE) !Block
  ENTCODS GAU Automatic journal -> [GAU]GAU0 =[PTR]ENTCODS (GAUTACE) !Other
  EXPNUM L*8 Export number
  EXTQTYCOD M*15 Planned quantity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  FCSCODCOD M*15 Cost [menu 35: 1=Entered,2=Displayed,3=Hidden]
  FCSCODSCR M*15 Cost [menu 99: 1=Form and table,2=Form,3=Table]
  FUPDATFLG M*4 Reminder date [menu 1: 1=No,2=Yes]
  FUPDATSCR M*18 Reminder date [menu 99: 1=Form and table,2=Form,3=Table]
  FUPFLG M*4 No. of reminders [menu 1: 1=No,2=Yes]
  FUPSCR M*18 Reminders [menu 99: 1=Form and table,2=Form,3=Table]
  GENBUT M*4 Generation [menu 1: 1=No,2=Yes]
  GFY AGF Group -> [AGF]AGF0 =[PTR]GFY (AGRPFCY) !Block
  GPGCODCOD M*15 Grouping code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  GROPRICOD M*15 Gross price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  GROPRISCR M*18 Gross price [menu 99: 1=Form and table,2=Form,3=Table]
  IDECOD01 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD02 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD1 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD2 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDESCR01 M*15 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR02 M*15 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR1 M*18 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR2 M*18 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  INVDTACOD M*15 Invoicing elements [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVFCYCOD M*15 Invoicing site [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVREFCOD M*15 Internal reference [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ITMDESCOD M*15(2) Descriptions [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ITMDESSCR M*18(2) Descriptions [menu 99: 1=Form and table,2=Form,3=Table]
  LEDTYPCOD M*15(20) Ledger type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LEDTYPSCR M*18 Ledger type [menu 99: 1=Form and table,2=Form,3=Table]
  LEDTYPSRT C*4(20) Sort by ledger type
  LINAMTFLG M*4 Line amount - tax [menu 1: 1=No,2=Yes]
  LINAMTSCR M*18 Line amount - tax [menu 99: 1=Form and table,2=Form,3=Table]
  LININVFLG M*4 Invoiced line [menu 1: 1=No,2=Yes]
  LININVSCR M*18 Invoiced line [menu 99: 1=Form and table,2=Form,3=Table]
  LINTYPFLG M*4 Line type [menu 1: 1=No,2=Yes]
  LINTYPSCR M*18 Line type [menu 99: 1=Form and table,2=Form,3=Table]
  LOCCOD M*15 Location [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOCSCR M*18 Location [menu 99: 1=Form and table,2=Form,3=Table]
  LOTCOD M*15 Lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOTFLG M*4 Lot [menu 1: 1=No,2=Yes]
  LOTSCR M*18 Lot [menu 99: 1=Form and table,2=Form,3=Table]
  MATFLG M*4 Matching tolerance [menu 1: 1=No,2=Yes]
  MATSCR M*18 Tolerance code [menu 99: 1=Form and table,2=Form,3=Table]
  MATTOLCOD M*15 Matching tolerance [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MATTOLSCR M*18 Matching tolerance [menu 99: 1=Form and table,2=Form,3=Table]
  MATTYPCOD M*15 Tolerance code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MATTYPSCR M*18 Tolerance code [menu 99: 1=Form and table,2=Form,3=Table]
  MCCIMPMOD M*15 Provisional cost [menu 2366: 1=No,2=Report,3=Trace,4=Report and trace]
  MDLCOD M*15 Delivery mode [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MFGFCYCOD M*15 Production site [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MFGNUMFLG M*4 Work order [menu 1: 1=No,2=Yes]
  MFGNUMSCR M*18 Work order no. [menu 99: 1=Form and table,2=Form,3=Table]
  MODALL M*15 Allocation method [menu 398: 1=Manual,2=Automatic (global),3=Automatic (detailed)]
  MVTDESCOD M*15(2) Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESSCR M*18 Movement description [menu 99: 1=Form and table,2=Form,3=Table]
  MVTPRICOD M*15(2) Movement price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTPRISCR M*18 Movement price [menu 99: 1=Form and table,2=Form,3=Table]
  NBRCOL C*2 No. of fixed columns
  NBSLOFLG M*4 Sub-lot no. [menu 1: 1=No,2=Yes]
  NPRFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  NPRNAM ARP Document -> [ARP]ARP0 =[PTR]NPRNAM (AREPORT) !Block
  OCNDATCOD M*15 Acknowledgment date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  OCNDATFLG M*4 Acknowledgment date [menu 1: 1=No,2=Yes]
  OCNDATSCR M*18 Ack. date [menu 99: 1=Form and table,2=Form,3=Table]
  OCNNUMCOD M*15 Acknowledgement ID [menu 35: 1=Entered,2=Displayed,3=Hidden]
  OCNNUMFLG M*4 Acknowledgement ID [menu 1: 1=No,2=Yes]
  OCNNUMSCR M*18 Ack. ID [menu 99: 1=Form and table,2=Form,3=Table]
  OCNREMCOD M*15 Ack. notes [menu 35: 1=Entered,2=Displayed,3=Hidden]
  OPEENDCOD M*15 End date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  OPESTRCOD M*15 Start date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDDATCOD M*15 Order date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDDATSCR M*18 Order date [menu 99: 1=Form and table,2=Form,3=Table]
  ORDFREFRTCOD M*15 Free freight threshold [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDMAXAMTCOD M*15 Maximum order [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDREFCOD M*15 Internal reference [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDVOLCOD M*15 Order volume total [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDWEICOD M*15 Order weight total [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORICRYCOD M*15 Country of origin [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORICRYSCR M*18 Country of origin [menu 99: 1=Form and table,2=Form,3=Table]
  ORIFLG M*4 Request source [menu 1: 1=No,2=Yes]
  ORISCR M*18 Request source [menu 99: 1=Form and table,2=Form,3=Table]
  PICRETFLG M*4 Requirement considered [menu 1: 1=No,2=Yes]
  PIOCOD M*15 Priority [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PJTCOD M*15 Project [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PJTHCOD M*15 Header project [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PJTSCR M*18 Project [menu 99: 1=Form and table,2=Form,3=Table]
  PLICOD M*15 Price list code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  POHFCYCOD M*15 Order site [menu 35: 1=Entered,2=Displayed,3=Hidden]
  POHFCYSCR M*18 Order site [menu 99: 1=Form and table,2=Form,3=Table]
  POHNLCOD M*15 Order no. and line [menu 35: 1=Entered,2=Displayed,3=Hidden]
  POHNLFLG M*4 Start/end ln [menu 556: 1=Start of line,2=End of line,3=According to reference product]
  POHNLSCR M*18 Order no. and line [menu 99: 1=Form and table,2=Form,3=Table]
  POHNUMFLG M*4 Purchase order [menu 1: 1=No,2=Yes]
  POHNUMSCR M*18 Purchase order [menu 99: 1=Form and table,2=Form,3=Table]
  PORTVACOD M*15 Portuguese VAT [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PORTVASCR M*15 Portuguese VAT [menu 99: 1=Form and table,2=Form,3=Table]
  PRICOD M*15 Net price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PRIFLG M*4 Net price [menu 1: 1=No,2=Yes]
  PRISCR M*18 Net price [menu 99: 1=Form and table,2=Form,3=Table]
  PRNCOD1 M*15 Printing [menu 708: 1=No print,2=Labels,3=.,4=Transfer document,5=Analysis document]
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PRNNBFLG1 M*4 No. prints [menu 1: 1=No,2=Yes]
  PRNNBSCR1 M*15 No. prints [menu 99: 1=Form and table,2=Form,3=Table]
  PRNSCR M*18 Printed [menu 99: 1=Form and table,2=Form,3=Table]
  PRNSCR1 M*15 Printing [menu 99: 1=Form and table,2=Form,3=Table]
  PSHFLG M*4 Request [menu 1: 1=No,2=Yes]
  PSHSCR M*18 Request [menu 99: 1=Form and table,2=Form,3=Table]
  PTECOD M*15 Payment term [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PTRDES A*35 Description
  PTRNUM TRS Transaction
  PTRTYP M*20 Transaction type [menu 517: 1=RFQ,2=Purchase request,3=Standard order,4=Subcontract order,5=Open order,6=Receipt,7=Return,8=Invoice/Credit note,9=Subcontract order (EO)]
  PTRTYPCAR A*2 Alpha no.
  PURTYPCOD M*15 Purchase type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PURTYPSCR M*18 Purchase type [menu 99: 1=Form and table,2=Form,3=Table]
  PUUFLG M*4 Purchase unit [menu 1: 1=No,2=Yes]
  PUUSCR M*18 Purchase unit [menu 99: 1=Form and table,2=Form,3=Table]
  QRQBUT M*4 RFQs [menu 1: 1=No,2=Yes]
  QTYPICFLG M*4 Selected quantity [menu 1: 1=No,2=Yes]
  QTYPICSCR M*18 Selected qty [menu 99: 1=Form and table,2=Form,3=Table]
  QTYPUUCOD M*20 PUR quantity [menu 514: 1=Entered with unit,2=Entered without unit,3=Displayed,4=Hidden]
  QTYSTUCOD M*15 STK quantity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  QTYSTUSCR M*18 STK quantity [menu 99: 1=Form and table,2=Form,3=Table]
  QTYUOMCOD M*20 Ordered qty. [menu 514: 1=Entered with unit,2=Entered without unit,3=Displayed,4=Hidden]
  QTYVOUCOD M*15 Volume [menu 35: 1=Entered,2=Displayed,3=Hidden]
  QTYVOUSCR M*18 Volume [menu 99: 1=Form and table,2=Form,3=Table]
  QTYWEUCOD M*15 Weight [menu 35: 1=Entered,2=Displayed,3=Hidden]
  QTYWEUSCR M*18 Weight [menu 99: 1=Form and table,2=Form,3=Table]
  QUAFLG M*4 QC management [menu 1: 1=No,2=Yes]
  QUAFLGCOD M*15 QC code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  QUAFLGSCR M*18 QC code [menu 99: 1=Form and table,2=Form,3=Table]
  QUASCR M*18 QC management [menu 99: 1=Form and table,2=Form,3=Table]
  RATCURCOD M*15 Currency rate [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RCPADDCOD M*15 Receipt address [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RCPADDSCR M*18 Receipt address [menu 99: 1=Form and table,2=Form,3=Table]
  RCPDAT1COD M*15 Receipt date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RCPFCYCOD M*15 Receiving site [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RCPFCYSCR M*18 Receiving site [menu 99: 1=Form and table,2=Form,3=Table]
  REACSTPURCOD M*15 Actual purchase cost [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REACSTPURSCR M*18 Actual purchase cost [menu 99: 1=Form and table,2=Form,3=Table]
  REFORICOD M*15 Original document ref [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REFORIPOS M*18 Position on line [menu 556: 1=Start of line,2=End of line,3=According to reference product]
  REFORISCR M*18 Original document ref [menu 99: 1=Form and table,2=Form,3=Table]
  REQCOD M*15 Requester [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REVFLG M*4 Revision no. [menu 1: 1=No,2=Yes]
  REVSCR M*18 Revision no. [menu 99: 1=Form and table,2=Form,3=Table]
  RSPFLG M*4 No. of responses [menu 1: 1=No,2=Yes]
  RSPSCR M*18 Responses [menu 99: 1=Form and table,2=Form,3=Table]
  SCOADDCOD M*15 Subcontract address [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SCOADDSCR M*18 Subcon. address [menu 99: 1=Form and table,2=Form,3=Table]
  SCOLTICOD M*15 Subcontract LT [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SCOSTA M*15 Authorized statuses [menu 370: 1=Planned,2=Firm,3=By selection]
  SERCOD M*15 Starting serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD M*15(2) Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERESCR M*18(2) Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERESCR1 M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERSCR M*18 Starting serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SLOCOD M*15 Sublot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SLOSCR M*18 Sublot [menu 99: 1=Form and table,2=Form,3=Table]
  SOHNUMFLG M*4 Sales order [menu 1: 1=No,2=Yes]
  SOHNUMSCR M*18 Sales order [menu 99: 1=Form and table,2=Form,3=Table]
  SPERFLG M*4 Expiration [menu 1: 1=No,2=Yes]
  SPOTFLG M*4 Potency [menu 1: 1=No,2=Yes]
  SPTVACOD M*15 VAT Spain [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SRGWAIFLG M*4 Receipt at dock [menu 1: 1=No,2=Yes]
  SRUB1FLG M*4 Heading 1 [menu 1: 1=No,2=Yes]
  SRUB2FLG M*4 Section 2 [menu 1: 1=No,2=Yes]
  SRUB3FLG M*4 Section 3 [menu 1: 1=No,2=Yes]
  SRUB4FLG M*4 Section 4 [menu 1: 1=No,2=Yes]
  STACOD M*15 Status [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STAFLG M*4 Document status [menu 1: 1=No,2=Yes]
  STASCR M*18 Status [menu 99: 1=Form and table,2=Form,3=Table]
  STCNUMCOD M*15 Cost structure [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STCNUMSCR M*18 Cost structure [menu 99: 1=Form and table,2=Form,3=Table]
  STKFLG M*4 Automatic issue [menu 1: 1=No,2=Yes]
  STOCODMAN M*4 Manual only [menu 1: 1=No,2=Yes]
  STOFCYCOD M*15(2) Shipment site [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STOFCYSCR M*18 Shipment site [menu 99: 1=Form and table,2=Form,3=Table]
  STRDATCOD M*15 Due date basis [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SVCDATCOD M*15(2) Benefit period [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SVCDATSCR M*15(2) Benefit period [menu 99: 1=Form and table,2=Form,3=Table]
  TECFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  TECNAM ARP Document -> [ARP]ARP0 =[PTR]TECNAM (AREPORT) !Block
  TRSAUTO M*4 Automtc. transaction [menu 1: 1=No,2=Yes]
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Block
  TRSCODS ADI Movement code -> [ADI]CODE =14;TRSCODS (ATABDIV) !Other
  TRSFAMCOD M*15 Stock movement group [menu 35: 1=Entered,2=Displayed,3=Hidden]
  TRSFAMDEF ADI Transaction group -> [ADI]CODE =9;TRSFAMDEF (ATABDIV) !Block
  TRSFAMS ADI Transaction group -> [ADI]CODE =9;TRSFAMS (ATABDIV) !Other
  TRSFAMSCR M*18 Stock movement group [menu 99: 1=Form and table,2=Form,3=Table]
  UNTWEICOD M*15 Unit weight [menu 35: 1=Entered,2=Displayed,3=Hidden]
  UNTWEISCR M*18 Unit weight [menu 99: 1=Form and table,2=Form,3=Table]
  UOMCOECOD M*15 Coefficient [menu 35: 1=Entered,2=Displayed,3=Hidden]
  UOMCOESCR M*18 Coefficient [menu 99: 1=Form and table,2=Form,3=Table]
  UOMSAIFLG M*4 UOM entry [menu 1: 1=No,2=Yes]
  UOMSAIFLG1 M*4 Enter PAC [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLCCOD M*15 Location reference [menu 35: 1=Entered,2=Displayed,3=Hidden]
  USEPLCSCR M*18 Location reference [menu 99: 1=Form and table,2=Form,3=Table]
  VACBPRCOD M*15 Tax rule [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VATCOD M*15(7) Tax codes [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VATSCR M*18(7) Tax codes [menu 99: 1=Form and table,2=Form,3=Table]
  VLTFDRCOD M*15 Valuation tab [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHCOD M*15 Warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHCOD1 M*15 Line warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHOBY M*15 Single warehouse [menu 1: 1=No,2=Yes]
  WRHSCR M*15 Warehouse [menu 99: 1=Form and table,2=Form,3=Table]
  WRHSCR1 M*15 Line warehouse [menu 99: 1=Form and table,2=Form,3=Table]

## PVCRFOOT (PVF) - Purchase documents - footer elt
Keys (first = PK; D = duplicates allowed): PVF0 VCRNUM+VCRTYP+IND; PVF1 VCRTYP+VCRNUM+IND; PVF2 NUM+VCRTYP+VCRNUM+IND
Fields:
  AMTCOD M*10 Amount code [menu 269: 1=Percent,2=Amount]
  AMTCODLIB A*10 Amount description
  AUUID AUUID Single identifier
  CLCBAS M*15 Calculation basis [menu 537: 1=None,2=Exclude tax amount,3=Include tax amount,4=Action]
  CLCORD C*3 Calculation order
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEBCDT M*6 Debit/Credit [menu 626: 1=Debit,2=Credit]
  DEPFLG M*4 Subject to discount [menu 1: 1=No,2=Yes]
  DISVATFLG M*4 Rebate on VAT [menu 1: 1=No,2=Yes]
  DTAAMTTAX MD1 Tax amount
  DTADEDTAX MD1 Deductible tax
  DTADEP MD1 Discount amount
  DTADISBAS MD1 Rebate tax basis
  EXPNUM L*8 Export number
  FORMAT A*15 Format
  INCDCR M*10 Increase/Decrease [menu 254: 1=Increase,2=Decrease]
  IND L*8 Index
  INVCPLAMT MD1 Invoiced amt.
  INVDTA PFI Invoicing element -> [PFI]PFI0 =[PVF]INVDTA (PFOOTINV) !Block
  INVDTAAMT MD1 Entry element amount
  INVDTAFLG M*4 Addition indicator [menu 1: 1=No,2=Yes]
  INVDTAVAT VAT Tax -> [TVT]TVT0 =INVDTAVAT;[V]GSUPCLE (TABVAT) !Block
  INVLINAMT MD1 Line element amount
  INVLINFLG C*1 Presence on line
  INVORDAMT MD1 Calculated element amount
  INVORDFLG M*4 Presence on order [menu 1: 1=No,2=Yes]
  NUM PIH Invoice number -> [PIH]PIH0 =[PVF]NUM (PINVOICE) !Other
  POHNUM VCR Order number
  PTHNUM VCR Receipt number
  RCPCPLAMT MD1 Received mvt
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRNUM VCR Entry
  VCRTYP M*20 Entry type [menu 517: 1=RFQ,2=Purchase request,3=Standard order,4=Subcontract order,5=Open order,6=Receipt,7=Return,8=Invoice/Credit note,9=Subcontract order (EO)]

## PVCRVAT (PVV) - Purchase documents - taxes
Keys (first = PK; D = duplicates allowed): PVV0 VCRNUM+VCRTYP+IND; PVV1 VCRTYP+VCRNUM+IND; PVV2 NUM+VCRTYP+VCRNUM+IND
Fields:
  AMTTAX MD1 Tax amount
  AUUID AUUID Single identifier
  BASDEPATI MD1 Discount basis tax incl.
  BASDEPNOT MD1 Discount basis tax excl.
  BASTAX MD1 Tax basis
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DEDRAT DCB*3.6 Deductible %
  DEDTAX MD1 Deductible tax
  DISBAS MD1 Rebate tax basis
  EXPNUM L*8 Export number
  IND L*8 Index
  NUM PIH Invoice number -> [PIH]PIH0 =[PVV]NUM (PINVOICE) !Other
  POHNUM VCR Order number
  PTHNUM VCR Receipt number
  PURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  TAX VAT Taxes -> [TVT]TVT0 =TAX;[V]GSUPCLE (TABVAT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VATCHA M*4 Subject to tax [menu 1: 1=No,2=Yes]
  VATGRO MD1 Gross basis
  VATRAT DCB*3.6 Rate
  VATSUPAMT MD1 Extra tax amount
  VATTYP M*15 Tax type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]
  VCRNUM VCR Entry
  VCRTYP M*20 Entry type [menu 517: 1=RFQ,2=Purchase request,3=Standard order,4=Subcontract order,5=Open order,6=Receipt,7=Return,8=Invoice/Credit note,9=Subcontract order (EO)]

## PWRKORDERS (PWO) - Requirements considered
Keys (first = PK; D = duplicates allowed): PWO0 PRONUM+CODFNC+LINNUM+WIPTYP+WIPNUM+PSDLIN
Fields:
  AUUID AUUID Single identifier
  CODFNC A*3 Function code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PWO]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[PWO]ITMREF (ITMMASTER) !Other
  LINNUM L*8 Line number
  PRONUM L*8 Process number
  PSDLIN L*8 Line
  PUU UOM Purchase unit -> [TUN]TUN0 =[PWO]PUU (TABUNIT) !Other
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  STU UOM Stock unit -> [TUN]TUN0 =[PWO]STU (TABUNIT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PWO]UPDUSR (AUTILIS) !Other
  WIPNUM VCR Order no.
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]

## PWRKPND (PWR) - Return line detail temporary
Notes: differs in V9.0 P12 (diff: AT3_PWRKPND.htm); differs in V10 P1 (diff: ATD_PWRKPND.htm)
Keys (first = PK; D = duplicates allowed): PWR0 PRONUM+PNHNUM+PNDLIN
Fields:
  ACCANA GAC Analytical account -> [GAC]GAC0 =COAANA;ACCANA (GACCOUNT) !Other
  AMTCUR MD1 Amount in currency
  AMTLED MD1 Analytical curr amt
  AMTNOTLIN MD1 Line amount - tax
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AUUID AUUID Single identifier
  BPAINV ADR Billing address
  BPOCRY CRY Shipping country -> [TCY]TCY0 =[PWR]BPOCRY (TABCOUNTRY) !Other
  BPSINV BPS Bill-by BP -> [BPS]BPS0 =[PWR]BPSINV (BPSUPPLIER) !Other
  BPSNDE A*20 Supplier packing slip no.
  BPSNUM BPS Supplier -> [BPS]BPS0 =[PWR]BPSNUM (BPSUPPLIER) !Other
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CEEFLG M*4 EU invoice [menu 1: 1=No,2=Yes]
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  COA COA(10) Chart code -> [COA]COA0 =[PWR]COA (GCOA) !RTZ
  COAANA COA Analytical plan code -> [COA]COA0 =[PWR]COAANA (GCOA) !Other
  CPR MD8 Cost price
  CPRCOE COE Landed cost coef.
  CPRCUR CUR Currency -> [TCU]TCU0 =[PWR]CPRCUR (TABCUR) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PWR]CUR (TABCUR) !Other
  CURLEDANA CUR Analytical currency -> [TCU]TCU0 =[PWR]CURLEDANA (TABCUR) !Other
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DIE DIE Dimension type code -> [DIE]DIE0 =[PWR]DIE (GDIE) !Other act:ANA
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[PWR]DISCRGREN1 (PPREASON) !Other act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[PWR]DISCRGREN2 (PPREASON) !Other act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[PWR]DISCRGREN3 (PPREASON) !Other act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECINCRAT RAT Intrastat increase act:DEB
  GLU UOM Non-financial unit -> [TUN]TUN0 =[PWR]GLU (TABUNIT) !Other
  GROPRI MD8 Gross price
  INVQTYPUU QTY Invoiced PUR
  INVQTYSTU QTY Invoiced STU
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PWR]ITMREF (ITMMASTER) !Other
  LED LED(10) Ledger -> [LED]LED0 =[PWR]LED (GLED) !RTZ
  LINACC GAC(10) Accounts -> [GAC]GAC0 =COA(indice);LINACC(indice) (GACCOUNT) !Other
  LINAMT MD1 Line amount - tax
  LINATIAMT MD1 Line amount + tax
  LINAUTFLG M*4 Automatic flow [menu 1: 1=No,2=Yes]
  LINCAT M*15 Movement category [menu 574: 1=Standard,2=For subcontracting]
  LINEECFLG M*4 Debit line [menu 1: 1=No,2=Yes] act:DEB
  LININVFLG M*4 Invoiced line [menu 1: 1=No,2=Yes]
  LINPRNFLG M*4 Line printed [menu 1: 1=No,2=Yes]
  LINPSTDAT D Reversal date
  LINPSTFLG M*4 Posted line [menu 1: 1=No,2=Yes]
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINSTOFCY FCY Shipment site -> [FCY]FCY0 =[PWR]LINSTOFCY (FACILITY) !Other
  LINTEX TXC Text
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  NETCUR CUR Currency -> [TCU]TCU0 =[PWR]NETCUR (TABCUR) !Other
  NETPRI MD8 Net price
  NETPRIPUU MD8 Net price PUR
  ORDFLG M*15 Reinstatement [menu 540: 1=No,2=Yes, same Llne,3=Yes, other line,4=Yes, other order]
  ORICRY CRY Destination country -> [TCY]TCY0 =[PWR]ORICRY (TABCOUNTRY) !Other
  PJT PJT Project -> [PIM]PIM0 =[PWR]PJT (PIMPL) !Block
  PNDLIN L*8 Line
  PNHFCY FCY Return site -> [FCY]FCY0 =[PWR]PNHFCY (FACILITY) !Other
  PNHNUM VCR Return no.
  POHFCY FCY Order site -> [FCY]FCY0 =[PWR]POHFCY (FACILITY) !Other
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 PO sequence no.
  PRIREN PPR Price reason -> [PPR]PPR0 =[PWR]PRIREN (PPREASON) !Other
  PRONUM L*8 Process number
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PWR]PUU (TABUNIT) !Other
  QTYBUDLIN QTY Qty to be decommitted
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Quantity
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  RTNDAT D Return date
  RTNDES DES Reason description
  RTNREN SHO Return reason
  SRDLIN L*8 Sales return line
  SRDQTYSTU QTY Sale return qty STK
  SRHNUM VCR Return no.
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[PWR]STU (TABUNIT) !Other
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Other act:PTX
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UNTWEI WEI Unit weight
  UOM UOM Return unit -> [TUN]TUN0 =[PWR]UOM (TABUNIT) !Other
  UOMFLG M*4 Return PAC [menu 1: 1=No,2=Yes]
  UOMPUUCOE COE STK-PUR conversion
  UOMSTUCOE COE STK conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change author
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Other
  WEU UOM Weight unit -> [TUN]TUN0 =[PWR]WEU (TABUNIT) !Other

## PWRKPNH (PWE) - Temporary return
Keys (first = PK; D = duplicates allowed): PWE0 PRONUM+PNHNUM; PWE1 PRONUM+CPY+PNHFCY+BPSINV+CUR+PNHNUM
Fields:
  AMTATI MD1 Amount + tax
  AMTNOT MD1 Amount - tax
  AUUID AUUID Single identifier
  AUZNUM A*15 Authorization number
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPAADD ADR Address
  BPAADDLIG ADL(3) Address line
  BPAINV ADR Billing address
  BPAPAY ADR Pay-to BP address
  BPRNAM NAM(2) Company name
  BPRPAY BPR Pay-to -> [BPR]BPR0 =[PWE]BPRPAY (BPARTNER) !Other
  BPSINV BPS Bill-by supplier -> [BPS]BPS0 =[PWE]BPSINV (BPSUPPLIER) !Other
  BPSNUM BPS Supplier -> [BPS]BPS0 =[PWE]BPSNUM (BPSUPPLIER) !Other
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PWE]BPTNUM (BPCARRIER) !Other
  BUY AUS Buyer -> [AUS]CODUSR =[PWE]BUY (AUTILIS) !Other
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CFMFLG M*4 Posted [menu 1: 1=No,2=Yes]
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CPY CPY Company -> [CPY]CPY0 =[PWE]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[PWE]CRY (TABCOUNTRY) !Other
  CRYNAM NCY Country name
  CTY CTY City
  CUR CUR Currency -> [TCU]TCU0 =[PWE]CUR (TABCUR) !Other
  CURLEDANA CUR Analytical currency -> [TCU]TCU0 =[PWE]CURLEDANA (TABCUR) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[PWE]DIE (GDIE) !Other act:ANA
  EECICT ICT Incoterm -> [ICTH]ICT0 =[PWE]EECICT (INCOTERM) !Other
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Other act:DEB
  EECNUM A*20 EU identification act:DEB
  EECNUMDEB C*4 EU Intrastat act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Other act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  ENTCOD GAU Stock auto journal -> [GAU]GAU0 =[PWE]ENTCOD (GAUTACE) !Other
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[PWE]FFWNUM (BPCARRIER) !Other
  ICTCTY CTY Incoterm town
  INVFLG M*15 Invoiced [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  INVLINNBR C*4 No. invoiced lines
  LINNBR C*4 Number of lines
  MDL MDL Delivery mode -> [TMD]TMD0 =[PWE]MDL (TABMODELIV) !Other
  PNHFCY FCY Return site -> [FCY]FCY0 =[PWE]PNHFCY (FACILITY) !Other
  PNHNUM VCR Return no.
  POSCOD POS Postal code
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PRONUM L*8 Process number
  PSTDAT D Reversal date
  PSTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  PSTLINNBR C*4 No. of posted lines
  PURTYP M*15 Purchase type [menu 507: 1=Commercial,2=General]
  REM A*250 Notes
  RTNDAT D Return date
  SAT SAT County
  TEX1 TXC Text
  TEX2 TXC Text
  TOTGROWEI DCB*11.4 Gross weight
  TOTNETWEI DCB*11.4 Net weight
  TOTVOL DCB*11.4 Volume
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Other
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Other act:STS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Other
  VACTYP C*1 Tax rule type
  VOU UOM Volume unit -> [TUN]TUN0 =[PWE]VOU (TABUNIT) !Other
  WEU UOM Weight unit -> [TUN]TUN0 =[PWE]WEU (TABUNIT) !Other

## PWRKPOC (PWC) - Temporary product-contract
Notes: differs in V9.0 P12 (diff: AT3_PWRKPOC.htm); differs in V10 P1 (diff: ATD_PWRKPOC.htm)
Keys (first = PK; D = duplicates allowed): PWC0 PRONUM+POHNUM+POPLIN
Fields:
  AMTVLT MD1 Costing amount
  AUUID AUUID Single identifier
  COA COA(10) Chart code -> [COA]COA0 =[PWC]COA (GCOA) !RTZ
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PWC]CREUSR (AUTILIS) !Other
  DAYDSP C*3(7) Daily distribution
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EECICT2 ICT Incoterm -> [ICTH]ICT0 =[PWC]EECICT2 (INCOTERM) !Other
  EECLOC2 M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNUM2 A*20 EU identification act:DEB
  EXTQTYPUU QTY Expected PUR quantity
  FCYADD ADR Receipt address
  FFWADD2 ADR Forwarding agent address
  FFWNUM2 BPT Freight agent -> [BPT]BPT0 =[PWC]FFWNUM2 (BPCARRIER) !Other
  FIMHOR C*4 Firm horizon
  FIMHORUOM M*15 Firm horizon time un [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  FMTREM A*15(9) Charge/Discount format
  FRTHOR C*4 Planning horizon
  FRTHORUOM M*15 Planning horizon time unit [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  ICTCTY2 CTY Incoterm town
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PWC]ITMREF (ITMMASTER) !Other
  ITMREFBPS A*20 Supplier product
  LINACC GAC(10) Accounts -> [GAC]GAC0 =COA(indice);LINACC(indice) (GACCOUNT) !Other
  LINCREFLG C*1 Creation flag
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINSTOFCY FCY Shipment site -> [FCY]FCY0 =[PWC]LINSTOFCY (FACILITY) !Other
  LINTEX TXC Text
  PJT PJT Project -> [PIM]PIM0 =[PWC]PJT (PIMPL) !Block
  PLI PLI Price list code
  POHNUM VCR Order no.
  POPLIN L*8 Line
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[PWC]PRHFCY (FACILITY) !Other
  PRIVLT MD8 Costing price
  PRONUM L*8 Process number
  PUU UOM Purchase unit -> [TUN]TUN0 =[PWC]PUU (TABUNIT) !Other
  STCNUM VCR Cost structure
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Other act:PTX
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PWC]UPDUSR (AUTILIS) !Other
  USEPLC A*30 Location reference
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Other
  WCURVLT CUR Currency -> [TCU]TCU0 =[PWC]WCURVLT (TABCUR) !Other
  WEEDSP C*3(5) Weekly distribution
  XENDDAT D Valid to
  XONUM C*2(50) Indentify cancel
  XPUUFLG M*4 Flag for modifying PUU [menu 1: 1=No,2=Yes]
  XSTRDAT D Valid from

## PWRKPOP (PWP) - Temporary product-contract
Notes: differs in V9.0 P12 (diff: AT3_PWRKPOP.htm); differs in V10 P1 (diff: ATD_PWRKPOP.htm)
Keys (first = PK; D = duplicates allowed): PWP0 PRONUM+POHNUM+POPLIN+POPSEQ
Fields:
  AUUID AUUID Single identifier
  CCE1 CCE Analytical dimension 1 -> [CCE]CCE0 =[V]GDIE(1);CCE1 (CACCE) !Other
  CCE10 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(10);CCE10 (CACCE) !Other
  CCE11 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(11);CCE11 (CACCE) !Other
  CCE12 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(12);CCE12 (CACCE) !Other
  CCE13 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(13);CCE13 (CACCE) !Other
  CCE14 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(14);CCE14 (CACCE) !Other
  CCE15 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(15);CCE15 (CACCE) !Other
  CCE16 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(16);CCE16 (CACCE) !Other
  CCE17 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(17);CCE17 (CACCE) !Other
  CCE18 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(18);CCE18 (CACCE) !Other
  CCE19 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(19);CCE19 (CACCE) !Other
  CCE2 CCE Analytical dimension 2 -> [CCE]CCE0 =[V]GDIE(2);CCE2 (CACCE) !Other
  CCE20 CCE Analytical dimension -> [CCE]CCE0 =[V]GDIE(20);CCE20 (CACCE) !Other
  CCE3 CCE Analytical dimension 3 -> [CCE]CCE0 =[V]GDIE(3);CCE3 (CACCE) !Other
  CCE4 CCE Analytical dimension 4 -> [CCE]CCE0 =[V]GDIE(4);CCE4 (CACCE) !Other
  CCE5 CCE Analytical dimension 5 -> [CCE]CCE0 =[V]GDIE(5);CCE5 (CACCE) !Other
  CCE6 CCE Analytical dimension 6 -> [CCE]CCE0 =[V]GDIE(6);CCE6 (CACCE) !Other
  CCE7 CCE Analytical dimension 7 -> [CCE]CCE0 =[V]GDIE(7);CCE7 (CACCE) !Other
  CCE8 CCE Analytical dimension 8 -> [CCE]CCE0 =[V]GDIE(8);CCE8 (CACCE) !Other
  CCE9 CCE Analytical dimension 9 -> [CCE]CCE0 =[V]GDIE(9);CCE9 (CACCE) !Other
  CREDATTIM ADATIM Date time
  CREFLG C*4 Creation flag
  CREUSR AUS User -> [AUS]CODUSR =[PWP]CREUSR (AUTILIS) !Other
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[PWP]DISCRGREN1 (PPREASON) !Other act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[PWP]DISCRGREN2 (PPREASON) !Other act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[PWP]DISCRGREN3 (PPREASON) !Other act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECINCRAT RAT Intrastat increase act:DEB
  GROPRI MD8 Gross price
  NETPRI MD8 Net price
  ORICRY CRY Country of origin -> [TCY]TCY0 =[PWP]ORICRY (TABCOUNTRY) !Other
  PJT PJT Project -> [PIM]PIM0 =[PWP]PJT (PIMPL) !Other
  POHNUM VCR Order no.
  POPCREFLG M*4 Creation flag [menu 1: 1=No,2=Yes]
  POPDAT D Application end date
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  POPSTRDAT D Price effectivity date
  PRIFLG M*4 Price search flag [menu 1: 1=No,2=Yes]
  PRIREN PPR Price reason -> [PPR]PPR0 =[PWP]PRIREN (PPREASON) !Other
  PRONUM L*8 Process number
  QUAFLG M*4 QC management [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDFLG C*4 Update flag
  UPDUSR AUS User -> [AUS]CODUSR =[PWP]UPDUSR (AUTILIS) !Other

## PWRKPOQ (PWQ) - Temporary order detail
Keys (first = PK; D = duplicates allowed): PWQ0 TYPORI+POHNUM+POPLIN+POQSEQ
Fields:
  AUUID AUUID Single identifier
  CMMQTYPUU QTY Qty commited
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PWQ]CREUSR (AUTILIS) !Other
  EXTOURNE D Reversal date
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Sequence number
  TMPQTYPUU QTY Temporary qty
  TYPORI C*1 Line origin
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PWQ]UPDUSR (AUTILIS) !Other

## PWRKPQF (PWF) - RFQ ADR supplier temporary
Keys (first = PK; D = duplicates allowed): PWF0 PRONUM+BPSNUM
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPAADDLIG ADL(3) Address line
  BPRNAM NAM(2) Company name
  BPSNUM BPS Supplier -> [BPS]BPS0 =[PWF]BPSNUM (BPSUPPLIER) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[PWF]CRY (TABCOUNTRY) !Other
  CRYNAM NCY Country name
  CTY CTY City
  POSCOD POS Postal code
  PRONUM L*8 Process number
  SAT SAT County
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## PWRKPTD (PWD) - Temporary detail receipt
Notes: differs in V9.0 P12 (diff: AT3_PWRKPTD.htm); differs in V10 P1 (diff: ATD_PWRKPTD.htm)
Keys (first = PK; D = duplicates allowed): PWD0 PRONUM+PTHNUM+PTDLIN
Fields:
  ACCANA GAC Analytical account -> [GAC]GAC0 =COAANA;ACCANA (GACCOUNT) !Other
  AMTCUR MD1 Amount in currency
  AMTLED MD1 Analytical curr amt
  AMTNOTLIN MD1 Line amount - tax
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AUUID AUUID Single identifier
  BASTAXLIN1 MD1 Tax basis 1
  BPOCRY CRY Shipping country -> [TCY]TCY0 =[PWD]BPOCRY (TABCOUNTRY) !Other
  BPSINV BPS Bill-by supplier -> [BPS]BPS0 =[PWD]BPSINV (BPSUPPLIER) !Other
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CEEFLG M*4 EU invoice [menu 1: 1=No,2=Yes]
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  COA COA(10) Chart code -> [COA]COA0 =[PWD]COA (GCOA) !RTZ
  COAANA COA Analytical plan code -> [COA]COA0 =[PWD]COAANA (GCOA) !Other
  CPR MD8 Production cost PUR
  CPRCOE COE Landed cost coef.
  CPRCUR CUR Currency -> [TCU]TCU0 =[PWD]CPRCUR (TABCUR) !Other
  CPRPRI MD8 Production cost PUR
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PWD]CUR (TABCUR) !Other
  CURLEDANA CUR Analytical currency -> [TCU]TCU0 =[PWD]CURLEDANA (TABCUR) !Other
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DIE DIE Dimension type code -> [DIE]DIE0 =[PWD]DIE (GDIE) !Other act:ANA
  DISCRGAMT1 MD1 Discount/Charge 1
  DISCRGAMT2 MD1 Discount/Charge 2
  DISCRGAMT3 MD1 Discount/Charge 3
  DISCRGAMT4 MD1 Discount/Charge 4
  DISCRGAMT5 MD1 Discount/Charge 5
  DISCRGAMT6 MD1 Discount/Charge 6
  DISCRGAMT7 MD1 Discount/Charge 7
  DISCRGAMT8 MD1 Discount/Charge 8
  DISCRGAMT9 MD1 Discount/Charge 9
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[PWD]DISCRGREN1 (PPREASON) !Other act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[PWD]DISCRGREN2 (PPREASON) !Other act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[PWD]DISCRGREN3 (PPREASON) !Other act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECINCRAT RAT Intrastat increase act:DEB
  GLU UOM Non-financial unit -> [TUN]TUN0 =[PWD]GLU (TABUNIT) !Other
  GROPRI MD8 Gross price
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[PWD]ITMREF (ITMMASTER) !Other
  LED LED(10) Ledger -> [LED]LED0 =[PWD]LED (GLED) !RTZ
  LINACC GAC(10) Accounts -> [GAC]GAC0 =COA(indice);LINACC(indice) (GACCOUNT) !Other
  LINAMT MD1 Line amount - tax
  LINATIAMT MD1 Line amount + tax
  LINCAT M*15 Movement category [menu 574: 1=Standard,2=For subcontracting]
  LINEECFLG M*4 Debit line [menu 1: 1=No,2=Yes] act:DEB
  LININVFLG M*4 Invoiced line [menu 1: 1=No,2=Yes]
  LINPRNFLG M*4 Line printed [menu 1: 1=No,2=Yes]
  LINPSTFLG M*4 Posted line [menu 1: 1=No,2=Yes]
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  NETCUR CUR Currency -> [TCU]TCU0 =[PWD]NETCUR (TABCUR) !Other
  NETPRI MD8 Net price
  NETPRIPUU MD8 Net price PUR
  ORICRY CRY Country of origin -> [TCY]TCY0 =[PWD]ORICRY (TABCOUNTRY) !Other
  PJT PJT Project -> [PIM]PIM0 =[PWD]PJT (PIMPL) !Block
  POHFCY FCY Order site -> [FCY]FCY0 =[PWD]POHFCY (FACILITY) !Other
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPLIN L*8 Order line
  POPSEQ L*8 Sequence
  POQSEQ L*8 Order seq no.
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[PWD]PRHFCY (FACILITY) !Other
  PRIREN PPR Price reason -> [PPR]PPR0 =[PWD]PRIREN (PPREASON) !Other
  PRONUM L*8 Process number
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[PWD]PUU (TABUNIT) !Other
  QTYBUDLIN QTY Qty to be decommitted
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYVOU QTY Volume
  QTYWEU QTY Weight
  QUAFLG M*4 QC management [menu 1: 1=No,2=Yes]
  QUARTNFLG M*4 Return from QC [menu 1: 1=No,2=Yes]
  RATDIV RCU(10) Dividing rate
  RATMLT RCU(10) Multiplying rate
  RCPDAT D Receipt date
  RRRQTYPUU QTY Quantity R PUR
  RRRQTYSTU QTY Quantity R STK
  RTNQTYPUU QTY Returned PUR qty.
  RTNQTYSTU QTY Returned STK qty.
  SATISS SAT Issue region act:PTX
  STU UOM Stock unit -> [TUN]TUN0 =[PWD]STU (TABUNIT) !Other
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Other act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Other act:PTX
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Other

## PWRKPTH (PWH) - Temporary receipt
Keys (first = PK; D = duplicates allowed): PWH0 PRONUM+PTHNUM; PWH1 PRONUM+CPY+PRHFCY+BPSINV+CUR+PTHNUM
Fields:
  AMTATI MD1 Amount + tax
  AMTNOT MD1 Amount - tax
  AUUID AUUID Single identifier
  BPAADD ADR Address
  BPAINV ADR Billing address
  BPAPAY ADR Pay-to BP address
  BPRPAY BPR Pay-to -> [BPR]BPR0 =[PWH]BPRPAY (BPARTNER) !Other
  BPSINV BPS Bill-by supplier -> [BPS]BPS0 =[PWH]BPSINV (BPSUPPLIER) !Other
  BPSNDE A*20 Supplier packing slip no.
  BPSNUM BPS Supplier -> [BPS]BPS0 =[PWH]BPSNUM (BPSUPPLIER) !Other
  BPTNUM BPT Carrier -> [BPT]BPT0 =[PWH]BPTNUM (BPCARRIER) !Other
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Other act:ANA
  CHGCOE RCU Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CPY CPY Company -> [CPY]CPY0 =[PWH]CPY (COMPANY) !Delete
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[PWH]CUR (TABCUR) !Other
  CURLEDANA CUR Analytical currency -> [TCU]TCU0 =[PWH]CURLEDANA (TABCUR) !Other
  DIE DIE Dimension type code -> [DIE]DIE0 =[PWH]DIE (GDIE) !Other act:ANA
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[PWH]DSPVOU (TABUNIT) !Other
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[PWH]DSPWEU (TABUNIT) !Other
  EECICT ICT Incoterm -> [ICTH]ICT0 =[PWH]EECICT (INCOTERM) !Other
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Other act:DEB
  EECNUM A*20 EU identification act:DEB
  EECNUMDEB C*4 EU Intrastat act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Other act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[PWH]FFWNUM (BPCARRIER) !Other
  ICTCTY CTY Incoterm town
  INVDTALIN1 PFI Invoice line element -> [PFI]PFI0 =[PWH]INVDTALIN1 (PFOOTINV) !Other act:PPR
  INVDTALIN2 PFI(9) Invoice line allocation elemen -> [PFI]PFI0 =[PWH]INVDTALIN2 (PFOOTINV) !Other
  INVDTAVAT1 VAT Price line tax -> [TVT]TVT0 =INVDTAVAT1(indice);[V]GSUPCLE (TABVAT) !Other act:PPR
  INVDTAVAT2 VAT(9) Distribution line tax -> [TVT]TVT0 =INVDTAVAT2(indice);[V]GSUPCLE (TABVAT) !Other
  INVFLG M*15 Invoiced [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  INVLINCTR C*4 No. invoiced lines
  INVLINNBR C*4 No. invoiced lines
  MDL MDL Delivery mode -> [TMD]TMD0 =[PWH]MDL (TABMODELIV) !Other
  NDEDAT D Packing slip date
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[PWH]PRHFCY (FACILITY) !Other
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PRONUM L*8 Process number
  PSTFLG M*4 Posted [menu 1: 1=No,2=Yes]
  PSTLINNBR C*4 No. of posted lines
  PTHNUM VCR Receipt no.
  PURTYP M*15 Purchase type [menu 507: 1=Commercial,2=General]
  RCPDAT D Receipt date
  TOTAMTATI MD1 Total including tax
  TOTAMTATIL MD1 Tax incl. total cy currency
  TOTAMTNOT MD1 Total excluding tax
  TOTAMTNOTL MD1 Total excl. tax (co currency)
  TOTGROWEI DCB*11.4 Gross weight
  TOTLINAMT MD1 Invoice lines excluding tax
  TOTLINQTY DCB*11.6 Total quantity lines
  TOTLINVOU QTY Line volume total
  TOTLINWEU QTY Line weight total
  TOTNETWEI DCB*11.4 Net weight
  TOTTAXAMT MD1 Tax total
  TOTVOL DCB*11.4 Volume
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Other act:STS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Other
  VACTYP C*1 Tax rule type
  VOU UOM Volume unit -> [TUN]TUN0 =[PWH]VOU (TABUNIT) !Other
  WEU UOM Weight unit -> [TUN]TUN0 =[PWH]WEU (TABUNIT) !Other

## PWRKSTT (PWS) - Subcontract
Keys (first = PK; D = duplicates allowed): PWS0 PRONUM+CODFNC+VCRTYP+VCRNUM+VCRLIN+VCRSEQ+TRSTYP
Fields:
  AUUID AUUID Single identifier
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CODFNC A*3 Function code
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[PWS]CREUSR (AUTILIS) !Other
  ENTCOD GAU Auto journal code -> [GAU]GAU0 =[PWS]ENTCOD (GAUTACE) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[PWS]ITMREF (ITMMASTER) !RTZ
  MAXQTYRCP QTY Maximum qty
  MVTDES DES Movement description
  PRONUM L*8 Process number
  QQQQTYSTU QTY Quantity Q STK
  QTYSTU QTY STK quantity
  QTYUOM QTY Quantity STK
  RETQTY QTY Requirement quantity
  RRRQTYSTU QTY Quantity R STK
  STU UOM Stock unit -> [TUN]TUN0 =[PWS]STU (TABUNIT) !Other
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !Other
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  TRSTYP M*15 Mvt type [menu 704: 35 values, see local-menus.md]
  UOM UOM Order unit -> [TUN]TUN0 =[PWS]UOM (TABUNIT) !Other
  UOMSTUCOE COE STK conversion
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[PWS]UPDUSR (AUTILIS) !Other
  VCRLIN L*8 Entry line no.
  VCRNUM VCR Entry
  VCRSEQ L*8 Document sequence no.
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]
  WLOCSEQ L*8 Sequence
  WSTOFLG C*4 Entry OK indicator
  WSTOSEQ L*8 Sequence number

## SCOHEAD (SCO) - Subcontract order
Keys (first = PK; D = duplicates allowed): SCO0 SCONUM; SCO1 MFGFCY+SCOTRKFLG (D); SCO2 MTOREF (D)
Fields:
  ALLSTA M*15 Allocation status [menu 336: 1=Not allocated,2=Partial,3=Complete,4=Partial/Shortage,5=Complete/Shortage]
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersite [menu 1: 1=No,2=Yes]
  BPRNUM BPR Supplier -> [BPR]BPR0 =[SCO]BPRNUM (BPARTNER) !Block
  CHGCOE RCU Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLODAT D Closing date
  CPY CPY Company -> [CPY]CPY0 =[SCO]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SCO]CUR (TABCUR) !Other
  DETALLNBR L*8 Number of detail allocations
  EXPNUM L*8 Export number
  INVFCY FCY Invoicing site -> [FCY]FCY0 =[SCO]INVFCY (FACILITY) !Block
  ITMCLENBR L*8 Number of products closed
  ITMLINNBR L*8 Number of products
  MATCLENBR L*8 Number of materials closed
  MATLINNBR L*8 Number of materials
  MFGFCY FCY Production site -> [FCY]FCY0 =[SCO]MFGFCY (FACILITY) !Other
  MTOREF MTO MTO network -> [MTO]MTO0 =MTOREF (MTOHEAD) !RTZ
  OPECLENBR L*8 No. of operations closed
  OPELINNBR L*8 Number of operations
  ORDDAT D Order date
  OVRALLNBR L*8 Number of global allocations
  POHFCY FCY Order site -> [FCY]FCY0 =[SCO]POHFCY (FACILITY) !Block
  PRPMATNBR L*8 No. of prepared mat
  PRPSTA M*15 Picking status [menu 338: 1=Not prepared,2=Partial,3=Full]
  RETDAT D Requirement date
  SCODES DES Description
  SCONUM VCR Subcontract order
  SCOSTA M*10 Document status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  SCOTEX TEX Text
  SCOTRKFLG M*15 Tracking flag [menu 339: 1=Pending,2=Being optimized,3=Printed,4=In progress,5=Completed,6=Closed + Costed]
  SHTMATNBR L*8 Number short
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SCOITM (SCI) - Subcontract order
Notes: differs in V9.0 P12 (diff: AT3_SCOITM.htm); differs in V10 P1 (diff: ATD_SCOITM.htm)
Keys (first = PK; D = duplicates allowed): SCI0 SCONUM+SCILIN; SCI1 VCRTYPORI+VCRNUMORI+VCRLINORI+VCRSEQORI (D); SCI2 POHNUM+POPLIN+POQSEQ (D); SCI3 PJT (D)
Fields:
  AUUID AUUID Single identifier
  AVASCOQTY QTY Producible quantity
  BASQTY QTY Base quantity
  BOMALT C*2 BOM code
  BPAADD ADR Subcon. address
  BPRNUM BPR Supplier -> [BPR]BPR0 =[SCI]BPRNUM (BPARTNER) !RTZ
  CPLQTY QTY Total completed qty.
  CPY CPY Company -> [CPY]CPY0 =[SCI]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  EXTQTY QTY Planned quantity
  GROPRI MD8 Gross price
  INVQTY QTY Invoiced qty.
  ITMREF ITM Product -> [ITM]ITM0 =[SCI]ITMREF (ITMMASTER) !Block
  ITMSTA M*15 Manufacturing status [menu 2221: 1=On hold,2=Under progress,3=Ordered,4=Received,5=Closed]
  LOC LOC Location -> [STC]STC0 =mfgfcy;loc (STOLOC) !Other
  LOT LOT Lot
  LTI C*3 Lead time
  NETPRI MD8 Net price
  ORDQTY QTY Ordered qty.
  PIO M*2 Priority [menu 365: 1=Normal,2=Urgent,3=Very urgent]
  PJT PJT Project -> [PIM]PIM0 =[SCI]PJT (PIMPL) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Order sequence
  PRHADD ADR Receipt address
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[SCI]PRHFCY (FACILITY) !Block
  PRIREN PPR Price reason -> [PPR]PPR0 =[SCI]PRIREN (PPREASON) !RTZ
  PUU UOM Purchase unit -> [TUN]TUN0 =[SCI]PUU (TABUNIT) !Block
  PUUSTUCOE COE PUR-STK conversion
  QTYCOD M*15 Management unit [menu 225: 1=One,2=Per hundred,3=Per thousand,4=Percentage,5=By lot]
  QTYPUU QTY PUR quantity
  QUACPLQTY QTY Actual QC quantity
  REFPRI MD8 Reference price
  REJCPLQTY QTY Actual rejected qty.
  RMNEXTQTY QTY Remaining quantity
  SCILIN L*8 Product no.
  SCITRKFLG M*15 Status [menu 2238: 1=On hold,2=Being optimized,3=Printed,4=In progress,5=Closed,6=Cost price calculated]
  SCONUM VCR Subcontract order
  STU UOM Stock unit -> [TUN]TUN0 =[SCI]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WIPNUM VCR Order no.
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]

## SCOMAT (SCM) - Order sub-contract materials
Keys (first = PK; D = duplicates allowed): SCM0 SCONUM+SCILIN+SCMLIN; SCM1 STOFCY+DLVDAT (D); SCM2 STOFCY+PIO+DLVDAT (D); SCM3 ITMREF+BOMALT+BOMSEQ+CPNITMREF (D); SCM4 POHNUM+POPLIN+POQSEQ (D)
Fields:
  ALLQTY QTY Allocated quantity
  ALLSTA M*15 Allocation status [menu 340: 1=None,2=Global with shortage,3=Global,4=Detailed with shortage,5=Detailed]
  AUUID AUUID Single identifier
  BASQTY QTY Base quantity
  BOMALT C*2 BOM code
  BOMOFS C*4 Operation lead time
  BOMQTY QTY UOM link quantity
  BOMSEQ C*4 BOM sequence
  BOMSTUCOE COE UOM-STK factor
  BOMUOM UOM UOM -> [TUN]TUN0 =[SCM]BOMUOM (TABUNIT) !Block
  CPLCRG MD8 Actual charge
  CPLPRI MD8 Actual price
  CPNITMREF ITM Component -> [ITM]ITM0 =[SCM]CPNITMREF (ITMMASTER) !Other
  CPNTYP M*15 Component type [menu 438: 1=Normal,2=Option,3=Variant,4=By-product,5=Text,6=Costing,7=Service,8=Multiple option,9=Normal (with formula)]
  CPY CPY Company -> [CPY]CPY0 =[SCM]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[SCM]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[SCM]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[SCM]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  DLVDAT D Delivery date
  DLVQTY QTY Delivered qty.
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  GROPRI MD8 Gross price
  INVQTY QTY Invoiced qty.
  ISSMGTCOD M*15 Stock issuing method [menu 724: 1=By lot,2=FIFO,3=FEFO]
  ITMREF ITM Parent -> [ITM]ITM0 =[SCM]ITMREF (ITMMASTER) !Block
  LIKQTY QTY Link quantity
  LIKQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  LINAMT MD6 Line amount - tax
  LINAMTL MD6 Total excl. tax (co currency)
  LOC LOC Location -> [STC]STC0 =FCY;LOC (STOLOC) !Other
  LOT LOT Preferred lot
  MATSTA M*15 Material status [menu 2223: 1=On hold,2=Under progress,3=Closed,4=Excluded,5=Ordered,6=Received]
  MFGFCY FCY Production site -> [FCY]FCY0 =[SCM]MFGFCY (FACILITY) !Other
  NETPRI MD8 Net price
  NETPRIL MD8 Net price, tax excl. (company)
  ORDQTY QTY Ordered qty.
  PICPRN M*4 Materials requisition printing [menu 1: 1=No,2=Yes]
  PIO C*2 Priority
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Order sequence
  PRIREN PPR Price reason -> [PPR]PPR0 =[SCM]PRIREN (PPREASON) !RTZ
  QTYRND M*15 Quantity rounding [menu 293: 1=Round to the nearest,2=Greater than,3=Less than]
  REFPRI MD8 Reference price
  RELSCATIA M*4 Shrink with release [menu 1: 1=No,2=Yes]
  RETQTY QTY Requirement quantity
  SCA DCB*3.3 Scrap factor %
  SCILIN L*8 Product no.
  SCMLIN L*8 Line
  SCMTEX TXC Text
  SCMTRKFLG M*15 Material tracking [menu 2238: 1=On hold,2=Being optimized,3=Printed,4=In progress,5=Closed,6=Cost price calculated]
  SCOFLG M*30 Type of supply [menu 2225: 1=Internal,2=To be sent to the subcontractor,3=Supplied by the subcontractor]
  SCONUM VCR Subcontract order
  SCSLIN L*8 Service line
  SHTQTY QTY Shortage
  STA A*12 Preferential status
  STDQTY QTY Standard quantity
  STOFCY FCY Storage site -> [FCY]FCY0 =[SCM]STOFCY (FACILITY) !Other
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[SCM]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEQTY QTY Consumed quantity
  WIPNUM VCR Order no.
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]

## SCOSRV (SCS) - Order sub-contract services
Keys (first = PK; D = duplicates allowed): SCS0 SCONUM+SCILIN+SCSLIN; SCS1 POHNUM+POPLIN+POQSEQ (D); SCS2 ITMREF+BOMALT+BOMSEQ+SRVITMREF (D)
Fields:
  AUUID AUUID Single identifier
  BOMALT C*2 BOM code
  BOMSEQ C*4 BOM sequence
  BPRNUM BPR Supplier -> [BPR]BPR0 =[SCS]BPRNUM (BPARTNER) !RTZ
  CPLCRG MD8 Actual charge
  CPLPRI MD8 Actual price
  CPLQTY QTY Total completed qty.
  CPY CPY Company -> [CPY]CPY0 =[SCS]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[SCS]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[SCS]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[SCS]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EXPNUM L*8 Export number
  EXTQTY QTY Planned quantity
  EXTSTRQTY QTY Sub-contract quantity
  EXTSTUQTY QTY Expected STK quantity
  GROPRI MD8 Gross price
  INVQTY QTY Invoiced qty.
  ITMREF ITM Parent -> [ITM]ITM0 =[SCS]ITMREF (ITMMASTER) !Other
  LINAMT MD6 Line amount - tax
  LINAMTL MD6 Total excl. tax (co currency)
  NETPRI MD8 Net price
  NETPRIL MD8 Net price, tax excl. (company)
  OPEEND D End date
  OPESTA M*15 Service status [menu 2239: 1=On hold,2=In progress,3=Closed,4=Ordered,5=Received,6=Inoviced]
  OPESTR D Start date
  OPESTRCOE COE STK-OPE factor
  OPESTU UOM Stock unit -> [TUN]TUN0 =[SCS]OPESTU (TABUNIT) !Other
  OPESTUCOE COE STK-OPE conversion
  OPSNUM VCR Load no.
  ORDQTY QTY Ordered qty.
  PIO C*2 Priority
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPLIN L*8 Line
  POQSEQ L*8 Order sequence
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[SCS]PRHFCY (FACILITY) !Block
  PRIREN PPR Price reason -> [PPR]PPR0 =[SCS]PRIREN (PPREASON) !RTZ
  QUACPLQTY QTY Actual QC quantity
  REFPRI MD8 Reference price
  REJCPLQTY QTY Actual rejected qty.
  RMNEXTQTY QTY Remaining quantity
  RPLIND C*3 Alternate index
  SCILIN L*8 Product no.
  SCOLTI C*4 Subcontract LT
  SCONUM VCR Subcontract order
  SCOPUU UOM Sub-contracting PO unit -> [TUN]TUN0 =[SCS]SCOPUU (TABUNIT) !Other
  SCSLIN L*8 Line
  SCSTEX TXC Text
  SCSTRKFLG M*15 Service situation [menu 2238: 1=On hold,2=Being optimized,3=Printed,4=In progress,5=Closed,6=Cost price calculated]
  SRVITMREF ITM Subcontracted prod. -> [ITM]ITM0 =[SCS]SRVITMREF (ITMMASTER) !Block
  STDQTY QTY Standard quantity
  STRQTYCOD M*15 Link quantity code [menu 226: 1=Proportional,2=Fixed]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WIPNUM VCR WIP no.
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]

## SCOTRK (SCK) - Sub-contract tracking
Notes: differs in V9.0 P12 (diff: AT3_SCOTRK.htm); differs in V10 P1 (diff: ATD_SCOTRK.htm)
Keys (first = PK; D = duplicates allowed): SCK0 SCONUM+SCILIN+SCSLIN+SCMLIN+PTHNUM+PTDLIN; SCK1 PTHNUM+PTDLIN+SCONUM+SCILIN+SCSLIN+SCMLIN; SCK2 POHNUM+POPLIN+POQSEQ (D)
Fields:
  AUUID AUUID Single identifier
  BPRNUM BPR Supplier -> [BPR]BPR0 =[SCK]BPRNUM (BPARTNER) !RTZ
  CPLCRG MD8 Actual charge
  CPLPRI MD8 Actual price
  CPLQTY QTY Actual accepted qty
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[SCK]CREUSR (AUTILIS) !Other
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  EXTPRI MD8 Expected price
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  INVQTY QTY Invoiced qty.
  IPTDAT D Allocation date
  ITMREF ITM Product -> [ITM]ITM0 =[SCK]ITMREF (ITMMASTER) !Block
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  LOT LOT Lot
  PJT PJT Project -> [PIM]PIM0 =[SCK]PJT (PIMPL) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Order sequence
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[SCK]PRHFCY (FACILITY) !Block
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  SCILIN L*8 Product no.
  SCMLIN L*8 Line
  SCONUM VCR Subcontract order
  SCSLIN L*8 Service line
  STA A*3 Status
  STU UOM Stock unit -> [TUN]TUN0 =[SCK]STU (TABUNIT) !Block
  UOM UOM Release unit -> [TUN]TUN0 =[SCK]UOM (TABUNIT) !Block
  UOMCPLQTY QTY Actual quantity OK
  UOMSTUCOE COE STK conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[SCK]UPDUSR (AUTILIS) !Other

## SHIPDOC (SHIPD) - Shipment documents
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): SHIPD0 VCRNUM+VCRTYP+SDLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SHIPD]CREUSR (AUTILIS) !Other
  SDBP BPR BPs -> [BPR]BPR0 =[SHIPD]SDBP (BPARTNER) !Block
  SDCMT A*30 Comments
  SDDATE D Document date
  SDFILNAM A*250 File name
  SDLIN L*8 Line
  SDNTYP ADI File type -> [ADI]CODE =902;SDNTYP (ATABDIV) !Block
  SDORI M*10 Document origin [menu 2512: 1=Not applicable,2=Air,3=Sea,4=Road,5=Rail]
  SDREF1 A*30 Reference 1
  SDREF2 A*30 Reference 2
  SDTYPE ADI Document type -> [ADI]CODE =107;SDTYPE (ATABDIV) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SHIPD]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## SHIPMENT (SHH) - Shipment
Notes: differs in V9.0 P12 (diff: AT3_SHIPMENT.htm); differs in V10 P1 (diff: ATD_SHIPMENT.htm)
Keys (first = PK; D = duplicates allowed): SHH0 SHIPNUM
Fields:
  ARVCRY CRY Destination country -> [TCY]TCY0 =[SHH]ARVCRY (TABCOUNTRY) !Block
  ARVDAT D Arrival date
  ARVEXPDAT D Exp. arrival date
  ARVTPC TPC Transit - arrival -> [TPC]TPC0 =[SHH]ARVTPC (TABPLACE) !Block
  AUUID AUUID Single identifier
  AVAVOL QTY Available volume
  AVAWEI QTY Avail. weight
  BPRNUM BPR BP code -> [BPR]BPR0 =[SHH]BPRNUM (BPARTNER) !Block
  BPSNUM BPS Supplier -> [BPS]BPS0 =[SHH]BPSNUM (BPSUPPLIER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[SHH]BPTNUM (BPCARRIER) !Block
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SHH]CREUSR (AUTILIS) !Other
  CRRVOL QTY Shipment total vol.
  CRRWEI QTY Shipment total wgt.
  DPECRY CRY Country of origin -> [TCY]TCY0 =[SHH]DPECRY (TABCOUNTRY) !Block
  DPEDAT D Departure date
  DPETPC TPC Transit - start -> [TPC]TPC0 =[SHH]DPETPC (TABPLACE) !Block
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SHH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SHH]DSPWEU (TABUNIT) !Block
  FCY FCY Site -> [FCY]FCY0 =[SHH]FCY (FACILITY) !Block
  LEGCPY CPY Company -> [CPY]CPY0 =[SHH]LEGCPY (COMPANY) !Block
  MAXVOL VOL Max volume
  MAXWEI WEI Max wgt.
  SHIPDAT D Ship date
  SHIPLAG C*4 Date shift
  SHIPMGT M*15 Management [menu 592: 1=Order line,2=Multiple containers,3=Single container]
  SHIPNBCTR C*4 Number of containers
  SHIPNUM VCR Shipment number
  SHIPTYP M*15 Record type [menu 2510: 1=Shipment,2=Pre-received order]
  SHIPUID A*15 Shipment ID
  TCTRNUM TCTR Freight container -> [TCTR]TCTR0 =[SHH]TCTRNUM (TABCONTAINER) !Block
  TRNMOD M*15 Transport mode [menu 2027: 1=Air,2=Sea,3=Road,4=Rail,5=Multimodal,6=Not defined]
  TRNNUM VCR Transport no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SHH]UPDUSR (AUTILIS) !Other

## SHIPMENTD (SHD) - Shipment detail
Notes: differs in V9.0 P12 (diff: AT3_SHIPMENTD.htm); differs in V10 P1 (diff: ATD_SHIPMENTD.htm)
Keys (first = PK; D = duplicates allowed): SHD0 SHIPNUM+SHIPLIN; SHD1 SHIPNUM+CTRNUM+SHIPLIN; SHD2 POHNUM+POPLIN+POQSEQ (D)
Fields:
  AUUID AUUID Single identifier
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CPRCOE COE Landed cost coef.
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SHD]CREUSR (AUTILIS) !Other
  CTRLIN L*8 Line
  CTRNUM VCR Container no.
  CTRUID A*20 Container ID
  EXTRCPDAT D Exp. receipt date
  FCSCPR MD1 Stock cost total
  FCSCSTPUR MD1 Purchase cost total
  ITMREF ITM Product -> [ITM]ITM0 =[SHD]ITMREF (ITMMASTER) !Block
  LEGCPY CPY Company -> [CPY]CPY0 =[SHD]LEGCPY (COMPANY) !Block
  LINAMT MD1 Line amount - tax
  LINVOU UOM Volume unit -> [TUN]TUN0 =[SHD]LINVOU (TABUNIT) !Block
  LINWEU UOM Weight unit -> [TUN]TUN0 =[SHD]LINWEU (TABUNIT) !Block
  NETCUR CUR Currency -> [TCU]TCU0 =[SHD]NETCUR (TABCUR) !Block
  POHFCY FCY Order site -> [FCY]FCY0 =[SHD]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Sequence number
  PRCPFLG M*4 Pre-received [menu 1: 1=No,2=Yes]
  PRCPQTY QTY Pre-received qty.
  PRCPQTYPUU QTY Pre-received PUR qty.
  PRCPQTYSTU QTY Pre-received STK qty.
  PRCPREN ADI Reason for closing -> [ADI]CODE =201;PRCPREN (ATABDIV) !Block
  PUU UOM Purchase unit -> [TUN]TUN0 =[SHD]PUU (TABUNIT) !Block
  QTYEXPFLG M*4 Reinteg. shipped qty [menu 1: 1=No,2=Yes]
  QTYVOU QTY Volume
  QTYWEU QTY Weight
  RCPQTYPUU QTY Received PUR
  RCPQTYSTU QTY Received STK
  SHIPLIN L*8 Line
  SHIPNUM VCR Shipment number
  SHIQTY QTY Shipped qty.
  SHIQTYPUU QTY PUR qty. being deliv.
  SHIQTYSTU QTY STK qty. being deliv.
  STCNUM VCR Cost structure
  STU UOM Stock unit -> [TUN]TUN0 =[SHD]STU (TABUNIT) !Block
  UOM UOM Order unit -> [TUN]TUN0 =[SHD]UOM (TABUNIT) !Block
  UOMPUUCOE COE STK-PUR conversion
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SHD]UPDUSR (AUTILIS) !Other

## SHIPTRACK (SHIPT) - Shipment logistical tracking
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): SHIPT0 VCRNUM+VCRTYP+STLIN
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SHIPT]CREUSR (AUTILIS) !Other
  STLIN ISEQ Line number
  TRKCMT A*30 Comments
  TRKCOD ADI Step -> [ADI]CODE =108;TRKCOD (ATABDIV) !Block
  TRKDEPCOD A*15 Dependency
  TRKDEPLIN L*8 Line
  TRKENDDAT D End date
  TRKLIGSTAT M*15 Line status [menu 593: 1=To do,2=In progress,3=Completed]
  TRKLIN L*8 Line
  TRKMDY M*4 Mandatory [menu 1: 1=No,2=Yes]
  TRKNUM VCR Tracking number
  TRKPLNDAT D Due date
  TRKSORT ISORT Sort order
  TRKUSR AUS User -> [AUS]CODUSR =[SHIPT]TRKUSR (AUTILIS) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SHIPT]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 701: 40 values, see local-menus.md]

## TMPPRPT (TPRPT) - Temporary print key table
Notes: differs in V10 P1 (diff: ATD_TMPPRPT.htm)
Keys (first = PK; D = duplicates allowed): TPRPT0 NUMREQ+USR+RPTCOD+VCRNUM
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TPRPT]CREUSR (AUTILIS) !Other
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
  RPTCOD ARP Report code -> [ARP]ARP0 =[TPRPT]RPTCOD (AREPORT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TPRPT]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TPRPT]USR (AUTILIS) !Other
  VCRNUM VCR Document no.

## TRANSPORT (TRNP) - Transport
Notes: differs in V9.0 P12 (diff: AT3_TRANSPORT.htm)
Keys (first = PK; D = duplicates allowed): TRNP0 TRNNUM; TRNP1 ARVEXPDAT+TRNNUM (D)
Fields:
  ARVDAT D Arrival date
  ARVEXPDAT D Exp. arrival date
  ARVTPC TPC Transit - arrival -> [TPC]TPC0 =[TRNP]ARVTPC (TABPLACE) !Block
  AUUID AUUID Single identifier
  AWB A*15 Air waybill
  BPRNUM BPR BP code -> [BPR]BPR0 =[TRNP]BPRNUM (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[TRNP]BPTNUM (BPCARRIER) !Block
  CIM A*15 CIM/CIV waybill
  CMR A*15 CMR waybill
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TRNP]CREUSR (AUTILIS) !Other
  CTBL A*15 Combined transp. doc.
  DESAXX AX3 Description
  DPEDAT D Departure date
  DPETPC TPC Transit - start -> [TPC]TPC0 =[TRNP]DPETPC (TABPLACE) !Block
  FLINUM A*15 Flight number
  FLYNAM A*30 Company
  HAWB A*15 HAWB
  HBOL A*15 Bill of lading
  MBOL A*15 Master Bill
  REGNUM A*30 Registration
  ROANAM A*30 Name
  SHIPLAG C*4 Date shift
  TRANUM A*30 Train number
  TRNMOD M*15 Transport mode [menu 2027: 1=Air,2=Sea,3=Road,4=Rail,5=Multimodal,6=Not defined]
  TRNNUM VCR Transport no.
  TRNSTA M*30 Status [menu 591: 1=Created,2=In progress,3=Arrived]
  TRNUID A*15 Transport ID
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TRNP]UPDUSR (AUTILIS) !Other
  VESNAM A*30 Company
  VESSEL A*30 Vessel name
  VOYNUM A*30 Voyage number
  WAGNAM A*30 Company
  WAGNUM A*15 Wagon

## UPORDER (UOH) - PO history
Keys (first = PK; D = duplicates allowed): POH0 POHNUM+REVNUM
Fields:
  APPFLG M*15 Signed [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPAADD ADR Address
  BPAADDLIG ADL(3) Address line
  BPAINV ADR Billing address
  BPAPAY ADR Pay-to BP address
  BPCORD BPR Sold-to -> [BPR]BPR0 =[UOH]BPCORD (BPARTNER) !Block
  BPOADD ADR Ship-from address
  BPOADDLIG ADL(3) Address line
  BPOCRY CRY Country -> [TCY]TCY0 =[UOH]BPOCRY (TABCOUNTRY) !Block
  BPOCRYNAM NCY Country name
  BPOCTY CTY City
  BPONAM NAM(2) Company name
  BPOPOSCOD POS Postal code
  BPOSAT SAT County
  BPRNAM NAM(2) Company name
  BPRPAY BPR Pay-to -> [BPR]BPR0 =[UOH]BPRPAY (BPARTNER) !Block
  BPSINV BPR Supplier invoice -> [BPR]BPR0 =[UOH]BPSINV (BPARTNER) !Block
  BPSNUM BPR Supplier -> [BPR]BPR0 =[UOH]BPSNUM (BPARTNER) !Block
  BPTNUM BPT Carrier -> [BPT]BPT0 =[UOH]BPTNUM (BPCARRIER) !Block
  BUY AUS Buyer -> [AUS]CODUSR =[UOH]BUY (AUTILIS) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CHGCOE DCB*5.6 Rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLEFLG M*4 Closed [menu 1: 1=No,2=Yes]
  CLELINNBR C*4 No. closed lines
  COPNBR C*1 No. copies order note
  CPY CPY Company -> [CPY]CPY0 =[UOH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRY CRY Country -> [TCY]TCY0 =[UOH]CRY (TABCOUNTRY) !Block
  CRYNAM NCY Country name
  CTY CTY City
  CUR CUR Currency -> [TCU]TCU0 =[UOH]CUR (TABCUR) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[UOH]DIE (GDIE) !Block act:ANA
  DISCRGTYP M*10 Discount / charge type [menu 255: 1=Amount,2=% combined,3=% series] act:PPR
  DME M*15 Partial delivery [menu 414: 1=Authorized,2=Full delivery line,3=Full order line]
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[UOH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[UOH]DSPWEU (TABUNIT) !Block
  EECICT ICT Incoterm -> [ICTH]ICT0 =[UOH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNUM A*20 EU identification act:DEB
  ENDDAT D Validity end date
  EXPNUM L*8 Export number
  EXTRCPDAT1 D Exp. receipt date
  FBULINNBR C*4 No. lines > budg
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[UOH]FFWNUM (BPCARRIER) !Block
  FUPFLG M*4 Delivery reminders [menu 1: 1=No,2=Yes]
  GPGCOD A*20 Grouping code
  ICTCTY CTY Incoterm town
  INVDTALIN1 PFI Invoice line element -> [PFI]PFI0 =[UOH]INVDTALIN1 (PFOOTINV) !Block act:PPR
  INVDTALIN2 PFI(9) Invoice line allocation elemen -> [PFI]PFI0 =[UOH]INVDTALIN2 (PFOOTINV) !Block
  INVDTAVAT1 VAT Price line tax -> [TVT]TVT0 =INVDTAVAT1(indice);[V]GSUPCLE (TABVAT) !Block act:PPR
  INVDTAVAT2 VAT(9) Distribution line tax -> [TVT]TVT0 =INVDTAVAT2(indice);[V]GSUPCLE (TABVAT) !Block
  INVFCY FCY Invoicing site -> [FCY]FCY0 =[UOH]INVFCY (FACILITY) !Block
  INVFLG M*15 Invoiced [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  INVLINNBR C*4 No. invoiced lines
  INVNBR L*8 Number of invoices
  LAN LAN Language -> [TLA]TLA0 =[UOH]LAN (TABLAN) !Block
  LINNBR C*4 Number of lines
  MDL MDL Delivery mode -> [TMD]TMD0 =[UOH]MDL (TABMODELIV) !Block
  OCNDAT D Ack. date
  OCNFLG M*4 Ack. reminder [menu 1: 1=No,2=Yes]
  OCNNUM A*20 Ack. ID
  OCNREM A*150 Ack. notes
  ORDDAT D Order date
  ORDREF A*20 Internal reference
  ORIFCY FCY Original site -> [FCY]FCY0 =[UOH]ORIFCY (FACILITY) !Block
  POHFCY FCY Order site -> [FCY]FCY0 =[UOH]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POSCOD POS Postal code
  PRNFLG M*4 Printed [menu 1: 1=No,2=Yes]
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  PURTYP M*15 Purchase type [menu 507: 1=Commercial,2=General]
  RCPFCY FCY Receiving site -> [FCY]FCY0 =[UOH]RCPFCY (FACILITY) !Block
  RCPFLG M*15 Received [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  RCPLINNBR C*4 No. received lines
  RCPNBR L*8 Number of receipts
  REVCOD A*1 Revision code
  REVNUM C*4 Revision no.
  SALFCY FCY Sales site -> [FCY]FCY0 =[UOH]SALFCY (FACILITY) !Block
  SAT SAT County
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  STOFCY FCY Shipment site -> [FCY]FCY0 =[UOH]STOFCY (FACILITY) !Block
  STRDAT D Validity start date
  TEX1 TXC Text
  TEX2 TXC Text
  TOTLINAMT MD1 Invoice lines excluding tax
  TOTLINATI MD1 Lines total incl-tax
  TOTLINQTY DCB*11.6 Total quantity lines
  TOTLINVOU QTY Line volume total
  TOTLINWEU QTY Line weight total
  TOTORD MD1 Total order -tax
  TOTORDL MD1 Total excl. tax (co currency)
  TOTTAXAMT MD1 Tax total
  TOTVLT MD1 Expected total -tax
  TSSCOD ADI Statistical group -> [ADI]CODE =indice+40;TSSCOD(indice) (ATABDIV) !Other act:STS
  TTVORD MD1 Total order +tax
  TTVORDL MD1 Tax incl. total cy currency
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACTYP C*1 Tax rule type

## UPORDERC (UOC) - Cumulative PO history before R
Keys (first = PK; D = duplicates allowed): POC0 POHNUM+LINREVNUM+POPLIN
Fields:
  AMTVLT MD1 Costing amount
  AUUID AUUID Single identifier
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPSNUM BPS Supplier -> [BPS]BPS0 =[UOC]BPSNUM (BPSUPPLIER) !Other
  COA COA(10) Chart code -> [COA]COA0 =[UOC]COA (GCOA) !RTZ
  CPY CPY Company -> [CPY]CPY0 =[UOC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYDSP C*3(7) Daily distribution
  DLVREQNUM L*8 Number of delivery request pro
  EARDAT D Early/Late date
  EARHOU HM Early/late time
  EARQTY QTY Early/Late qty.
  EECICT2 ICT Incoterm -> [ICTH]ICT0 =[UOC]EECICT2 (INCOTERM) !Block
  EECLOC2 M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNUM2 A*20 EU identification act:DEB
  ENDDAT D Valid to
  EXPNUM L*8 Export number
  EXTQTYPUU QTY Expected PUR quantity
  EXTQTYSTU QTY Expected STK quantity
  FCYADD ADR Receipt address
  FFWADD2 ADR Forwarding agent address
  FFWNUM2 BPT Freight agent -> [BPT]BPT0 =[UOC]FFWNUM2 (BPCARRIER) !Block
  FIMHOR C*4 Firm horizon
  FRTHOR C*4 Planning horizon
  FRTHORUOM M*15 Planning horizon time unit [menu 291: 1=Calendar days,2=Work days,3=Weeks,4=Fortnights,5=Months]
  ICTCTY2 CTY Incoterm town
  INVQTYPUU QTY Invoiced PUR
  INVQTYSTU QTY Invoiced STU
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[UOC]ITMREF (ITMMASTER) !Block
  ITMREFBPS A*20 Supplier product
  LINACC GAC(10) Accounts -> [GAC]GAC0 =COA(indice);LINACC(indice) (GACCOUNT) !Block
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINREVNUM C*4 Revision no.
  ORDQTYPUU QTY Ordered PUR
  ORDQTYSTU QTY Ordered STK
  PLI PLI Price list code
  POHFCY FCY Order site -> [FCY]FCY0 =[UOC]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[UOC]PRHFCY (FACILITY) !Block
  PRIVLT MD8 Costing price
  PUU UOM Purchase unit -> [TUN]TUN0 =[UOC]PUU (TABUNIT) !Block
  RCPQTYPUU QTY Received PUR
  RCPQTYSTU QTY Received STK
  REVCOD A*1 Revision code
  RTNQTYPUU QTY Returned PUR qty.
  RTNQTYSTU QTY Returned STK qty.
  STOFCY FCY Shipment site -> [FCY]FCY0 =[UOC]STOFCY (FACILITY) !Block
  STRDAT D Valid from
  STU UOM Stock unit -> [TUN]TUN0 =[UOC]STU (TABUNIT) !Block
  TEX TXC Text
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  WEEDSP C*3(5) Weekly distribution

## UPORDERP (UOP) - PO price history
Keys (first = PK; D = duplicates allowed): POP0 POHNUM+LINREVNUM+POPLIN+POPSEQ
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[UOP]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DISCRGREN1 PPR Discount 1 reason -> [PPR]PPR0 =[UOP]DISCRGREN1 (PPREASON) !Block act:PP1
  DISCRGREN2 PPR Discount 2 reason -> [PPR]PPR0 =[UOP]DISCRGREN2 (PPREASON) !Block act:PP2
  DISCRGREN3 PPR Discount 3 reason -> [PPR]PPR0 =[UOP]DISCRGREN3 (PPREASON) !Block act:PP3
  DISCRGREN4 C*4 Discount 4 reason act:PP4
  DISCRGREN5 C*4 Discount 5 reason act:PP5
  DISCRGREN6 C*4 Discount 6 reason act:PP6
  DISCRGREN7 C*4 Discount 7 reason act:PP7
  DISCRGREN8 C*4 Discount 8 reason act:PP8
  DISCRGREN9 C*4 Discount 9 reason act:PP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:PP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:PP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:PP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:PP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:PP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:PP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:PP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:PP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:PP9
  EECINCRAT RAT Intrastat increase act:DEB
  EXPNUM L*8 Export number
  FCYADD ADR Receipt address
  GROPRI MD8 Gross price
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[UOP]ITMREF (ITMMASTER) !Block
  LINBUY AUS Buyer -> [AUS]CODUSR =[UOP]LINBUY (AUTILIS) !Block
  LINREVNUM C*4 Revision no.
  NETPRI MD8 Net price
  ORICRY CRY Country of origin -> [TCY]TCY0 =[UOP]ORICRY (TABCOUNTRY) !Block
  PJT A*20 Project
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPCREFLG M*4 Creation flag [menu 1: 1=No,2=Yes]
  POPDAT D Application end date
  POPLIN L*8 Line
  POPSEQ L*8 Sequence
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[UOP]PRHFCY (FACILITY) !Block
  PRIREN PPR Price reason -> [PPR]PPR0 =[UOP]PRIREN (PPREASON) !Block
  QUAFLG M*4 QC management [menu 1: 1=No,2=Yes]
  REVCOD A*1 Revision code
  STRDAT D Price effectivity date
  TAXISS VAT Issue tax -> [TVT]TVT0 =TAXISS;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH1 VAT Other tax 1 -> [TVT]TVT0 =TAXOTH1;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXOTH2 VAT Other tax 2 -> [TVT]TVT0 =TAXOTH2;[V]GSUPCLE (TABVAT) !Block act:PTX
  TAXRCP VAT Receipt tax -> [TVT]TVT0 =TAXRCP;[V]GSUPCLE (TABVAT) !Block act:PTX
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## UPORDERQ (UOQ) - PO quantity history
Keys (first = PK; D = duplicates allowed): POQ0 POHNUM+LINREVNUM+POPLIN+POQSEQ
Fields:
  AMTTAXISS MD1 Issue tax amount act:PTX
  AMTTAXLIN1 MD1 Tax amount 1
  AMTTAXLIN2 MD1 Tax amount 2
  AMTTAXLIN3 MD1 Tax amount 3
  AMTTAXOTH1 MD1 Amount other tax 1 act:PTX
  AMTTAXOTH2 MD1 Amount other tax 2 act:PTX
  AMTTAXRCP MD1 Receipt tax amount act:PTX
  AUUID AUUID Single identifier
  BASTAXLIN1 MD1 Tax basis 1
  BPAINV ADR Billing address
  BPSINV BPS Bill-by BP -> [BPS]BPS0 =[UOQ]BPSINV (BPSUPPLIER) !Other
  BPSNUM BPS Supplier -> [BPS]BPS0 =[UOQ]BPSNUM (BPSUPPLIER) !Other
  CAD M*7 Sequencing [menu 278: 1=Day,2=Week,3=Month]
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLCAMT3 MD1 Tax calculation basis 3
  CLCAMT4 MD1 Tax calculation basis 4 act:PTX
  CLCAMT5 MD1 Tax calculation basis 5 act:PTX
  CLCAMT6 MD1 Tax calculation basis 6 act:PTX
  CLCAMT7 MD1 Tax calculation basis 7 act:PTX
  CMMFLG C*1 Commitment indic
  CMMNUM VCR Commitment no.
  CMMTAX M*25 Commitment type [menu 578: 1=Tax-excl. amount,2=Tax-excl. amount + Non-deductible VAT]
  CPR MD8 Stock cost per unit
  CPRAMT MD5 Fixed cost per unit
  CPRCOE COE Landed cost coef.
  CPRCUR CUR Company currency -> [TCU]TCU0 =[UOQ]CPRCUR (TABCUR) !Block
  CPRPRI MD8 Production cost PUR
  CPY CPY Company -> [CPY]CPY0 =[UOQ]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CSTPUR MD8 Purchase cost per unit
  DEDTAXISS MD1 Deductible tax act:PTX
  DEDTAXLIN1 MD1 Deductible tax 1
  DEDTAXLIN2 MD1 Deductible tax 2
  DEDTAXLIN3 MD1 Deductible tax 3
  DEDTAXOTH1 MD1 Deductible tax act:PTX
  DEDTAXOTH2 MD1 Deductible tax act:PTX
  DEDTAXRCP MD1 Deductible tax act:PTX
  DEMENDDAT D Requesteded end date
  DEMENDHOU C*4 Requested end time
  DEMRCPDAT D Requested receipt date
  DEMRCPHOU C*4 Requested delivery time
  DISBASLIN1 MD1 Rebate tax basis 1
  DISCRGAMT1 MD1 Discount/Charge 1
  DISCRGAMT2 MD1 Discount/Charge 2
  DISCRGAMT3 MD1 Discount/Charge 3
  DISCRGAMT4 MD1 Discount/Charge 4
  DISCRGAMT5 MD1 Discount/Charge 5
  DISCRGAMT6 MD1 Discount/Charge 6
  DISCRGAMT7 MD1 Discount/Charge 7
  DISCRGAMT8 MD1 Discount/Charge 8
  DISCRGAMT9 MD1 Discount/Charge 9
  EXPNUM L*8 Export number
  EXTRCPDAT D Exp. receipt date
  FBUFLG M*4 Budget overrun [menu 1: 1=No,2=Yes]
  FCSCPR MD1 Stock cost total
  FCSCSTPUR MD1 Purchase cost total
  FCYADD ADR Receipt address
  INVQTYPUU QTY Invoiced PUR
  INVQTYSTU QTY Invoiced STU
  INVRCPNBR C*4 No. of invoice receipts
  ITMREF ITM Product -> [ITM]ITM0 =[UOQ]ITMREF (ITMMASTER) !Block
  ITMREFBPS A*20 Supplier product
  ITMREFORI ITM Released product -> [ITM]ITM0 =[UOQ]ITMREFORI (ITMMASTER) !Block
  LASINVDAT D Last invoice date
  LASRCPDAT D Last receipt date
  LIKQTYCOE COE Link qty. coef.
  LINAMT MD1 Line amount - tax
  LINAMTCPR MD8 Stock cost
  LINATI MD1 Line amount + tax
  LINATIAMT MD1 Line amount + tax
  LINCLEFLG M*4 Line closed [menu 1: 1=No,2=Yes]
  LINCSTPUR MD8 Purchase cost
  LININVFLG M*4 Invoiced line [menu 1: 1=No,2=Yes]
  LININVNBR C*4 Number of invoices
  LINOCNDAT D Ack. date
  LINOCNFLG C*1 Acknowledgement flag
  LINOCNNUM A*20 Ack. ID
  LINPRNFLG M*4 Line printed [menu 1: 1=No,2=Yes]
  LINPURTYP M*5 Purchase type [menu 646: 1=Purchase,2=Fixed asset,3=Services]
  LINRCPNBR C*4 Number of receipts
  LINREVNUM C*4 Revision no.
  LINSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  LINSTOFCY FCY Shipment site -> [FCY]FCY0 =[UOQ]LINSTOFCY (FACILITY) !Block
  LINTEX TXC Text
  LINTYP M*20 Line type [menu 570: 1=Normal,2=Parent product BOM,3=Service,4=Supplied material]
  LINVOU UOM Volume unit -> [TUN]TUN0 =[UOQ]LINVOU (TABUNIT) !Block
  LINWEU UOM Weight unit -> [TUN]TUN0 =[UOQ]LINWEU (TABUNIT) !Block
  MON C*2 Months
  NETCUR CUR Currency -> [TCU]TCU0 =[UOQ]NETCUR (TABCUR) !Block
  OCNLIN L*8 Interco. sales line
  OCNSEQ L*8 Interco. sales seq.
  OFS LTI Reorder LT
  ORDDAT D Order date
  ORI M*15 Request source [menu 505: 1=Purchases,2=Direct order,3=Received direct order,4=Transfer,5=Production]
  POHFCY FCY Order site -> [FCY]FCY0 =[UOQ]POHFCY (FACILITY) !Block
  POHNUM VCR Order no.
  POHTYP M*20 Order type [menu 506: 1=Order,2=Contract]
  POPLIN L*8 Line
  POQLNK A*16 Line + sequence
  POQSEQ L*8 Sequence number
  PPDLIN L*8 Response line
  PQHNUM VCR RFQ no.
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[UOQ]PRHFCY (FACILITY) !Block
  PTDLIN L*8 Line
  PTHNUM VCR Receipt no.
  PUU UOM Purchase unit -> [TUN]TUN0 =[UOQ]PUU (TABUNIT) !Block
  QTYPUU QTY PUR quantity
  QTYSTU QTY STK quantity
  QTYUOM QTY Ordered qty.
  QTYVOU QTY Volume
  QTYWEU QTY Weight
  RCPCLEFLG M*4 Closed by receipt [menu 1: 1=No,2=Yes]
  RCPQTYPUU QTY Received PUR
  RCPQTYSTU QTY Received STK
  REACSTPUR MD8 Actual purchase cost
  RETQTYPUU QTY Required PUR
  RETQTYSTU QTY Required STK
  RETRCPDAT D Requirement date
  REVCOD A*1 Revision code
  SCOADD ADR Subcon. address
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  SOHNUM VCR Sales order no.
  SOPLIN L*8 Sales order line
  SOQSEQ L*8 Sequence number
  STCNUM VCR Cost structure
  STU UOM Stock unit -> [TUN]TUN0 =[UOQ]STU (TABUNIT) !Block
  UOM UOM Order unit -> [TUN]TUN0 =[UOQ]UOM (TABUNIT) !Block
  UOMFLG M*4 Order in PAC [menu 1: 1=No,2=Yes]
  UOMPUUCOE COE STK-PUR conversion
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  WEE C*2 Week no.
  WIPNUM VCR Order no.
  WIPSTA M*15 WIP status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  WIPTYP M*15 Order type [menu 306: 14 values, see local-menus.md]
  YEA C*4 Year

## WRKPURFCS (WPF) - Purchase cost report
Keys (first = PK; D = duplicates allowed): WPF0 NUMREQ+USR+NUMLIG
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[WPF]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[WPF]CUR (TABCUR) !Other
  FCSCOD FCS Cost -> [FCS]FCS0 =[WPF]FCSCOD (FRECST) !Other
  FCSNAT M*40 Cost nature [menu 2276: 1=Packaging,2=Loading,3=Pre-transport,4=Export customs formality,5=Main transport loading,6=Main transport,7=Main transport unloading,8=Import customs formalities,9=Post-transport,10=Unloading,11=Insurance,12=Others]
  NUMLIG L*8 Line no.
  NUMREQ L*8 Query no.
  PCST A*15(6) Period
  PERCOD M*15 Period [menu 2231: 1=Day,2=Week,3=Half-month,4=Month,5=Quarter,6=Half-year,7=Year,8=Decade]
  REGROUP M*4 Grouping [menu 1: 1=No,2=Yes]
  RPTCOD ARP Report code -> [ARP]ARP0 =[WPF]RPTCOD (AREPORT) !BSRA
  TOTLIN MD1 Total
  TOTPCST MD1(6) Amount
  TYPMNT M*15 Amount type [menu 2504: 1=Adjusted,2=Calculated]
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[WPF]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[WPF]USR (AUTILIS) !Other

