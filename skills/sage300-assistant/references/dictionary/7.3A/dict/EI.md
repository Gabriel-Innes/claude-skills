# EI module - compiled AOM dictionary

## EICLASS - Classification Code Mapping (view EI0313)
Keys (first = PK; D=dups allowed, M=modifiable): ITEMFROM+ITEMTYPE+ITEMNO
Fields (NAME type description [values]):
  ITEMFROM Integer Item From [1=Inventory Control,2=Accounts Receivable,3=Accounts Payable]
  ITEMTYPE Integer AR Item Type [0=]
  ITEMNO String*24 Item Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ITCCODE String*3 Classification Code

## EICURR - S300-Peppol Currrency Mapping (view EI0120)
Keys (first = PK; D=dups allowed, M=modifiable): CURID
Fields (NAME type description [values]):
  CURID String*3 Sage 300 Currency Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PPLCURID String*20 Peppol Currency Code

## EICUST - Customer eInvoicing (view EI0130)
Keys (first = PK; D=dups allowed, M=modifiable): IDCUST
Fields (NAME type description [values]):
  IDCUST String*12 Customer Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PEPPOLID String*50 Customer Peppol ID
  SST String*60 SST Registration Number
  TIN String*20 Tax Identification Number
  CNTYNAME Integer Country Name [1=Afghanistan,2=Albania,3=Algeria,4=American Samoa,5=Andorra,6=Angola,7=Anguilla,8=Antarctica,9=Antigua and Barbuda,10=Argentina,11=Armenia,12=Aruba,13=Australia,14=Austria,15=Azerbaijan,16=Bahamas,17=Bahrain,18=Bangladesh,19=Barbados,20=Belarus,21=Belgium,22=Belize,23=Benin,24=Bermuda,25=Bhutan,26=Bolivia,27=Bosnia and Herzegovina,28=Botswana,29=Brazil,30=British Indian Ocean Territory,31=British Virgin Islands,32=Brunei,33=Bulgaria,34=Burkina Faso,35=Burma (Myanmar),36=Burundi,37=Cambodia,38=Cameroon,39=Canada,40=Cape Verde,41=Cayman Islands,42=Central African Republic,43=Chad,44=Chile,45=China,46=Christmas Island,47=Cocos (Keeling) Islands,48=Colombia,49=Comoros,50=Cook Islands,51=Costa Rica,52=Croatia,53=Cuba,54=Cyprus,55=Czech Republic,56=Democratic Republic of the Congo,57=Denmark,58=Djibouti,59=Dominica,60=Dominican Republic,61=Ecuador,62=Egypt,63=El Salvador,64=Equatorial Guinea,65=Eritrea,66=Estonia,67=Ethiopia,68=Falkland Islands,69=Faroe Islands,70=Fiji,71=Finland,72=France,73=French Polynesia,74=Gabon,75=Gambia,76=Georgia,77=Germany,78=Ghana,79=Gibraltar,80=Greece,81=Greenland,82=Grenada,83=Guam,84=Guatemala,85=Guinea,86=Guinea-Bissau,87=Guyana,88=Haiti,89=Holy See (Vatican City),90=Honduras,91=Hungary,92=Iceland,93=India,94=Indonesia,95=Iran,96=Iraq,97=Ireland,98=Isle of Man,99=Israel,100=Italy,101=Ivory Coast,102=Jamaica,103=Japan,104=Jersey,105=Jordan,106=Kazakhstan,107=Kenya,108=Kiribati,109=Kuwait,110=Kyrgyzstan,111=Laos,112=Latvia,113=Lebanon,114=Lesotho,115=Liberia,116=Libya,117=Liechtenstein,118=Lithuania,119=Luxembourg,120=Macedonia,121=Madagascar,122=Malawi,123=Malaysia,124=Maldives,125=Mali,126=Malta,127=Marshall Islands,128=Mauritania,129=Mauritius,130=Mayotte,131=Mexico,132=Micronesia,133=Moldova,134=Monaco,135=Mongolia,136=Montenegro,137=Montserrat,138=Morocco,139=Mozambique,140=Namibia,141=Nauru,142=Nepal,143=Netherlands,144=Netherlands Antilles,145=New Caledonia,146=New Zealand,147=Nicaragua,148=Niger,149=Nigeria,150=Niue,151=North Korea,152=Northern Mariana Islands,153=Norway,154=Oman,155=Pakistan,156=Palau,157=Panama,158=Papua New Guinea,159=Paraguay,160=Peru,161=Philippines,162=Pitcairn Islands,163=Poland,164=Portugal,165=Puerto Rico,166=Qatar,167=Republic of the Congo,168=Romania,169=Russia,170=Rwanda,171=Saint Barthelemy,172=Saint Helena,173=Saint Kitts and Nevis,174=Saint Lucia,175=Saint Martin,176=Saint Pierre and Miquelon,177=Saint Vincent and the Grenadines,178=Samoa,179=San Marino,180=Sao Tome and Principe,181=Saudi Arabia,182=Senegal,183=Serbia,184=Seychelles,185=Sierra Leone,186=Singapore,187=Slovakia,188=Slovenia,189=Solomon Islands,190=Somalia,191=South Africa,192=South Korea,193=Spain,194=Sri Lanka,195=Sudan,196=Suriname,197=Svalbard,198=Swaziland,199=Sweden,200=Switzerland,201=Syria,202=Taiwan,203=Tajikistan,204=Tanzania,205=Thailand,206=Timor-Leste,207=Togo,208=Tokelau,209=Tonga,210=Trinidad and Tobago,211=Tunisia,212=Turkey,213=Turkmenistan,214=Turks and Caicos Islands,215=Tuvalu,216=Uganda,217=Ukraine,218=United Arab Emirates,219=United Kingdom,220=United States,221=Uruguay,222=US Virgin Islands,223=Uzbekistan,224=Vanuatu,225=Venezuela,226=Vietnam,227=Wallis and Futuna,228=Western Sahara,229=Yemen,230=Zambia,231=Zimbabwe]

