# Luis Sandro González Solalinde
# A01365445
# Lenguajes y Traductores
# Entrega 3
import ply.yacc as yacc
import ply.lex as lex
import re

its=[]
varNames = []
symbolList = []
nums=[]
operators=[]
temporals=["T0" ,"T1" ,"T2" ,"T3" ,"T4" ,"T5" ,"T6" ,"T7" ,"T8" ,"T9" ,"T10" ,"T11" ,"T12" ,"T13" ,"T14" ,"T15" ,"T16" ,"T17" ,"T18" ,"T19" ,"T20" ,"T21" ,"T22" ,"T23" ,"T24" ,"T25" ,"T26" ,"T27" ,"T28" ,"T29" ,"T30" ,"T31" ,"T32" ,"T33" ,"T34" ,"T35" ,"T36" ,"T37" ,"T38" ,"T39" ,"T40" ,"T41" ,"T42" ,"T43" ,"T44" ,"T45" ,"T46" ,"T47" ,"T48" ,"T49" ,"T50" ,"T51" ,"T52" ,"T53" ,"T54" ,"T55" ,"T56" ,"T57" ,"T58" ,"T59" ,"T60" ,"T61" ,"T62" ,"T63" ,"T64" ,"T65" ,"T66" ,"T67" ,"T68" ,"T69" ,"T70" ,"T71" ,"T72" ,"T73" ,"T74" ,"T75" ,"T76" ,"T77" ,"T78" ,"T79" ,"T80" ,"T81" ,"T82" ,"T83" ,"T84" ,"T85" ,"T86" ,"T87" ,"T88" ,"T89" ,"T90" ,"T91" ,"T92" ,"T93" ,"T94" ,"T95" ,"T96" ,"T97" ,"T98" ,"T99" ,"T100" ,"T101" ,"T102" ,"T103" ,"T104" ,"T105" ,"T106" ,"T107" ,"T108" ,"T109" ,"T110" ,"T111" ,"T112" ,"T113" ,"T114" ,"T115" ,"T116" ,"T117" ,"T118" ,"T119" ,"T120" ,"T121" ,"T122" ,"T123" ,"T124" ,"T125" ,"T126" ,"T127" ,"T128" ,"T129" ,"T130" ,"T131" ,"T132" ,"T133" ,"T134" ,"T135" ,"T136" ,"T137" ,"T138" ,"T139" ,"T140" ,"T141" ,"T142" ,"T143" ,"T144" ,"T145" ,"T146" ,"T147" ,"T148" ,"T149" ,"T150" ,"T151" ,"T152" ,"T153" ,"T154" ,"T155" ,"T156" ,"T157" ,"T158" ,"T159" ,"T160" ,"T161" ,"T162" ,"T163" ,"T164" ,"T165" ,"T166" ,"T167" ,"T168" ,"T169" ,"T170" ,"T171" ,"T172" ,"T173" ,"T174" ,"T175" ,"T176" ,"T177" ,"T178" ,"T179" ,"T180" ,"T181" ,"T182" ,"T183" ,"T184" ,"T185" ,"T186" ,"T187" ,"T188" ,"T189" ,"T190" ,"T191" ,"T192" ,"T193" ,"T194" ,"T195" ,"T196" ,"T197" ,"T198" ,"T199" ,"T200" ,"T201" ,"T202" ,"T203" ,"T204" ,"T205" ,"T206" ,"T207" ,"T208" ,"T209" ,"T210" ,"T211" ,"T212" ,"T213" ,"T214" ,"T215" ,"T216" ,"T217" ,"T218" ,"T219" ,"T220" ,"T221" ,"T222" ,"T223" ,"T224" ,"T225" ,"T226" ,"T227" ,"T228" ,"T229" ,"T230" ,"T231" ,"T232" ,"T233" ,"T234" ,"T235" ,"T236" ,"T237" ,"T238" ,"T239" ,"T240" ,"T241" ,"T242" ,"T243" ,"T244" ,"T245" ,"T246" ,"T247" ,"T248" ,"T249" ,"T250" ,"T251" ,"T252" ,"T253" ,"T254" ,"T255" ,"T256" ,"T257" ,"T258" ,"T259" ,"T260" ,"T261" ,"T262" ,"T263" ,"T264" ,"T265" ,"T266" ,"T267" ,"T268" ,"T269" ,"T270" ,"T271" ,"T272" ,"T273" ,"T274" ,"T275" ,"T276" ,"T277" ,"T278" ,"T279" ,"T280" ,"T281" ,"T282" ,"T283" ,"T284" ,"T285" ,"T286" ,"T287" ,"T288" ,"T289" ,"T290" ,"T291" ,"T292" ,"T293" ,"T294" ,"T295" ,"T296" ,"T297" ,"T298" ,"T299" ,"T300" ,"T301" ,"T302" ,"T303" ,"T304" ,"T305" ,"T306" ,"T307" ,"T308" ,"T309" ,"T310" ,"T311" ,"T312" ,"T313" ,"T314" ,"T315" ,"T316" ,"T317" ,"T318" ,"T319" ,"T320" ,"T321" ,"T322" ,"T323" ,"T324" ,"T325" ,"T326" ,"T327" ,"T328" ,"T329" ,"T330" ,"T331" ,"T332" ,"T333" ,"T334" ,"T335" ,"T336" ,"T337" ,"T338" ,"T339" ,"T340" ,"T341" ,"T342" ,"T343" ,"T344" ,"T345" ,"T346" ,"T347" ,"T348" ,"T349" ,"T350" ,"T351" ,"T352" ,"T353" ,"T354" ,"T355" ,"T356" ,"T357" ,"T358" ,"T359" ,"T360" ,"T361" ,"T362" ,"T363" ,"T364" ,"T365" ,"T366" ,"T367" ,"T368" ,"T369" ,"T370" ,"T371" ,"T372" ,"T373" ,"T374" ,"T375" ,"T376" ,"T377" ,"T378" ,"T379" ,"T380" ,"T381" ,"T382" ,"T383" ,"T384" ,"T385" ,"T386" ,"T387" ,"T388" ,"T389" ,"T390" ,"T391" ,"T392" ,"T393" ,"T394" ,"T395" ,"T396" ,"T397" ,"T398" ,"T399" ,"T400" ,"T401" ,"T402" ,"T403" ,"T404" ,"T405" ,"T406" ,"T407" ,"T408" ,"T409" ,"T410" ,"T411" ,"T412" ,"T413" ,"T414" ,"T415" ,"T416" ,"T417" ,"T418" ,"T419" ,"T420" ,"T421" ,"T422" ,"T423" ,"T424" ,"T425" ,"T426" ,"T427" ,"T428" ,"T429" ,"T430" ,"T431" ,"T432" ,"T433" ,"T434" ,"T435" ,"T436" ,"T437" ,"T438" ,"T439" ,"T440" ,"T441" ,"T442" ,"T443" ,"T444" ,"T445" ,"T446" ,"T447" ,"T448" ,"T449" ,"T450" ,"T451" ,"T452" ,"T453" ,"T454" ,"T455" ,"T456" ,"T457" ,"T458" ,"T459" ,"T460" ,"T461" ,"T462" ,"T463" ,"T464" ,"T465" ,"T466" ,"T467" ,"T468" ,"T469" ,"T470" ,"T471" ,"T472" ,"T473" ,"T474" ,"T475" ,"T476" ,"T477" ,"T478" ,"T479" ,"T480" ,"T481" ,"T482" ,"T483" ,"T484" ,"T485" ,"T486" ,"T487" ,"T488" ,"T489" ,"T490" ,"T491" ,"T492" ,"T493" ,"T494" ,"T495" ,"T496" ,"T497" ,"T498" ,"T499" ,"T500" ,"T501" ,"T502" ,"T503" ,"T504" ,"T505" ,"T506" ,"T507" ,"T508" ,"T509" ,"T510" ,"T511" ,"T512" ,"T513" ,"T514" ,"T515" ,"T516" ,"T517" ,"T518" ,"T519" ,"T520" ,"T521" ,"T522" ,"T523" ,"T524" ,"T525" ,"T526" ,"T527" ,"T528" ,"T529" ,"T530" ,"T531" ,"T532" ,"T533" ,"T534" ,"T535" ,"T536" ,"T537" ,"T538" ,"T539" ,"T540" ,"T541" ,"T542" ,"T543" ,"T544" ,"T545" ,"T546" ,"T547" ,"T548" ,"T549" ,"T550" ,"T551" ,"T552" ,"T553" ,"T554" ,"T555" ,"T556" ,"T557" ,"T558" ,"T559" ,"T560" ,"T561" ,"T562" ,"T563" ,"T564" ,"T565" ,"T566" ,"T567" ,"T568" ,"T569" ,"T570" ,"T571" ,"T572" ,"T573" ,"T574" ,"T575" ,"T576" ,"T577" ,"T578" ,"T579" ,"T580" ,"T581" ,"T582" ,"T583" ,"T584" ,"T585" ,"T586" ,"T587" ,"T588" ,"T589" ,"T590" ,"T591" ,"T592" ,"T593" ,"T594" ,"T595" ,"T596" ,"T597" ,"T598" ,"T599" ,"T600" ,"T601" ,"T602" ,"T603" ,"T604" ,"T605" ,"T606" ,"T607" ,"T608" ,"T609" ,"T610" ,"T611" ,"T612" ,"T613" ,"T614" ,"T615" ,"T616" ,"T617" ,"T618" ,"T619" ,"T620" ,"T621" ,"T622" ,"T623" ,"T624" ,"T625" ,"T626" ,"T627" ,"T628" ,"T629" ,"T630" ,"T631" ,"T632" ,"T633" ,"T634" ,"T635" ,"T636" ,"T637" ,"T638" ,"T639" ,"T640" ,"T641" ,"T642" ,"T643" ,"T644" ,"T645" ,"T646" ,"T647" ,"T648" ,"T649" ,"T650" ,"T651" ,"T652" ,"T653" ,"T654" ,"T655" ,"T656" ,"T657" ,"T658" ,"T659" ,"T660" ,"T661" ,"T662" ,"T663" ,"T664" ,"T665" ,"T666" ,"T667" ,"T668" ,"T669" ,"T670" ,"T671" ,"T672" ,"T673" ,"T674" ,"T675" ,"T676" ,"T677" ,"T678" ,"T679" ,"T680" ,"T681" ,"T682" ,"T683" ,"T684" ,"T685" ,"T686" ,"T687" ,"T688" ,"T689" ,"T690" ,"T691" ,"T692" ,"T693" ,"T694" ,"T695" ,"T696" ,"T697" ,"T698" ,"T699" ,"T700" ,"T701" ,"T702" ,"T703" ,"T704" ,"T705" ,"T706" ,"T707" ,"T708" ,"T709" ,"T710" ,"T711" ,"T712" ,"T713" ,"T714" ,"T715" ,"T716" ,"T717" ,"T718" ,"T719" ,"T720" ,"T721" ,"T722" ,"T723" ,"T724" ,"T725" ,"T726" ,"T727" ,"T728" ,"T729" ,"T730" ,"T731" ,"T732" ,"T733" ,"T734" ,"T735" ,"T736" ,"T737" ,"T738" ,"T739" ,"T740" ,"T741" ,"T742" ,"T743" ,"T744" ,"T745" ,"T746" ,"T747" ,"T748" ,"T749" ,"T750" ,"T751" ,"T752" ,"T753" ,"T754" ,"T755" ,"T756" ,"T757" ,"T758" ,"T759" ,"T760" ,"T761" ,"T762" ,"T763" ,"T764" ,"T765" ,"T766" ,"T767" ,"T768" ,"T769" ,"T770" ,"T771" ,"T772" ,"T773" ,"T774" ,"T775" ,"T776" ,"T777" ,"T778" ,"T779" ,"T780" ,"T781" ,"T782" ,"T783" ,"T784" ,"T785" ,"T786" ,"T787" ,"T788" ,"T789" ,"T790" ,"T791" ,"T792" ,"T793" ,"T794" ,"T795" ,"T796" ,"T797" ,"T798" ,"T799" ,"T800" ,"T801" ,"T802" ,"T803" ,"T804" ,"T805" ,"T806" ,"T807" ,"T808" ,"T809" ,"T810" ,"T811" ,"T812" ,"T813" ,"T814" ,"T815" ,"T816" ,"T817" ,"T818" ,"T819" ,"T820" ,"T821" ,"T822" ,"T823" ,"T824" ,"T825" ,"T826" ,"T827" ,"T828" ,"T829" ,"T830" ,"T831" ,"T832" ,"T833" ,"T834" ,"T835" ,"T836" ,"T837" ,"T838" ,"T839" ,"T840" ,"T841" ,"T842" ,"T843" ,"T844" ,"T845" ,"T846" ,"T847" ,"T848" ,"T849" ,"T850" ,"T851" ,"T852" ,"T853" ,"T854" ,"T855" ,"T856" ,"T857" ,"T858" ,"T859" ,"T860" ,"T861" ,"T862" ,"T863" ,"T864" ,"T865" ,"T866" ,"T867" ,"T868" ,"T869" ,"T870" ,"T871" ,"T872" ,"T873" ,"T874" ,"T875" ,"T876" ,"T877" ,"T878" ,"T879" ,"T880" ,"T881" ,"T882" ,"T883" ,"T884" ,"T885" ,"T886" ,"T887" ,"T888" ,"T889" ,"T890" ,"T891" ,"T892" ,"T893" ,"T894" ,"T895" ,"T896" ,"T897" ,"T898" ,"T899" ,"T900" ,"T901" ,"T902" ,"T903" ,"T904" ,"T905" ,"T906" ,"T907" ,"T908" ,"T909" ,"T910" ,"T911" ,"T912" ,"T913" ,"T914" ,"T915" ,"T916" ,"T917" ,"T918" ,"T919" ,"T920" ,"T921" ,"T922" ,"T923" ,"T924" ,"T925" ,"T926" ,"T927" ,"T928" ,"T929" ,"T930" ,"T931" ,"T932" ,"T933" ,"T934" ,"T935" ,"T936" ,"T937" ,"T938" ,"T939" ,"T940" ,"T941" ,"T942" ,"T943" ,"T944" ,"T945" ,"T946" ,"T947" ,"T948" ,"T949" ,"T950" ,"T951" ,"T952" ,"T953" ,"T954" ,"T955" ,"T956" ,"T957" ,"T958" ,"T959" ,"T960" ,"T961" ,"T962" ,"T963" ,"T964" ,"T965" ,"T966" ,"T967" ,"T968" ,"T969" ,"T970" ,"T971" ,"T972" ,"T973" ,"T974" ,"T975" ,"T976" ,"T977" ,"T978" ,"T979" ,"T980" ,"T981" ,"T982" ,"T983" ,"T984" ,"T985" ,"T986" ,"T987" ,"T988" ,"T989" ,"T990" ,"T991" ,"T992" ,"T993" ,"T994" ,"T995" ,"T996" ,"T997" ,"T998" ,"T999"]
temporals.reverse()
temporalso=temporals
tempsInUse = []
ret_add = []
tempsUsed = []
quads=[]
auxiliar=[]
asig=""
step = []
count = 0
orindicator=0
size =""
subname = ""
jumpstart = []
reserved = {
	'prog' : 'Prog',
	'fin'  : 'Fin',
	'dim'  : 'Dim',
	'as'   : 'As',
	'main' : 'Main',
	'float': 'Float',
	'cls'  : 'CLS',
	'out'  : 'Out',
	'word' : 'Word',
	'endmain' : 'EndMain',
	'in'   : 'In',
	'do'   : 'Do',
	'until': 'Until',
	'while': 'While',
	'loop' : 'Loop',
	'for'  : 'For',
	'to'   : 'To',
	'step' : 'Step',
	'next' : 'Next',
	'gosub': 'GoSub',
	'and'  : 'And',
	'or'   : 'Or',
	'not'  : 'Not',
	'sub'  : 'Sub',
	'ret'  : 'Ret',
	'let'  : 'Let',
	'if'   : 'If',
	'then' : 'Then',
	'else' : 'Else',
	'elsif': 'Elsif',
	'endif': 'Endif',
	'wend' : 'Wend'
 }

