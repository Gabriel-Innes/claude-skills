<!-- source: https://online-help.sagex3.com/erp/11/en-US/MCD/ATB_0.htm and the linked table / local-menu / data-type pages (Sage X3 V11 online help, 'Table dictionary') compiled by scripts/build_dict_x3.py | version: Sage X3 V11 | verified: 2026-10-02 -->
# Sales module - Sage X3 V11 table dictionary

Format per table: heading `TABLE (ABBREVIATION) - description`; `Keys` lists the indexes (first = primary key, `(D)` = duplicates allowed) with their column expression; then one field per line: `NAME TYPE*LENGTH(DIM) title [menu N: value=text,...] -> join or linked table`. `(DIM)` means an array stored as NAME_0 .. NAME_(DIM-1) in SQL. `-> [ABR]KEY=expr (TABLE)` is the dictionary's link expression (the foreign-key join); `-> TABLE` alone means the data type links to that table. Local menu values with more than 15 entries are in `../local-menus.md`; data types in `../data-types.md`.

## BITMPSORDERP (BISOP) - Sales orders - price
Keys (first = PK; D = duplicates allowed): BISOP0 BISOPADXUID+SOHNUM+SOPLIN+SOPSEQ
Fields:
  AUUID AUUID Single identifier
  BISOPADXUID L*8 Identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BISOP]CREUSR (AUTILIS) !Other
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SOPSEQ L*8 Sequence
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BISOP]UPDUSR (AUTILIS) !Other

## BITMPSORDERQ (BISOQ) - Sales orders - quantities
Keys (first = PK; D = duplicates allowed): BISOQ0 BISOQADXUID+SOHNUM+SOPLIN+SOQSEQ
Fields:
  AUUID AUUID Single identifier
  BISOQADXUID L*8 Identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[BISOQ]CREUSR (AUTILIS) !Other
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SOPSEQ L*8 Sequence
  SOQSEQ L*8 Sequence number
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[BISOQ]UPDUSR (AUTILIS) !Other

## COFAWRK (CAW) - Certificate of analysis
Keys (first = PK; D = duplicates allowed): CAW0 SDHNUM+SDDLIN+LOT+COFAUID
Fields:
  AUUID AUUID Single identifier
  COFAUID L*8 Process number
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  ITMREF ITM Product -> [ITM]ITM0 =[CAW]ITMREF (ITMMASTER) !Block
  LOT LOT Lot
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[CAW]UPDUSR (AUTILIS) !Other
  VCRLIN L*5 Line no.
  VCRNUM VCR Analysis request

## LTAPAR (LTP) - Sage Sales Tax connection
Notes: activity code LTA; differs in V9.0 P12 (diff: AT3_LTAPAR.htm)
Keys (first = PK; D = duplicates allowed): LTP0 DOSSIER
Fields:
  ACCTID A*20 Account
  AUUID AUUID Single identifier
  AVRREQ M*4 Verification [menu 1: 1=No,2=Yes]
  CLCALL M*4 Calculate [menu 1: 1=No,2=Yes]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[LTP]CREUSR (AUTILIS) !Other
  CRY CRY(25) Country -> [TCY]TCY0 =[LTP]CRY (TABCOUNTRY) !Other
  DEVURL A*100 Development URL
  DOSSIER ADS Folder -> [ADS]DOSSIER =[LTP]DOSSIER (ADOSSIER) !Other
  JVBRIP A*100 Java bridge IP
  JVBRPT L*8 Java bridge port
  LICKEY A*50 License key
  PRDURL A*100 Test URL
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[LTP]UPDUSR (AUTILIS) !Other
  USEPRDURL M*4 URL type [menu 1: 1=No,2=Yes]
  VCRDISDTA SFI(25) SST document disc. -> [SFI]SFI0 =[LTP]VCRDISDTA (SFOOTINV) !Block

## LTAVCR (LTV) - Local tax by sales document
Notes: activity code LTA
Keys (first = PK; D = duplicates allowed): LTV0 VCRTYP+VCRNUM+LTVSEQ
Fields:
  AMTNOT MD1 Amount - tax
  AMTTAX MD1 Tax amount
  AUUID AUUID Single identifier
  BASTAX MD1 Tax basis
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS Creation user -> [AUS]CODUSR =[LTV]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[LTV]CUR (TABCUR) !Delete
  DTA SFI Invoicing element -> [SFI]SFI0 =[LTV]DTA (SFOOTINV) !Other
  EXEAMTTAX MD1(10) Exemption amount
  JURNAM A*30 Description
  JURTYP A*10 Tax type
  LTVSEQ L*8 Sequence number
  PAYS CRY Country -> [TCY]TCY0 =[LTV]PAYS (TABCOUNTRY) !Block
  SAT SAT Region (county, state, ..)
  TAXDAT D Tax date
  TAXNAM A*30 Taxes
  TAXRAT DCB*3.6 Rate
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS Change user -> [AUS]CODUSR =[LTV]UPDUSR (AUTILIS) !Other
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 476: 23 values, see local-menus.md]

## SALESTAX (STB) - Sales tax report
Keys (first = PK; D = duplicates allowed): STB0 PID+VAT (D); STB1 VCRNUM+VCRTYP+VAT+PID (D)
Fields:
  ACCDAT D Accounting date
  AMTEXE MD1 Exemption amount
  AMTNON MD1 Non-taxable
  AMTTAX MD1 Taxable amount
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[STB]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[STB]CUR (TABCUR) !Block
  FPER C*5 Periods
  FRTNON MD1 Non taxable freight
  FRTTAX MD1 Taxable freight
  FYEAR C*5 Fiscal year
  GTE GTE Entry type -> [GTE]GTE0 =GTE;[V]GSUPCLE (GTYPACCENT) !Block
  NUM SIH Invoice number -> [SIV]SIV0 =[STB]NUM (SINVOICEV) !Other
  PID A*20 Processes
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATCOLL MD1 Output VAT
  VATDES DES Description
  VATEXN A*15 Exemption no.
  VATGRO MD1 Gross basis
  VATRAT DCB*3.6 Rate
  VATSUPAMT MD1 Extra tax amount
  VATTAX MD1 Tax amount
  VATTYP M*15 Tax type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]
  VCRDAT D Invoice date
  VCRLIN L*8 Line
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 476: 23 values, see local-menus.md]