## EIDIST - Distribution Code Mapping (view EI0200)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND+LINETYPE+ITEM+PALLOWCHRG
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  LINETYPE Integer Line Type [0=Item,1=Allowance,2=Charge]
  ITEM String*50 Item ID
  PALLOWCHRG String*20 Peppol Alow/Chrg Reason Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DISTID String*6 Distribution Code

## EIIDOC - Incoming Document Processing (view EI0250)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE; IDVEND+DATEINVC+IDINVC [D,M]; IDVEND+IDINVC [D,M]; UUID [D,M]
Fields (NAME type description [values]):
  SEQUENCE Long Transaction Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PEPPOLID String*50 Vendor Peppol ID
  PPLCURID String*20 Document Currency
  TRXTYPETXT Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note]
  IDINVC String*22 Document Number
  DATEINVC Date Document Date
  DATEDUE Date Document Due Date
  CNTBTCH BCD*5.0 Document Batch Number
  CNTITEM BCD*4.0 Document Entry Number
  DOCPRINTED Integer Document Printed
  PROCDTTM String*50 Time Processed
  PROCESSDT Date Date Processed
  DWNLDDT Date Date Downloaded
  IMPORTAPP String*10 Import App
  IMPORTSTT Integer Import Status [0=Not Imported,1=Imported,2=Failed,3=Not Applicable]
  IMPORTMSG String*250 Import Message
  IMPORTDT Date Import Date
  IMPORTTM Time Import Time
  IMPORTBY String*30 Import By
  SELECTED Integer Selected [0=No,1=Yes,2=]
  DELETED Integer Deleted/Rejected
  HASH String*50 Hash Key
  IDVEND String*12 Imported Vendor Number
  UUID String*150 UUID
  DOCTOTAL BCD*10.3 Document Total
  BILLTYPE Integer Billing Type [0=Standard,1=Self-Billed]

## EIITCC - Classification Code (view EI0310)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*3 Classification Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*250 Description

## EIIXML - Incoming Document XML Files (view EI0320)
Keys (first = PK; D=dups allowed, M=modifiable): SEQUENCE+PARTSEQ
Fields (NAME type description [values]):
  SEQUENCE Long Transaction Sequence Number
  PARTSEQ Long File Part Sequence Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  BLOCK1 String*255 Block 1
  BLOCK2 String*255 Block 2
  BLOCK3 String*255 Block 3
  BLOCK4 String*255 Block 4
  BLOCK5 String*255 Block 5
  BLOCK6 String*255 Block 6
  BLOCK7 String*255 Block 7
  BLOCK8 String*255 Block 8