tokens = ['ID','Coma','Num','Name','OP','CP','PYC','Menor','Mayor','Igual','Mas','Menos','Multi','Div','String']+ list(reserved.values())
t_ignore = r' '

def t_COMMENT(t):
	r'\#.*'
	pass

def t_ignore_newline(t):
	r'\n+'

def t_ID(t):
	r'[a-zA-Z_][a-zA-Z0-9_]*:'
	t.type=reserved.get(t.value,'ID')
	global subname
	subname= t.value
	return t

def t_Coma(t):
	r','
	t.type='Coma'
	return t

def t_Name(t):
	r'[_A-Za-z]+[_A-Za-z0-9]*'
	t.type=reserved.get(t.value,'Name')
	return t

def t_Num(t):
	r'\d+ | \d+.\d+'
	t.type='Num'
	t.value=int(t.value)
	nums.append(t.value)
	return t

def t_OP(t):
	r'\('
	t.type='OP'
	return t

def t_CP(t):
	r'\)'
	t.type='CP'
	return t

def t_PYC(t):
	r';'
	t.type='PYC'
	return t

def t_Menor(t):
	r'<'
	t.type='Menor'
	return t

def t_Mayor(t):
	r'>'
	t.type='Mayor'
	return t

def t_Igual(t):
	r'='
	t.type='Igual'
	return t