## SALTRS (SLT) - Entered sales transactions
Notes: differs in V9.0 P12 (diff: AT3_SALTRS.htm); differs in V10 P1 (diff: ATD_SALTRS.htm)
Keys (first = PK; D = duplicates allowed): SLT0 STRTYP+STRNUM; SLT1 STRNUM+STRTYP
Fields:
  ACSCOD A*20 Access code
  ALLQTYCOD M*4 Allocated quantity [menu 1: 1=No,2=Yes]
  ALLQTYSCR M*15 Allocated quantity [menu 99: 1=Form and table,2=Form,3=Table]
  ALLTYPCOD M*15 Allocation type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ALLTYPCODD M*15 Allocation type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ALLTYPSCRD M*15 Allocation type [menu 99: 1=Form and table,2=Form,3=Table]
  AMTCOD M*4 Document amount [menu 1: 1=No,2=Yes]
  AMTLINCOD M*15 Line amount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AMTLINSCR M*15 Line amount [menu 99: 1=Form and table,2=Form,3=Table]
  AQRCOD M*15 Status [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AQRSCR M*15 Status [menu 99: 1=Form and table,2=Form,3=Table]
  ARVDATCOD M*15 Arrival date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AUUID AUUID Single identifier
  AUZUSRCOD M*15 Authorized user [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AVASTOCOD M*4 Availability [menu 1: 1=No,2=Yes]
  AVSTOCOD1 M*15 Available stock [menu 35: 1=Entered,2=Displayed,3=Hidden]
  AVSTOSCR1 M*15 Available stock [menu 99: 1=Form and table,2=Form,3=Table]
  BELVCSCOD M*15 VCS number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BETCPYCOD M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCYCOD M*4 Intersites [menu 1: 1=No,2=Yes]
  BOLCOD M*15 Bill of lading [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPAADDCOD M*15 Delivery address [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPAADDCODD M*15 Deliv address detail [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPAADDSCRD M*15 Deliv address detail [menu 99: 1=Form and table,2=Form,3=Table]
  BPCGRUCOD M*15 Group customer [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCINVCOD M*15 Bill-to customer [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCLOCCOD M*15 Location [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCORDCOD M*4 Sold-to [menu 1: 1=No,2=Yes]
  BPCPYRCOD M*15 Pay-by [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPCSALPRICOD M*15 Consumer sales price [menu 35: 1=Entered,2=Displayed,3=Hidden] act:EDIX3
  BPCSALPRISCR M*15 Consumer sales price [menu 99: 1=Form and table,2=Form,3=Table] act:EDIX3
  BPRFCTCOD M*15 Factor [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPRSACCOD M*15 Control [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSLOTCOD M*15 Supplier lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSLOTCOD1 M*15 Supplier lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPSLOTSCR M*18 Supplier lot [menu 99: 1=Form and table,2=Form,3=Table]
  BPSLOTSCR1 M*18 Supplier lot [menu 99: 1=Form and table,2=Form,3=Table]
  BPTNUMCOD M*15 Carrier [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPTNUMCODD M*15 Carrier detail [menu 35: 1=Entered,2=Displayed,3=Hidden]
  BPTNUMSCRD M*15 Carrier detail [menu 99: 1=Form and table,2=Form,3=Table]
  BVRREFNUMCOD MM*15 ISR reference number [menu 35: 1=Entered,2=Displayed,3=Hidden] act:KSW
  CCECOD M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCECODD M*15 Detail dimension [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ANA
  CCECODS M*15 Analytical dimension [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CCEDEF A*20 Default dimension
  CCESCRD M*15 Detail dimension [menu 99: 1=Form and table,2=Form,3=Table] act:ANA
  CCLRENCOD M*4 Closing reason [menu 1: 1=No,2=Yes]
  CCLRENCODD M*4 Closing reason [menu 1: 1=No,2=Yes]
  CCLRENSCRD M*15 Closing reason [menu 99: 1=Form and table,2=Form,3=Table]
  CDTBTNCOD M*4 Credit release [menu 1: 1=No,2=Yes]
  CFMFLGCOD M*4 Closed [menu 1: 1=No,2=Yes]
  CFMFLGSCR M*15 Closed [menu 99: 1=Form and table,2=Form,3=Table]
  CHGCOD M*15 Currency (type, rate) [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CNDNAMCOD M*15 Delivery contact [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CNDNAMSCR M*15 Delivery contact [menu 99: 1=Form and table,2=Form,3=Table]
  CNOFLGCOD M*15 Credit memo subject [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CNOFLGSCR M*15 Credit memo subject [menu 99: 1=Form and table,2=Form,3=Table]
  CNONUMCOD M*4 Credit memo no. [menu 1: 1=No,2=Yes]
  CNONUMSCR M*15 Credit memo no. [menu 99: 1=Form and table,2=Form,3=Table]
  CNORENCOD M*15 Memo reason [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CNTNAMCOD M*15 Person to contact [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CPLAMTCOD M*15 Actual amount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CPLAMTSCR M*15 Actual amount [menu 99: 1=Form and table,2=Form,3=Table]
  CPRPRICOD M*15 Cost price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  CPRPRISCR M*15 Cost price [menu 99: 1=Form and table,2=Form,3=Table]
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CURCOD M*15 Currency [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DATSELCOD M*15 Select delivery date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DAYLTICOD M*15 Delivery lead time [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DAYLTICODD M*15 Delivery LT detail [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DAYLTISCRD M*15 Delivery LT detail [menu 99: 1=Form and table,2=Form,3=Table]
  DCLEECNUMCOD M*15 VAT declaration no. [menu 35: 1=Entered,2=Displayed,3=Hidden] act:VATTN
  DEMDLVCOD M*15 Req. delivery date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DEMDLVCODD M*15 Req. delivery date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DEMDLVHCOD M*15 Exp. delivery time [menu 35: 1=Entered,2=Displayed,3=Hidden] act:EDIX3
  DEMDLVLCOD M*15 Earliest deliv. time [menu 35: 1=Entered,2=Displayed,3=Hidden] act:EDIX3
  DEMDLVLSCR M*15 Earliest deliv. time [menu 99: 1=Form and table,2=Form,3=Table] act:EDIX3
  DEMDLVSCRD M*15 Req. delivery date [menu 99: 1=Form and table,2=Form,3=Table]
  DEMSTACOD M*15 Order type [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DEMSTASCR M*15 Order type [menu 99: 1=Form and table,2=Form,3=Table]
  DEPCOD M*15 Settlement discount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DESAXX AX3 Description
  DESCOD M*15 Comments [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DISCRGCOD1 M*15 Discount/Charge 1 [menu 35: 1=Entered,2=Displayed,3=Hidden] act:SP1
  DISCRGCOD2 M*15 Discount/Charge 2 [menu 35: 1=Entered,2=Displayed,3=Hidden] act:SP2
  DISCRGCOD3 M*15 Discount/Charge 3 [menu 35: 1=Entered,2=Displayed,3=Hidden] act:SP3
  DISCRGCOD4 C*4 Discount/Charge 4 act:SP4
  DISCRGCOD5 C*4 Discount/Charge 5 act:SP5
  DISCRGCOD6 C*4 Discount/Charge 6 act:SP6
  DISCRGCOD7 C*4 Discount/Charge 7 act:SP7
  DISCRGCOD8 C*4 Discount/Charge 8 act:SP8
  DISCRGCOD9 C*4 Discount/Charge 9 act:SP9
  DISCRGSCR1 M*15 Discount/Charge 1 [menu 99: 1=Form and table,2=Form,3=Table] act:SP1
  DISCRGSCR2 M*15 Discount/Charge 2 [menu 99: 1=Form and table,2=Form,3=Table] act:SP2
  DISCRGSCR3 M*15 Discount/Charge 3 [menu 99: 1=Form and table,2=Form,3=Table] act:SP3
  DISCRGSCR4 C*4 Discount/Charge 4 act:SP4
  DISCRGSCR5 C*4 Discount/Charge 5 act:SP5
  DISCRGSCR6 C*4 Discount/Charge 6 act:SP6
  DISCRGSCR7 C*4 Discount/Charge 7 act:SP7
  DISCRGSCR8 C*4 Discount/Charge 8 act:SP8
  DISCRGSCR9 C*4 Discount/Charge 9 act:SP9
  DLVDATCOD M*15 Delivery date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DLVNUMCOD M*4 Delivery no. [menu 1: 1=No,2=Yes]
  DLVNUMSCR M*15 Delivery no. [menu 99: 1=Form and table,2=Form,3=Table]
  DLVPIOCOD M*15 Delivery priority [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DLVPIOCODD M*15 Deliv priority detail [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DLVPIOSCRD M*15 Deliv priority detail [menu 99: 1=Form and table,2=Form,3=Table]
  DLVQTYCOD M*4 Delivered quantity [menu 1: 1=No,2=Yes]
  DLVQTYSCR M*15 Delivered quantity [menu 99: 1=Form and table,2=Form,3=Table]
  DLVTYP M*20 Delivery type [menu 447: 1=Normal,2=Loan,3=Subcontract,4=All types,5=Nonbillable]
  DMECOD M*15 Partial delivery [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DOCFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  DOCNAM ARP Document -> [ARP]ARP0 =[SLT]DOCNAM (AREPORT) !Block
  DPEDATCOD M*15 Departure date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DRNCOD M*15 Route no. [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DRNCODD M*15 Route no. detail [menu 35: 1=Entered,2=Displayed,3=Hidden]
  DRNSCRD M*15 Route no. detail [menu 99: 1=Form and table,2=Form,3=Table]
  DUDDATCOD M*15 Due date basis [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ECCCOD M*15 Major version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCCODMIN M*15 Minor version [menu 35: 1=Entered,2=Displayed,3=Hidden] act:ECC
  ECCSCR M*15 Major version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  ECCSCRMIN M*15 Minor version [menu 99: 1=Form and table,2=Form,3=Table] act:ECC
  EECICTCOD M*15 Incoterm [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ELESGNCOD M*15 Electronic signature [menu 35: 1=Entered,2=Displayed,3=Hidden] act:KPO
  ENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  ENTCOD A*10 Auto journal code
  ETACOD M*15 Arrival time [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ETDCOD M*15 Departure time [menu 35: 1=Entered,2=Displayed,3=Hidden]
  EXPNUM L*8 Export number
  EXTAMTCOD M*15 Expected amount [menu 35: 1=Entered,2=Displayed,3=Hidden]
  EXTAMTSCR M*15 Expected amount [menu 99: 1=Form and table,2=Form,3=Table]
  EXTDLVCOD M*15 Exp delivery date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  EXTDLVSCR M*15 Exp delivery date [menu 99: 1=Form and table,2=Form,3=Table]
  EXTQTYCOD M*15 Expected quantity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  EXTQTYSCR M*15 Expected quantity [menu 99: 1=Form and table,2=Form,3=Table]
  EXTRTNCOD M*15 Expected return date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  EXTRTNCODD M*4 Expected return date [menu 1: 1=No,2=Yes]
  EXTRTNSCRD M*15 Expected return date [menu 99: 1=Form and table,2=Form,3=Table]
  EXYDATCOD M*15 Expiration date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  FLD40RENCOD M*15 VAT adjustment - 40 [menu 35: 1=Entered,2=Displayed,3=Hidden] act:KPO
  FLD41RENCOD M*15 VAT adjustment - 41 [menu 35: 1=Entered,2=Displayed,3=Hidden] act:KPO
  FLOPHYCODD M*15 Physical flow [menu 35: 1=Entered,2=Displayed,3=Hidden]
  FLOPHYSCRD M*15 Physical flow [menu 99: 1=Form and table,2=Form,3=Table]
  FMICOD M*15 Source for delivery [menu 35: 1=Entered,2=Displayed,3=Hidden]
  FMINUMCOD M*4 Back-to-back order no. [menu 1: 1=No,2=Yes]
  FMINUMSCR M*15 Back-to-back order no. [menu 99: 1=Form and table,2=Form,3=Table]
  FMISCR M*15 Source for delivery [menu 99: 1=Form and table,2=Form,3=Table]
  FOCFLGCOD M*4 Free [menu 1: 1=No,2=Yes]
  FOCFLGSCR M*15 Free [menu 99: 1=Form and table,2=Form,3=Table]
  GFY AGF Group -> [AGF]AGF0 =[SLT]GFY (AGRPFCY) !Block
  GROPRICOD M*15 Gross price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  GROPRISCR M*15 Gross price [menu 99: 1=Form and table,2=Form,3=Table]
  HLDCOD M*4 Block status [menu 1: 1=No,2=Yes]
  IDECOD01 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD02 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD1 M*15 Identifier 1 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDECOD2 M*15 Identifier 2 [menu 35: 1=Entered,2=Displayed,3=Hidden]
  IDESCR01 M*15 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR02 M*15 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR1 M*18 Identifier 1 [menu 99: 1=Form and table,2=Form,3=Table]
  IDESCR2 M*18 Identifier 2 [menu 99: 1=Form and table,2=Form,3=Table]
  IMECOD M*15 Invoicing mode [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVCAN M*4 Cancellation invoice [menu 1: 1=No,2=Yes] act:INVCA
  INVCNDCOD M*15 Invoic. term [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVCNDCODD M*15 Invoic. term [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVCNDSCRD M*15 Invoic. term [menu 99: 1=Form and table,2=Form,3=Table]
  INVDTACOD M*15 Invoicing elements [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVNUMCOD M*4 Invoice number [menu 1: 1=No,2=Yes]
  INVPRCCOD M*15 Percentage [menu 35: 1=Entered,2=Displayed,3=Hidden]
  INVPRCSCR M*15 Percentage [menu 99: 1=Form and table,2=Form,3=Table]
  INVTYP M*20 Invoice type [menu 448: 1=Invoice,2=Credit memo,3=Proforma,4=All types]
  INVUPDCOD M*4 Deduct from invoice [menu 1: 1=No,2=Yes]
  INVUPDSCR M*15 Deduct from invoice [menu 99: 1=Form and table,2=Form,3=Table]
  ITMDE1ACOD M*4 Standard description [menu 1: 1=No,2=Yes]
  ITMDES1COD M*15 Standard description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ITMDES1SCR M*15 Standard description [menu 99: 1=Form and table,2=Form,3=Table]
  ITMDESACOD M*4 Translated description [menu 1: 1=No,2=Yes]
  ITMDESCOD M*15 Translated description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ITMDESSCR M*15 Translated description [menu 99: 1=Form and table,2=Form,3=Table]
  ITMSELCOD M*15 Select product [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LASDLVCOD M*4 Last delivery [menu 1: 1=No,2=Yes]
  LASINVCOD M*4 Last invoice [menu 1: 1=No,2=Yes]
  LICPLATCOD M*15 Registration [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LINAMTCOD M*4 Line amount [menu 1: 1=No,2=Yes]
  LINAMTSCR M*15 Line amount [menu 99: 1=Form and table,2=Form,3=Table]
  LINTYPCOD M*4 Line type [menu 1: 1=No,2=Yes]
  LINTYPSCR M*15 Line type [menu 99: 1=Form and table,2=Form,3=Table]
  LNDQTYCOD M*4 Quantity ready [menu 1: 1=No,2=Yes]
  LNDQTYSCR M*15 Quantity ready [menu 99: 1=Form and table,2=Form,3=Table]
  LNDRTNCOD M*15 Loan return date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOCCOD M*15 Location [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOCSCR M*15 Location [menu 99: 1=Form and table,2=Form,3=Table]
  LOTCOD M*15 Lot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  LOTSCR M*15 Lot [menu 99: 1=Form and table,2=Form,3=Table]
  MAXDLVDCOD M*15 Max delivery date [menu 35: 1=Entered,2=Displayed,3=Hidden] act:EDIX3
  MAXDLVDSCR M*15 Max delivery date [menu 99: 1=Form and table,2=Form,3=Table] act:EDIX3
  MAXDLVHCOD M*15 Max delivery time [menu 35: 1=Entered,2=Displayed,3=Hidden] act:EDIX3
  MAXDLVHSCR M*15 Max delivery time [menu 99: 1=Form and table,2=Form,3=Table] act:EDIX3
  MDLCOD M*15 Delivery mode [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MDLCODD M*15 Deliv mode detail [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MDLSCRD M*15 Deliv mode detail [menu 99: 1=Form and table,2=Form,3=Table]
  METCORCOD M*15 Method of correction [menu 35: 1=Entered,2=Displayed,3=Hidden] act:KSP
  MFGNUMCOD M*4 Work order no. [menu 1: 1=No,2=Yes]
  MFGNUMSCR M*15 Work order no. [menu 99: 1=Form and table,2=Form,3=Table]
  MVTDESCOD M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESCOD1 M*15 Movement description [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTDESSCR M*15 Movement description [menu 99: 1=Form and table,2=Form,3=Table]
  MVTPRICOD M*15 Movement price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTPRICOD1 M*15 Mvt price [menu 35: 1=Entered,2=Displayed,3=Hidden]
  MVTPRISCR M*18 Movement price [menu 99: 1=Form and table,2=Form,3=Table]
  NBRCOL C*2 No. of fixed columns
  NBSLOFLG M*4 Sub-lot no. [menu 1: 1=No,2=Yes]
  NETPRICOD M*4 Net price [menu 1: 1=No,2=Yes]
  NETPRISCR M*15 Net price [menu 99: 1=Form and table,2=Form,3=Table]
  NPRFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  NPRNAM ARP Document -> [ARP]ARP0 =[SLT]NPRNAM (AREPORT) !Block
  NTRFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  NTRNAM ARP Document -> [ARP]ARP0 =[SLT]NTRNAM (AREPORT) !Block
  ODLCOD M*15 One order per delivery [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDCAT M*20 Order categories [menu 446: 1=Normal,2=Loan,3=Direct invoice,4=All categories]
  ORDCLECOD M*15 Close unfilled lines [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDCOD M*4 Order [menu 1: 1=No,2=Yes]
  ORDCODD M*4 Order detail no. [menu 1: 1=No,2=Yes]
  ORDSCR M*15 Order [menu 99: 1=Form and table,2=Form,3=Table]
  ORDSCRD M*15 Order detail no. [menu 99: 1=Form and table,2=Form,3=Table]
  ORDUPDCOD M*15 Reactivated order [menu 35: 1=Entered,2=Displayed,3=Hidden]
  ORDUPDSCR M*15 Reactivated order [menu 99: 1=Form and table,2=Form,3=Table]
  PACNBRCOD M*15 Number of packages [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PAYBANCOD M*15 Payment bank ISR [menu 35: 1=Entered,2=Displayed,3=Hidden] act:KSW
  PBYPRCCOD M*15 Probability % [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PCKCOD M*15 Packaging/Capacity [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PCKSCR M*15 Packaging/Capacity [menu 99: 1=Form and table,2=Form,3=Table]
  PFMCOD M*4 Margin [menu 1: 1=No,2=Yes]
  PFMSCR M*15 Margin [menu 99: 1=Form and table,2=Form,3=Table]
  PIHNUMCOD M*4 Purchase invoice no. [menu 1: 1=No,2=Yes]
  PJTCOD M*15 Project [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PJTCODD M*15 Project [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PJTSCRD M*15 Project [menu 99: 1=Form and table,2=Form,3=Table]
  PKGTYP M*15 Packing type [menu 2753: 1=Declarative,2=Postpacking]
  PKTNUM TRS Transaction
  PLICOD M*15 Price list code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PLISCR M*15 Price list code [menu 99: 1=Form and table,2=Form,3=Table]
  PNHNUMCOD M*4 Supplier return no. [menu 1: 1=No,2=Yes]
  PNHNUMSCR M*15 Supplier return no. [menu 99: 1=Form and table,2=Form,3=Table]
  POHNUMCOD M*4 Purchase ord no. [menu 1: 1=No,2=Yes]
  POHNUMSCR M*15 Purchase ord no. [menu 99: 1=Form and table,2=Form,3=Table]
  PRECODCOD M*15 Preparation code [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PRECODSCR M*15 Preparation code [menu 99: 1=Form and table,2=Form,3=Table]
  PRFNUMCOD M*4 Proforma invoice no. [menu 1: 1=No,2=Yes]
  PRITYPCOD M*15 Price - / +tax [menu 35: 1=Entered,2=Displayed,3=Hidden]
  PRNCOD1 M*15 Printing [menu 708: 1=No print,2=Labels,3=.,4=Transfer document,5=Analysis document]
  PRNNBFLG1 M*4 No. prints [menu 1: 1=No,2=Yes]
  PRNNBSCR1 M*15 No. prints [menu 99: 1=Form and table,2=Form,3=Table]
  PRNSCR1 M*15 Printing [menu 99: 1=Form and table,2=Form,3=Table]
  PTECOD M*15 Payment term [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RATCURCOD M*15 Currency rate [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REPCOD M*15 Sales reps [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REPCODD M*15 Rep commission rate [menu 35: 1=Entered,2=Displayed,3=Hidden]
  REPSCRD M*15 Rep commission rate [menu 99: 1=Form and table,2=Form,3=Table]
  RTNDATCODD M*15 Return date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RTNDATSCRD M*15 Return date [menu 99: 1=Form and table,2=Form,3=Table]
  RTNQTYCOD M*4 Return quantity [menu 1: 1=No,2=Yes]
  RTNQTYSCR M*15 Return quantity [menu 99: 1=Form and table,2=Form,3=Table]
  RTNRENCOD M*15 Return reason [menu 35: 1=Entered,2=Displayed,3=Hidden]
  RTNRENSCR M*15 Return reason [menu 99: 1=Form and table,2=Form,3=Table]
  SAUCOD M*15 Sales unit [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SAUCOECOD M*15 SAL-STK conversion [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SAUCOESCR M*15 SAL-STK conv. [menu 99: 1=Form and table,2=Form,3=Table]
  SAUSCR M*15 Sales unit [menu 99: 1=Form and table,2=Form,3=Table]
  SDHTYPCOD M*4 Delivery type [menu 1: 1=No,2=Yes]
  SERCOD M*15 Starting serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERECOD1 M*15 Ending serial number [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SERESCR M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERESCR1 M*15 Ending serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SERSCR M*15 Starting serial number [menu 99: 1=Form and table,2=Form,3=Table]
  SHIDATCOD M*15 Shipment date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SHIDATCODD M*15 Shipment date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SHIDATSCRD M*15 Shipment date [menu 99: 1=Form and table,2=Form,3=Table]
  SHTQTYCOD M*4 Shortage [menu 1: 1=No,2=Yes]
  SHTQTYSCR M*15 Shortage [menu 99: 1=Form and table,2=Form,3=Table]
  SIHORICOD M*4 Invoice origin [menu 1: 1=No,2=Yes]
  SLOCOD M*15 Sublot [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SLOSCR M*15 Sublot [menu 99: 1=Form and table,2=Form,3=Table]
  SNSFLG M*4 Auto print [menu 1: 1=No,2=Yes]
  SNSNAM ARP Document -> [ARP]ARP0 =[SLT]SNSNAM (AREPORT) !Block
  SOHTYPCOD M*20 Order type [menu 1: 1=No,2=Yes]
  SPERFLG M*4 Expiration [menu 1: 1=No,2=Yes]
  SPOTFLG M*4 Potency [menu 1: 1=No,2=Yes]
  SQHNUMCOD M*4 Quote no. [menu 1: 1=No,2=Yes]
  SQHNUMCODD M*4 Quote no. [menu 1: 1=No,2=Yes]
  SQHNUMSCRD M*15 Quote no. [menu 99: 1=Form and table,2=Form,3=Table]
  SRGWAIFLG M*4 Receipt at dock [menu 1: 1=No,2=Yes]
  SRUB1FLG M*4 Heading 1 [menu 1: 1=No,2=Yes]
  SRUB2FLG M*4 Section 2 [menu 1: 1=No,2=Yes]
  SRUB3FLG M*4 Section 3 [menu 1: 1=No,2=Yes]
  SRUB4FLG M*4 Section 4 [menu 1: 1=No,2=Yes]
  SSTENTCOD M*15 Entity/Use [menu 35: 1=Entered,2=Displayed,3=Hidden] act:LTA
  STACOD M*4 Document status [menu 1: 1=No,2=Yes]
  STKFLG M*4 Automatic issue [menu 1: 1=No,2=Yes]
  STOFCYCOD M*15 Shipment site [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STOFCYCODD M*15 Shipment site [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STOFCYSCRD M*15 Shipment site [menu 99: 1=Form and table,2=Form,3=Table]
  STOMVTCOD M*15 Stock transaction [menu 35: 1=Entered,2=Displayed,3=Hidden]
  STRDES A*35 Description
  STRNUM TRS Transaction
  STRTYP M*10 Transaction type [menu 435: 1=Quote,2=Order,3=Contract order,4=Delivery,5=Invoice,6=Customer return,7=Loan return,8=Subcontract material return]
  STRTYPCAR A*2 Alpha no.
  STUCOD M*15 Stock unit [menu 1: 1=No,2=Yes]
  STUSCR M*15 Stock unit [menu 99: 1=Form and table,2=Form,3=Table]
  SVCDATCOD M*15 Benefit period [menu 35: 1=Entered,2=Displayed,3=Hidden] act:SVC
  SVCDATCODD M*15 Benefit period [menu 35: 1=Entered,2=Displayed,3=Hidden]
  SVCDATSCRD M*15 Benefit period [menu 99: 1=Form and table,2=Form,3=Table]
  TRAPLTCOD M*15 Trailer license plate [menu 35: 1=Entered,2=Displayed,3=Hidden]
  TRSCOD A*10 Movement code
  TRSFAM A*10 Stock movement group
  TRSFAMCOD M*15 Transaction group [menu 35: 1=Entered,2=Displayed,3=Hidden]
  UMRNUMCOD M*15 Mandate reference [menu 35: 1=Entered,2=Displayed,3=Hidden] act:SDD
  UNLCOD M*15 Release [menu 35: 1=Entered,2=Displayed,3=Hidden]
  UOMSAIFLG M*4 UOM entry [menu 1: 1=No,2=Yes]
  UOMSAIFLG1 M*4 Enter PAC [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USELIMDCOD M*15 Use-by date [menu 35: 1=Entered,2=Displayed,3=Hidden] act:EDIX3
  USELIMDSCR M*15 Use-by date [menu 99: 1=Form and table,2=Form,3=Table] act:EDIX3
  USEPLCCOD M*15 Location reference [menu 35: 1=Entered,2=Displayed,3=Hidden]
  USEPLCSCR M*15 Location reference [menu 99: 1=Form and table,2=Form,3=Table]
  VACBPRCOD M*15 Tax rule [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VACBPRCODD M*15 Tax rule [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VACITMCOD M*15 Tax level [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VACITMSCR M*15 Tax level [menu 99: 1=Form and table,2=Form,3=Table]
  VCRNUMOCOD M*4 Origin document no. [menu 1: 1=No,2=Yes]
  VCRNUMOSCR M*15 Origin document no. [menu 99: 1=Form and table,2=Form,3=Table]
  VLYDATCOD M*15 Validity date [menu 35: 1=Entered,2=Displayed,3=Hidden]
  VOLCOD M*15 Volume [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WALLQTYCOD M*15 Quantity to allocate [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WALLQTYSCR M*15 Quantity to allocate [menu 99: 1=Form and table,2=Form,3=Table]
  WEICOD M*15 Weight [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WEICODD M*15 Weight detail [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WEISCRD M*15 Weight detail [menu 99: 1=Form and table,2=Form,3=Table]
  WRHCOD M*15 Warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHCOD1 M*15 Line warehouse [menu 35: 1=Entered,2=Displayed,3=Hidden]
  WRHOBY M*15 Single warehouse [menu 1: 1=No,2=Yes]
  WRHSCR M*15 Warehouse [menu 99: 1=Form and table,2=Form,3=Table]
  WRHSCR1 M*15 Line warehouse [menu 99: 1=Form and table,2=Form,3=Table]

## SBODLINK (SBK) - Component qty. calculation (link)
Notes: differs in V9.0 P12 (diff: AT3_SBODLINK.htm); differs in V10 P1 (diff: ATD_SBODLINK.htm)
Keys (first = PK; D = duplicates allowed): SPK0 CLE
Fields:
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPCGRU BPR Group customer -> [BPR]BPR0 =[SBK]BPCGRU (BPARTNER) !Other
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[SBK]BPCINV (BPARTNER) !Other
  BPCORD BPR Sold-to -> [BPR]BPR0 =[SBK]BPCORD (BPARTNER) !Other
  BPCPYR BPR Pay-by -> [BPR]BPR0 =[SBK]BPCPYR (BPARTNER) !Other
  BPTNUM BPT Carrier -> [BPT]BPT0 =[SBK]BPTNUM (BPCARRIER) !Other
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLE A*3 Key
  CPRPRI MD8 Cost price parent product
  CPY CPY Sales company -> [CPY]CPY0 =[SBK]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SBK]CREUSR (AUTILIS) !Other
  ITMREF ITM Product -> [ITM]ITM0 =[SBK]ITMREF (ITMMASTER) !Other
  LINTYP M*20 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  MDL MDL Delivery mode -> [TMD]TMD0 =[SBK]MDL (TABMODELIV) !Other
  NETPRIATI MD8 Prnt pdct Tax incl net price
  NETPRINOT MD8 Prnt pdct Tax excl net price
  PCK PCK Packaging -> [TPA]TPA0 =[SBK]PCK (TABPACKAGE) !Other
  PFM MD1 Parent product margin
  PJT PJT Project -> [PIM]PIM0 =[SBK]PJT (PIMPL) !Block
  PNTITMREF ITS Parent product -> [ITS]ITS0 =PNTITMREF (ITMSALES) !RTZ
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  QTY QTY Parent prdct ord qty
  QTYSTU QTY Parent pdct ord qty STK
  SALFCY FCY Sales site -> [FCY]FCY0 =[SBK]SALFCY (FACILITY) !Other
  SAU UOM Parent product sales unit -> [TUN]TUN0 =[SBK]SAU (TABUNIT) !Other
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SBK]STOFCY (FACILITY) !Other
  STU UOM Stock unit prnt pdct -> [TUN]TUN0 =[SBK]STU (TABUNIT) !Other
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Other act:STC
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SBK]UPDUSR (AUTILIS) !Other
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block

## SDELIVERY (SDH) - Delivery header
Notes: differs in V9.0 P12 (diff: AT3_SDELIVERY.htm)
Keys (first = PK; D = duplicates allowed): SDH0 SDHNUM; SDH1 BPCORD+BPAADD+DLVDAT (D); SDH2 DLVDAT+SDHNUM; SDH3 INVFLG+CFMFLG+SALFCY+BPCINV (D); SDH4 CPY+EECNUMDEB+DLVDAT (D)
Fields:
  ADRVAL M*4 Validated [menu 1: 1=No,2=Yes] act:LTA
  AMTTAX MD1 Tax amount act:KUS
  ARVDAT D Arrival date
  ATDTCOD A*100 AT code act:KPO
  AUUID AUUID Single identifier
  BASTAX MD1 Tax basis act:KUS
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersite [menu 1: 1=No,2=Yes]
  BOLNUM VCR BOL number
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPAINV ADR Invoice address code
  BPCGRU BPR Group customer -> [BPR]BPR0 =[SDH]BPCGRU (BPARTNER) !Block
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[SDH]BPCINV (BPARTNER) !Block
  BPCLOC LOC Customer location -> [STC]STC0 =STOFCY;BPCLOC (STOLOC) !Other
  BPCORD BPR Sold-to -> [BPR]BPR0 =[SDH]BPCORD (BPARTNER) !Block
  BPCPYR BPR Pay-by -> [BPR]BPR0 =[SDH]BPCPYR (BPARTNER) !Block
  BPDADDLIG ADL(3) Delivery address
  BPDCRY CRY Delivery country -> [TCY]TCY0 =[SDH]BPDCRY (TABCOUNTRY) !Block
  BPDCRYNAM NCY Delivery country name
  BPDCTY CTY Delivery city
  BPDNAM NAM(2) Ship-to customer name
  BPDPOSCOD POS Deliv postal code
  BPDSAT SAT Delivery country
  BPIADDLIG ADL(3) Billing address
  BPICRY CRY Country of invoice -> [TCY]TCY0 =[SDH]BPICRY (TABCOUNTRY) !Block
  BPICRYNAM NCY Invoice country name
  BPICTY CTY Invoice city
  BPIEECNUM A*20 EU identification act:DEB
  BPINAM NAM(2) Bill-to customer name
  BPIPOSCOD POS Invoice postal code
  BPISAT SAT Invoice state
  BPTNUM BPT Carrier -> [BPT]BPT0 =[SDH]BPTNUM (BPCARRIER) !Block
  CAI A*10 CAI number act:KAG
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFMFLG M*4 Validated [menu 1: 1=No,2=Yes]
  CHGRAT DCB*5.6 Currency rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CNINAM AIN Invoice contact -> [AIN]AIN0 =CNINAM (CONTACTCRM) !Block
  COPNBR C*1 No. pckg slip copies
  CPY CPY Company -> [CPY]CPY0 =[SDH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SDH]CUR (TABCUR) !Block
  DATVLYCAI D*1 CAI validity date act:KAG
  DAYLTI C*3 Delivery lead time
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[SDH]DIE (GDIE) !Block act:ANA
  DISCRGTYP M*10 Discount / charge type [menu 255: 1=Amount,2=% combined,3=% series] act:SPR
  DLVATI MD1 Book amount +tax
  DLVATIL MD1 Dy amount tax incl. cy
  DLVDAT D Delivery date
  DLVHOU HM Delivery time
  DLVINVATI MD1 Valuation + tax
  DLVINVATIL MD1 Costing tax incl. cy
  DLVINVNOT MD1 Valuation - tax
  DLVINVNOTL MD1 Costing tax excl. cy
  DLVNOT MD1 Book amount -tax
  DLVNOTL MD1 Dy amount tax excl. cy
  DPEDAT D Departure date
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  DSPTOTQTY DCB*9.6 Quantity total
  DSPTOTVOL QTY Volume aggregation
  DSPTOTWEI QTY Weight aggregation
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SDH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SDH]DSPWEU (TABUNIT) !Block
  DUDCLC M*15 Due date origin [menu 407: 1=Invoice date,2=Shipment date]
  EECICT ICT Incoterm -> [ICTH]ICT0 =[SDH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block act:DEB
  EECNUMDEB C*4 EU Intrastat act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  ENTCOD GAU Stock auto journal -> [GAU]GAU0 =[SDH]ENTCOD (GAUTACE) !Block
  ETA HM Arrival time
  ETD HM Departure time
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[SDH]FFWNUM (BPCARRIER) !Block
  GEOCOD GEO Geographic code act:KUS
  GLBDOC M*4 Global document [menu 1: 1=No,2=Yes] act:KPO
  GLBDOCDAT D Global document date act:KPO
  GLBDOCNUM VCR Global document no. act:KPO
  GLBDOCTYP M*15 Global document type [menu 2047: 1=All types,2=Deliveries,3=Customer returns,4=Loan returns,5=Sub-cont material returns,6=Inter-site transfers,7=Sub-contract transfers,8=Sub-contract returns,9=Purchase returns,10=Transport note,11=Orders,12=Quotes,13=Proforma] act:KPO
  GROWEI WEI Gross weight
  HOULTI C*2 Delivery LT in hours
  ICTCTY CTY Incoterm town
  IME M*15 Invoicing mode [menu 408: 1=One/slip,2=One/closed order,3=One/order,4=One/ship-to,5=One/period,6=Manual]
  INSCTYFLG A*1 City interior flag act:KUS
  INVDTA SFI Invoicing element -> [SFI]SFI0 =[SDH]INVDTA (SFOOTINV) !Other act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVDTADSP DSP Distrib key -> [DSP]DSP0 =INVDTADSP;1 (CADSP) !Other act:SFI
  INVDTALIN C*2 Invoice line element act:SPR
  INVDTATYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  INVFLG M*4 Invoiced [menu 1: 1=No,2=Yes]
  INVORN C*3 Invoice sequence no.
  INVPER M*15 Invoice period [menu 406: 1=Per request,2=Daily,3=Weekly,4=10-day period,5=2-week period,6=Monthly]
  LAN LAN Language -> [TLA]TLA0 =[SDH]LAN (TABLAN) !Block
  LBENUM A*10 Label no.
  LICPLATE REGLIC Registration
  LINNBR C*4 Number of lines
  LND M*4 Loan [menu 1: 1=No,2=Yes]
  LNDRTNDAT D Loan return date
  MANDOC DOC Manual document act:KPO
  MDL MDL Delivery mode -> [TMD]TMD0 =[SDH]MDL (TABMODELIV) !Block
  NDEFLG M*4 Print packing slip [menu 1: 1=No,2=Yes]
  NETWEI WEI Net weight
  NPRFLG M*4 Print pick ticket [menu 1: 1=No,2=Yes]
  NTRFLG M*4 Print BOL [menu 1: 1=No,2=Yes]
  ORIFCY FCY Original site -> [FCY]FCY0 =[SDH]ORIFCY (FACILITY) !Block
  PACFLG M*4 Packing completed [menu 1: 1=No,2=Yes]
  PACNBR C*4 Number of packages
  PJT PJT Project -> [PIM]PIM0 =[SDH]PJT (PIMPL) !Block
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  PRFNUM VCR Proforma invoice no.
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[SDH]PRHFCY (FACILITY) !Block
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  PRNNDE M*4 Packing slip printed [menu 1: 1=No,2=Yes]
  PRNNPR M*4 Printed pick ticket [menu 1: 1=No,2=Yes]
  PRPTEX1 TXC Picking header text
  PRPTEX2 TXC Picking footer text
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  REP REP Sales rep -> [REP]REP0 =[SDH]REP (SALESREP) !Block act:REP
  RTNLINNBR C*4 No. of lines returned
  RTNSTA M*15 Return status [menu 451: 1=Not returned,2=Partially returned,3=Returned]
  SALFCY FCY Sales site -> [FCY]FCY0 =[SDH]SALFCY (FACILITY) !Block
  SCO M*4 For subcontract [menu 1: 1=No,2=Yes]
  SDHCAT M*20 Delivery category [menu 490: 1=Normal,2=Loan,3=For subcontract,4=Nonbillable]
  SDHNUM VCR Delivery no.
  SDHTEX1 TXC Deliv header text
  SDHTEX2 TXC Delivery footer text
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;[V]GSUPCLE (TABSDHTYP) !Block
  SFISSTCOD ADI SST tax code -> [ADI]CODE =203;SFISSTCOD (ATABDIV) !Block act:SFI
  SHIDAT D Shipment date
  SHIHOU HM Shipment time
  SIHNUM VCR Invoice no.
  SISDAT D Reversal date
  SISNUM VCR No. invoice to be issued
  SOHNUM VCR Order no.
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SDH]STOFCY (FACILITY) !Block
  TMPSDHNUM VCR Delivery no.
  TRLLICPLATE REGLIC Trailer license plate
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !RTZ
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Other act:STC
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VOL VOL Volume
  VOU UOM Volume unit -> [TUN]TUN0 =[SDH]VOU (TABUNIT) !Block
  VTT A*1 Vertex transaction type act:KUS
  WEU UOM Weight unit -> [TUN]TUN0 =[SDH]WEU (TABUNIT) !Block
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SDELIVERYD (SDD) - Delivery detail
Notes: differs in V9.0 P12 (diff: AT3_SDELIVERYD.htm); differs in V10 P1 (diff: ATD_SDELIVERYD.htm)
Keys (first = PK; D = duplicates allowed): SDD0 SDHNUM+SDDLIN; SDD1 SOHNUM+SOPLIN+SOQSEQ (D); SDD2 ITMREF+SHIDAT+SDHNUM (D); SDD3 BPCORD+BPAADD+ITMREF (D); SDD4 SDHNUM-SDDLIN (D)
Fields:
  AUUID AUUID Single identifier
  BASTAXLIN MD1 Taxable amount act:KUS
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Other
  BPCORD BPC Sold-to -> [BPC]BPC0 =[SDD]BPCORD (BPCUSTOMER) !Other
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CPRPRI MD8 Cost price
  CPY CPY Company -> [CPY]CPY0 =[SDD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DDTANOT MD1 Invoice line allocation elemen act:SFL
  DDTANUM SFI Invoice line allocation elemen -> [SFI]SFI0 =[SDD]DDTANUM (SFOOTINV) !Block act:SFL
  DISCRGREN1 SPR Discount 1 reason -> [SPR]SPR0 =[SDD]DISCRGREN1 (SPREASON) !Block act:SP1
  DISCRGREN2 SPR Discount 2 reason -> [SPR]SPR0 =[SDD]DISCRGREN2 (SPREASON) !Block act:SP2
  DISCRGREN3 SPR Discount 3 reason -> [SPR]SPR0 =[SDD]DISCRGREN3 (SPREASON) !Block act:SP3
  DISCRGREN4 C*4 Discount 4 reason act:SP4
  DISCRGREN5 C*4 Discount 5 reason act:SP5
  DISCRGREN6 C*4 Discount 6 reason act:SP6
  DISCRGREN7 C*4 Discount 7 reason act:SP7
  DISCRGREN8 C*4 Discount 8 reason act:SP8
  DISCRGREN9 C*4 Discount 9 reason act:SP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:SP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:SP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:SP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:SP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:SP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:SP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:SP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:SP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:SP9
  DSPLINFLG M*4 Distribution [menu 1: 1=No,2=Yes]
  DSPLINVOL QTY Line volume
  DSPLINWEI QTY Line weight
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SDD]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SDD]DSPWEU (TABUNIT) !Block
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  FOCFLG M*10 Free [menu 439: 1=No,2=Source,3=Yes]
  GEOCOD GEO Geographic code act:KUS
  GROPRI MD8 Gross price
  IMPNUMLIG L*8 Import line
  INSCTYFLG A*1 City interior flag act:KUS
  INVPRNBOM M*4 Print component on invoice [menu 1: 1=No,2=Yes]
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[SDD]ITMREF (ITMMASTER) !Block
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  LOC LOC Location filter -> [STC]STC0 =STOFCY;LOC (STOLOC) !Other
  LOT LOT Filter lot
  NDEPRNBOM M*4 PS print component [menu 1: 1=No,2=Yes]
  NETPRI MD8 Net price
  NETPRIATI MD8 Net price + tax
  NETPRINOT MD8 Net price - tax
  OALQTYSTU QTY Order qty alloc. STU
  ORILIN L*8 Free line source
  PACQTYSTU QTY Qty packed SAL
  PCK PCK Packaging -> [TPA]TPA0 =[SDD]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PCKFLG M*4 Packing [menu 1: 1=No,2=Yes]
  PFM MD1 Margin
  PJT PJT Project -> [PIM]PIM0 =[SDD]PJT (PIMPL) !Block
  PRELIN L*8 Preparation line
  PRHNUM VCR Pick ticket
  PRIREN SPR Price reason -> [SPR]SPR0 =[SDD]PRIREN (SPREASON) !Block
  PRPTEX TXC Picking ticket line text
  QTY QTY Delivered quantity
  QTYSTU QTY Delivered quantity STU
  RATTAXLIN RAT Tax rates act:KUS
  RCPFLG C*1 Shipment inquiry
  RCPQTYSTU QTY Received STK
  REP1 REP Sales rep 1 -> [REP]REP0 =[SDD]REP1 (SALESREP) !Block act:RE1
  REP2 REP Sales rep 2 -> [REP]REP0 =[SDD]REP2 (SALESREP) !Block act:RE2
  REPCOE CCR Commission factor
  REPRAT1 RAT Commission rate 1 act:RE1
  REPRAT2 RAT Commission rate 2 act:RE2
  RTNQTY QTY Return quantity
  RTNQTYSTU QTY Return quantity STK
  SAU UOM Sales unit -> [TUN]TUN0 =[SDD]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SDDLIN L*8 Delivery line
  SDDTEX TXC Packing slip line text
  SDHCAT M*20 Delivery category [menu 490: 1=Normal,2=Loan,3=For subcontract,4=Nonbillable]
  SDHNUM VCR Delivery no.
  SHIDAT D Shipment date
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHNUM VCR Order no.
  SOPLIN L*8 Order line
  SOQSEQ L*8 Sequence number
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STA A*12 Filter status
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SDD]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STU UOM Stock unit -> [TUN]TUN0 =[SDD]STU (TABUNIT) !Block
  TAXFLG M*4 Taxable flag [menu 1: 1=No,2=Yes] act:KUS
  TAXGEOFLG A*1 Taxed geo flag act:KUS
  TAXREGFLG M*4 Recorded tax flag [menu 1: 1=No,2=Yes] act:KUS
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UNTWEI WEI Unit weight
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYPORI M*15 Source document type [menu 701: 40 values, see local-menus.md]
  VTC A*1 Vertex transaction code act:KUS
  VTS A*1 Vertex transaction sub-type act:KUS
  WEU UOM Weight unit -> [TUN]TUN0 =[SDD]WEU (TABUNIT) !Block
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH
  WRTQTY QTY Qty waiting return
  WRTQTYSTU QTY Qty wtg ret STK

## SINCDET (SND) - Line price review definition
Keys (first = PK; D = duplicates allowed): SND0 COD+CODLIN
Fields:
  AUUID AUUID Single identifier
  COD A*7 Code
  CODLIN L*8 Line
  CODLINCAR A*8 Line
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DELFLG M*4 Deletion [menu 1: 1=No,2=Yes]
  DESAXX AX3 Description
  DESDET A*30
  INCFLD A*10(12) Field
  INCFLDUPD M*20(12) Type [menu 455: 1=Not modified,2=Variation in %,3=Variation in value,4=Assignment]
  INCFRM AFR*80(12) Value
  INCRND DCB*3.4(12) Rounded value
  INCRNDTYP M*20(12) Rounding [menu 746: 1=No rounding,2=Round to the nearest,3=Round down,4=Round up]
  LANDESSHO A*60 Descriptions
  NBFRM C*2 Number
  SELFRM AFR*250 Selection formula
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SINCENT (SNE) - Price update definition
Keys (first = PK; D = duplicates allowed): SNE0 COD
Fields:
  ACS ACS Access code -> [ACS]ACS0 =[SNE]ACS (ACCCOD) !Block
  AUUID AUUID Single identifier
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  COD A*7 Code
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CURNEW CUR New currency -> [TCU]TCU0 =[SNE]CURNEW (TABCUR) !Block
  CUROLD CUR Old currency -> [TCU]TCU0 =[SNE]CUROLD (TABCUR) !Block
  DESAXX AX3 Description
  EXPLNK AFR*60(10) Link expression
  LANDESSHO A*60 Descriptions
  LASCHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  LASCURNEW CUR New currency -> [TCU]TCU0 =[SNE]LASCURNEW (TABCUR) !Block
  LASCUROLD CUR Old currency -> [TCU]TCU0 =[SNE]LASCUROLD (TABCUR) !Block
  LASDATPRO D Last process
  LASENDCRD VCR Last price record
  LASENDDAT D Validity end date
  LASSTRCRD VCR First price record
  LASSTRDAT D Validity start date
  LASVLYDAT D Valid on
  NBTBL C*2 Number of tables
  NBVAR C*2 Number
  PLI SPC Price list code -> [SPC]SPC0 =[SNE]PLI (SPRICCONF) !Other
  PLIENDCRD VCR Last price record
  PLIENDDAT D Validity end date
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  PLISTRCRD VCR First price record
  PLISTRDAT D Validity start date
  SNEENAFLG M*4 Active [menu 1: 1=No,2=Yes]
  TBL ATB(10) Linked tables -> [ATB]CODFIC =[SNE]TBL (ATABLE) !Block
  TYP M*15 Type [menu 454: 1=Copy record,2=Modify record,3=Currency change]
  UPDCRDFLG M*4 Changeable [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATFLG M*4 Changeable [menu 1: 1=No,2=Yes]
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VARCOD A*10(20) Variable
  VARCTL ACL(20) Control table -> [ACL]ACL0 =[SNE]VARCTL (ACTL) !Block
  VARDEF AFR*30(20) Default value
  VARDES DES(20) Description
  VARDESAXX AX3(20) Description
  VARLAS AFR*20(20) Last value
  VARLNG DCB*8(20) Length
  VARTYP ATY(20) Type -> [ATY]CODTYP =[SNE]VARTYP (ATYPE) !Block
  VLYDAT D Valid on

## SINVOICED (SID) - Sales invoice detail
Notes: differs in V9.0 P12 (diff: AT3_SINVOICED.htm); differs in V10 P1 (diff: ATD_SINVOICED.htm)
Keys (first = PK; D = duplicates allowed): SID0 NUM+SIDLIN; SID1 BPCINV+SALFCY+NUM+SIDLIN; SID2 SOHNUM+CREDAT+NUM (D); SID3 SDHNUM+SDDLIN (D); SID4 CONNUM (D); SID5 SRHNUM (D); PJMPJT1 PJT (D)
Fields:
  ALLTYP M*15 Allocation type [menu 294: 1=Global,2=Detailed,3=Not used,4=Shortages/Detailed,5=Shortages/Global,6=Not used]
  AMTATILIN MD1 Amount + tax
  AMTDEPLIN MD1 Discount amount
  AMTLIN MD1 Line amount
  AMTNOTLIN MD1 Amount - tax
  AMTTAXLIN MD1(3) Tax amount
  AUUID AUUID Single identifier
  BASTAXLIN MD1(6) Taxable amount
  BPCINV BPC Bill-to customer -> [BPC]BPC0 =[SID]BPCINV (BPCUSTOMER) !Other
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CONNUM VCR Service contract no.
  CPRPRI MD8 Cost price
  CPY CPY Company -> [CPY]CPY0 =[SID]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DDTADEP MD1 Invoice line allocation elemen act:SFL
  DDTANOT MD1 Invoice line allocation elemen act:SFL
  DDTANUM SFI Invoice line allocation elemen -> [SFI]SFI0 =[SID]DDTANUM (SFOOTINV) !Block act:SFL
  DISCRGREN1 SPR Discount 1 reason -> [SPR]SPR0 =[SID]DISCRGREN1 (SPREASON) !Block act:SP1
  DISCRGREN2 SPR Discount 2 reason -> [SPR]SPR0 =[SID]DISCRGREN2 (SPREASON) !Block act:SP2
  DISCRGREN3 SPR Discount 3 reason -> [SPR]SPR0 =[SID]DISCRGREN3 (SPREASON) !Block act:SP3
  DISCRGREN4 C*4 Discount 4 reason act:SP4
  DISCRGREN5 C*4 Discount 5 reason act:SP5
  DISCRGREN6 C*4 Discount 6 reason act:SP6
  DISCRGREN7 C*4 Discount 7 reason act:SP7
  DISCRGREN8 C*4 Discount 8 reason act:SP8
  DISCRGREN9 C*4 Discount 9 reason act:SP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:SP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:SP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:SP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:SP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:SP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:SP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:SP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:SP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:SP9
  DSPLINFLG M*4 Distribution [menu 1: 1=No,2=Yes]
  DSPLINVOL QTY Line volume
  DSPLINWEI QTY Line weight
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SID]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SID]DSPWEU (TABUNIT) !Block
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EECFLOPHY M*4 Physical flow [menu 1: 1=No,2=Yes] act:DEB
  ENDDAT D End date
  EXPNUM L*8 Export number
  FOCFLG M*10 Free [menu 439: 1=No,2=Source,3=Yes]
  GEOCOD GEO Geographic code act:KUS
  GROPRI MD8 Gross price
  IMPNUMLIG L*8 Import line
  INSCTYFLG A*1 City interior flag act:KUS
  INVDAT D Invoice date
  INVPRC DCB*3.4 Percentage
  INVPRNBOM M*4 Print component on invoice [menu 1: 1=No,2=Yes]
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[SID]ITMREF (ITMMASTER) !Block
  LINEECFLG M*4 Debit line [menu 1: 1=No,2=Yes] act:DEB
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  LOC LOC Location filter -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOT LOT Filter lot
  NETPRI MD8 Net price
  NETPRIATI MD8 Net price + tax
  NETPRINOT MD8 Net price - tax
  NUM VCR Invoice no.
  ORILIN L*8 Free line source
  PERNBR C*4 Periodicity
  PERTYP M*15 Periodicity [menu 635: 1=Days,2=Week,3=10-day period,4=2-week period,5=Month]
  PFM MD1 Margin
  PIDLIN L*8 Purch invoice line
  PITFLG QTY Points management
  PJT PJT Project -> [PIM]PIM0 =PJT (PIMPL) !Block
  PRIORD MD5 Order price
  PRIREN SPR Price reason -> [SPR]SPR0 =[SID]PRIREN (SPREASON) !Block
  QTY QTY Invoiced qty.
  QTYSTU QTY Invoiced STU
  RATTAXLIN RAT Tax rates
  REP1 REP Sales rep 1 -> [REP]REP0 =[SID]REP1 (SALESREP) !Block act:RE1
  REP2 REP Sales rep 2 -> [REP]REP0 =[SID]REP2 (SALESREP) !Block act:RE2
  REPAMT1 MD1 Commission amount 1 act:RE1
  REPAMT2 MD1 Commission amount 2 act:RE2
  REPBAS1 MD1 Commission base 1 act:RE1
  REPBAS2 MD1 Commission base 2 act:RE2
  REPCOE CCR Commission factor
  REPRAT1 RAT Commission rate 1 act:RE1
  REPRAT2 RAT Commission rate 2 act:RE2
  SALFCY FCY Sales site -> [FCY]FCY0 =[SID]SALFCY (FACILITY) !Block
  SAU UOM Sales unit -> [TUN]TUN0 =[SID]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  SGHNUM VCR Transfer document
  SIDLIN L*8 Invoice line
  SIDORI M*15 Source doc type [menu 413: 1=Direct,2=Order,3=Shipment,4=Invoice,5=Quote,6=Return,7=Service contract,8=Service request,9=Transfer,10=Scheduled invoice]
  SIDORILIN L*8 Invoice line
  SIDPSONUM PSO Project doc number -> [PSOH]PSOH0 =[SID]SIDPSONUM (PJMSOLITMH) !Block act:PJM
  SIDSEQNUM L*8 Line act:PJM
  SIDTEX TXC Line text
  SIHORINUM VCR Invoice no.
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SOQSEQ L*8 Sequence number
  SRDLIN L*8 Return line
  SRENUM SRE Service request -> [SRE]SRE0 =[SID]SRENUM (SERREQUEST) !Other
  SRHNUM VCR Return no.
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STA A*12 Filter status
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SID]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  STRDAT D Start date
  STU UOM Stock unit -> [TUN]TUN0 =[SID]STU (TABUNIT) !Block
  TAXFLG M*4 Taxable flag [menu 1: 1=No,2=Yes] act:KUS
  TAXGEOFLG A*1 Taxed geo flag act:KUS
  TAXREGFLG M*4 Recorded tax flag [menu 1: 1=No,2=Yes] act:KUS
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  VCRINVCNDLIN L*8 Due date line
  VCRINVCNDTYP M*15 Due date origin [menu 476: 23 values, see local-menus.md]
  VTC A*1 Vertex transaction code act:KUS
  VTS A*1 Vertex transaction sub-type act:KUS
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SINVOICEV (SIV) - Costing sales invoice
Notes: differs in V9.0 P12 (diff: AT3_SINVOICEV.htm); differs in V10 P1 (diff: ATD_SINVOICEV.htm)
Keys (first = PK; D = duplicates allowed): SIV0 NUM; SIV1 SIHORI+SIHORINUM (D); SIV2 INVTYP+NUM
Fields:
  ADRVAL M*4 Validated [menu 1: 1=No,2=Yes] act:LTA
  ARVDAT D Arrival date
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPCGRU BPR Group customer -> [BPR]BPR0 =[SIV]BPCGRU (BPARTNER) !Block
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[SIV]BPCINV (BPARTNER) !Block
  BPCORD BPR Sold-to -> [BPR]BPR0 =[SIV]BPCORD (BPARTNER) !Block
  BPDADDLIG ADL(3) Delivery address
  BPDCRY CRY Delivery country -> [TCY]TCY0 =[SIV]BPDCRY (TABCOUNTRY) !Block
  BPDCRYNAM NCY Delivery country name
  BPDCTY CTY Delivery city
  BPDNAM NAM(2) Ship-to customer name
  BPDPOSCOD POS Deliv postal code
  BPDSAT SAT Delivery country
  BPIEECNUM A*20 EU identification act:DEB
  BPINAM NAM(2) Bill-to customer name
  BPRFCT FCT Factor -> [FCT]FCT0 =[SIV]BPRFCT (FACTOR) !Block act:FCT
  BPRPAY BPR Pay-by -> [BPR]BPR0 =[SIV]BPRPAY (BPARTNER) !Block
  CMGNUM CMG Marketing campaign -> [CMG]CMG0 =[SIV]CMGNUM (CMARKETING) !RTZ
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CNINAM AIN Invoice contact -> [AIN]AIN0 =CNINAM (CONTACTCRM) !Block
  CNOREN ADI Memo reason -> [ADI]CODE =8;CNOREN (ATABDIV) !Block
  COPNBE C*1 Credit memo copy no.
  COPNBR C*1 Invoice copies
  CPY CPY Company -> [CPY]CPY0 =[SIV]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SIV]CUR (TABCUR) !Block
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DISCRGTYP M*10 Discount / charge type [menu 255: 1=Amount,2=% combined,3=% series] act:SPR
  DPEDAT D Departure date
  DSPTOTQTY DCB*9.6 Quantity total
  DSPTOTVOL QTY Volume aggregation
  DSPTOTWEI QTY Weight aggregation
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SIV]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SIV]DSPWEU (TABUNIT) !Block
  EECICT ICT Incoterm -> [ICTH]ICT0 =[SIV]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block act:DEB
  EECNATR TEC Transaction nature -> [TEC]TEC0 =EECNATR;[V]GSUPCLE (TABEECNAT) !Block act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block act:DEB
  EECSCHR TSC Intrastat rule -> [TSC]TSC0 =EECSCHR;[V]GSUPCLE (TABEECSCH) !Block act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  ENTCOD GAU Stock auto journal -> [GAU]GAU0 =[SIV]ENTCOD (GAUTACE) !Block
  ETA HM Arrival time
  ETD HM Departure time
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[SIV]FFWNUM (BPCARRIER) !Block
  GEOCOD GEO Geographic code act:KUS
  ICTCTY CTY Incoterm town
  INSATI MD1(4) Prepayment amt +tax
  INSCTYFLG A*1 City interior flag act:KUS
  INSLIN C*3(4) line
  INSORDNUM VCR(4) Order no.
  INVCNOSTA M*4 Credit memo status on invoice [menu 1: 1=No,2=Yes]
  INVDAT D Invoice date
  INVDTA SFI Invoicing element -> [SFI]SFI0 =[SIV]INVDTA (SFOOTINV) !Other act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVDTADSP DSP Distrib key -> [DSP]DSP0 =INVDTADSP;1 (CADSP) !Other act:SFI
  INVDTALIN C*2 Invoice line element act:SPR
  INVDTATYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  INVREF REF Reference
  INVSTA M*15 Status [menu 2261: 1=Not posted,2=Not used,3=Posted]
  INVTYP M*15 Invoice category [menu 645: 1=Invoice,2=Credit memo,3=Debit note,4=Credit note,5=Proforma]
  LAN LAN Language -> [TLA]TLA0 =[SIV]LAN (TABLAN) !Block
  LICPLATE REGLIC Registration
  LINNBR C*4 Number of lines
  NUM VCR Invoice no.
  OPGNUM VCR Marketing operation
  OPGTYP A*3 Operation type
  ORIFCY FCY Original site -> [FCY]FCY0 =[SIV]ORIFCY (FACILITY) !Block
  PAM TAM(4) Payment method -> [TAM]TAM0 =PAM;[V]GSUPCLE (TABPAM) !Block
  PIHNUM VCR Purchase invoice no.
  PJT PJT Project -> [PIM]PIM0 =[SIV]PJT (PIMPL) !BSRA
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  REP REP Sales rep -> [REP]REP0 =[SIV]REP (SALESREP) !Block act:REP
  SALFCY FCY Sales site -> [FCY]FCY0 =[SIV]SALFCY (FACILITY) !Block
  SFISSTCOD ADI SST tax code -> [ADI]CODE =203;SFISSTCOD (ATABDIV) !Block act:SFI
  SIHCFMFLG M*4 Electronic signature [menu 1: 1=No,2=Yes] act:KPO
  SIHNUMEND VCR Sequence number act:KPO
  SIHORI M*12 Document origin [menu 413: 1=Direct,2=Order,3=Shipment,4=Invoice,5=Quote,6=Return,7=Service contract,8=Service request,9=Transfer,10=Scheduled invoice]
  SIHORIDAT D Source date
  SIHORINUM VCR Original document no.
  SIHORITYP M*15 Source doc type [menu 476: 23 values, see local-menus.md]
  SIHTEX1 TXC Invoice header text
  SIHTEX2 TXC Invoice footer text
  SIVTYP TSV Sales invoice type -> [TSV]TSV0 =SIVTYP;[V]GSUPCLE (TABSIVTYP) !Block
  SRGLOCDEF LOC Dock location -> [STC]STC0 =STOFCY;SRGLOCDEF (STOLOC) !Other
  STARPT M*4 Printing [menu 1: 1=No,2=Yes]
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SIV]STOFCY (FACILITY) !Block
  STOMVTFLG M*4 Stock transaction [menu 1: 1=No,2=Yes]
  TRLLICPLATE REGLIC Trailer license plate
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !RTZ
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Other act:STC
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VTT A*1 Vertex transaction type act:KUS

## SORDER (SOH) - Sales orders - header
Notes: differs in V9.0 P12 (diff: AT3_SORDER.htm); differs in V10 P1 (diff: ATD_SORDER.htm)
Keys (first = PK; D = duplicates allowed): SOH0 SOHNUM; SOH1 BPCORD+CUSORDREF (D); SOH2 CUSORDREF+BPCORD (D); SOH3 ORDSTA+BPCORD (D); SOH4 ORDSTA+SOHNUM; SOH5 ORDSTA+INVSTA+SOHCAT (D); SOH6 SOHNUMEND (D)
Fields:
  ADRVAL M*4 Validated [menu 1: 1=No,2=Yes] act:LTA
  ALLLINNBR C*4 No. of lines to allocate
  ALLSTA M*15 Allocation status [menu 416: 1=Not allocated,2=Partly allocated,3=Allocated]
  ALLTYP M*15 Allocation type [menu 450: 1=Global,2=Detailed]
  AMTTAX MD1 Tax amount act:KUS
  APPFLG M*15 Signed [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  AUUID AUUID Single identifier
  BASTAX MD1 Tax basis act:KUS
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersite [menu 1: 1=No,2=Yes]
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPAINV ADR Invoice address code
  BPAORD ADR Order addr code
  BPAPYR ADR Address pay-by
  BPCADDLIG ADL(3) Order address
  BPCCRY CRY Country of order -> [TCY]TCY0 =[SOH]BPCCRY (TABCOUNTRY) !Block
  BPCCRYNAM NCY Order country name
  BPCCTY CTY Order city
  BPCGRU BPR Group customer -> [BPR]BPR0 =[SOH]BPCGRU (BPARTNER) !Block
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[SOH]BPCINV (BPARTNER) !Block
  BPCNAM NAM(2) Sold-to customer name
  BPCORD BPR Sold-to -> [BPR]BPR0 =[SOH]BPCORD (BPARTNER) !Block
  BPCPOSCOD POS Order postal code
  BPCPYR BPR Pay-by -> [BPR]BPR0 =[SOH]BPCPYR (BPARTNER) !Block
  BPCSAT SAT Order state
  BPDADDLIG ADL(3) Delivery address
  BPDCRY CRY Delivery country -> [TCY]TCY0 =[SOH]BPDCRY (TABCOUNTRY) !Block
  BPDCRYNAM NCY Delivery country name
  BPDCTY CTY Delivery city
  BPDNAM NAM(2) Ship-to customer name
  BPDPOSCOD POS Deliv postal code
  BPDSAT SAT Delivery country
  BPIADDLIG ADL(3) Billing address
  BPICRY CRY Country of invoice -> [TCY]TCY0 =[SOH]BPICRY (TABCOUNTRY) !Block
  BPICRYNAM NCY Invoice country name
  BPICTY CTY Invoice city
  BPIEECNUM A*20 EU identification act:DEB
  BPINAM NAM(2) Bill-to customer name
  BPIPOSCOD POS Invoice postal code
  BPISAT SAT Invoice state
  BPTNUM BPT Carrier -> [BPT]BPT0 =[SOH]BPTNUM (BPCARRIER) !Block
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CCLDAT D Date closed
  CCLREN ADI Closing reason -> [ADI]CODE =201;CCLREN (ATABDIV) !Block
  CDTSTA M*15 Credit status [menu 419: 1=OK,2=On hold,3=Limit exceeded,4=Prepayment not paid,5=Credit card]
  CDTSTAP M*15 Previous credit status [menu 419: 1=OK,2=On hold,3=Limit exceeded,4=Prepayment not paid,5=Credit card]
  CHGRAT DCB*5.6 Currency rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLELINNBR C*4 No. closed lines
  CMGNUM CMG Marketing campaign -> [CMG]CMG0 =[SOH]CMGNUM (CMARKETING) !RTZ
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CNINAM AIN Invoice contact -> [AIN]AIN0 =CNINAM (CONTACTCRM) !Block
  CNTNAM AIN Person to contact -> [AIN]AIN0 =CNTNAM (CONTACTCRM) !Block
  COPNBR C*1 No. copies acknowledgement of receipt
  CPY CPY Company -> [CPY]CPY0 =[SOH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SOH]CUR (TABCUR) !Block
  CUSORDREF A*20 Customer order ref
  DAYLTI C*3 Delivery lead time
  DEMDLVDAT D Req. delivery date
  DEMDLVHOU HM Exp. delivery time act:EDIX3
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[SOH]DIE (GDIE) !Block act:ANA
  DISCRGTYP M*10 Discount / charge type [menu 255: 1=Amount,2=% combined,3=% series] act:SPR
  DLRATI MD1 Amount to deliver +tax
  DLRNOT MD1 Amount to deliver -tax
  DLVLINNBR C*4 No. of delivered lines
  DLVPIO M*15 Delivery priority [menu 410: 1=Normal,2=Urgent,3=Critical]
  DLVSTA M*15 Delivery status [menu 417: 1=Not delivered,2=Partly delivered,3=Delivered]
  DME M*15 Partial delivery [menu 414: 1=Authorized,2=Full delivery line,3=Full order line]
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  DSPTOTQTY DCB*9.6 Quantity total
  DSPTOTVOL QTY Volume aggregation
  DSPTOTWEI QTY Weight aggregation
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SOH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SOH]DSPWEU (TABUNIT) !Block
  EECICT ICT Incoterm -> [ICTH]ICT0 =[SOH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[SOH]FFWNUM (BPCARRIER) !Block
  GEOCOD GEO Geographic code act:KUS
  HLDCOD ADI Block code -> [ADI]CODE =204;HLDCOD (ATABDIV) !Block
  HLDCODP ADI Previous block code -> [ADI]CODE =204;HLDCODP (ATABDIV) !Block
  HLDDAT D Block/Release date
  HLDDATP D Previous block date
  HLDSTA M*10 Block status [menu 491: 1=OK,2=On hold]
  HLDTIM HM Block/Release time
  HLDTIMP HM Previous block time
  HLDUSR AUS Block/Release user -> [AUS]CODUSR =[SOH]HLDUSR (AUTILIS) !Block
  HLDUSRP AUS Previous block user -> [AUS]CODUSR =[SOH]HLDUSRP (AUTILIS) !Block
  ICTCTY CTY Incoterm town
  IME M*15 Invoicing mode [menu 408: 1=One/slip,2=One/closed order,3=One/order,4=One/ship-to,5=One/period,6=Manual]
  INRATI MD1 To invoice including tax
  INRNOT MD1 To invoice excluding tax
  INRSCHATI MD1 Invoicing open item
  INRSCHNOT MD1 Invoicing open item
  INSCTYFLG A*1 City interior flag act:KUS
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  INVDTA SFI Invoicing element -> [SFI]SFI0 =[SOH]INVDTA (SFOOTINV) !Other act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVDTADSP DSP Distrib key -> [DSP]DSP0 =INVDTADSP;1 (CADSP) !Other act:SFI
  INVDTALIN C*2 Invoice line element act:SPR
  INVDTATYP M*3 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  INVLINNBR C*4 No. invoiced lines
  INVSTA M*15 Invoice status [menu 418: 1=Not invoiced,2=Partly invoiced,3=Invoiced]
  LAN LAN Language -> [TLA]TLA0 =[SOH]LAN (TABLAN) !Block
  LASDLVDAT D Last delivery date
  LASDLVNUM VCR Last delivery no.
  LASINVDAT D Last invoice date
  LASINVNUM VCR Last invoice no.
  LINNBR C*4 Number of lines
  LNDRTNDAT D Loan return date
  MDL MDL Delivery mode -> [TMD]TMD0 =[SOH]MDL (TABMODELIV) !Block
  OCNFLG M*4 Print acknowledgment [menu 1: 1=No,2=Yes]
  OCNPRN M*4 Acknowledgment printed [menu 1: 1=No,2=Yes]
  ODL M*4 One order per delivery [menu 1: 1=No,2=Yes]
  OPGNUM VCR Marketing operation
  OPGTYP A*3 Operation type
  ORDATI MD1 Line amt. + tax
  ORDATIL MD1 Line amt. + tax (company)
  ORDCLE M*4 Close unfilled lines [menu 1: 1=No,2=Yes]
  ORDDAT D Order date
  ORDINVATI MD1 Valuation + tax
  ORDINVATIL MD1 Costing tax incl. cy
  ORDINVNOT MD1 Valuation - tax
  ORDINVNOTL MD1 Costing tax excl. cy
  ORDNOT MD1 Line amt. - tax
  ORDNOTL MD1 Line amt. - tax (company)
  ORDSTA M*15 Order state [menu 415: 1=Open,2=Closed]
  ORIFCY FCY Original site -> [FCY]FCY0 =[SOH]ORIFCY (FACILITY) !Block
  PFMTOT MD1 Total margin
  PJT PJT Project -> [PIM]PIM0 =[SOH]PJT (PIMPL) !Block
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  PRFNUM VCR Proforma invoice no.
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  REP REP Sales rep -> [REP]REP0 =[SOH]REP (SALESREP) !Block act:REP
  REVNUM C*4 Revision no.
  SALFCY FCY Sales site -> [FCY]FCY0 =[SOH]SALFCY (FACILITY) !Block
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;[V]GSUPCLE (TABSDHTYP) !Block
  SFISSTCOD ADI SST tax code -> [ADI]CODE =203;SFISSTCOD (ATABDIV) !Block act:SFI
  SHIADECOD A*35 Shipper / receiver code
  SHIDAT D Shipment date
  SINUM A*10 Integrale part no. act:SMI
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHCFMFLG M*4 Electronic signature [menu 1: 1=No,2=Yes] act:KPO
  SOHNUM VCR Order no.
  SOHNUMEND VCR Sequence number act:KPO
  SOHTEX1 TXC Ord header text
  SOHTEX2 TXC Ord footer text
  SOHTYP TSO Order type -> [TSO]TSO0 =SOHTYP;[V]GSUPCLE (TABSOHTYP) !Block
  SOHVALDAT D Validation date act:KPO
  SQHNUM VCR Quote no.
  SRENUM SRE Service request -> [SRE]SRE0 =[SOH]SRENUM (SERREQUEST) !RTZ
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SOH]STOFCY (FACILITY) !Block
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Other act:STC
  UNL M*4 Release [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VCRINVCNDDAT D Beginning due date
  VLYDATCON D Validity date
  VTT A*1 Vertex transaction type act:KUS

## SORDERC (SOC) - Sales orders - early / late
Notes: differs in V9.0 P12 (diff: AT3_SORDERC.htm); differs in V10 P1 (diff: ATD_SORDERC.htm)
Keys (first = PK; D = duplicates allowed): SOC0 SOHNUM+SOPLIN; SOC1 BPCORD+BPAADD+ITMREF (D); SOC2 CUSORDREF+BPCORD+BPAADD+ITMREFBPC
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Delivery address
  BPCORD BPC Sold-to -> [BPC]BPC0 =[SOC]BPCORD (BPCUSTOMER) !Other
  BPIEECNUM A*20 EU identification act:DEB
  CPLAMT MD1 Actual amount
  CPY CPY Company -> [CPY]CPY0 =[SOC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUMDATEAR D Cumulative customer start date
  CUSORDREF A*20 Customer order ref
  DLVQTYCUM QTY Total delivered
  DSPPRC C*3(7) Weekly quantity split
  EARDAT D Calculated early / late date
  EARDATCUS D Customer early/late date
  EARHOU HM Calculated early / late time
  EARHOUCUS HM Customer early/late time
  EARQTY QTY Calculated early / late quanti
  EARQTYCUS QTY Customer early/late qty
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EECICT ICT Incoterm -> [ICTH]ICT0 =[SOC]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EXTAMT MD1 Expected amount
  EXTQTY QTY Planned quantity
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[SOC]FFWNUM (BPCARRIER) !Block
  FIMHOR C*4 Firm horizon
  ICTCTY CTY Incoterm town
  ITMDES DES Description
  ITMDES1 DES Description
  ITMDESBPC DES Customer description
  ITMREF ITM Product -> [ITM]ITM0 =[SOC]ITMREF (ITMMASTER) !Block
  ITMREFBPC A*20 Customer product
  ITMREVNUM C*4 Revision no.
  ORDQTYCUM QTY Total ordered
  PJT PJT Project -> [PIM]PIM0 =[SOC]PJT (PIMPL) !Block
  PLI SPC Price list code -> [SPC]SPC0 =[SOC]PLI (SPRICCONF) !Other
  SALFCY FCY Sales site -> [FCY]FCY0 =[SOC]SALFCY (FACILITY) !Block
  SAU UOM Sales unit -> [TUN]TUN0 =[SOC]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SOCTEX TXC Product text
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SOC]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[SOC]STU (TABUNIT) !Block
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  VLYDATITM D Validity date

## SORDERP (SOP) - Sales orders - price
Notes: differs in V9.0 P12 (diff: AT3_SORDERP.htm); differs in V10 P1 (diff: ATD_SORDERP.htm)
Keys (first = PK; D = duplicates allowed): SOP0 SOHNUM+SOPLIN+SOPSEQ; SOP1 BPCORD+BPAADD+ITMREF+ENDDAT (D); SOP2 SOQSTA+SOHCAT+STOFCY+BPCORD+BPAADD (D); SOP3 SOHNUM+SOPLIN (D); SOP4 SOQSTA+SOHCAT+SALFCY+BPCINV (D)
Fields:
  AUUID AUUID Single identifier
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPCINV BPC Bill-to customer -> [BPC]BPC0 =[SOP]BPCINV (BPCUSTOMER) !Other
  BPCORD BPC Sold-to -> [BPC]BPC0 =[SOP]BPCORD (BPCUSTOMER) !Other
  BPCSALPRI MD8 Consumer sales price act:EDIX3
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CONNUM VCR Service contract no.
  CPRPRI MD8 Cost price
  CPY CPY Company -> [CPY]CPY0 =[SOP]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DISCRGREN1 SPR Discount 1 reason -> [SPR]SPR0 =[SOP]DISCRGREN1 (SPREASON) !Block act:SP1
  DISCRGREN2 SPR Discount 2 reason -> [SPR]SPR0 =[SOP]DISCRGREN2 (SPREASON) !Block act:SP2
  DISCRGREN3 SPR Discount 3 reason -> [SPR]SPR0 =[SOP]DISCRGREN3 (SPREASON) !Block act:SP3
  DISCRGREN4 C*4 Discount 4 reason act:SP4
  DISCRGREN5 C*4 Discount 5 reason act:SP5
  DISCRGREN6 C*4 Discount 6 reason act:SP6
  DISCRGREN7 C*4 Discount 7 reason act:SP7
  DISCRGREN8 C*4 Discount 8 reason act:SP8
  DISCRGREN9 C*4 Discount 9 reason act:SP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:SP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:SP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:SP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:SP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:SP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:SP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:SP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:SP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:SP9
  ENDDAT D Validity end date
  EXPNUM L*8 Export number
  FOCFLG M*10 Free [menu 439: 1=No,2=Source,3=Yes]
  GROPRI MD8 Gross price
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[SOP]ITMREF (ITMMASTER) !Block
  ITMREFBPC A*20 Customer product
  LINREVNUM C*4 Revision no.
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  NETPRI MD8 Net price
  NETPRIATI MD8 Net price + tax
  NETPRINOT MD8 Net price - tax
  ORILIN L*8 Free line source
  PFM MD1 Margin
  PRIREN SPR Price reason -> [SPR]SPR0 =[SOP]PRIREN (SPREASON) !Block
  REP1 REP Sales rep 1 -> [REP]REP0 =[SOP]REP1 (SALESREP) !Block act:RE1
  REP2 REP Sales rep 2 -> [REP]REP0 =[SOP]REP2 (SALESREP) !Block act:RE2
  REPCOE CCR Commission factor
  REPRAT1 RAT Commission rate 1 act:RE1
  REPRAT2 RAT Commission rate 2 act:RE2
  SALFCY FCY Sales site -> [FCY]FCY0 =[SOP]SALFCY (FACILITY) !Other
  SAU UOM Sales unit -> [TUN]TUN0 =[SOP]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SOPSEQ L*8 Sequence
  SOQSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  SQDLIN L*8 Quote line
  SQHNUM VCR Quote no.
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SOP]STOFCY (FACILITY) !Other
  STRDAT D Validity start date
  STU UOM Stock unit -> [TUN]TUN0 =[SOP]STU (TABUNIT) !Block
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## SORDERQ (SOQ) - Sales orders - quantities
Notes: differs in V9.0 P12 (diff: AT3_SORDERQ.htm); differs in V10 P1 (diff: ATD_SORDERQ.htm)
Keys (first = PK; D = duplicates allowed): SOQ0 SOHNUM+SOPLIN+SOQSEQ; SOQ1 STOFCY+SHIDAT+BPCORD+BPAADD+ITMREF (D); SOQ2 ITMREF+SHIDAT (D); SOQ3 SOQSTA+SHIDAT+DLVPIOCMP+SOHNUM+SOPLIN+SOQSEQ; SOQ4 SOQSTA+SOHCAT+STOFCY+BPCORD+BPAADD (D); SOQ6 SHIDAT+SOHNUM+SOPLIN+SOQSEQ; SOQPJM1 PJT+ITMREF+SOHNUM+SOPLIN+SOQSEQ
Fields:
  ALLQTY QTY Allocated qty.
  ALLQTYSTU QTY Allocated qty STU
  ALLTYP M*15 Allocation type [menu 450: 1=Global,2=Detailed]
  AUUID AUUID Single identifier
  BASTAXLIN MD1 Taxable amount act:KUS
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPCORD BPC Sold-to -> [BPC]BPC0 =[SOQ]BPCORD (BPCUSTOMER) !Other
  BPTNUM BPT Carrier -> [BPT]BPT0 =[SOQ]BPTNUM (BPCARRIER) !Block
  CAD M*7 Sequencing [menu 278: 1=Day,2=Week,3=Month]
  CCLDAT D Date closed
  CCLREN ADI Closing reason -> [ADI]CODE =201;CCLREN (ATABDIV) !Block
  CPY CPY Company -> [CPY]CPY0 =[SOQ]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYLTI C*3 Delivery LT in days
  DDTANOT MD1 Invoice line allocation elemen act:SFL
  DDTANUM SFI Invoice line allocation elemen -> [SFI]SFI0 =[SOQ]DDTANUM (SFOOTINV) !Block act:SFL
  DEMDLVDAT D Req. delivery date
  DEMDLVHOU HM Delivery request time
  DEMDLVREF A*20 Delivery req ref
  DEMNUM VCR Order no.
  DEMSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  DLVDAY C*2 Day
  DLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  DLVPIO M*15 Delivery priority [menu 410: 1=Normal,2=Urgent,3=Critical]
  DLVPIOCMP C*1 Compl priority del
  DLVQTY QTY Delivered quantity
  DLVQTYSTU QTY Delivered qty STU
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  DSPLINFLG M*4 Distribution [menu 1: 1=No,2=Yes]
  DSPLINVOL QTY Line volume
  DSPLINWEI QTY Line weight
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SOQ]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SOQ]DSPWEU (TABUNIT) !Block
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  EXTDLVDAT D Exp delivery date
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  FMILIN L*8 Back-to-back order line
  FMINUM VCR Back-to-back order no.
  FMISEQ L*8 Back-to-back order seq.
  GEOCOD GEO Geographic code act:KUS
  IMPNUMLIG L*8 Import line
  INSCTYFLG A*1 City interior flag act:KUS
  INVAMT MC1 Amount invoiced
  INVFLG M*4 Invoiced [menu 1: 1=No,2=Yes]
  INVPRNBOM M*4 Print component on invoice [menu 1: 1=No,2=Yes]
  INVQTY QTY Invoiced qty.
  INVQTYSTU QTY Invoiced STU
  ITMREF ITM Product -> [ITM]ITM0 =[SOQ]ITMREF (ITMMASTER) !Block
  LINORDNUM L*8 Origin line act:EDIX3
  LOC LOC Location filter -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOT LOT Filter lot
  LPRQTY QTY Qty. on list prep.
  LPRQTYSTU QTY Qty list prep STU
  MAXDLVDAT D Max delivery date act:EDIX3
  MAXDLVHOU HM Max delivery time act:EDIX3
  MDL MDL Delivery mode -> [TMD]TMD0 =[SOQ]MDL (TABMODELIV) !Block
  MON C*2 Months
  NDEPRNBOM M*4 PS print component [menu 1: 1=No,2=Yes]
  OCNPRNBOM M*4 Print component on acknowledgement [menu 1: 1=No,2=Yes]
  ODLQTY QTY Qty. in process
  ODLQTYSTU QTY STK qty. in process
  OPRQTY QTY Qty. being prepared
  OPRQTYSTU QTY Qty being prep STU
  ORDDAT D Order date
  ORIQTY QTY Initial order quantity
  PCK PCK Packaging -> [TPA]TPA0 =[SOQ]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PERENDDAT D Period end date
  PERNBRDAY C*3 Number of period days
  PERSTRDAT D Period start date
  PITFLG QTY Points management
  PJT PJT Project -> [PIM]PIM0 =[SOQ]PJT (PIMPL) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Sequence number
  PRECOD PRC Preparation code
  PREQTY QTY Qty. prepared
  PREQTYSTU QTY Qty prepared STU
  QTY QTY Ordered quantity
  QTYSTU QTY Ordered STU
  RATTAXLIN RAT Tax rates act:KUS
  SALFCY FCY Sales site -> [FCY]FCY0 =[SOQ]SALFCY (FACILITY) !Block
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  SHIDAT D Shipment date
  SHIHOU HM Shipment time
  SHTQTY QTY Shortage
  SHTQTYSTU QTY Qty shortage STU
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SOQPSONUM PSO Project doc number -> [PSOH]PSOH0 =[SOQ]SOQPSONUM (PJMSOLITMH) !Block act:PJM
  SOQSEQ L*8 Sequence number
  SOQSEQNUM L*8 Line act:PJM
  SOQSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  SOQTEX TXC Line text
  STA A*12 Filter status
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SOQ]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  TAXFLG M*4 Taxable flag [menu 1: 1=No,2=Yes] act:KUS
  TAXGEOFLG A*1 Taxed geo flag act:KUS
  TAXREGFLG M*4 Recorded tax flag [menu 1: 1=No,2=Yes] act:KUS
  TDLQTY QTY Qty to deliver
  TDLQTYSTU QTY STK qty to deliver
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USELIMDAT D Use-by date act:EDIX3
  USEPLC A*30 Location reference
  VTC A*1 Vertex transaction code act:KUS
  VTS A*1 Vertex transaction sub-type act:KUS
  WEE C*2 Week no.
  YEA C*4 Year

## SPPRTCONF (SPP) - Price catalog definition
Keys (first = PK; D = duplicates allowed): SPP0 COD
Fields:
  AUUID AUUID Single identifier
  BPCCRI A*150 Customer filter
  BPCEND BPC To customer -> [BPC]BPC0 =[SPP]BPCEND (BPCUSTOMER) !Other
  BPCSTR BPC From customer -> [BPC]BPC0 =[SPP]BPCSTR (BPCUSTOMER) !Other
  BPRCRI A*150 BP filter
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  COD SPP Catalog -> [SPP]SPP0 =[SPP]COD (SPPRTCONF) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SPP]CUR (TABCUR) !Other
  DAT D Date
  DESAXX AX3 Description
  FLGCHGTYP M*4 Rate type flag [menu 1: 1=No,2=Yes]
  FLGCUR M*4 Currency flag [menu 1: 1=No,2=Yes]
  FLGPRITYP M*4 Price type flag [menu 1: 1=No,2=Yes]
  ITMCRI A*150 Product filter
  ITMEND ITS To product -> [ITS]ITS0 =[SPP]ITMEND (ITMSALES) !Other
  ITMSTR ITS From product -> [ITS]ITS0 =[SPP]ITMSTR (ITMSALES) !Other
  ITSCRI A*150 Product/Sales filter
  LANDESSHO A*60 Descriptions
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  SALFCY FCY Sales site -> [FCY]FCY0 =[SPP]SALFCY (FACILITY) !Other
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SPP]STOFCY (FACILITY) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SPRICFICH (SPF) - Customer prices (records)
Keys (first = PK; D = duplicates allowed): SPF0 PLI+PLICRD
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  EXPNUM L*8 Export number
  LINNBR C*4 Number of lines
  PLI SPC Price list code -> [SPC]SPC0 =[SPF]PLI (SPRICCONF) !Delete
  PLICRD VCR Price list record
  PLICRDIDX A*10 Index
  PLIENDDAT D Validity end date
  PLISTRDAT D Validity start date
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SPRICINCR (SPI) - Price increase
Keys (first = PK; D = duplicates allowed): SPI0 PLI+PLICRD+PLILIN
Fields:
  AUUID AUUID Single identifier
  COMCOE CCR Comm factor
  CPNITMREF ITM Component -> [ITM]ITM0 =[SPI]CPNITMREF (ITMMASTER) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CRIT1 SPU Criteria 1
  CRIT2 SPU Criteria 2
  CRIT3 SPU Criterion 3
  CRIT4 SPU Criterion 4
  CRIT5 SPU Criterion 5
  CUR CUR Currency -> [TCU]TCU0 =[SPI]CUR (TABCUR) !Block
  DCGVAL MD8(9) Charge/discount value
  EXPNUM L*8 Export number
  FOCAMTBKT MD1 Free Class
  FOCAMTMIN MD1 Free threshold
  FOCITMREF ITM Free product -> [ITM]ITM0 =[SPI]FOCITMREF (ITMMASTER) !Block
  FOCQTY QTY Free quantity
  FOCQTYBKT QTY Free Class
  FOCQTYMIN QTY Free threshold
  FOCUOM UOM Unit -> [TUN]TUN0 =[SPI]FOCUOM (TABUNIT) !Block
  IMPNUMLIG L*8 Import line
  LTI C*3 Lead time
  MAXAMT MD1 Maximum value
  MAXQTY QTY Maximum quantity
  MINAMT MD1 Minimum value
  MINQTY QTY Minimum quantity
  PLI SPC Price list code -> [SPC]SPC0 =[SPI]PLI (SPRICCONF) !Delete
  PLICRD VCR Price list record
  PLICRI SPX Criteria
  PLICRI1 SPU Criteria 1
  PLICRI2 SPU Criteria 2
  PLICRI3 SPU Criterion 3
  PLICRI4 SPU Criterion 4
  PLICRI5 SPU Criterion 5
  PLIENDDAT D Validity end date
  PLILIN L*8 Line
  PLISTRDAT D Validity start date
  PRI MD8 Price
  PRIDIV C*4 Price factor
  UOM UOM Unit -> [TUN]TUN0 =[SPI]UOM (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SPRICLINK (SPK) - Sales price list search
Notes: differs in V9.0 P12 (diff: AT3_SPRICLINK.htm); differs in V10 P1 (diff: ATD_SPRICLINK.htm)
Keys (first = PK; D = duplicates allowed): SPK0 CLE
Fields:
  AUUID AUUID Single identifier
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPCGRU BPC Group customer -> [BPC]BPC0 =[SPK]BPCGRU (BPCUSTOMER) !Other
  BPCINV BPC Bill-to customer -> [BPC]BPC0 =[SPK]BPCINV (BPCUSTOMER) !Other
  BPTNUM BPT Carrier -> [BPT]BPT0 =[SPK]BPTNUM (BPCARRIER) !Other
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CLE A*3 Key
  CPY CPY Sales company -> [CPY]CPY0 =[SPK]CPY (COMPANY) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SPK]CREUSR (AUTILIS) !Other
  CRY CRY Country -> [TCY]TCY0 =[SPK]CRY (TABCOUNTRY) !Other
  CSTTYP M*15 Cost type [menu 219: 1=Standard,2=Revised,3=Budgeted,4=Simulated]
  CUSORDREF A*20 Customer order ref
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EECICT ICT Incoterm -> [ICTH]ICT0 =[SPK]EECICT (INCOTERM) !Other
  FOCITM M*4 Free product [menu 1: 1=No,2=Yes]
  LINTYP M*20 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  LINTYP_A M*30 Line category [menu 469: 1=Standard and product,2=Component and option and variant]
  LINTYP_B M*30 Product cat. [menu 470: 1=Standard line,2=Kit line,3=BOM line]
  LINTYP_C M*30 Component C. [menu 471: 1=Component,2=Option,3=Variant]
  MDL MDL Delivery mode -> [TMD]TMD0 =[SPK]MDL (TABMODELIV) !Other
  PCK PCK Packaging -> [TPA]TPA0 =[SPK]PCK (TABPACKAGE) !Other
  PJT PJT Project -> [PIM]PIM0 =[SPK]PJT (PIMPL) !Block
  PJTNUM PJT Project number -> [PIM]PIM0 =[SPK]PJTNUM (PIMPL) !Block
  PLIBPRCNR M*15 BP concerns [menu 2210: 1=Outside group,2=Group,3=All]
  PNTITMREF ITS Parent product -> [ITS]ITS0 =PNTITMREF (ITMSALES) !RTZ
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Other
  SALFCY FCY Sales site -> [FCY]FCY0 =[SPK]SALFCY (FACILITY) !Other
  SAT SAT Subdivision
  SOHTYP TSO Order type -> [TSO]TSO0 =SOHTYP;[V]GSUPCLE (TABSOHTYP) !Other
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SPK]STOFCY (FACILITY) !Other
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Other act:STC
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SPK]UPDUSR (AUTILIS) !Other
  USEPLC A*30 Location reference
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Other

## SPRICPRTQ (SPQ) - Sales price catalog
Keys (first = PK; D = duplicates allowed): SPQ0 COD+BPCORD+ITMREF+SPQLIN; SPQ1 COD+ITMREF+BPCORD+SPQLIN
Fields:
  AUUID AUUID Single identifier
  BPCORD BPR Sold-to -> [BPR]BPR0 =[SPQ]BPCORD (BPARTNER) !Delete
  COD SPP Catalog -> [SPP]SPP0 =[SPQ]COD (SPPRTCONF) !Delete
  COMCOE CCR Comm factor
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SPQ]CUR (TABCUR) !Other
  DAT D Date
  DCGVAL MD8(9) Charge/discount value
  FOCITMREF ITM Free product -> [ITM]ITM0 =[SPQ]FOCITMREF (ITMMASTER) !Delete
  FOCQTY QTY Free quantity
  FOCUOM UOM Unit -> [TUN]TUN0 =[SPQ]FOCUOM (TABUNIT) !Other
  GROPRI MD8 Gross price
  ITMREF ITM Product -> [ITM]ITM0 =[SPQ]ITMREF (ITMMASTER) !Delete
  LTI C*3 Lead time
  MINQTY QTY Minimum quantity
  NETPRI MD8 Net price
  PLI SPC(12) Price list code -> [SPC]SPC0 =[SPQ]PLI (SPRICCONF) !Delete
  PLICRD VCR(12) Price list record
  PLILIN L*8(12) Line
  PLIREN SPR(12) Reason -> [SPR]SPR0 =[SPQ]PLIREN (SPREASON) !Other
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  SALFCY FCY Sales site -> [FCY]FCY0 =[SPQ]SALFCY (FACILITY) !Delete
  SPQLIN L*8 Line
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SPQ]STOFCY (FACILITY) !Delete
  UOM UOM Unit -> [TUN]TUN0 =[SPQ]UOM (TABUNIT) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## SQUOTE (SQH) - Quote header
Notes: differs in V9.0 P12 (diff: AT3_SQUOTE.htm)
Keys (first = PK; D = duplicates allowed): SQH0 SQHNUM; SQH1 BPCORD+CUSQUOREF (D); SQH2 SQHNUMEND (D)
Fields:
  ADRVAL M*4 Validated [menu 1: 1=No,2=Yes] act:LTA
  AMTTAX MD1 Tax amount act:KUS
  APPFLG M*15 Signed [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  AUUID AUUID Single identifier
  BASTAX MD1 Tax basis act:KUS
  BPAADD ADR Delivery address
  BPAORD ADR Order addr code
  BPCADDLIG ADL(3) Address
  BPCCRY CRY Country -> [TCY]TCY0 =[SQH]BPCCRY (TABCOUNTRY) !Block
  BPCCRYNAM NCY Country name
  BPCCTY CTY City
  BPCNAM NAM(2) Customer name
  BPCORD BPR Customer -> [BPR]BPR0 =[SQH]BPCORD (BPARTNER) !Block
  BPCPOSCOD POS Postal code
  BPCSAT SAT Order state
  BPDADDLIG ADL(3) Delivery address
  BPDCRY CRY Delivery country -> [TCY]TCY0 =[SQH]BPDCRY (TABCOUNTRY) !Block
  BPDCRYNAM NCY Delivery country name
  BPDCTY CTY Delivery city
  BPDNAM NAM(2) Ship-to customer name
  BPDPOSCOD POS Deliv postal code
  BPDSAT SAT Delivery country
  BPIEECNUM A*20 EU identification act:DEB
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CFMLINNBR C*4 Number of validated lines
  CHGRAT DCB*5.6 Currency rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CNCNAM AIN Order contact -> [AIN]AIN0 =CNCNAM (CONTACTCRM) !Block
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  COPNBR C*1 No. copies quote
  CPY CPY Company -> [CPY]CPY0 =[SQH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SQH]CUR (TABCUR) !Block
  CUSQUOREF A*20 Quote reference
  DAYLTI C*3 Delivery LT in days
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[SQH]DIE (GDIE) !Block act:ANA
  DISCRGTYP M*10 Discount / charge type [menu 255: 1=Amount,2=% combined,3=% series] act:SPR
  DSPTOTQTY DCB*9.6 Quantity total
  DSPTOTVOL QTY Volume aggregation
  DSPTOTWEI QTY Weight aggregation
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SQH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SQH]DSPWEU (TABUNIT) !Block
  EECICT ICT Incoterm -> [ICTH]ICT0 =[SQH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[SQH]FFWNUM (BPCARRIER) !Block
  GEOCOD GEO Geographic code act:KUS
  ICTCTY CTY Incoterm town
  INSCTYFLG A*1 City interior flag act:KUS
  INVDTA SFI Invoicing element -> [SFI]SFI0 =[SQH]INVDTA (SFOOTINV) !Other act:SFI
  INVDTAAMT DCB*11.4 % or amt inv el act:SFI
  INVDTADSP DSP Distrib key -> [DSP]DSP0 =INVDTADSP;1 (CADSP) !Other act:SFI
  INVDTALIN C*2 Invoice line element act:SPR
  INVDTATYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  LAN LAN Language -> [TLA]TLA0 =[SQH]LAN (TABLAN) !Block
  LINNBR C*4 Number of lines
  ORDDAT D Order date
  ORDNBR C*2 Number of orders
  PBYPRC C*3 Probability %
  PFMTOT MD1 Total margin
  PJT PJT Project -> [PIM]PIM0 =[SQH]PJT (PIMPL) !Block
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  PRFNUM VCR Proforma invoice no.
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  QUOATI MD1 Line amt. + tax
  QUOATIL MD1 Line amt. + tax (company)
  QUODAT D Quote date
  QUOINVATI MD1 Valuation + tax
  QUOINVATIL MD1 Costing tax incl. cy
  QUOINVNOT MD1 Valuation - tax
  QUOINVNOTL MD1 Costing tax excl. cy
  QUONOT MD1 Line amt. - tax
  QUONOTL MD1 Line amt. - tax (company)
  QUOPRN M*4 Printed quote [menu 1: 1=No,2=Yes]
  QUOSTA M*15 Quote status [menu 430: 1=Not ordered,2=Partially ordered,3=Completely ordered]
  REP REP Sales rep -> [REP]REP0 =[SQH]REP (SALESREP) !Block act:REP
  SALFCY FCY Sales site -> [FCY]FCY0 =[SQH]SALFCY (FACILITY) !Block
  SFISSTCOD ADI SST tax code -> [ADI]CODE =203;SFISSTCOD (ATABDIV) !Block act:SFI
  SINUM A*10 Integrale part no. act:SMI
  SOHNUM VCR Order no.
  SOHTYP TSO Order type -> [TSO]TSO0 =SOHTYP;[V]GSUPCLE (TABSOHTYP) !Block
  SQHCFMFLG M*4 Electronic signature [menu 1: 1=No,2=Yes] act:KPO
  SQHNUM VCR Quote no.
  SQHNUMEND VCR Sequence number act:KPO
  SQHTEX1 TXC Quote header text
  SQHTEX2 TXC Quote footer text
  SQHTYP TSQ Quote type -> [TSQ]TSQ0 =SQHTYP;[V]GSUPCLE (TABSQHTYP) !Block
  SQHVALDAT D Validation date act:KPO
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SQH]STOFCY (FACILITY) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VLYDAT D Validity date
  VTT A*1 Vertex transaction type act:KUS

## SQUOTED (SQD) - Quote detail
Notes: differs in V9.0 P12 (diff: AT3_SQUOTED.htm); differs in V10 P1 (diff: ATD_SQUOTED.htm)
Keys (first = PK; D = duplicates allowed): SQD0 SQHNUM+SQDLIN; SQD1 ORDFLG+SALFCY+BPCORD (D); PJMPJT1 PJT (D)
Fields:
  AUUID AUUID Single identifier
  BASTAXLIN MD1 Taxable amount act:KUS
  BPAADD ADR Delivery address
  BPCORD BPC Sold-to -> [BPC]BPC0 =[SQD]BPCORD (BPCUSTOMER) !Other
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CPRPRI MD8 Cost price
  CPY CPY Company -> [CPY]CPY0 =[SQD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYLTI C*3 Delivery LT in days
  DDTANOT MD1 Invoice line allocation elemen act:SFL
  DDTANUM SFI Invoice line allocation elemen -> [SFI]SFI0 =[SQD]DDTANUM (SFOOTINV) !Block act:SFL
  DISCRGREN1 SPR Discount 1 reason -> [SPR]SPR0 =[SQD]DISCRGREN1 (SPREASON) !Block act:SP1
  DISCRGREN2 SPR Discount 2 reason -> [SPR]SPR0 =[SQD]DISCRGREN2 (SPREASON) !Block act:SP2
  DISCRGREN3 SPR Discount 3 reason -> [SPR]SPR0 =[SQD]DISCRGREN3 (SPREASON) !Block act:SP3
  DISCRGREN4 C*4 Discount 4 reason act:SP4
  DISCRGREN5 C*4 Discount 5 reason act:SP5
  DISCRGREN6 C*4 Discount 6 reason act:SP6
  DISCRGREN7 C*4 Discount 7 reason act:SP7
  DISCRGREN8 C*4 Discount 8 reason act:SP8
  DISCRGREN9 C*4 Discount 9 reason act:SP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:SP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:SP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:SP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:SP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:SP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:SP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:SP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:SP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:SP9
  DLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  DSPLINFLG M*4 Distribution [menu 1: 1=No,2=Yes]
  DSPLINVOL QTY Line volume
  DSPLINWEI QTY Line weight
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[SQD]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[SQD]DSPWEU (TABUNIT) !Block
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  FOCFLG M*10 Free [menu 439: 1=No,2=Source,3=Yes]
  GEOCOD GEO Geographic code act:KUS
  GROPRI MD8 Gross price
  IMPNUMLIG L*8 Import line
  INSCTYFLG A*1 City interior flag act:KUS
  INVPRNBOM M*4 Print component on invoice [menu 1: 1=No,2=Yes]
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[SQD]ITMREF (ITMMASTER) !Block
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  NDEPRNBOM M*4 PS print component [menu 1: 1=No,2=Yes]
  NETPRI MD8 Net price
  NETPRIATI MD8 Net price + tax
  NETPRINOT MD8 Net price - tax
  OCNPRNBOM M*4 Print component on acknowledgement [menu 1: 1=No,2=Yes]
  ORDFLG M*4 Ordered [menu 1: 1=No,2=Yes]
  ORDQTY QTY Ordered qty.
  ORILIN L*8 Free line source
  PFM MD1 Margin
  PJT PJT Project -> [PIM]PIM0 =[SQD]PJT (PIMPL) !Block
  PRIREN SPR Price reason -> [SPR]SPR0 =[SQD]PRIREN (SPREASON) !Block
  QTY QTY Quote quantity
  QUODAT D Quote date
  RATTAXLIN RAT Tax rates act:KUS
  REP1 REP Sales rep 1 -> [REP]REP0 =[SQD]REP1 (SALESREP) !Block act:RE1
  REP2 REP Sales rep 2 -> [REP]REP0 =[SQD]REP2 (SALESREP) !Block act:RE2
  REPCOE CCR Commission factor
  REPRAT1 RAT Commission rate 1 act:RE1
  REPRAT2 RAT Commission rate 2 act:RE2
  SALFCY FCY Sales site -> [FCY]FCY0 =[SQD]SALFCY (FACILITY) !Block
  SAU UOM Sales unit -> [TUN]TUN0 =[SQD]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SQDLIN L*8 Quote line
  SQDPSONUM PSO Project doc number -> [PSOH]PSOH0 =[SQD]SQDPSONUM (PJMSOLITMH) !Block act:PJM
  SQDSEQNUM L*8 Line act:PJM
  SQDTEX TXC Line text
  SQHNUM VCR Quote no.
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SQD]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[SQD]STU (TABUNIT) !Block
  TAXFLG M*4 Taxable flag [menu 1: 1=No,2=Yes] act:KUS
  TAXGEOFLG A*1 Taxed geo flag act:KUS
  TAXREGFLG M*4 Recorded tax flag [menu 1: 1=No,2=Yes] act:KUS
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  VTC A*1 Vertex transaction code act:KUS
  VTS A*1 Vertex transaction sub-type act:KUS

## SRETURN (SRH) - Sales return header
Notes: differs in V9.0 P12 (diff: AT3_SRETURN.htm); differs in V10 P1 (diff: ATD_SRETURN.htm)
Keys (first = PK; D = duplicates allowed): SRH0 SRHNUM; SRH1 SDHNUM (D); SRH2 CPY+EECNUMDEB+RTNDAT (D); SRH3 RTNDAT+SRHNUM
Fields:
  ARVDATR D Arrival date
  ATDTCODR A*100 AT code act:KPO
  AUUID AUUID Single identifier
  AUZUSR A*5 Authorized user
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersite [menu 1: 1=No,2=Yes]
  BPAADD ADR Delivery address
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[SRH]BPCINV (BPARTNER) !Block
  BPCORD BPR Sold-to -> [BPR]BPR0 =[SRH]BPCORD (BPARTNER) !Block
  BPDADDLIG ADL(3) Delivery address
  BPDCRY CRY Delivery country -> [TCY]TCY0 =[SRH]BPDCRY (TABCOUNTRY) !Block
  BPDCRYNAM NCY Delivery country name
  BPDCTY CTY Delivery city
  BPDNAM NAM(2) Ship-to customer name
  BPDPOSCOD POS Deliv postal code
  BPDSAT SAT Delivery country
  BPIEECNUM A*20 EU identification act:DEB
  CCE CCE Dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CPY CPY Company -> [CPY]CPY0 =[SRH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DIE DIE Dimension type code -> [DIE]DIE0 =[SRH]DIE (GDIE) !Block act:ANA
  DLVDAT D Delivery date
  DPEDATR D Departure date
  EECICT ICT Incoterm -> [ICTH]ICT0 =[SRH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EECNAT TEC Transaction nature -> [TEC]TEC0 =EECNAT;[V]GSUPCLE (TABEECNAT) !Block act:DEB
  EECNUMDEB C*4 EU Intrastat act:DEB
  EECSCH TSC Intrastat rule -> [TSC]TSC0 =EECSCH;[V]GSUPCLE (TABEECSCH) !Block act:DEB
  EECTRN M*15 Intrastat transp. mode [menu 237: 1=By sea,2=By rail,3=By road,4=By air,5=By mail,6=.,7=By inland navigation,8=Internal navigation,9=Self-propelled] act:DEB
  ENTCOD GAU Stock auto journal -> [GAU]GAU0 =[SRH]ENTCOD (GAUTACE) !Block
  ETAR HM Arrival time
  ETDR HM Departure time
  EXPNUM L*8 Export number
  EXTRTNDAT D Expected return date
  EXYDAT D Expiration date
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[SRH]FFWNUM (BPCARRIER) !Block
  GLBDOCDATR D Global document date act:KPO
  GLBDOCNUMR VCR Global document no. act:KPO
  GLBDOCR M*4 Global document [menu 1: 1=No,2=Yes] act:KPO
  GLBDOCTYPR M*15 Global document type [menu 2047: 1=All types,2=Deliveries,3=Customer returns,4=Loan returns,5=Sub-cont material returns,6=Inter-site transfers,7=Sub-contract transfers,8=Sub-contract returns,9=Purchase returns,10=Transport note,11=Orders,12=Quotes,13=Proforma] act:KPO
  ICTCTY CTY Incoterm town
  LAN LAN Language -> [TLA]TLA0 =[SRH]LAN (TABLAN) !Block
  LICPLATER REGLIC Registration
  LNDRTN M*4 Loan return [menu 1: 1=No,2=Yes]
  MANDOCR DOC Manual document act:KPO
  ORIFCY FCY Original site -> [FCY]FCY0 =[SRH]ORIFCY (FACILITY) !Block
  PJT PJT Project -> [PIM]PIM0 =[SRH]PJT (PIMPL) !Block
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  RTNDAT D Return date
  SALFCY FCY Sales site -> [FCY]FCY0 =[SRH]SALFCY (FACILITY) !Block
  SCORTN M*4 Subcon. mat. rtrns. [menu 1: 1=No,2=Yes]
  SDHNUM VCR Loan delivery no.
  SRGLOCDEF LOC Dock location -> [STC]STC0 =STOFCY;SRGLOCDEF (STOLOC) !Other
  SRHCAT M*20 Return category [menu 493: 1=Normal,2=Loan,3=For subcontract]
  SRHCFMFLG M*4 Signed [menu 1: 1=No,2=Yes] act:KPO
  SRHNUM VCR Return no.
  SRHTEX1 TXC Return header text
  SRHTEX2 TXC Return footer text
  SRHTYP TRE Return type -> [TRE]TRE0 =SRHTYP;[V]GSUPCLE (TABSRHTYP) !Block
  STOFCY FCY Receiving site -> [FCY]FCY0 =[SRH]STOFCY (FACILITY) !Block
  STOFCYDLV FCY Shipment site -> [FCY]FCY0 =[SRH]STOFCYDLV (FACILITY) !Block
  TMPSRHNUM VCR Return no.
  TRLLICPLATER REGLIC Trailer license plate
  TRSCOD ADI Movement code -> [ADI]CODE =14;TRSCOD (ATABDIV) !RTZ
  TRSFAM ADI Transaction group -> [ADI]CODE =9;TRSFAM (ATABDIV) !RTZ
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRHE WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SRETURND (SRD) - Sales return detail
Notes: differs in V9.0 P12 (diff: AT3_SRETURND.htm); differs in V10 P1 (diff: ATD_SRETURND.htm)
Keys (first = PK; D = duplicates allowed): SRD0 SRHNUM+SRDLIN; SRD1 SDHNUM+SDDLIN (D); SRD2 SIHNUM+RTNCNOFLG (D)
Fields:
  AUUID AUUID Single identifier
  CPY CPY Company -> [CPY]CPY0 =[SRD]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SRD]CUR (TABCUR) !Block
  DLVQTY QTY Delivered qty.
  EXPNUM L*8 Export number
  EXTQTY QTY Expected return qty.
  EXTQTYSTU QTY Fcast retn qty STK
  IMPNUMLIG L*8 Import line
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[SRD]ITMREF (ITMMASTER) !Block
  NETPRI MD8 Net price
  NETPRIATI MD8 Net price + tax
  NETPRINOT MD8 Net price - tax
  ORDUPD M*4 Reactivated order [menu 1: 1=No,2=Yes]
  PJT PJT Project -> [PIM]PIM0 =[SRD]PJT (PIMPL) !Block
  PNDLIN L*8 Suppl return line
  PNHNUM VCR Supplier return no.
  PRIORD MD5 Order price
  QTY QTY Return quantity
  QTYSTU QTY Return quantity STK
  RTNCNOFLG M*4 Credit memo subject [menu 1: 1=No,2=Yes]
  RTNDAT D Return date
  RTNINVUPD M*4 Ret deduct from inv [menu 1: 1=No,2=Yes]
  RTNREN ADI Return reason -> [ADI]CODE =7;RTNREN (ATABDIV) !Block
  RTNSTOUPD M*4 Actual stock return [menu 1: 1=No,2=Yes]
  SAU UOM Sales unit -> [TUN]TUN0 =[SRD]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SCSDAT D Reversal date
  SCSLIN L*8 AAE line
  SCSNUM VCR No. credit note to be issued
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  SIDLIN L*8 Credit memo line
  SIHNUM VCR Credit memo no.
  SRDLIN L*8 Return line
  SRDTEX TXC Return line text
  SRHCAT M*20 Return category [menu 493: 1=Normal,2=Loan,3=For subcontract]
  SRHNUM VCR Return no.
  STOFCY FCY Receiving site -> [FCY]FCY0 =[SRD]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[SRD]STU (TABUNIT) !Block
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  WRH WRH Warehouse -> [WRH]WRH0 =WRH (WAREHOUSE) !Other act:WRH

## SVCRFOOT (SVF) - Sales document - footer el.
Keys (first = PK; D = duplicates allowed): SVF0 VCRNUM+VCRTYP+DTA; SVF1 VCRTYP+VCRNUM+DTA; SVF2 VCRTYP+VCRNUM+CLCORD+DTA; SVF3 NUM+VCRTYP+VCRNUM+DTA
Fields:
  AMTCOD M*10 Amount code [menu 269: 1=Percent,2=Amount]
  AUUID AUUID Single identifier
  CLCORD C*2 Calculation order
  CPY CPY Company -> [CPY]CPY0 =[SVF]CPY (COMPANY) !Other
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SVF]CUR (TABCUR) !Block
  DTA SFI Invoicing element -> [SFI]SFI0 =[SVF]DTA (SFOOTINV) !Other
  DTAAMT DCB*9.2 % or amt inv el
  DTADEP MD1 Discount amount
  DTADEPFLG M*4 Subject to discount [menu 1: 1=No,2=Yes]
  DTADSP DSP Distrib key -> [DSP]DSP0 =DTADSP;1 (CADSP) !Other
  DTANET MD1(10) Subject amount elt
  DTANOT MD1 Amount element -tax
  DTATYP M*6 Value type [menu 243: 1=Exclude tax,2=Include tax]
  DTAVAT VAT(10) Tax -> [TVT]TVT0 =DTAVAT(indice);[V]GSUPCLE (TABVAT) !Block
  DTAVATAMT MD1(10) Tax amount
  DTAVATDEP MD1(10) Discount amount
  DTAVATNOT MD1(10) Amount element -tax
  DTAVATRAT RAT(10) Rate
  NUM SIH Invoice number -> [SIV]SIV0 =[SVF]NUM (SINVOICEV) !Other
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 476: 23 values, see local-menus.md]

## SVCRINVCND (SVIC) - Scheduled invoice
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): SVIC0 VCRTYP+VCRNUMORI+VCRLINORI+VCRSEQORI; SVIC1 VCRTYP+VCRNUMORI (D); SVIC2 VCRTYP-VCRNUMORI+VCRLINORI+VCRSEQORI
Fields:
  AMTATI MD1 Amount + tax
  AMTNOT MD1 Amount - tax
  AUUID AUUID Single identifier
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[SVIC]BPCINV (BPARTNER) !Block
  BPCORD BPC Sold-to -> [BPC]BPC0 =[SVIC]BPCORD (BPCUSTOMER) !Other
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SVIC]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[SVIC]CUR (TABCUR) !Other
  INVCND INVCND Code -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  INVCNDTYP M*10 Open item type [menu 2420: 1=Normal,2=Fixed percentage,3=Frequency]
  ITMREF ITM Product -> [ITM]ITM0 =[SVIC]ITMREF (ITMMASTER) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  NETPRIATI MD8 Net price + tax
  NETPRINOT MD8 Net price - tax
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  QTY QTY Delivered quantity
  SALFCY FCY Sales site -> [FCY]FCY0 =[SVIC]SALFCY (FACILITY) !Block
  SAU UOM Sales unit -> [TUN]TUN0 =[SVIC]SAU (TABUNIT) !Block
  STOFCY FCY Shipment site -> [FCY]FCY0 =[SVIC]STOFCY (FACILITY) !Block
  TOT_CN_AMT MD1 Amount
  TOT_CN_QTY QTY Quantity
  TOT_EXT_AMT MD1 Amount
  TOT_EXT_QTY QTY Quantity
  TOT_INV_AMT MD1 Amount invoiced
  TOT_INV_QTY QTY Invoiced quantity
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SVIC]UPDUSR (AUTILIS) !Other
  VCRINVCNDDAT D Date
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYP M*15 Entry type [menu 476: 23 values, see local-menus.md]

## SVCRINVCNDD (SVICD) - Scheduled invoice
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): SVICD0 VCRTYP+VCRNUMORI+VCRLINORI+VCRSEQORI+VCRINVCNDLIN; SVICD1 VCRTYP+VCRNUMORI+VCRLINORI+VCRSEQORI (D); SVICD2 VCRTYP+VCRNUMORI (D); SVICD3 VCRTYP-VCRNUMORI+VCRLINORI+VCRSEQORI+VCRINVCNDLIN; SVICD4 VCRNUMORI+VCRLINORI+NEXINVDAT+VCRINVCNDLIN (D)
Fields:
  AMT_CONS_GRP MC1
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SVICD]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[SVICD]CUR (TABCUR) !Block
  DNETPRIATI MD8 Net price + tax
  DNETPRINOT MD8 Net price - tax
  INVCNDAMTATI MC1 Amount + tax
  INVCNDAMTNOT MC1 Amount - tax
  INVCNDLIN L*8 Line number
  INVCNDQTY QTY Quantity
  INVCNDSTA M*15 Status [menu 2419: 1=To be invoiced,2=Invoiced,3=Credit memo,4=Closed,5=Included on invoice,6=Included on credit memo]
  INVPERCENT DCB*3.4 Percentage
  IS_CONS_GRP M*4 [menu 1: 1=No,2=Yes]
  IS_EXTRABILL M*5 Excess [menu 1: 1=No,2=Yes]
  IS_RES_SPLIT M*4 Split [menu 1: 1=No,2=Yes]
  LINORI_SPLIT L*8 Origin line
  LIN_CN_AMT MC1 Amount
  LIN_CN_QTY QTY Quantity
  LIN_EXT_AMT MC1 Amount
  LIN_EXT_QTY QTY Quantity
  LIN_INV_PRI MD8 Price
  MODDAT D Change date
  MODFLG M*15 Modification [menu 2421: 1=No,2=Price,3=Quantity,4=Splitting,5=Grouping,6=Generation]
  NEXINVDAT D Next invoice
  PERFROM D Period start
  PERTO D Period end
  PRC_CONS_GRP DCB*3.4
  QTY_CONS_GRP QTY
  SAU UOM Sales unit -> [TUN]TUN0 =[SVICD]SAU (TABUNIT) !Block
  SIDLIN L*8 Invoice line
  SIHNUM VCR Invoice no.
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SVICD]UPDUSR (AUTILIS) !Other
  VCRINVCNDLIN L*8 Line number
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYP M*15 Entry type [menu 476: 23 values, see local-menus.md]

## SVCRVAT (SVV) - Sales document - tax
Notes: differs in V9.0 P12 (diff: AT3_SVCRVAT.htm); differs in V10 P1 (diff: ATD_SVCRVAT.htm)
Keys (first = PK; D = duplicates allowed): SVV0 VCRTYP+VCRNUM+VAT; SVV1 VCRTYP+VCRNUM+VATTYP+VAT; SVV2 NUM+VCRTYP+VCRNUM+VAT
Fields:
  AMTTAX MD1 Tax amount
  AUUID AUUID Single identifier
  BASDEPATI MD1 Discount basis tax incl.
  BASDEPNOT MD1 Discount basis tax excl.
  BASTAX MD1 Tax basis
  CPY CPY Company -> [CPY]CPY0 =[SVV]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[SVV]CUR (TABCUR) !Block
  EXEAMTTAX MD1 Exemption amount
  NUM SIH Invoice number -> [SIV]SIV0 =[SVV]NUM (SINVOICEV) !Other
  THEAMTTAX DCB*19.8 Theor. tax amt act:KAG
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VAT VAT Tax -> [TVT]TVT0 =VAT;[V]GSUPCLE (TABVAT) !Block
  VATAMT MD1 Tax amount
  VATGRO MD1 Gross basis
  VATNET MD1 Subject basis
  VATRAT DCB*3.6 Rate
  VATSUPAMT MD1 Extra tax amount
  VATTYP M*15 Tax type [menu 232: 1=VAT,2=Additional tax,3=Special tax,4=Local tax]
  VCRNUM VCR Entry
  VCRTYP M*15 Entry type [menu 476: 23 values, see local-menus.md]
  WITHOLTAXFLG M*4 Withholding tax [menu 1: 1=No,2=Yes]

## SWRKDLV (SWD) - Automatic delivery generation
Keys (first = PK; D = duplicates allowed): SWD0 PRONUM+SWDKEY+SOHNUM+SOPLIN+SOQSEQ; SWD1 PRONUM+SOHNUM (D)
Fields:
  AUUID AUUID Single identifier
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Other
  BPCINV BPC Bill-to customer -> [BPC]BPC0 =[SWD]BPCINV (BPCUSTOMER) !Other
  BPCORD BPC Sold-to -> [BPC]BPC0 =[SWD]BPCORD (BPCUSTOMER) !Other
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SWD]CREUSR (AUTILIS) !Other
  DMEFORPRH M*15 Partial delivery [menu 414: 1=Authorized,2=Full delivery line,3=Full order line]
  IME M*15 Invoicing mode [menu 408: 1=One/slip,2=One/closed order,3=One/order,4=One/ship-to,5=One/period,6=Manual]
  MDL MDL Delivery mode -> [TMD]TMD0 =[SWD]MDL (TABMODELIV) !Other
  ODL M*4 One order per delivery [menu 1: 1=No,2=Yes]
  PRONUM L*8 Process number
  QTY QTY Qty to deliver
  QTYSTU QTY STK qty to deliver
  SOHNUM VCR Order no.
  SOPLIN L*8 Sales order line
  SOQSEQ L*8 Sequence number
  SWDDATA A*250 Data
  SWDDATA2 A*250 Data
  SWDKEY A*80 Data
  SWDKEYD L*8 Break key
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWD]UPDUSR (AUTILIS) !Other

## SWRKINV (SWI) - Automatic billing
Keys (first = PK; D = duplicates allowed): SWI0 PRONUM+SWIKEY+SWIKEY1+NUM+LIN+SEQ; SWI1 PRONUM+NUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SWI]CREUSR (AUTILIS) !Other
  LIN L*8 Line number
  NUM VCR Document no.
  PRONUM L*8 Process number
  QTY QTY Quantity to invoice
  QTYSTU QTY Qty to be invd STK
  SEQ L*8 Sequence
  SWICHR A*50(3) Alphanumeric
  SWIDAT D(3) Date
  SWIDATA A*250 Data
  SWIDCB DCB*11.6(3) Decimal
  SWIINT L*8(3) Long integer
  SWIKEY A*20 Data
  SWIKEY1 A*66 Data
  SWIKEYD L*8 Break key
  SWILINNBR L*8 Number of lines
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWI]UPDUSR (AUTILIS) !Other

## SWRKINVCND (SWICND) - Automatic billing
Notes: not in V9.0 P12 (new table); not in V10 P1 (new table)
Keys (first = PK; D = duplicates allowed): SWI0 PRONUM+SWIKEY+SWIKEY1+NUM+LIN+SEQ+VCRINVCNDLIN; SWI1 PRONUM+NUM (D)
Fields:
  AUUID AUUID Single identifier
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[SWICND]CREUSR (AUTILIS) !Other
  INVCNDTYP M*10 Open item type [menu 2420: 1=Normal,2=Fixed percentage,3=Frequency]
  LIN L*8 Line number
  NUM VCR Document no.
  PRONUM L*8 Process number
  QTY QTY Quantity to invoice
  QTYSTU QTY Qty to be invd STK
  SEQ L*8 Sequence
  SWICHR A*50(3) Alphanumeric
  SWIDAT D(3) Date
  SWIDATA A*250 Data
  SWIDCB DCB*11.6(3) Decimal
  SWIINT L*8(3) Long integer
  SWIKEY A*20 Data
  SWIKEY1 A*66 Data
  SWIKEYD L*8 Break key
  SWILINNBR L*8 Number of lines
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[SWICND]UPDUSR (AUTILIS) !Other
  VCRINVCNDLIN L*8 Line number
  VCRLINORI L*8 Source document line
  VCRNUMORI VCR Original document
  VCRSEQORI L*8 Source document sequence no.
  VCRTYP M*15 Entry type [menu 476: 23 values, see local-menus.md]

## TABSOHTYP (TSO) - Order type table
Notes: differs in V9.0 P12 (diff: AT3_TABSOHTYP.htm)
Keys (first = PK; D = duplicates allowed): TSO0 SOHTYP+LEG; TSO1 SOHTYP (D)
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TSO]CODNUM (ACODNUM) !Block
  CODNUMEND ANM Sequence number -> [ANM]ANM0 =[TSO]CODNUMEND (ACODNUM) !Block act:KPO
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  GFY AGF Group -> [AGF]AGF0 =[TSO]GFY (AGRPFCY) !Block
  LANDESSHO A*60 Descriptions
  LEG ADI -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document] act:KPO
  SDHTYP TSD Delivery type -> [TSD]TSD0 =SDHTYP;[V]GSUPCLE (TABSDHTYP) !Block
  SHOAXX AX1 Short description
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHTYP TSO Order type -> [TSO]TSO0 =[TSO]SOHTYP (TABSOHTYP) !Other
  TSODES A*30 Description
  TSOSOH A*10 Description
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSQHTYP (TSQ) - Quote type table
Notes: differs in V9.0 P12 (diff: AT3_TABSQHTYP.htm)
Keys (first = PK; D = duplicates allowed): TSQ0 SQHTYP+LEG; TSQ1 SQHTYP (D)
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TSQ]CODNUM (ACODNUM) !Block
  CODNUMEND ANM Sequence number -> [ANM]ANM0 =[TSQ]CODNUMEND (ACODNUM) !Block act:KPO
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  GFY AGF Group -> [AGF]AGF0 =[TSQ]GFY (AGRPFCY) !Block
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document] act:KPO
  SHOAXX AX1 Short description
  SOHTYP TSO Order type -> [TSO]TSO0 =SOHTYP;LEG (TABSOHTYP) !Block
  SQHTYP TSQ Quote type -> [TSQ]TSQ0 =SQHTYP;LEG (TABSQHTYP) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TABSRHTYP (TRE) - Return type table
Keys (first = PK; D = duplicates allowed): TRE0 SRHTYP+LEG; TRE1 SRHTYP (D)
Fields:
  AUUID AUUID Single identifier
  CODNUM ANM Sequence number -> [ANM]ANM0 =[TRE]CODNUM (ACODNUM) !Block
  CODNUMCPY ANM Inter-cy counter -> [ANM]ANM0 =[TRE]CODNUMCPY (ACODNUM) !Block
  CODNUMCPYD ANM Fnl inter-cy cntr -> [ANM]ANM0 =[TRE]CODNUMCPYD (ACODNUM) !Block act:KPO
  CODNUMEND ANM Final counter -> [ANM]ANM0 =[TRE]CODNUMEND (ACODNUM) !Block act:KPO
  CODNUMFCY ANM Intersite sequence no. -> [ANM]ANM0 =[TRE]CODNUMFCY (ACODNUM) !Block
  CODNUMFCYD ANM Fnl inter-site cntr -> [ANM]ANM0 =[TRE]CODNUMFCYD (ACODNUM) !Block act:KPO
  COMAT M*4 Transport document [menu 1: 1=No,2=Yes] act:KPO
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DESAXX AX3 Description
  GFY AGF Group -> [AGF]AGF0 =[TRE]GFY (AGRPFCY) !Block
  LANDESSHO A*60 Descriptions
  LEG ADI Legislation -> [ADI]CODE =909;LEG (ATABDIV) !Block
  MANCOU M*4 Manual sequence no. [menu 1: 1=No,2=Yes]
  RECTYP M*15 Record type [menu 2029: 1=Normal,2=Manual document recovery,3=Backup document recovery,4=External document] act:KPO
  SAFTTRNTYP M*15 SAF-T document type [menu 2046: 1=GT (transport note),2=GR (packing slip),3=GA (assets transport),4=GC (loan packing slip),5=GD (supplier returns)] act:KPO
  SHOAXX AX1 Short description
  SRHCAT M*20 Return category [menu 493: 1=Normal,2=Loan,3=For subcontract]
  SRHTYP TRE Return type -> [TRE]TRE0 =SRHTYP;LEG (TABSRHTYP) !Delete
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user

## TMPSRPT (TRPT) - Temporary print key table
Notes: differs in V9.0 P12 (diff: AT3_TMPSRPT.htm); differs in V10 P1 (diff: ATD_TMPSRPT.htm)
Keys (first = PK; D = duplicates allowed): TSRPT0 NUMREQ+USR+RPTCOD+VCRNUM
Fields:
  AUUID AUUID Single identifier
  CLEA1 A*40 Alpha 1
  CLEA2 A*40 Alpha 2
  CLEA3 A*40 Alpha 3
  CLED1 D Date 1
  CLED2 D Date 2
  CLEMD1 DCB*13.2 Decimal 1
  CLEMD2 DCB*13.2 Decimal
  CLEMD3 DCB*13.2 Decimal
  CLEN1 L*8 Numeric 1
  CLEN2 L*8 Numeric 2
  CLEN3 L*8 Numeric 3
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TRPT]CREUSR (AUTILIS) !Other
  CSHVATRGM M*4 Cash VAT [menu 1: 1=No,2=Yes]
  DEPMGTMOD C*2 Discount method
  MOTDESCRIPT A*65 Description
  NUMEND A*40 Final number
  NUMREQ L*8 Query no.
  PTATCOD A*50 AT code
  PTCPYADDLIG A*35(3) Address line
  PTCPYCTY A*30 City
  PTCPYNAM A*40 Company
  PTCPYPOSCOD POS Postal code
  PTCPYSAT SAT State
  PTMENTION01 A*100 Legal mention
  PTMENTION02 A*100 Legal mention
  PTMENTION03 A*100 Legal mention
  PTMENTION04 A*100 Legal mention
  PTMENTION05 A*100 Legal mention
  PTMENTION06 A*100 Legal mention
  PTMENTION07 A*60 Legal mention
  RPTCOD ARP Report code -> [ARP]ARP0 =[TRPT]RPTCOD (AREPORT) !Other
  SAFTINVTYP M*15 SAF-T document type [menu 2028: 1=Invoice,2=Simplified invoice,3=Debit note,4=Credit note,5=Fixed assets sale,6=Fixed assets return,7=Invoice-Receipt,8=Proforma,9=Consignment invoice]
  SDDPRN C*2 SDD info print
  SIVACPTDDE MD1 Prepayment requested
  SIVACPTECH MD1 Open item amount
  SIVACPTVER MD1 Prepayment paid
  SIVCUR CUR Currency -> [TCU]TCU0 =[TRPT]SIVCUR (TABCUR) !Other
  SOHTYP TSO Order type -> [TSO]TSO0 =[TRPT]SOHTYP (TABSOHTYP) !BSRA
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TRPT]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TRPT]USR (AUTILIS) !Other
  VALDAT D Validation date
  VCRNUM VCR Document no.
  WITHOLTAX DCB*13.4 Withholding tax

## TMPSRPTDET (TSRPTD) - Temporary print key table
Notes: not in V9.0 P12 (new table)
Keys (first = PK; D = duplicates allowed): TSRPTD0 NUMREQ+USR+RPTCOD+VCRNUM+LIN
Fields:
  AUUID AUUID Single identifier
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[TSRPTD]CREUSR (AUTILIS) !Other
  LIN L*8 Line no.
  NUMREQ L*8 Query no.
  RPTCOD ARP Report code -> [ARP]ARP0 =[TSRPTD]RPTCOD (AREPORT) !Other
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[TSRPTD]UPDUSR (AUTILIS) !Other
  USR AUS Operator -> [AUS]CODUSR =[TSRPTD]USR (AUTILIS) !Other
  VATEXEREA A*100 VAT exemption reasons
  VCRNUM VCR Document no.

## UNFILWRK (UNF) - Unfilled orders report
Keys (first = PK; D = duplicates allowed): UNF0 REQNUM+USER+RPTCOD+NUMLIG
Fields:
  AUUID AUUID Single identifier
  BKOQTY QTY Backorder quantity
  BPCORD BPR Sold-to -> [BPR]BPR0 =[UNF]BPCORD (BPARTNER) !Block
  CHGRAT DCB*5.6 Currency rate
  CREDATTIM ADATIM Date time
  CREUSR AUS User -> [AUS]CODUSR =[UNF]CREUSR (AUTILIS) !Other
  CUR CUR Currency -> [TCU]TCU0 =[UNF]CUR (TABCUR) !Block
  EXTRCPDAT D Exp. receipt date
  ITMREF ITM Product -> [ITM]ITM0 =[UNF]ITMREF (ITMMASTER) !Block
  NETPRINOT MD8 Net price - tax
  NUMLIG L*8 Line no.
  ORDDAT D Order date
  POHFCY FCY Order site -> [FCY]FCY0 =[UNF]POHFCY (FACILITY) !Block
  POHNUM VCR Order number
  PRHFCY FCY Receiving site -> [FCY]FCY0 =[UNF]PRHFCY (FACILITY) !Block
  REQNUM L*8 Request no.
  RPTCOD A*10 Report code
  SALFCY FCY Sales site -> [FCY]FCY0 =[UNF]SALFCY (FACILITY) !RTZ
  SAU UOM Sales unit -> [TUN]TUN0 =[UNF]SAU (TABUNIT) !Block
  SHIDAT D Ship date
  SOHNUM VCR Order number
  SOPLIN L*8 Order line
  SOQSEQ L*8 Sequence number
  STOFCY FCY Site -> [FCY]FCY0 =[UNF]STOFCY (FACILITY) !Block
  UPDDATTIM ADATIM Date time
  UPDUSR AUS User -> [AUS]CODUSR =[UNF]UPDUSR (AUTILIS) !Other
  USER AUS User code -> [AUS]CODUSR =[UNF]USER (AUTILIS) !Other

## VSORDER (VOH) - Sales order history - header
Notes: differs in V9.0 P12 (diff: AT3_VSORDER.htm); differs in V10 P1 (diff: ATD_VSORDER.htm)
Keys (first = PK; D = duplicates allowed): VOH0 SOHNUM+REVNUM
Fields:
  ALLLINNBR C*4 No. of lines to allocate
  ALLSTA M*15 Allocation status [menu 416: 1=Not allocated,2=Partly allocated,3=Allocated]
  ALLTYP M*15 Allocation type [menu 450: 1=Global,2=Detailed]
  AMTTAX MD1 Tax amount act:KUS
  APPFLG M*15 Signed [menu 280: 1=No,2=In part,3=In full,4=Not managed,5=Yes automatic]
  AUUID AUUID Single identifier
  BASTAX MD1 Tax basis act:KUS
  BETCPY M*4 Intercompany [menu 1: 1=No,2=Yes]
  BETFCY M*4 Intersites [menu 1: 1=No,2=Yes]
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPAINV ADR Invoice address code
  BPAORD ADR Order addr code
  BPCADDLIG ADL(3) Order address
  BPCCRY CRY Country of order -> [TCY]TCY0 =[VOH]BPCCRY (TABCOUNTRY) !Block
  BPCCRYNAM NCY Order country name
  BPCCTY CTY Order city
  BPCGRU BPR Group customer -> [BPR]BPR0 =[VOH]BPCGRU (BPARTNER) !Block
  BPCINV BPR Bill-to customer -> [BPR]BPR0 =[VOH]BPCINV (BPARTNER) !Block
  BPCNAM NAM(2) Sold-to customer name
  BPCORD BPR Sold-to -> [BPR]BPR0 =[VOH]BPCORD (BPARTNER) !Block
  BPCPOSCOD POS Order postal code
  BPCPYR BPR Pay-by customer -> [BPR]BPR0 =[VOH]BPCPYR (BPARTNER) !Block
  BPCSAT SAT Order state
  BPDADDLIG ADL(3) Delivery address
  BPDCRY CRY Delivery country -> [TCY]TCY0 =[VOH]BPDCRY (TABCOUNTRY) !Block
  BPDCRYNAM NCY Delivery country name
  BPDCTY CTY Delivery city
  BPDNAM NAM(2) Ship-to customer name
  BPDPOSCOD POS Deliv postal code
  BPDSAT SAT Delivery country
  BPIADDLIG ADL(3) Billing address
  BPICRY CRY Country of invoice -> [TCY]TCY0 =[VOH]BPICRY (TABCOUNTRY) !Block
  BPICRYNAM NCY Invoice country name
  BPICTY CTY Invoice city
  BPIEECNUM A*20 EU identification act:DEB
  BPINAM NAM(2) Bill-to customer name
  BPIPOSCOD POS Invoice postal code
  BPISAT SAT Invoice state
  BPTNUM BPT Carrier -> [BPT]BPT0 =[VOH]BPTNUM (BPCARRIER) !Block
  CCE CCE Analytical dimension -> [CCE]CCE0 =DIE(indice);CCE(indice) (CACCE) !Block act:ANA
  CCLDAT D Date closed
  CCLREN ADI Closing reason -> [ADI]CODE =201;CCLREN (ATABDIV) !Block
  CDTSTA M*15 Credit status [menu 419: 1=OK,2=On hold,3=Limit exceeded,4=Prepayment not paid,5=Credit card]
  CHGRAT DCB*5.6 Currency rate
  CHGTYP M*15 Rate type [menu 202: 1=Daily rate,2=Monthly rate,3=Average rate,4=Customs doc file exchange]
  CLELINNBR C*4 No. closed lines
  CMGNUM CMG Marketing campaign -> [CMG]CMG0 =[VOH]CMGNUM (CMARKETING) !RTZ
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CNINAM AIN Invoice contact -> [AIN]AIN0 =CNINAM (CONTACTCRM) !Block
  CNTNAM AIN Person to contact -> [AIN]AIN0 =CNTNAM (CONTACTCRM) !Block
  COPNBR C*1 No. copies acknowledgement of receipt
  CPY CPY Company -> [CPY]CPY0 =[VOH]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUR CUR Currency -> [TCU]TCU0 =[VOH]CUR (TABCUR) !Block
  CUSORDREF A*20 Customer order ref
  DAYLTI C*3 Delivery LT in days
  DEMDLVDAT D Req. delivery date
  DEP TDA Settlement discount -> [TDA]TDA0 =DEP;[V]GSUPCLE (TABDEPAGIO) !Block
  DIE DIE Dimension type code -> [DIE]DIE0 =[VOH]DIE (GDIE) !Block act:ANA
  DISCRGTYP M*10 Discount / charge type [menu 255: 1=Amount,2=% combined,3=% series] act:SPR
  DLRATI MD1 Amount to deliver +tax
  DLRNOT MD1 Amount to deliver -tax
  DLVLINNBR C*4 No. of delivered lines
  DLVPIO M*15 Delivery priority [menu 410: 1=Normal,2=Urgent,3=Critical]
  DLVSTA M*15 Delivery status [menu 417: 1=Not delivered,2=Partly delivered,3=Delivered]
  DME M*15 Partial delivery [menu 414: 1=Authorized,2=Full delivery line,3=Full order line]
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  DSPTOTQTY DCB*9.6 Quantity total
  DSPTOTVOL QTY Volume aggregation
  DSPTOTWEI QTY Weight aggregation
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[VOH]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[VOH]DSPWEU (TABUNIT) !Block
  EECICT ICT Incoterm -> [ICTH]ICT0 =[VOH]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EXPNUM L*8 Export number
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[VOH]FFWNUM (BPCARRIER) !Block
  GEOCOD GEO Geographic code act:KUS
  ICTCTY CTY Incoterm town
  IME M*15 Invoicing mode [menu 408: 1=One/slip,2=One/closed order,3=One/order,4=One/ship-to,5=One/period,6=Manual]
  INRATI MD1 To invoice including tax
  INRNOT MD1 To invoice excluding tax
  INRSCHATI MD1 Invoicing open item
  INRSCHNOT MD1 Invoicing open item
  INSCTYFLG A*1 City interior flag act:KUS
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  INVDTA SFI(10) Invoicing element -> [SFI]SFI0 =[VOH]INVDTA (SFOOTINV) !Other
  INVDTAAMT DCB*11.4(10) % or amt inv el
  INVDTADSP DSP Distrib key -> [DSP]DSP0 =INVDTADSP;1 (CADSP) !Other act:SFI
  INVDTALIN C*2 Invoice line element act:SPR
  INVDTATYP M*6 Value type [menu 2227: 1=Tax excluded,2=Tax included,3=%] act:SFI
  INVLINNBR C*4 No. invoiced lines
  INVSTA M*15 Invoice status [menu 418: 1=Not invoiced,2=Partly invoiced,3=Invoiced]
  LAN LAN Language -> [TLA]TLA0 =[VOH]LAN (TABLAN) !Block
  LASDLVDAT D Last delivery date
  LASDLVNUM VCR Last delivery no.
  LASINVDAT D Last invoice date
  LASINVNUM VCR Last invoice no.
  LINNBR C*4 Number of lines
  LNDRTNDAT D Loan return date
  MDL MDL Delivery mode -> [TMD]TMD0 =[VOH]MDL (TABMODELIV) !Block
  OCNFLG M*4 Print acknowledgment [menu 1: 1=No,2=Yes]
  OCNPRN M*4 Acknowledgment printed [menu 1: 1=No,2=Yes]
  ODL M*4 One order per delivery [menu 1: 1=No,2=Yes]
  OPGNUM VCR Marketing operation
  OPGTYP A*3 Operation type
  ORDATI MD1 Tax-included order amount
  ORDATIL MD1 Line amt. + tax (company)
  ORDCLE M*4 Close unfilled lines [menu 1: 1=No,2=Yes]
  ORDDAT D Order date
  ORDINVATI MD1 Valuation + tax
  ORDINVATIL MD1 Costing tax incl. cy
  ORDINVNOT MD1 Valuation - tax
  ORDINVNOTL MD1 Costing tax excl. cy
  ORDNOT MD1 Order amount -tax
  ORDNOTL MD1 Line amt. - tax (company)
  ORDSTA M*15 Order state [menu 415: 1=Open,2=Closed]
  ORIFCY FCY Original site -> [FCY]FCY0 =[VOH]ORIFCY (FACILITY) !Block
  PFMTOT MD1 Total margin
  PJT PJT Project -> [PIM]PIM0 =[VOH]PJT (PIMPL) !Block
  PLISTC PRS Structure code -> [PRS]PRS0 =1;PLISTC (PRICSTRUCT) !Other
  PRFNUM VCR Proforma invoice no.
  PRITYP M*6 Price - / +tax [menu 243: 1=Exclude tax,2=Include tax]
  PTE PTE Payment term -> [TPT]TPT0 =PTE;[V]GCURLEG;1 (TABPAYTERM) !Block
  REP REP Sales rep -> [REP]REP0 =[VOH]REP (SALESREP) !Block act:REP
  REVCOD A*1 Revision code
  REVNUM C*4 Revision no.
  SALFCY FCY Sales site -> [FCY]FCY0 =[VOH]SALFCY (FACILITY) !Block
  SFISSTCOD ADI SST tax code -> [ADI]CODE =203;SFISSTCOD (ATABDIV) !Block act:SFI
  SHIADECOD A*35 Shipper / receiver code
  SHIDAT D Shipment date
  SINUM A*10 Integrale part no. act:SMI
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHNUM VCR Order no.
  SOHTEX1 TXC Ord header text
  SOHTEX2 TXC Ord footer text
  SOHTYP TSO Order type -> [TSO]TSO0 =SOHTYP;[V]GSUPCLE (TABSOHTYP) !Block
  SQHNUM VCR Quote no.
  SRENUM SRE Service request -> [SRE]SRE0 =[VOH]SRENUM (SERREQUEST) !RTZ
  SSTENTCOD ADI Entity/Use -> [ADI]CODE =202;SSTENTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[VOH]STOFCY (FACILITY) !Block
  TSCCOD ADI Statistical group -> [ADI]CODE =indice+30;TSCCOD(indice) (ATABDIV) !Other act:STC
  UNL M*4 Release [menu 1: 1=No,2=Yes]
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VCRINVCNDDAT D Beginning due date
  VLYDATCON D Validity date
  VTT A*1 Vertex transaction type act:KUS

## VSORDERC (VOC) - Cumulative sales order history
Keys (first = PK; D = duplicates allowed): VOC0 SOHNUM+ITMREVNUM+SOPLIN
Fields:
  AUUID AUUID Single identifier
  BPAADD ADR Delivery address
  BPCORD BPC Sold-to -> [BPC]BPC0 =[VOC]BPCORD (BPCUSTOMER) !Other
  BPIEECNUM A*20 EU identification act:DEB
  CPY CPY Company -> [CPY]CPY0 =[VOC]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  CUMDATEAR D Cumulative customer start date
  CUSORDREF A*20 Customer order ref
  DLVQTYCUM QTY Total delivered
  DSPPRC C*3(7) Weekly quantity split
  EARDAT D Calculated early / late date
  EARDATCUS D Customer early/late date
  EARHOU HM Calculated early / late time
  EARHOUCUS HM Customer early/late time
  EARQTY QTY Calculated early / late quanti
  EARQTYCUS QTY Customer early/late qty
  EECICT ICT Incoterm -> [ICTH]ICT0 =[VOC]EECICT (INCOTERM) !Block
  EECLOC M*15 Intrastat transport location [menu 236: 1=Domestic,2=Other EU,3=Outside EU] act:DEB
  EXTQTY QTY Planned quantity
  FFWADD ADR Forwarding agent address
  FFWNUM BPT Freight agent -> [BPT]BPT0 =[VOC]FFWNUM (BPCARRIER) !Block
  FIMHOR C*4 Firm horizon
  ICTCTY CTY Incoterm town
  ITMDES DES Description
  ITMDES1 DES Description
  ITMDESBPC DES Customer description
  ITMREF ITM Product -> [ITM]ITM0 =[VOC]ITMREF (ITMMASTER) !Block
  ITMREFBPC A*20 Customer product
  ITMREVNUM C*4 Revision no.
  ORDQTYCUM QTY Total ordered
  PLI SPC Price list code -> [SPC]SPC0 =[VOC]PLI (SPRICCONF) !Other
  REVCOD A*1 Revision code
  SALFCY FCY Sales site -> [FCY]FCY0 =[VOC]SALFCY (FACILITY) !Block
  SAU UOM Sales unit -> [TUN]TUN0 =[VOC]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SOCTEX TXC Product text
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[VOC]STOFCY (FACILITY) !Block
  STU UOM Stock unit -> [TUN]TUN0 =[VOC]STU (TABUNIT) !Block
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  VACBPR TVB Tax rule -> [TVB]TVB0 =VACBPR;[V]GSUPCLE (TABVACBPR) !Block
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block
  VLYDATITM D Validity date

## VSORDERP (VOP) - Sales order history - price
Notes: differs in V9.0 P12 (diff: AT3_VSORDERP.htm); differs in V10 P1 (diff: ATD_VSORDERP.htm)
Keys (first = PK; D = duplicates allowed): VOP0 SOHNUM+LINREVNUM+SOPLIN+SOPSEQ
Fields:
  AUUID AUUID Single identifier
  BPAADD BPD Delivery address -> [BPD]BPD0 =BPCORD;BPAADD (BPDLVCUST) !Block
  BPCINV BPC Bill-to customer -> [BPC]BPC0 =[VOP]BPCINV (BPCUSTOMER) !Other
  BPCORD BPC Sold-to -> [BPC]BPC0 =[VOP]BPCORD (BPCUSTOMER) !Other
  CLCAMT1 MD1 Tax calculation basis 1
  CLCAMT2 MD1 Tax calculation basis 2
  CNDNAM AIN Delivery contact -> [AIN]AIN0 =CNDNAM (CONTACTCRM) !Block
  CONNUM VCR Service contract no.
  CPRPRI MD8 Cost price
  CPY CPY Company -> [CPY]CPY0 =[VOP]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DISCRGREN1 SPR Discount 1 reason -> [SPR]SPR0 =[VOP]DISCRGREN1 (SPREASON) !Block act:SP1
  DISCRGREN2 SPR Discount 2 reason -> [SPR]SPR0 =[VOP]DISCRGREN2 (SPREASON) !Block act:SP2
  DISCRGREN3 SPR Discount 3 reason -> [SPR]SPR0 =[VOP]DISCRGREN3 (SPREASON) !Block act:SP3
  DISCRGREN4 C*4 Discount 4 reason act:SP4
  DISCRGREN5 C*4 Discount 5 reason act:SP5
  DISCRGREN6 C*4 Discount 6 reason act:SP6
  DISCRGREN7 C*4 Discount 7 reason act:SP7
  DISCRGREN8 C*4 Discount 8 reason act:SP8
  DISCRGREN9 C*4 Discount 9 reason act:SP9
  DISCRGVAL1 MD8 Discount/Charge 1 act:SP1
  DISCRGVAL2 MD8 Discount/Charge 2 act:SP2
  DISCRGVAL3 MD8 Discount/Charge 3 act:SP3
  DISCRGVAL4 DCB*19.8 Discount/Charge 4 act:SP4
  DISCRGVAL5 DCB*19.8 Discount/Charge 5 act:SP5
  DISCRGVAL6 DCB*19.8 Discount/Charge 6 act:SP6
  DISCRGVAL7 DCB*19.8 Discount/Charge 7 act:SP7
  DISCRGVAL8 DCB*19.8 Discount/Charge 8 act:SP8
  DISCRGVAL9 DCB*19.8 Discount/Charge 9 act:SP9
  ENDDAT D Validity end date
  EXPNUM L*8 Export number
  FOCFLG M*10 Free [menu 439: 1=No,2=Source,3=Yes]
  GROPRI MD8 Gross price
  INVCND INVCND Invoic. term -> [INVCND]INVCND0 =INVCND;[V]GSUPCLE (TABINVCND) !Block
  ITMDES DES Description
  ITMDES1 DES Description
  ITMREF ITM Product -> [ITM]ITM0 =[VOP]ITMREF (ITMMASTER) !Block
  ITMREFBPC A*20 Customer product
  LINREVNUM C*4 Revision no.
  LINTYP M*15 Line type [menu 423: 1=Normal,2=Fixed kit,3=Kit component,4=Kit option,5=Kit variant,6=Flex kit,7=BOM component,8=BOM option,9=BOM variant,10=Subcontracted,11=Service,12=Supplied material,13=Fixed-amount service]
  NETPRI MD8 Net price
  NETPRIATI MD8 Net price + tax
  NETPRINOT MD8 Net price - tax
  ORILIN L*8 Free line source
  PFM MD1 Margin
  PRIREN SPR Price reason -> [SPR]SPR0 =[VOP]PRIREN (SPREASON) !Block
  REP1 REP Sales rep 1 -> [REP]REP0 =[VOP]REP1 (SALESREP) !Block act:RE1
  REP2 REP Sales rep 2 -> [REP]REP0 =[VOP]REP2 (SALESREP) !Block act:RE2
  REPCOE CCR Commission factor
  REPRAT1 RAT Commission rate 1 act:RE1
  REPRAT2 RAT Commission rate 2 act:RE2
  REVCOD A*1 Revision code
  SALFCY FCY Sales site -> [FCY]FCY0 =[VOP]SALFCY (FACILITY) !Other
  SAU UOM Sales unit -> [TUN]TUN0 =[VOP]SAU (TABUNIT) !Block
  SAUSTUCOE COE SAL-STK conv.
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SOPSEQ L*8 Sequence
  SOQSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  SQDLIN L*8 Quote line
  SQHNUM VCR Quote no.
  SSTCOD ADI SST tax code -> [ADI]CODE =203;SSTCOD (ATABDIV) !Block act:LTA
  STOFCY FCY Shipment site -> [FCY]FCY0 =[VOP]STOFCY (FACILITY) !Other
  STRDAT D Validity start date
  STU UOM Stock unit -> [TUN]TUN0 =[VOP]STU (TABUNIT) !Block
  TSICOD ADI Statistical group -> [ADI]CODE =indice+20;TSICOD(indice) (ATABDIV) !Other act:STI
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  VACITM TVI(3) Tax level -> [TVI]TVI0 =VACITM(indice);[V]GSUPCLE (TABVACITM) !Block
  VAT VAT(3) Tax -> [TVT]TVT0 =VAT(indice);[V]GSUPCLE (TABVAT) !Block

## VSORDERQ (VOQ) - Sales order history - Qties.
Notes: differs in V9.0 P12 (diff: AT3_VSORDERQ.htm); differs in V10 P1 (diff: ATD_VSORDERQ.htm)
Keys (first = PK; D = duplicates allowed): VOQ0 SOHNUM+LINREVNUM+SOPLIN+SOQSEQ
Fields:
  ALLQTY QTY Allocated qty.
  ALLQTYSTU QTY Allocated qty STU
  ALLTYP M*15 Allocation type [menu 450: 1=Global,2=Detailed]
  AUUID AUUID Single identifier
  BASTAXLIN MD1 Taxable amount act:KUS
  BPAADD ADR Delivery address
  BPCORD BPC Sold-to -> [BPC]BPC0 =[VOQ]BPCORD (BPCUSTOMER) !Other
  BPTNUM BPT Carrier -> [BPT]BPT0 =[VOQ]BPTNUM (BPCARRIER) !Block
  CAD M*7 Sequencing [menu 278: 1=Day,2=Week,3=Month]
  CCLDAT D Date closed
  CCLREN ADI Closing reason -> [ADI]CODE =201;CCLREN (ATABDIV) !Block
  CPY CPY Company -> [CPY]CPY0 =[VOQ]CPY (COMPANY) !Block
  CREDAT D Date created
  CREDATTIM ADATIM Date time
  CREUSR A*5 Creation user
  DAYLTI C*3 Delivery LT in days
  DDTANOT MD1 Invoice line allocation elemen act:SFL
  DDTANUM SFI Invoice line allocation elemen -> [SFI]SFI0 =[VOQ]DDTANUM (SFOOTINV) !Block act:SFL
  DEMDLVDAT D Req. delivery date
  DEMDLVHOU HM Delivery request time
  DEMNUM VCR Order no.
  DEMSTA M*10 Order status [menu 317: 1=Firm,2=Planned,3=Suggested,4=Closed]
  DLVDAY C*2 Day
  DLVFLG M*4 Deliverable [menu 1: 1=No,2=Yes]
  DLVPIO M*15 Delivery priority [menu 410: 1=Normal,2=Urgent,3=Critical]
  DLVPIOCMP C*1 Compl priority del
  DLVQTY QTY Delivered qty.
  DLVQTYSTU QTY Delivered qty STU
  DRN M*15 Route no. [menu 409: 1=Route code 1,2=Route code 2,3=Route code 3]
  DSPLINFLG M*4 Distribution [menu 1: 1=No,2=Yes]
  DSPLINVOL QTY Line volume
  DSPLINWEI QTY Line weight
  DSPVOU UOM Volume unit -> [TUN]TUN0 =[VOQ]DSPVOU (TABUNIT) !Block
  DSPWEU UOM Weight unit -> [TUN]TUN0 =[VOQ]DSPWEU (TABUNIT) !Block
  ECCVALMAJ ECS Major version act:ECC
  ECCVALMIN EVL Minor version act:ECC
  EXPNUM L*8 Export number
  EXTDLVDAT D Exp delivery date
  FMI M*20 Product source [menu 445: 1=Normal,2=PO - Direct to customer,3=PO - Receive and ship,4=Transfer,5=Work order]
  FMILIN L*8 Back-to-back order line
  FMINUM VCR Back-to-back order no.
  FMISEQ L*8 Back-to-back order seq.
  GEOCOD GEO Geographic code act:KUS
  INSCTYFLG A*1 City interior flag act:KUS
  INVAMT MC1 Amount invoiced
  INVFLG M*4 Invoiced [menu 1: 1=No,2=Yes]
  INVPRNBOM M*4 Print component on invoice [menu 1: 1=No,2=Yes]
  INVQTY QTY Invoiced qty.
  INVQTYSTU QTY Invoiced STU
  ITMREF ITM Product -> [ITM]ITM0 =[VOQ]ITMREF (ITMMASTER) !Block
  LINREVNUM C*4 Revision no.
  LOC LOC Location filter -> [STC]STC0 =STOFCY;LOC (STOLOC) !Block
  LOT LOT Filter lot
  LPRQTY QTY Qty. on list prep.
  LPRQTYSTU QTY Qty list prep STU
  MDL MDL Delivery mode -> [TMD]TMD0 =[VOQ]MDL (TABMODELIV) !Block
  MON C*2 Months
  NDEPRNBOM M*4 PS print component [menu 1: 1=No,2=Yes]
  OCNPRNBOM M*4 Print component on acknowledgement [menu 1: 1=No,2=Yes]
  ODLQTY QTY Qty. in process
  ODLQTYSTU QTY STK qty. in process
  OPRQTY QTY Qty. being prepared
  OPRQTYSTU QTY Qty being prep STU
  ORDDAT D Order date
  ORIQTY QTY Initial order quantity
  PCK PCK Packaging -> [TPA]TPA0 =[VOQ]PCK (TABPACKAGE) !Block
  PCKCAP COE Packaging capacity
  PERENDDAT D Period end date
  PERNBRDAY C*3 Number of period days
  PERSTRDAT D Period start date
  PJT PJT Project -> [PIM]PIM0 =[VOQ]PJT (PIMPL) !Block
  POHNUM VCR Order no.
  POPLIN L*8 Line
  POQSEQ L*8 Sequence number
  PRECOD PRC Preparation code
  PREQTY QTY Qty. prepared
  PREQTYSTU QTY Qty prepared STU
  QTY QTY Ordered qty.
  QTYSTU QTY Ordered STU
  RATTAXLIN RAT Tax rates act:KUS
  REVCOD A*1 Revision code
  SALFCY FCY Sales site -> [FCY]FCY0 =[VOQ]SALFCY (FACILITY) !Block
  SDDLIN L*8 Delivery line
  SDHNUM VCR Delivery no.
  SHIDAT D Shipment date
  SHIHOU HM Shipment time
  SHTQTY QTY Shortage
  SHTQTYSTU QTY Qty shortage STU
  SOHCAT M*15 Order category [menu 412: 1=Normal,2=Loan,3=Direct invoicing,4=Contract]
  SOHNUM VCR Order no.
  SOPLIN L*8 Line
  SOQSEQ L*8 Sequence number
  SOQSTA M*7 Line status [menu 279: 1=Pending,2=Late,3=Closed]
  SOQTEX TXC Text
  STA A*12 Filter status
  STOFCY FCY Shipment site -> [FCY]FCY0 =[VOQ]STOFCY (FACILITY) !Block
  STOMGTCOD M*15 Stock management [menu 215: 1=Not managed,2=Managed,3=Potency managed]
  TAXFLG M*4 Taxable flag [menu 1: 1=No,2=Yes] act:KUS
  TAXGEOFLG A*1 Taxed geo flag act:KUS
  TAXREGFLG M*4 Recorded tax flag [menu 1: 1=No,2=Yes] act:KUS
  TDLQTY QTY Qty to deliver
  TDLQTYSTU QTY STK qty to deliver
  UPDDAT D Change date
  UPDDATTIM ADATIM Date time
  UPDUSR A*5 Change user
  USEPLC A*30 Location reference
  VTC A*1 Vertex transaction code act:KUS
  VTS A*1 Vertex transaction sub-type act:KUS
  WEE C*2 Week no.
  YEA C*4 Year