## EIMISC - S300-Peppol Charge Mapping (view EI0470)
Keys (first = PK; D=dups allowed, M=modifiable): MISCCHARGE
Fields (NAME type description [values]):
  MISCCHARGE String*6 Sage 300 Misc. Charge Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  CTYPE Integer Code Type [1=Allowance,2=Charge]
  PPLMISCID String*20 Peppol Misc. Charge Code

## EIMSIC - MSIC Code (view EI0475)
Keys (first = PK; D=dups allowed, M=modifiable): CODE
Fields (NAME type description [values]):
  CODE String*5 MSIC Code
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  DESC String*250 Business Activity Description

## EIODOC - Outgoing Document Processing (view EI0500)
Keys (first = PK; D=dups allowed, M=modifiable): IDINVC+IDVEND; IDCUST+IDINVC [D,M]; TRXTYPETXT+IDCUST+IDINVC [D,M]; UUID [D,M]
Fields (NAME type description [values]):
  IDINVC String*22 Document Number
  IDVEND String*12 Vendor Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  IDCUST String*12 Customer Number
  TRXTYPETXT Integer Document Type [1=Invoice,2=Debit Note,3=Credit Note,4=Interest]
  SRCEAPPL String*2 Source Application
  DATEINVC Date Document Date
  PPLACPNT String*30 Peppol Access Point
  PPLTRANS String*50 Peppol Transaction ID
  PPLSTATUS Integer Peppol Transaction Status [0=Not Sent,1=Sent,9=Error]
  PPLAPSTT Integer Peppol Transaction AP Status [0=Not Sent,1=Sent,9=Error,11=Received,12=Processing,13=Transmitted,14=Failed to transmit,15=Pending response from LHDN,16=Rejected by LHDN]
  PPLMSG String*250 Peppol Transaction Message
  PPLDATE1 Date Submission Date
  PPLTIME1 String*60 Submission Date Time
  PPLDATE2 Date Last Sync Date
  PPLTIME2 String*60 Last Sync Date Time
  SELECTED Integer Selected [0=No,1=Yes,2=]
  DOCPRINTED Integer Document Printed
  UUID String*150 UUID
  LONGID String*150 LONGID
  HASH String*50 Hash Key
  DOCTOTAL BCD*10.3 Document Total
  ENTEREDBY String*8 Entered By
  CURID String*3 Sage 300 Currency Code