def t_Mas(t):
	r'\+'
	t.type='Mas'
	return t

def t_Menos(t):
	r'\-'
	t.type='Menos'
	return t

def t_Multi(t):
	r'\*'
	t.type='Multi'
	return t

def t_Div(t):
	r'/'
	t.type='Div'
	return t

def t_String(t):
	r'["][a-zA-Z 0-9:!@#$%^&*()-+=/?<>,]+["]'
	t.type='String'
	return t

def t_error(t):
	#print("Caracter no reconocido")
	t.lexer.skip(1)

lexer = lex.lex()




def p_Ordnas(p):
	'''
	Ordnas : Prog ID M Fin
	| Prog ID D M S Fin
	| Prog ID D M Fin
	| Prog ID M S Fin
	'''
	global count
	quads.append([count,"Fin"])
	print("Éxito. No hay errores en el código.")
	#print("Tabla de símbolos: ", symbolList)
	print("Cuádruplos: ",*quads,sep="\n")
	#print("\n")
	#symbolList.clear()
	#varNames.clear()
	#operators.clear()
	#global temporals
	#temporals=temporalso.copy()
	#tempsInUse.clear()
	#quads.clear()
	#global count
	#count = 0

def p_D(p):
	'''
	D : Dim N As Class PYC
	| D D
	'''

