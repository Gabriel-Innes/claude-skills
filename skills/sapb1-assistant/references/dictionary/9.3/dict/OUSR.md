<!-- source: erpref.com (schema IP: SAP) | version: SAP Business One 9.3 | verified: 2026-10-01 -->
# OUSR - Users
Module: Administration | 113 columns | ObjType: 12
Indexes (name: columns; first = primary key; U = unique):
  PRIMARY U: USERID
  PASSWORD: PASSWORD
  USER_CODE U: USER_CODE
  INTERNAL U: INTERNAL_K
Fields (name type(len) description [values] ->parent table):
  USERID Int(6) User Signature
  PASSWORD nVarChar(254) User Password default=0
  PASSWORD1 nVarChar(8) User Password
  PASSWORD2 nVarChar(8) User Password
  INTERNAL_K Int(6) Internal Number
  USER_CODE nVarChar(25) User Code
  U_NAME nVarChar(155) User Name
  GROUPS Int(6) User Group default=0 [0=Regular, 99=Deleted]
  PASSWORD4 nVarChar(254) Password
  ALLOWENCES Text(16) User Confirmation
  SUPERUSER VarChar(1) Superuser default=N [Y=Yes, N=No]
  DISCOUNT Num(19,6) Max. Discount
  PASSWORD3 nVarChar(8) User Password
  Info1File nVarChar(4) Info1File
  Info1Field Int(6) Info1Field
  Info2File nVarChar(4) Info2File
  Info2Field Int(6) Info2Field
  Info3File nVarChar(4) Info3File
  Info3Field Int(6) Info3Field
  Info4File nVarChar(4) Info4File
  Info4Field Int(6) Info4Field
  dType VarChar(1) dType default=S [Y=Yes, N=No, X=, H=SHA1, S=SHA256]
  E_Mail nVarChar(100) E-Mail
  PortNum nVarChar(50) Mobile Phone Number
  OutOfOffic VarChar(1) Out of Office default=N [Y=Yes, N=No]
  SendEMail VarChar(1) Send E-Mail default=N [Y=Yes, N=No]
  SendSMS VarChar(1) Send SMS default=N [Y=Yes, N=No]
  DfltsGroup nVarChar(8) Defaults ->OUDG
  CashLimit VarChar(1) Cash Amount Limit default=N [Y=Yes, N=No]
  MaxCashSum Num(19,6) Max. Cash Total
  Fax nVarChar(20) Fax Number
  SendFax VarChar(1) Send Fax default=N [Y=Yes, N=No]
  Locked VarChar(1) User Locked default=N [Y=Yes, N=No]
  Department Int(6) Department default=-2 ->OUDP
  Branch Int(6) Branch default=-2 ->OUBR
  UserPrefs Text(16) User Preferences
  Language Int(11) Language
  Charset Int(6) Font Language
  OpenCdt VarChar(1) Open Window for Credit Reference default=N [Y=Yes, N=No]
  CdtPrvDays Int(11) Vouchers from Last Days default=1
  DsplyRates VarChar(1) Display Rate Table on start up default=N [Y=Yes, N=No]
  AuImpRates VarChar(1) Import Currency Rates Automatically default=N [Y=Yes, N=No]
  OpenDps VarChar(1) Open Postdated Checks Window default=N [Y=Yes, N=No]
  RcrFlag VarChar(1) Display Transactions Scheduled for Today default=N [Y=Yes, N=No]
  CheckFiles VarChar(1) File Check default=N [Y=Yes, N=No]
  OpenCredit VarChar(1) Open Postdated Credit Vouchers Window [Y=Always, N=No, D=By Date]
  CreditDay1 Int(6) Credit Handling Day 1 default=1
  CreditDay2 Int(6) Credit Handling Day 2 default=15
  WallPaper Text(16) Wallpaper
  WllPprDsp Int(6) Wallpaper Display [1=Centralized, 2=Full Screen, 3=Tile]
  AdvImagePr VarChar(1) Extended Image Processing [N=Partial, O=Without, Y=Full]
  ContactLog VarChar(1) Today's Activity Alert default=N [Y=Yes, N=No]
  LastWarned Date(8) Last Warned Date
  AlertPolFr Int(6) Message Check Frequency default=5
  ScreenLock Int(6) Screen Lock Delay default=30
  ShowNewMsg VarChar(1) Open Message on Arrival default=Y [Y=Yes, N=No]
  Picture nVarChar(200) Picture
  Position nVarChar(90) Position
  Address nVarChar(100) Address
  Country nVarChar(3) Country ->OCRY
  Tel1 nVarChar(20) Telephone 1
  Tel2 nVarChar(20) Telephone 2
  GENDER VarChar(1) Gender default=F [F=Female, M=Male]
  Birthday Date(8) Birthday
  EnbMenuFlt VarChar(1) Enable Forbidden Menu Items default=N [N=No, Y=Yes]
  objType nVarChar(20) Object Type - History default=12
  logInstanc Int(11) Log Instance - History
  userSign Int(6) Creating User - History ->OUSR
  createDate Date(8) Creation Date - History
  userSign2 Int(6) Updating User - History ->OUSR
  updateDate Date(8) Date of Update - History
  OneLogPwd VarChar(1) At first logon change password default=Y [N=Password should not be changed at first login, Y=Password should be changed at first login]
  lastLogin Date(8) Last Logon Date
  LastPwds Text(16) Last Passwords 1
  LastPwds2 nVarChar(254) Last Passwords 2 default=0
  LastPwdSet Date(8) Last Password Change
  FailedLog Int(11) Failed Login Count default=0
  PwdNeverEx VarChar(1) Password Never Expires default=N [Y=Yes, N=No]
  SalesDisc Num(19,6) Max. Sales Discount
  PurchDisc Num(19,6) Max. Purchase Discount
  LstLogoutD Date(8) Last Logoff Date
  LstLoginT Int(11) Last Logon Time
  LstLogoutT Int(11) Last Logoff Time
  LstPwdChT Int(11) Last Password Change Time
  LstPwdChB nVarChar(8) Last Password Changed By
  RclFlag VarChar(1) Display Recurring Transactions default=N [Y=Yes, N=No]
  MobileUser VarChar(1) Mobile User default=N [Y=Yes, N=No]
  MobileIMEI nVarChar(64) Mobile IMEI
  PrsWkCntEb VarChar(1) Personal Work Center Enable default=N [Y=Yes, N=No]
  SnapShotId Int(11) Snapshot ID default=0
  STData nVarChar(40) User Password Salt
  SupportUsr VarChar(1) Support User default=N [N=No, Y=Yes]
  NoSTPwdNum Int(6) Password encrypted w/o Salt (cryptography) default=0
  DomainUser nVarChar(50) Domain user name bound in SLD
  CUSAgree VarChar(1) CUS Agreement [Y=Yes, N=No]
  EmailSig Text(16) E-Mail Signature
  TPLId Int(6) Template ID ->UICU
  DigCrtPath Text(16) Digital Certificate Path
  ShowNewTsk VarChar(1) Open Worklist on Task Arrival default=Y [Y=Yes, N=No]
  IntgrtEb VarChar(1) Enable Setting Integration default=N [Y=Yes, N=No]
  AllBrnchF VarChar(1) Allow Viewing of All (Including Unassigned To) Branches in Financial Reports default=Y [Y=Yes, N=No]
  EvtNotify VarChar(1) Allow Event Notification default=Y
  IgnDtOwn VarChar(1) Ignore Data Ownership for this user default=N [Y=Yes, N=No]
  EnterAsTab VarChar(1) Use Numeric Keypad Enter Key as Tab Key default=N [Y=Yes, N=No]
  DotAsSep VarChar(1) Use Del Key As Separator default=N [Y=Yes, N=No]
  MouseOnly VarChar(1) Document Operation by Mouse Only default=N [Y=Yes, N=No]
  Color Int(6) Company Color [0=Combined, 1=Classic, 2=Gray, 3=Violet, 4=Blue, 5=Green, 6=Yellow, 7=Orange, 8=Red, 9=Brown]
  SkinType nVarChar(254) Skin Type
  Font nVarChar(50) Font
  FontSize Int(11) Font Size
  NaturalPer VarChar(1) Natural Person default=N [N=No, Y=Yes]
  DPPStatus VarChar(1) Data Protection Status default=N [N=None, D=Erased, B=Blocked, U=Unblocked]
  AutoAsnBPL VarChar(1) Auto. Assign Branches default=N [Y=Yes, N=No]