## EIOPT - Registration (view EI0550)
Keys (first = PK; D=dups allowed, M=modifiable): OPTION
Fields (NAME type description [values]):
  OPTION String*10 Option
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  ACPTTYPE Integer Access Point Type [0=SESAMi]
  PEPPOLID String*50 Peppol ID
  REGDT Date Registration Date
  REGSTATUS Integer Registration Status [0=Unregistered,1=Submitted,2=Received,3=Processing,4=Success,5=Failed]
  CNTYNAME Integer Country Full Name [1=Afghanistan,2=Albania,3=Algeria,4=American Samoa,5=Andorra,6=Angola,7=Anguilla,8=Antarctica,9=Antigua and Barbuda,10=Argentina,11=Armenia,12=Aruba,13=Australia,14=Austria,15=Azerbaijan,16=Bahamas,17=Bahrain,18=Bangladesh,19=Barbados,20=Belarus,21=Belgium,22=Belize,23=Benin,24=Bermuda,25=Bhutan,26=Bolivia,27=Bosnia and Herzegovina,28=Botswana,29=Brazil,30=British Indian Ocean Territory,31=British Virgin Islands,32=Brunei,33=Bulgaria,34=Burkina Faso,35=Burma (Myanmar),36=Burundi,37=Cambodia,38=Cameroon,39=Canada,40=Cape Verde,41=Cayman Islands,42=Central African Republic,43=Chad,44=Chile,45=China,46=Christmas Island,47=Cocos (Keeling) Islands,48=Colombia,49=Comoros,50=Cook Islands,51=Costa Rica,52=Croatia,53=Cuba,54=Cyprus,55=Czech Republic,56=Democratic Republic of the Congo,57=Denmark,58=Djibouti,59=Dominica,60=Dominican Republic,61=Ecuador,62=Egypt,63=El Salvador,64=Equatorial Guinea,65=Eritrea,66=Estonia,67=Ethiopia,68=Falkland Islands,69=Faroe Islands,70=Fiji,71=Finland,72=France,73=French Polynesia,74=Gabon,75=Gambia,76=Georgia,77=Germany,78=Ghana,79=Gibraltar,80=Greece,81=Greenland,82=Grenada,83=Guam,84=Guatemala,85=Guinea,86=Guinea-Bissau,87=Guyana,88=Haiti,89=Holy See (Vatican City),90=Honduras,91=Hungary,92=Iceland,93=India,94=Indonesia,95=Iran,96=Iraq,97=Ireland,98=Isle of Man,99=Israel,100=Italy,101=Ivory Coast,102=Jamaica,103=Japan,104=Jersey,105=Jordan,106=Kazakhstan,107=Kenya,108=Kiribati,109=Kuwait,110=Kyrgyzstan,111=Laos,112=Latvia,113=Lebanon,114=Lesotho,115=Liberia,116=Libya,117=Liechtenstein,118=Lithuania,119=Luxembourg,120=Macedonia,121=Madagascar,122=Malawi,123=Malaysia,124=Maldives,125=Mali,126=Malta,127=Marshall Islands,128=Mauritania,129=Mauritius,130=Mayotte,131=Mexico,132=Micronesia,133=Moldova,134=Monaco,135=Mongolia,136=Montenegro,137=Montserrat,138=Morocco,139=Mozambique,140=Namibia,141=Nauru,142=Nepal,143=Netherlands,144=Netherlands Antilles,145=New Caledonia,146=New Zealand,147=Nicaragua,148=Niger,149=Nigeria,150=Niue,151=North Korea,152=Northern Mariana Islands,153=Norway,154=Oman,155=Pakistan,156=Palau,157=Panama,158=Papua New Guinea,159=Paraguay,160=Peru,161=Philippines,162=Pitcairn Islands,163=Poland,164=Portugal,165=Puerto Rico,166=Qatar,167=Republic of the Congo,168=Romania,169=Russia,170=Rwanda,171=Saint Barthelemy,172=Saint Helena,173=Saint Kitts and Nevis,174=Saint Lucia,175=Saint Martin,176=Saint Pierre and Miquelon,177=Saint Vincent and the Grenadines,178=Samoa,179=San Marino,180=Sao Tome and Principe,181=Saudi Arabia,182=Senegal,183=Serbia,184=Seychelles,185=Sierra Leone,186=Singapore,187=Slovakia,188=Slovenia,189=Solomon Islands,190=Somalia,191=South Africa,192=South Korea,193=Spain,194=Sri Lanka,195=Sudan,196=Suriname,197=Svalbard,198=Swaziland,199=Sweden,200=Switzerland,201=Syria,202=Taiwan,203=Tajikistan,204=Tanzania,205=Thailand,206=Timor-Leste,207=Togo,208=Tokelau,209=Tonga,210=Trinidad and Tobago,211=Tunisia,212=Turkey,213=Turkmenistan,214=Turks and Caicos Islands,215=Tuvalu,216=Uganda,217=Ukraine,218=United Arab Emirates,219=United Kingdom,220=United States,221=Uruguay,222=US Virgin Islands,223=Uzbekistan,224=Vanuatu,225=Venezuela,226=Vietnam,227=Wallis and Futuna,228=Western Sahara,229=Yemen,230=Zambia,231=Zimbabwe]
  INDUSTRY Integer Industry [0=,1=Agriculture,2=Animal Products,3=Automotive/Automotive Parts,4=Business Services,5=Chemicals,6=Computers/Information Technology,7=Construction, Real Estate,8=Consumer Products,9=Cosmetics/Personal Care & Beauty Products,10=Education Services,11=Electronic/Electrical Products,12=Energy,13=Environmental,14=Fashion, Textiles & Garments,15=Food & Beverages,16=Furniture/Wood/Wood Products,17=Gifts/Crafts,18=Hobbies/Toys/Sports Goods,19=Home Appliances,20=Industrial Automation & Products,21=Industrial Products & Services [A-N],22=Industrial Products & Services [O-Z],23=Jewelry,24=Machinery,25=Marine/Shipbuilding,26=Medical & Health Services,27=Metals/Mineral/Materials,28=Office Equipment/Supplies,29=Paper/Printing/Publishing,30=Petroleum & Petrochemical,31=Product & Packaging Design,32=Safety and Security,33=Shipping/Logistics,34=Telecommunication Products,35=Transportation/Transport Equipment]
  CONTACT String*60 Contact
  JOBTITLE String*60 Job Title
  PHONE String*30 Mobile
  MOBILE String*30 Phone Number
  EMAIL1 String*60 Email1
  ENCREGID Binary*255 Registration Id
  ENCCHANNEL Binary*255 Channel
  ENCCLIENT Binary*255 Client
  PPLLISTING Integer Peppol Listing [0=Not Published,1=To Be Published,2=Published]
  PPLMSG String*250 last Peppol/SESAMi API message
  PPLCODE Integer last Peppol/SESAMi API return code
  NEXTDOCSEQ Long Next Incoming Document Sequence Number
  INVBASEURL String*250 Invoice Base URL for QR Code
  DISTITEM String*6 Default Dist for Item
  DISTALLOW String*6 Default Dist for Allowance
  DISTCHARGE String*6 Default Dist for Charge
  LSTRDATE Date Last Retrieval Date
  LSTRTIME Time Last Retrieval Time
  SST String*60 SST Registration Number
  TIN String*20 Tax Identification Number
  TTN String*20 Tourism Tax Registration Number
  MSIC String*5 Standard Industrial Classification