def p_N(p):
	'''
	N : Name
	| Name Coma N
	'''
	i=0
	while True:
		try:
			if(p[i]!=","):
				varNames.append(p[i])
			i=i+1
		except IndexError:
			break

def p_Class(p):
	'''
	Class : Float
	| Word
	| Float Size
	| Word Size
	'''
	global size
	while(len(varNames)>0):
		x=varNames.pop()
		if(str(x)!="None"):
			symbolList.append([str(x)+size,p[1]]) #Agregar que cheque que no existan las variables
		size=""


def p_Size(p):
	'''
	Size : OP Num CP
	| OP Num Coma Num CP
	| OP Num Coma Num Coma Num CP
	'''
	global size
	i=0
	while True:
		try:
			if(str(p[i])!="None"):
				size=size+str(p[i])
			i=i+1
		except IndexError:
			break

def p_Oper(p):
	'''
	Oper : Mul
	| Mul Mas Mul QMas
	| Mul Menos Mul QMin
	'''

def p_QMas(p):
	'''
	QMas :
	'''
	global operators
	for iterator in range(len(operators)):
		try:
			if (operators[iterator] == ''):
				operators.remove(operators[iterator])
			if ("(" in str(operators[iterator]) and not ")" in str(operators[iterator])):
				operators.remove(operators[iterator])
		except IndexError:
			break
	op2=operators.pop()
	op1=operators.pop()
	temp=temporals.pop()
	operators.append(temp)
	global count
	quads.append([count,"+",op1,op2,temp])
	tempsInUse.append(temp)
	count+=1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_QMin(p):
	'''
	QMin :
	'''
	global operators
	for iterator in range(len(operators)):
		#print(len(operators))
		try:
			if (operators[iterator]== ''):
				operators.remove(operators[iterator])
			if ("(" in str(operators[iterator]) and not ")" in str(operators[iterator])):
				operators.remove(operators[iterator])
		except IndexError:
			break
	op2 = operators.pop()
	op1 = operators.pop()
	temp = temporals.pop()
	operators.append(temp)
	global count
	quads.append([count, "-", op1, op2, temp])
	tempsInUse.append(temp)
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_QDiv(p):
	'''
	QDiv :
	'''
	global operators
	for iterator in range(len(operators)):
		#print(len(operators))
		try:
			if (operators[iterator] == ''):
				operators.remove(operators[iterator])
			if ("(" in str(operators[iterator]) and not ")" in str(operators[iterator])):
				operators.remove(operators[iterator])
		except IndexError:
			break
	op2 = operators.pop()
	op1 = operators.pop()
	temp = temporals.pop()
	operators.append(temp)
	global count
	quads.append([count, "/", op1, op2, temp])
	tempsInUse.append(temp)
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_QMul(p):
	'''
	QMul :
	'''
	global operators
	for iterator in range(len(operators)):
		try:
			if (operators[iterator] == ''):
				operators.remove(operators[iterator])
			if ("(" in str(operators[iterator])):
				if (")" not in str(operators[iterator])):
					print("no hay",operators[iterator])
					operators.remove(operators[iterator])
		except IndexError:
			break
	op2 = operators.pop()
	op1 = operators.pop()
	temp = temporals.pop()
	operators.append(temp)
	global count
	quads.append([count, "*", op1, op2, temp])
	tempsInUse.append(temp)
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_Mul(p):
	'''
	Mul : Par
	| Par Multi Par QMul
	| Par Div Par QDiv
	'''

def p_Par(p):
	'''
	Par : Num
	| Name
	| OP Oper CP
	| Name OP Num CP
	| Name OP Num Coma Num CP
	| Name OP Num Coma Num Coma Num CP
	| Name OP Name CP
	| Name OP Name Coma Name CP
	| Name OP Name Coma Name Coma Name CP
	'''
	x = ""
	if (type(p[1]) == int):
		operators.append(p[1])
	else:
		for i in range(0, 100):
			try:
				if(str(p[i])!="None"):
					x = x + str(p[i])
				#print(p[i])
			except IndexError:
				break
		operators.append(x)

def p_Var(p):
	'''
	Var : Name
	| Name OP Num CP
	| Name OP Num Coma Num CP
	| Name OP Num Coma Num Coma Num CP
	| Name OP Name CP
	| Name OP Name Coma Name CP
	| Name OP Name Coma Name Coma Name CP
	'''
	global asig
	x = ""
	for i in range(1, 9):
		try:
			if (str(p[i]) != "None"):
				x = x + str(p[i])
		except IndexError:
			break
	asig=x
	operators.append(x)


def p_VarC(p):
	'''
	VarC : Name
	| Name OP Num CP
	| Name OP Num Coma Num CP
	| Name OP Num Coma Num Coma Num CP
	| Name OP Name CP
	| Name OP Name Coma Name CP
	| Name OP Name Coma Name Coma Name CP
	| Num
	'''
	x=""
	if(type(p[1])==int):
		operators.append(p[1])
	else:
		for i in range(1,100):
			try:
				if(str(p[i])!="None"):
					x=x+p[i]
			except IndexError:
				break
		operators.append(x)

def p_L(p):
	'''
	L : Let Var Igual Oper
	'''
	global count
	global asig
	#print(operators)
	x=operators.pop()
	#print(x)
	if(str(x).isdigit()):
		quads.append([count,"=",asig,x])
	else:
		quads.append([count,"=",asig,tempsInUse.pop()])
	operators.append(x)
	count = count + 1

def p_M(p):
	'''
	M : Main Action EndMain
	'''
	global count
	quads.append([count,"Endmain"])
	count = count +1
def p_Action(p):
	'''
	Action : L PYC
	| CLS PYC
	| O PYC
	| Ins PYC
	| Ifs PYC
	| W PYC
	| Dos PYC
	| Fors PYC
	| G PYC
	| L PYC Action
	| CLS PYC Action
	| O PYC Action
	| Ins PYC Action
	| Ifs PYC Action
	| W PYC Action
	| Dos PYC Action
	| Fors PYC Action
	| G PYC Action
	'''

def p_O(p):
	'''
	O : Out String
	'''
	global count
	quads.append([count,"Out",p[2]])
	count=count+1

def p_Ins(p):
	'''
	Ins : In String Var
	'''
	global count
	quads.append([count, "In", p[2],operators.pop()])
	count = count + 1

def p_Ifs(p):
	'''
	Ifs : If Cond QIf Then Action QIfEnd1 Endif
	| If Cond QIf Then Action QIfEnd1 Elsif Ifs
	| If Cond QIf Then Action QIfEnd2 Else QIf Action QIfEnd3 Endif
	'''

def p_QIf(p):
	'''
	QIf :
	'''
	global jumpstart
	global count
	x=count
	jumpstart.append(x)
	count = count + 1



def p_QIfEnd1(p):
	'''
	QIfEnd1 :
	'''
	global jumpstart
	global count
	x=jumpstart.pop()
	for i in range(count-x-1):
		auxiliar.append(quads.pop())
	quads.append([x,"Gotof",tempsInUse.pop(),count])
	for i in range(len(auxiliar)):
		quads.append(auxiliar.pop())

def p_QIfEnd2(p):
	'''
	QIfEnd2 :
	'''
	global jumpstart
	global count
	x=jumpstart.pop()
	for i in range(count-x-1):
		auxiliar.append(quads.pop())
	quads.append([x,"Gotof",tempsInUse.pop(),count+1])
	for i in range(len(auxiliar)):
		quads.append(auxiliar.pop())

def p_QIfEnd3(p):
	'''
	QIfEnd3 :
	'''
	global jumpstart
	global count
	x=jumpstart.pop()
	for i in range(count-x-1):
		auxiliar.append(quads.pop())
	quads.append([x,"Goto",count])
	for i in range(len(auxiliar)):
		quads.append(auxiliar.pop())



def p_W(p):
	'''
	W : While Cond QWhile Action QWhileEnd Wend
	'''

def p_QWhile(p):
	'''
	QWhile :
	'''
	global jumpstart
	global count
	x=count
	jumpstart.append(x)
	count = count + 1

def p_QWhileEnd(p):
	'''
	QWhileEnd :
	'''
	global jumpstart
	global count
	global orindicator
	x = jumpstart.pop()
	for i in range(count - x-1):
		auxiliar.append(quads.pop())
	a=tempsInUse.pop()
	quads.append([x, "Gotof", a, count+1])
	for i in range(len(auxiliar)):
		quads.append(auxiliar.pop())
	if(orindicator==1):
		quads.append([count, "Goto", x - 3])
	else:
		quads.append([count,"Goto",x-1])
	orindicator=0
	count=count+1

def p_Dos(p):
	'''
	Dos : Do OP While Cond QWhile CP Action QWhileEnd Loop
	| Do OP Until Cond QDo CP Action QDoEnd Loop
	'''

def p_QDo(p):
	'''
	QDo :
	'''
	global jumpstart
	global count
	x = count
	jumpstart.append(x)
	count = count + 2

def p_QDoEnd(p):
	'''
	QDoEnd :
	'''
	global jumpstart
	global count
	x = jumpstart.pop()
	for i in range(count - x-2):
		auxiliar.append(quads.pop())
	quads.append([x, "Gotof", tempsInUse.pop(), x + 2])
	quads.append([x+1,"Goto",count+1])
	for i in range(len(auxiliar)):
		quads.append(auxiliar.pop())
	quads.append([count, "Goto", x - 1])
	count = count + 1


def p_Fors(p):
	'''
	Fors : For Var Igual VarC To VarC Step VarC QFor Action QForEnd Next

	'''

def p_QFor(p):
	'''
	QFor :
	'''
	global jumpstart
	global count
	global step
	step.append(operators.pop()) #Step

	b = operators.pop() #Límite
	c = operators.pop() #Valor incial
	d = operators.pop()#Variable
	quads.append([count, "=", str(d), c])
	its.append(d)
	count = count + 1
	x = temporals.pop()
	quads.append([count, "=", x, b])
	tempsUsed.append(x)

	count = count + 1
	tempsInUse.append(x)
	x = temporals.pop()
	z=temporals.pop()
	quads.append([count,"<=",str(d),tempsInUse.pop(),x])
	tempsInUse.append(x)
	count=count+1
	y = count
	jumpstart.append(y)
	count = count + 1
	tempsUsed.append(y)
	tempsUsed.append(z)


def p_QForEnd(p):
	'''
	QForEnd :
	'''
	global jumpstart
	global count
	global step
	x = jumpstart.pop()
	for i in range(count - x - 1):
		auxiliar.append(quads.pop())
	quads.append([x, "Gotof", tempsInUse.pop(), count + 2])
	for i in range(len(auxiliar)):
		quads.append(auxiliar.pop())
	#y=tempsInUse.pop()
	#print(tempsInUse)
	d=its.pop()
	#print("d",d)
	quads.append([count,"+",d,step.pop(),d])
	count=count+1
	quads.append([count, "Goto", x - 1])
	count = count + 1


def p_G(p):
	'''
	G : GoSub ID
	'''
	global count
	x=count+1
	ret_add.append(x)
	quads.append([count,"Gosub",p[2]])
	count = count +1