## EIPCUR - Peppol Currencies (view EI0600)
Keys (first = PK; D=dups allowed, M=modifiable): ID
Fields (NAME type description [values]):
  ID String*20 Peppol Currency
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*250 Short Description
  TEXTDESC String*250 Description

## EIPMIS - Peppol Allowances/Charges (view EI0610)
Keys (first = PK; D=dups allowed, M=modifiable): ID+CTYPE
Fields (NAME type description [values]):
  ID String*20 Peppol Allowance/Charge
  CTYPE Integer Code Type [1=Allowance,2=Charge]
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*250 Short Description
  TEXTDESC String*250 Description

## EIPUNT - Peppol UOMs (view EI0620)
Keys (first = PK; D=dups allowed, M=modifiable): ID
Fields (NAME type description [values]):
  ID String*20 Peppol UOM
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  NAME String*250 Short Description
  TEXTDESC String*250 Description

## EIUNIT - S300-Peppol UOM Mapping (view EI0780)
Keys (first = PK; D=dups allowed, M=modifiable): UNIT
Fields (NAME type description [values]):
  UNIT String*10 Sage 300 UOM
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PPLUNIT String*20 Peppol UOM

## EIVEND - Vendor eInvoicing (view EI0820)
Keys (first = PK; D=dups allowed, M=modifiable): IDVEND; PEPPOLID+CURNCODE [D,M]
Fields (NAME type description [values]):
  IDVEND String*12 Vendor Number
  AUDTDATE Date
  AUDTTIME Time
  AUDTUSER String*8
  AUDTORG String*6
  PEPPOLID String*50 Vendor Peppol ID
  CURNCODE String*3 Vendor Currency Code
  VENDTYPE Integer Vendor Type [1=AP Vendor,2=PO Vendor]
  DISTITEM String*6 Default Dist for Item
  DISTALLOW String*6 Default Dist for Allowance
  DISTCHARGE String*6 Default Dist for Charge
  SST String*60 SST Registration Number
  TIN String*20 Tax Identification Number
  CNTYNAME Integer Country Name [1=Afghanistan,2=Albania,3=Algeria,4=American Samoa,5=Andorra,6=Angola,7=Anguilla,8=Antarctica,9=Antigua and Barbuda,10=Argentina,11=Armenia,12=Aruba,13=Australia,14=Austria,15=Azerbaijan,16=Bahamas,17=Bahrain,18=Bangladesh,19=Barbados,20=Belarus,21=Belgium,22=Belize,23=Benin,24=Bermuda,25=Bhutan,26=Bolivia,27=Bosnia and Herzegovina,28=Botswana,29=Brazil,30=British Indian Ocean Territory,31=British Virgin Islands,32=Brunei,33=Bulgaria,34=Burkina Faso,35=Burma (Myanmar),36=Burundi,37=Cambodia,38=Cameroon,39=Canada,40=Cape Verde,41=Cayman Islands,42=Central African Republic,43=Chad,44=Chile,45=China,46=Christmas Island,47=Cocos (Keeling) Islands,48=Colombia,49=Comoros,50=Cook Islands,51=Costa Rica,52=Croatia,53=Cuba,54=Cyprus,55=Czech Republic,56=Democratic Republic of the Congo,57=Denmark,58=Djibouti,59=Dominica,60=Dominican Republic,61=Ecuador,62=Egypt,63=El Salvador,64=Equatorial Guinea,65=Eritrea,66=Estonia,67=Ethiopia,68=Falkland Islands,69=Faroe Islands,70=Fiji,71=Finland,72=France,73=French Polynesia,74=Gabon,75=Gambia,76=Georgia,77=Germany,78=Ghana,79=Gibraltar,80=Greece,81=Greenland,82=Grenada,83=Guam,84=Guatemala,85=Guinea,86=Guinea-Bissau,87=Guyana,88=Haiti,89=Holy See (Vatican City),90=Honduras,91=Hungary,92=Iceland,93=India,94=Indonesia,95=Iran,96=Iraq,97=Ireland,98=Isle of Man,99=Israel,100=Italy,101=Ivory Coast,102=Jamaica,103=Japan,104=Jersey,105=Jordan,106=Kazakhstan,107=Kenya,108=Kiribati,109=Kuwait,110=Kyrgyzstan,111=Laos,112=Latvia,113=Lebanon,114=Lesotho,115=Liberia,116=Libya,117=Liechtenstein,118=Lithuania,119=Luxembourg,120=Macedonia,121=Madagascar,122=Malawi,123=Malaysia,124=Maldives,125=Mali,126=Malta,127=Marshall Islands,128=Mauritania,129=Mauritius,130=Mayotte,131=Mexico,132=Micronesia,133=Moldova,134=Monaco,135=Mongolia,136=Montenegro,137=Montserrat,138=Morocco,139=Mozambique,140=Namibia,141=Nauru,142=Nepal,143=Netherlands,144=Netherlands Antilles,145=New Caledonia,146=New Zealand,147=Nicaragua,148=Niger,149=Nigeria,150=Niue,151=North Korea,152=Northern Mariana Islands,153=Norway,154=Oman,155=Pakistan,156=Palau,157=Panama,158=Papua New Guinea,159=Paraguay,160=Peru,161=Philippines,162=Pitcairn Islands,163=Poland,164=Portugal,165=Puerto Rico,166=Qatar,167=Republic of the Congo,168=Romania,169=Russia,170=Rwanda,171=Saint Barthelemy,172=Saint Helena,173=Saint Kitts and Nevis,174=Saint Lucia,175=Saint Martin,176=Saint Pierre and Miquelon,177=Saint Vincent and the Grenadines,178=Samoa,179=San Marino,180=Sao Tome and Principe,181=Saudi Arabia,182=Senegal,183=Serbia,184=Seychelles,185=Sierra Leone,186=Singapore,187=Slovakia,188=Slovenia,189=Solomon Islands,190=Somalia,191=South Africa,192=South Korea,193=Spain,194=Sri Lanka,195=Sudan,196=Suriname,197=Svalbard,198=Swaziland,199=Sweden,200=Switzerland,201=Syria,202=Taiwan,203=Tajikistan,204=Tanzania,205=Thailand,206=Timor-Leste,207=Togo,208=Tokelau,209=Tonga,210=Trinidad and Tobago,211=Tunisia,212=Turkey,213=Turkmenistan,214=Turks and Caicos Islands,215=Tuvalu,216=Uganda,217=Ukraine,218=United Arab Emirates,219=United Kingdom,220=United States,221=Uruguay,222=US Virgin Islands,223=Uzbekistan,224=Vanuatu,225=Venezuela,226=Vietnam,227=Wallis and Futuna,228=Western Sahara,229=Yemen,230=Zambia,231=Zimbabwe]
  TTN String*20 Tourism Tax Registration Number
  MSIC String*5 Standard Industrial Classification
  SELFBILL Integer Self-Billed Vendor [0=No,1=Yes]