def p_Cond(p):
	'''
	Cond : OP Cond CP
	| Not OP Cond CP
	| OP Cond CP And Cond QAnd
	| OP Cond CP Or Cond QOr
	| Not OP Cond CP And Cond QAnd
	| Not OP Cond CP Or Cond QOr
	| VarC Mayor VarC QGre
	| VarC Menor VarC QLes
	| VarC Igual VarC QEq
	| VarC Mayor Num QGre
	| VarC Menor Num QLes
	| VarC Igual Num QEq
	| Num Mayor VarC QGre
	| Num Menor VarC QLes
	| Num Igual VarC QEq
	| Num Mayor Num QGre
	| Num Menor Num QLes
	| Num Igual Num QEq
	| VarC Mayor VarC QGre And Cond QAnd
	| VarC Menor VarC QLes And Cond QAnd
	| VarC Igual VarC QEq And Cond QAnd
	| VarC Mayor Num QGre And Cond QAnd
	| VarC Menor Num QLes And Cond QAnd
	| VarC Igual Num QEq And Cond QAnd
	| Num Mayor VarC QGre And Cond QAnd
	| Num Menor VarC QLes And Cond QAnd
	| Num Igual VarC QEq And Cond QAnd
	| Num Mayor Num QGre And Cond QAnd
	| Num Menor Num QLes And Cond QAnd
	| Num Igual Num QEq And Cond QAnd
	| VarC Mayor VarC QGre Or Cond QOr
	| VarC Menor VarC QLes Or Cond QOr
	| VarC Igual VarC QEq Or Cond QOr
	| VarC Mayor Num QGre Or Cond QOr
	| VarC Menor Num QLes Or Cond QOr
	| VarC Igual Num QEq Or Cond QOr
	| Num Mayor VarC QGre Or Cond QOr
	| Num Menor VarC QLes Or Cond QOr
	| Num Igual VarC QEq Or Cond QOr
	| Num Mayor Num QGre Or Cond QOr
	| Num Menor Num QLes Or Cond QOr
	| Num Igual Num QEq Or Cond QOr
	'''

def p_QGre(p):
	'''
	QGre :
	'''
	op2 = operators.pop()
	op1 = operators.pop()
	temp = temporals.pop()
	operators.append(temp)
	tempsInUse.append(temp)
	global count
	quads.append([count, ">", op1, op2, temp])
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)
def p_QLes(p):
	'''
	QLes :
	'''
	op2 = operators.pop()
	op1 = operators.pop()
	temp = temporals.pop()
	operators.append(temp)
	tempsInUse.append(temp)
	global count
	quads.append([count, "<", op1, op2, temp])
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_QEq(p):
	'''
	QEq :
	'''
	op2 = operators.pop()
	op1 = operators.pop()
	temp = temporals.pop()
	operators.append(temp)
	tempsInUse.append(temp)
	global count
	quads.append([count, "==", op1, op2, temp])
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_QAnd(p):
	'''
	QAnd :
	'''
	op2 = tempsInUse.pop()
	op1 = tempsInUse.pop()
	temp = temporals.pop()
	operators.append(temp)
	tempsInUse.append(temp)
	global count
	quads.append([count, "AND", op1, op2, temp])
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_QOr(p):
	'''
	QOr :
	'''
	global orindicator
	orindicator = 1
	op2 = tempsInUse.pop()
	op1 = tempsInUse.pop()
	temp = temporals.pop()
	operators.append(temp)
	tempsInUse.append(temp)
	global count
	quads.append([count, "OR", op1, op2, temp])
	count += 1
	if op1 in temporalso:
		temporals.append(op1)
	if op2 in temporalso:
		temporals.append(op2)
	tempsUsed.append(temp)

def p_S(p):
	'''
	S : Sub ID QSub Action Ret QSubEnd
	| Sub ID QSub Action Ret QSubEnd S
	'''

def p_QSub(p):
	'''
	QSub :
	'''
	global count
	global subname
	quads.append([count,"Sub",subname])
	count = count +1

def p_QSubEnd(p):
	'''
	QSubEnd :
	'''
	global ret_add
	global count
	quads.append([count, "Goto", ret_add.pop(0)])
	count = count + 1

def p_error(p):
	print("Hay Error(es) en el código")
	print(p)

parser = yacc.yacc()

def execution():
	for iterator in range(len(tempsUsed)):
		vars()[tempsUsed[iterator]]=float(0)
	for iterator in range(len(symbolList)):
		if("(" in symbolList[iterator][0]):
			axxa=symbolList[iterator][0].split("(")
			#print(axxa,"x")
			if(len(axxa[1])==2 or len(axxa[1])==3):
				tam = 1
			elif(len(axxa[1])==4 or len(axxa[1])==5):
				tam = 2
			elif(len(axxa[1])==6 or len(axxa[1])==7):
				tam = 3
			if (symbolList[iterator][1] == "word"):
				if(tam==3):
					vars()[axxa[0]] = [[[int(0) for pololo in range(0, int(axxa[1][0]))]for iterator in range(0, int(axxa[1][2]))]for seconditerator in range(0, int(axxa[1][4]))]

				elif(tam == 2):
					vars()[axxa[0]] = []
					for iterator in range(0, int(axxa[1][2])):
						vars()[axxa[0]].append([int(0) for pololo in range(0, int(axxa[1][0]))])
				elif(tam == 1):
					vars()[axxa[0]] = [int(0) for pololo in range(0, int(axxa[1].strip(")")))]
			else:
				if (tam == 3):
					helpingarray = []
					vars()[axxa[0]] = []
					for iterator in range(0, int(axxa[1][2])):
						helpingarray.append([float(0.0) for pololo in range(0, int(axxa[1][0]))])
					for seconditerator in range(0, int(axxa[1][4])):
						vars()[axxa[0]].append(helpingarray)
				elif (tam == 2):
					vars()[axxa[0]] = []
					for iterator in range(0,int(axxa[1][2])):
						vars()[axxa[0]].append([float(0.0) for pololo in range(0, int(axxa[1][0]))])
				elif (tam == 1):
					vars()[axxa[0]] = [float(0.0) for pololo in range(0, int(axxa[1][0]))]
		else:
			if(symbolList[iterator][1]=="word"):
				vars()[symbolList[iterator][0]]=int(0)
			else:
				vars()[symbolList[iterator][0]] = float(0.0)
	#print(locals())
	quads.reverse()
	a=0
	b=0
	c=0
	usedQuads=[]
	while quads:
		currentQuad = quads.pop()
		#print(currentQuad)
		if (currentQuad[1] == "+"):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if(tam==1):
						if(type(axxa[1][0])==str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a= locals()[axxa[0]][int(axxa[1][0])]
					elif(tam==2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif(type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif(tam==3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a=currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if(tam==1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			c = a + b
			locals()[currentQuad[4]]=c
			#print((currentQuad[4],locals()[currentQuad[4]])
			usedQuads.append(currentQuad)

		elif (currentQuad[1] == "-"):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			c = a - b
			locals()[currentQuad[4]] = c
			#print((currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)

		elif (currentQuad[1] == "*"):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (not axxa[1][0].isnumeric() ):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			c = a * b
			locals()[currentQuad[4]] = c
			#print((currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)

		elif (currentQuad[1] == "/"):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			if(type(locals()[currentQuad[4]])==int):
				c = int(a / b)
			else:
				c=float(a/b)
			locals()[currentQuad[4]] = c
			usedQuads.append(currentQuad)

		elif (currentQuad[1] == "="):
			d=currentQuad[3]
			#print(currentQuad[2])
			if(isinstance(d,(int))):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					#print(axxa)
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							locals()[axxa[0]][locals()[axxa[1][0]]] = int(currentQuad[3])
						else:
							locals()[axxa[0]][int(axxa[1][0])] = int(currentQuad[3])
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]] =int(currentQuad[3])
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])] =int(currentQuad[3])
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]] =int(currentQuad[3])
						else:
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])] =int(currentQuad[3])
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]] = int(currentQuad[3])
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])] = int(currentQuad[3])
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]] = int(currentQuad[3])
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])] = int(currentQuad[3])
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]] = int(currentQuad[3])
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])] = int(currentQuad[3])
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]] = int(currentQuad[3])
						else:
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])] = int(currentQuad[3])
				else:
					locals()[currentQuad[2]] = int(currentQuad[3])
			elif(isinstance(d,(float))):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							locals()[axxa[0]][locals()[axxa[1][0]]] = float(currentQuad[3])
						else:
							locals()[axxa[0]][int(axxa[1][0])] = float(currentQuad[3])
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]] =float(currentQuad[3])
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])] =float(currentQuad[3])
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]] =float(currentQuad[3])
						else:
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])] =float(currentQuad[3])
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]] = float(currentQuad[3])
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])] = float(currentQuad[3])
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]] = float(currentQuad[3])
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])] = float(currentQuad[3])
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]] = float(currentQuad[3])
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])] = float(currentQuad[3])
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]] = float(currentQuad[3])
						else:
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])] = float(currentQuad[3])
				else:
					locals()[currentQuad[2]] = float(currentQuad[3])
			else:
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					#print(axxa)
					#print(axxa,len(axxa[1]))
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							locals()[axxa[0]][locals()[axxa[1][0]]] = int(locals()[currentQuad[3]])
						else:
							locals()[axxa[0]][int(axxa[1][0])] = int(locals()[currentQuad[3]])
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]] = int(locals()[currentQuad[3]])
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])] = int(locals()[currentQuad[3]])
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]] = int(locals()[currentQuad[3]])
						else:
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])] = int(locals()[currentQuad[3]])
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]] = int(locals()[currentQuad[3]])
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])] = int(locals()[currentQuad[3]])
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]] = int(locals()[currentQuad[3]])
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])] = int(locals()[currentQuad[3]])
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]] = int(locals()[currentQuad[3]])
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])] = int(locals()[currentQuad[3]])
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]] = int(locals()[currentQuad[3]])
						else:
							locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])] = int(locals()[currentQuad[3]])
				else:
					#print(currentQuad)
					try:
						if(type(locals()[currentQuad[2]])==int):
							locals()[currentQuad[2]] = int(locals()[currentQuad[3]])
						else:
							locals()[currentQuad[2]] = float(locals()[currentQuad[3]])
					except KeyError:
						locals()[currentQuad[2]] = int(locals()[currentQuad[3]])
			usedQuads.append(currentQuad)

		elif (currentQuad[1] == ">"):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			if(a>b):
				locals()[currentQuad[4]]=1
				#print("r",currentQuad[4], locals()[currentQuad[4]])
			else:
				locals()[currentQuad[4]]=0
				#print("r",currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)

		elif (currentQuad[1] == "<"):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			if(a<b):
				locals()[currentQuad[4]]=1
				#print("a",currentQuad[4], locals()[currentQuad[4]])
			else:
				locals()[currentQuad[4]]=0
				#print("a",currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)
		elif (currentQuad[1] == "<="):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
				#print("b",b)
			if(a<=b):
				locals()[currentQuad[4]]=1
				#print("a",currentQuad[4], locals()[currentQuad[4]])
			else:
				locals()[currentQuad[4]]=0
				#print("a",currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)
		elif (currentQuad[1] == "=="):
			if (type(currentQuad[2]) == str):
				if ("(" in currentQuad[2]):
					axxa = currentQuad[2].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							a = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				if ("(" in currentQuad[3]):
					axxa = currentQuad[3].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])]
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]
						else:
							b = locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]
				else:
					b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			if(a==b):
				locals()[currentQuad[4]]=1
				#print("a",currentQuad[4], locals()[currentQuad[4]])
			else:
				locals()[currentQuad[4]]=0
				#print("a",currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)
		elif (currentQuad[1] == "AND"):
			if (type(currentQuad[2]) == str):
				a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			if (a==1 and  b==1):
				locals()[currentQuad[4]] = 1
				#print("a", currentQuad[4], locals()[currentQuad[4]])
			else:
				locals()[currentQuad[4]] = 0
				#print("a", currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)

		elif (currentQuad[1] == "OR"):
			if (type(currentQuad[2]) == str):
				a = locals()[currentQuad[2]]
			else:
				a = currentQuad[2]
			if (type(currentQuad[3]) == str):
				b = locals()[currentQuad[3]]
			else:
				b = currentQuad[3]
			if (a==1 or b==1):
				locals()[currentQuad[4]] = 1
				#print("a", currentQuad[4], locals()[currentQuad[4]])
			else:
				locals()[currentQuad[4]] = 0
				#print("a", currentQuad[4], locals()[currentQuad[4]])
			usedQuads.append(currentQuad)
		elif (currentQuad[1] == "Gotof"):
			a = currentQuad[0]
			b = currentQuad[3]
			c= locals()[currentQuad[2]]
			if(c==0):
				#print(quads)
				#print(usedQuads)
				if (a > b):
					usedQuads.append(currentQuad)
					for iterator in range(currentQuad[0] - currentQuad[3]+1):
						quads.append(usedQuads.pop())
				else:
					usedQuads.append(currentQuad)
					for iterator in range(currentQuad[3] - currentQuad[0] -1):
						usedQuads.append(quads.pop())
				#print(quads)
				#print(usedQuads)
			else:
				usedQuads.append(currentQuad)

		elif (currentQuad[1] == "Goto"):
			a=currentQuad[0]
			b = currentQuad[2]
			#print(quads)
			#print(usedQuads)
			if(a>b):
				usedQuads.append(currentQuad)
				for iterator in range(a-b+1):
					#print(currentQuad[0],currentQuad[2])
					quads.append(usedQuads.pop())
			else:
				usedQuads.append(currentQuad)
				for iterator in range(b-a-1):
					usedQuads.append(quads.pop())
		elif (currentQuad[1] == "In"):
			b = currentQuad[2].strip("\"")
			a = re.findall(r'\%\w+', currentQuad[2].strip("\""))
			auxiliar = []
			for iterator in range(len(a)):
				auxiliar.append(a[iterator].replace(a[iterator], a[iterator].strip("%")))
			for iterator in range(len(a)):
				if("(" in a[iterator]):
					axxa = a[iterator].split("(")
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (type(axxa[1][0]) == str):
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]]))
						else:
							b = b.replace(a[iterator], str(locals()[axxa[0]][int(axxa[1][0])]))
					elif (tam == 2):
						if (type(axxa[1][0]) == str and type(axxa[1][2]) == str):
							b = b.replace(a[iterator], str([axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]))
						elif (type(axxa[1][0]) == str and type(axxa[1][2]) != str):
							b = b.replace(a[iterator], str([axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]))
						elif (type(axxa[1][0]) != str and type(axxa[1][2]) == str):
							b = b.replace(a[iterator], str([axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]))
						else:
							b = b.replace(a[iterator], str([axxa[0]][int(axxa[1][0])][int(axxa[1][2])]))
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]))
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]))
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]))
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]))
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]))
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]))
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]))
						else:
							b = b.replace(a[iterator], str(locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]))
				else:
					b = b.replace(a[iterator], str(locals()[auxiliar[iterator]]))
			print(b)
			if(type(locals()[currentQuad[3]])==int):
				locals()[currentQuad[3]]=int(input())
			else:
				locals()[currentQuad[3]] = float(input())
			#print(currentQuad[3],locals()[currentQuad[3]])
			usedQuads.append(currentQuad)
		elif (currentQuad[1] == "Out"):
			b=currentQuad[2].strip("\"")
			a=re.findall(r'%[^\s]+',currentQuad[2].strip("\""))
			#print("a,",a)
			auxiliar=[]
			for iterator in range(len(a)):
				auxiliar.append(a[iterator].replace(a[iterator],a[iterator].strip('%')))
			for iterator in range(len(auxiliar)):
				if ("(" in auxiliar[iterator]):
					axxa = auxiliar[iterator].split("(")
					#print(auxiliar[iterator])
					if (len(axxa[1]) == 1 or len(axxa[1]) == 2):
						tam = 1
					elif (len(axxa[1]) == 3 or len(axxa[1]) == 4):
						tam = 2
					elif (len(axxa[1]) == 5 or len(axxa[1]) == 6):
						tam = 3
					if (tam == 1):
						if (axxa[1][0].isnumeric()):
							#print(axxa[1][0])
							b = b.replace(a[iterator], str(locals()[axxa[0]][int(axxa[1][0])]))
						else:
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]]))
					elif (tam == 2):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]]))
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])]))
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric()):
							b = b.replace(a[iterator], str(locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]]))
						else:
							b = b.replace(a[iterator],str(locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])]))
					elif (tam == 3):
						if (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(
								locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][locals()[axxa[1][4]]]))
						elif (not axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(
								locals()[axxa[0]][locals()[axxa[1][0]]][locals()[axxa[1][2]]][int(axxa[1][4])]))
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(
								locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][locals()[axxa[1][4]]]))
						elif (not axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(
								locals()[axxa[0]][locals()[axxa[1][0]]][int(axxa[1][2])][int(axxa[1][4])]))
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(
								locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][locals()[axxa[1][4]]]))
						elif (axxa[1][0].isnumeric() and not axxa[1][2].isnumeric() and axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(
								locals()[axxa[0]][int(axxa[1][0])][locals()[axxa[1][2]]][int(axxa[1][4])]))
						elif (axxa[1][0].isnumeric() and axxa[1][2].isnumeric() and not axxa[1][4].isnumeric()):
							b = b.replace(a[iterator], str(
								locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][locals()[axxa[1][4]]]))
						else:
							b = b.replace(a[iterator],
										  str(locals()[axxa[0]][int(axxa[1][0])][int(axxa[1][2])][int(axxa[1][4])]))
				else:
					b = b.replace(a[iterator], str(locals()[auxiliar[iterator]]))
			print(b.replace('%',''))
			usedQuads.append(currentQuad)
		elif(currentQuad[1]=="Endmain"):
			break
		elif(currentQuad[1]== "Sub"):
			usedQuads.append(currentQuad)
		elif(currentQuad[1]=="Gosub"):
			currPlace = currentQuad[0]
			for iterator in range(len(quads)):
				try:
					if(quads[iterator][1]== "Sub" and quads[iterator][2]== currentQuad[2]):
						checkQuad = quads[iterator][0]
				except IndexError:
					break
			for iterator in range(len(usedQuads)):
				try:
					if (usedQuads[iterator][1] == "Sub" and usedQuads[iterator][2] == currentQuad[2]):
						checkQuad = quads[iterator][0]
				except IndexError:
					break
			if (currPlace > checkQuad):
				usedQuads.append(currentQuad)
				for iterator in range(currPlace - checkQuad +1):
					# print(currentQuad[0],currentQuad[2])
					quads.append(usedQuads.pop())
			else:
				usedQuads.append(currentQuad)
				for iterator in range(checkQuad - currPlace-1):
					usedQuads.append(quads.pop())


while True:
	try:
		nombre=input('Ordnas -> ') # hay dos archivos prueba: prueba.txt y matrices.txt
		file=open(nombre,'r')
		s=file.read()
		file.close()
	except EOFError:
		break
	parser.parse(s,debug=0) # Agregar  ',deubug = 1' en el paréntesis para ver el proceso entero
	execution()
