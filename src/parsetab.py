
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightNewleftLessLessEqualGreaterGreaterEqualEqualsDifferentrightLPARENTHESISRPARENTHESISADD Alter AlterB Bool Break CALL COMMA Case DIV Different Else Equals Este False Greater GreaterEqual Hammer ID IsTrue LPARENTHESIS Less LessEqual MUL MoveLeft MoveRight New Norte Num Number Oeste PRINCIPAL PrintValues Proc RPARENTHESIS Repeat SEMMICOLOM SUB Stop Sur TEXTVALUE Then True Until Values When Whilestart : main\n            | main Procedmain :  Proc PRINCIPAL LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOMProced : Proc ID LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOMrecursivo : recursivo instruccion\n                 recursivo : instruccioninstruccion : varDeclaration\n                     | Values_f\n                     | Alter_f\n                     | AlterB_f\n                     | MoveRight_f\n                     | MoveLeft_f\n                     | Hammer_f\n                     | Stop_f\n                     | IsTrue_f\n                     | Repeat_f\n                     | Until_f\n                     | While_f\n                     | Case_f\n                     | Case2_f\n                     | PrintValues_f\n                     | call_f\n                     | emptyValues_f : Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOMvalorDato : True\n                | False\n                | Number\n                | Alter_f\n                | AlterB_fAlter_f : Alter LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM\n               | Alter LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM\n               | Alter LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM\n               | Alter LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOMAlterB_f : AlterB LPARENTHESIS ID RPARENTHESIS SEMMICOLOMMoveRight_f : MoveRight SEMMICOLOMMoveLeft_f : MoveLeft SEMMICOLOMHammer_f : Hammer LPARENTHESIS Norte RPARENTHESIS SEMMICOLOM\n                 | Hammer LPARENTHESIS Sur RPARENTHESIS SEMMICOLOM\n                 | Hammer LPARENTHESIS Este RPARENTHESIS SEMMICOLOM\n                 | Hammer LPARENTHESIS Oeste RPARENTHESIS SEMMICOLOMStop_f : Stop SEMMICOLOMRepeat_f : Repeat LPARENTHESIS recursivo Break RPARENTHESIS SEMMICOLOMUntil_f : Until LPARENTHESIS recursivo RPARENTHESIS condicional SEMMICOLOMWhile_f : While condicional LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOMCase_f : Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM\n              | Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS recursivo RPARENTHESIS Else LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOMopciones : opciones When valorDato Then LPARENTHESIS recursivo RPARENTHESIS\n                | When valorDato Then LPARENTHESIS recursivo RPARENTHESISCase2_f : Case ID opciones SEMMICOLOM\n                | Case ID opciones Else recursivo SEMMICOLOM something : ID COMMA something\n                 | expresionNum COMMA something\n                 | expresionNum\n                 | Number COMMA something\n                 | Number\n                 | TEXTVALUE COMMA something\n                 | emptyPrintValues_f : PrintValues LPARENTHESIS something RPARENTHESIS SEMMICOLOM empty : condicional : IsTrue_f\n                   | Greater_f\n                   | GreaterEqual_f\n                   | Equals_f\n                   | Different_f\n                   | LessEqual_f\n                   | Less_fIsTrue_f : IsTrue ID SEMMICOLOMGreater_f : expresionNum Greater expresionNum SEMMICOLOMGreaterEqual_f : expresionNum GreaterEqual expresionNum SEMMICOLOMEquals_f : expresionNum Equals expresionNum SEMMICOLOMDifferent_f : expresionNum Different expresionNum SEMMICOLOMLessEqual_f : expresionNum LessEqual expresionNum SEMMICOLOMLess_f : expresionNum Less expresionNum SEMMICOLOMvarDeclaration : New ID COMMA LPARENTHESIS tipoDatos COMMA valorDato RPARENTHESIS SEMMICOLOM expresionNum : ID\n                     | Alter_f tipoDatos : Bool\n                 | Numcall_f : CALL LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'
    
_lr_action_items = {'Proc':([0,2,74,],[3,5,-3,]),'$end':([1,2,4,74,103,],[0,-1,-2,-3,-4,]),'PRINCIPAL':([3,],[6,]),'ID':([5,29,37,40,41,48,49,50,71,72,87,88,89,90,91,92,93,113,132,133,134,135,],[7,47,55,66,70,76,77,78,97,102,66,66,66,66,66,66,66,66,97,97,97,97,]),'LPARENTHESIS':([6,7,30,31,32,35,38,39,42,43,58,59,60,61,62,63,64,65,69,75,83,153,154,155,156,157,158,162,178,180,207,],[8,9,48,49,50,53,56,57,71,72,86,-60,-61,-62,-63,-64,-65,-66,93,104,-67,-68,-69,-70,-71,-72,-73,181,188,189,208,]),'New':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[29,29,29,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,29,-5,-35,-36,-41,29,29,-67,29,29,29,29,-49,29,-34,-37,-38,-39,-40,29,-58,-79,-42,-43,-44,-50,29,-24,29,29,29,29,29,-74,-30,-31,-32,-33,-45,29,29,-46,]),'Values':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[30,30,30,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,30,-5,-35,-36,-41,30,30,-67,30,30,30,30,-49,30,-34,-37,-38,-39,-40,30,-58,-79,-42,-43,-44,-50,30,-24,30,30,30,30,30,-74,-30,-31,-32,-33,-45,30,30,-46,]),'Alter':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,40,44,46,51,52,54,56,57,71,83,84,85,86,87,88,89,90,91,92,93,95,105,113,114,122,123,124,132,133,134,135,145,146,147,148,149,160,163,168,169,171,172,173,174,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[31,31,31,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,31,31,-5,-35,-36,-41,31,31,31,-67,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-49,31,31,31,31,31,31,-34,-37,-38,-39,-40,31,-58,-79,31,31,31,31,31,-42,-43,-44,-50,31,-24,31,31,31,31,31,-74,-30,-31,-32,-33,-45,31,31,-46,]),'AlterB':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,95,105,114,122,123,124,145,146,147,148,149,160,163,168,169,171,172,173,174,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[32,32,32,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,32,-5,-35,-36,-41,32,32,-67,32,32,32,32,32,32,-49,32,32,-34,-37,-38,-39,-40,32,-58,-79,32,32,32,32,32,-42,-43,-44,-50,32,-24,32,32,32,32,32,-74,-30,-31,-32,-33,-45,32,32,-46,]),'MoveRight':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[33,33,33,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,33,-5,-35,-36,-41,33,33,-67,33,33,33,33,-49,33,-34,-37,-38,-39,-40,33,-58,-79,-42,-43,-44,-50,33,-24,33,33,33,33,33,-74,-30,-31,-32,-33,-45,33,33,-46,]),'MoveLeft':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[34,34,34,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,34,-5,-35,-36,-41,34,34,-67,34,34,34,34,-49,34,-34,-37,-38,-39,-40,34,-58,-79,-42,-43,-44,-50,34,-24,34,34,34,34,34,-74,-30,-31,-32,-33,-45,34,34,-46,]),'Hammer':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[35,35,35,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,35,-5,-35,-36,-41,35,35,-67,35,35,35,35,-49,35,-34,-37,-38,-39,-40,35,-58,-79,-42,-43,-44,-50,35,-24,35,35,35,35,35,-74,-30,-31,-32,-33,-45,35,35,-46,]),'Stop':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[36,36,36,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,36,-5,-35,-36,-41,36,36,-67,36,36,36,36,-49,36,-34,-37,-38,-39,-40,36,-58,-79,-42,-43,-44,-50,36,-24,36,36,36,36,36,-74,-30,-31,-32,-33,-45,36,36,-46,]),'IsTrue':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,40,44,46,51,52,54,56,57,83,84,85,86,93,113,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[37,37,37,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,37,37,-5,-35,-36,-41,37,37,-67,37,37,37,37,37,37,-49,37,-34,-37,-38,-39,-40,37,-58,-79,-42,-43,-44,-50,37,-24,37,37,37,37,37,-74,-30,-31,-32,-33,-45,37,37,-46,]),'Repeat':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[38,38,38,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,38,-5,-35,-36,-41,38,38,-67,38,38,38,38,-49,38,-34,-37,-38,-39,-40,38,-58,-79,-42,-43,-44,-50,38,-24,38,38,38,38,38,-74,-30,-31,-32,-33,-45,38,38,-46,]),'Until':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[39,39,39,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,39,-5,-35,-36,-41,39,39,-67,39,39,39,39,-49,39,-34,-37,-38,-39,-40,39,-58,-79,-42,-43,-44,-50,39,-24,39,39,39,39,39,-74,-30,-31,-32,-33,-45,39,39,-46,]),'While':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[40,40,40,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,40,-5,-35,-36,-41,40,40,-67,40,40,40,40,-49,40,-34,-37,-38,-39,-40,40,-58,-79,-42,-43,-44,-50,40,-24,40,40,40,40,40,-74,-30,-31,-32,-33,-45,40,40,-46,]),'Case':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[41,41,41,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,41,-5,-35,-36,-41,41,41,-67,41,41,41,41,-49,41,-34,-37,-38,-39,-40,41,-58,-79,-42,-43,-44,-50,41,-24,41,41,41,41,41,-74,-30,-31,-32,-33,-45,41,41,-46,]),'PrintValues':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[42,42,42,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,42,-5,-35,-36,-41,42,42,-67,42,42,42,42,-49,42,-34,-37,-38,-39,-40,42,-58,-79,-42,-43,-44,-50,42,-24,42,42,42,42,42,-74,-30,-31,-32,-33,-45,42,42,-46,]),'CALL':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,56,57,83,84,85,86,114,122,123,145,146,147,148,149,160,163,168,175,176,177,179,181,183,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[43,43,43,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,43,-5,-35,-36,-41,43,43,-67,43,43,43,43,-49,43,-34,-37,-38,-39,-40,43,-58,-79,-42,-43,-44,-50,43,-24,43,43,43,43,43,-74,-30,-31,-32,-33,-45,43,43,-46,]),'RPARENTHESIS':([8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,44,46,51,52,54,57,59,60,61,62,63,64,65,68,71,78,79,80,81,82,83,85,86,96,97,98,99,101,102,112,114,121,122,126,127,128,129,130,132,133,134,135,140,145,146,147,148,149,153,154,155,156,157,158,163,164,165,166,167,168,175,176,177,179,181,182,183,184,185,186,187,188,189,190,196,197,199,200,201,202,203,206,208,209,211,],[-59,-59,45,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,73,-5,-35,-36,-41,-59,-60,-61,-62,-63,-64,-65,-66,-76,-59,107,108,109,110,111,-67,113,-59,131,-75,-53,-55,-57,136,150,152,159,-49,-25,-26,-27,-28,-29,-59,-59,-59,-59,170,-34,-37,-38,-39,-40,-68,-69,-70,-71,-72,-73,-58,-51,-52,-54,-56,-79,-42,-43,-44,-50,-59,191,-24,192,193,194,195,-59,-59,198,204,205,-74,-30,-31,-32,-33,-45,-59,210,-46,]),'Break':([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,46,51,52,54,56,83,84,122,145,146,147,148,149,163,168,175,176,177,179,183,199,200,201,202,203,206,211,],[-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-5,-35,-36,-41,-59,-67,112,-49,-34,-37,-38,-39,-40,-58,-79,-42,-43,-44,-50,-24,-74,-30,-31,-32,-33,-45,-46,]),'SEMMICOLOM':([11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,33,34,36,45,46,51,52,54,55,59,60,61,62,63,64,65,66,68,73,83,94,107,108,109,110,111,115,116,117,118,119,120,122,123,131,136,145,146,147,148,149,150,151,152,153,154,155,156,157,158,160,163,168,170,175,176,177,179,183,191,192,193,194,195,198,199,200,201,202,203,204,205,206,210,211,],[-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,51,52,54,74,-5,-35,-36,-41,83,-60,-61,-62,-63,-64,-65,-66,-75,-76,103,-67,122,145,146,147,148,149,153,154,155,156,157,158,-49,-59,163,168,-34,-37,-38,-39,-40,175,176,177,-68,-69,-70,-71,-72,-73,179,-58,-79,183,-42,-43,-44,-50,-24,199,200,201,202,203,-48,-74,-30,-31,-32,-33,206,-47,-45,211,-46,]),'When':([41,70,94,198,205,],[69,95,124,-48,-47,]),'COMMA':([47,68,76,77,97,98,99,100,137,138,139,141,142,143,144,200,201,202,203,],[75,-76,105,106,132,133,134,135,169,-77,-78,171,172,173,174,-30,-31,-32,-33,]),'Norte':([53,],[79,]),'Sur':([53,],[80,]),'Este':([53,],[81,]),'Oeste':([53,],[82,]),'Greater':([66,67,68,200,201,202,203,],[-75,87,-76,-30,-31,-32,-33,]),'GreaterEqual':([66,67,68,200,201,202,203,],[-75,88,-76,-30,-31,-32,-33,]),'Equals':([66,67,68,200,201,202,203,],[-75,89,-76,-30,-31,-32,-33,]),'Different':([66,67,68,200,201,202,203,],[-75,90,-76,-30,-31,-32,-33,]),'LessEqual':([66,67,68,200,201,202,203,],[-75,91,-76,-30,-31,-32,-33,]),'Less':([66,67,68,200,201,202,203,],[-75,92,-76,-30,-31,-32,-33,]),'Number':([71,95,105,124,132,133,134,135,169,171,172,173,174,],[99,128,128,128,99,99,99,99,128,128,128,128,128,]),'TEXTVALUE':([71,132,133,134,135,],[100,100,100,100,100,]),'Else':([94,198,204,205,],[123,-48,207,-47,]),'True':([95,105,124,169,171,172,173,174,],[126,126,126,126,126,126,126,126,]),'False':([95,105,124,169,171,172,173,174,],[127,127,127,127,127,127,127,127,]),'Bool':([104,],[138,]),'Num':([104,],[139,]),'ADD':([106,],[141,]),'SUB':([106,],[142,]),'MUL':([106,],[143,]),'DIV':([106,],[144,]),'Then':([125,126,127,128,129,130,145,159,161,200,201,202,203,],[162,-25,-26,-27,-28,-29,-34,178,180,-30,-31,-32,-33,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'main':([0,],[2,]),'Proced':([2,],[4,]),'recursivo':([8,9,56,57,86,123,181,188,189,208,],[10,44,84,85,114,160,190,196,197,209,]),'instruccion':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[11,11,46,46,11,11,46,46,11,46,11,46,11,11,11,46,46,46,11,46,]),'varDeclaration':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'Values_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'Alter_f':([8,9,10,40,44,56,57,71,84,85,86,87,88,89,90,91,92,93,95,105,113,114,123,124,132,133,134,135,160,169,171,172,173,174,181,188,189,190,196,197,208,209,],[14,14,14,68,14,14,14,68,14,14,14,68,68,68,68,68,68,68,129,129,68,14,14,129,68,68,68,68,14,129,129,129,129,129,14,14,14,14,14,14,14,14,]),'AlterB_f':([8,9,10,44,56,57,84,85,86,95,105,114,123,124,160,169,171,172,173,174,181,188,189,190,196,197,208,209,],[15,15,15,15,15,15,15,15,15,130,130,15,15,130,15,130,130,130,130,130,15,15,15,15,15,15,15,15,]),'MoveRight_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'MoveLeft_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'Hammer_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'Stop_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'IsTrue_f':([8,9,10,40,44,56,57,84,85,86,93,113,114,123,160,181,188,189,190,196,197,208,209,],[20,20,20,59,20,20,20,20,20,20,59,59,20,20,20,20,20,20,20,20,20,20,20,]),'Repeat_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'Until_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'While_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'Case_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'Case2_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,25,]),'PrintValues_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,]),'call_f':([8,9,10,44,56,57,84,85,86,114,123,160,181,188,189,190,196,197,208,209,],[27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,27,]),'empty':([8,9,10,44,56,57,71,84,85,86,114,123,132,133,134,135,160,181,188,189,190,196,197,208,209,],[28,28,28,28,28,28,101,28,28,28,28,28,101,101,101,101,28,28,28,28,28,28,28,28,28,]),'condicional':([40,93,113,],[58,121,151,]),'Greater_f':([40,93,113,],[60,60,60,]),'GreaterEqual_f':([40,93,113,],[61,61,61,]),'Equals_f':([40,93,113,],[62,62,62,]),'Different_f':([40,93,113,],[63,63,63,]),'LessEqual_f':([40,93,113,],[64,64,64,]),'Less_f':([40,93,113,],[65,65,65,]),'expresionNum':([40,71,87,88,89,90,91,92,93,113,132,133,134,135,],[67,98,115,116,117,118,119,120,67,67,98,98,98,98,]),'opciones':([70,],[94,]),'something':([71,132,133,134,135,],[96,164,165,166,167,]),'valorDato':([95,105,124,169,171,172,173,174,],[125,140,161,182,184,185,186,187,]),'tipoDatos':([104,],[137,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> main','start',1,'p_start','SintacticAnalyzer.py',29),
  ('start -> main Proced','start',2,'p_start','SintacticAnalyzer.py',30),
  ('main -> Proc PRINCIPAL LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM','main',6,'p_main','SintacticAnalyzer.py',35),
  ('Proced -> Proc ID LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM','Proced',6,'p_Proced','SintacticAnalyzer.py',40),
  ('recursivo -> recursivo instruccion','recursivo',2,'p_recursivo','SintacticAnalyzer.py',48),
  ('recursivo -> instruccion','recursivo',1,'p_recursivo2','SintacticAnalyzer.py',52),
  ('instruccion -> varDeclaration','instruccion',1,'p_instruccion','SintacticAnalyzer.py',57),
  ('instruccion -> Values_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',58),
  ('instruccion -> Alter_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',59),
  ('instruccion -> AlterB_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',60),
  ('instruccion -> MoveRight_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',61),
  ('instruccion -> MoveLeft_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',62),
  ('instruccion -> Hammer_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',63),
  ('instruccion -> Stop_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',64),
  ('instruccion -> IsTrue_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',65),
  ('instruccion -> Repeat_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',66),
  ('instruccion -> Until_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',67),
  ('instruccion -> While_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',68),
  ('instruccion -> Case_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',69),
  ('instruccion -> Case2_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',70),
  ('instruccion -> PrintValues_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',71),
  ('instruccion -> call_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',72),
  ('instruccion -> empty','instruccion',1,'p_instruccion','SintacticAnalyzer.py',73),
  ('Values_f -> Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOM','Values_f',7,'p_Values_f','SintacticAnalyzer.py',79),
  ('valorDato -> True','valorDato',1,'p_valorDato','SintacticAnalyzer.py',83),
  ('valorDato -> False','valorDato',1,'p_valorDato','SintacticAnalyzer.py',84),
  ('valorDato -> Number','valorDato',1,'p_valorDato','SintacticAnalyzer.py',85),
  ('valorDato -> Alter_f','valorDato',1,'p_valorDato','SintacticAnalyzer.py',86),
  ('valorDato -> AlterB_f','valorDato',1,'p_valorDato','SintacticAnalyzer.py',87),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',93),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',94),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',95),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',96),
  ('AlterB_f -> AlterB LPARENTHESIS ID RPARENTHESIS SEMMICOLOM','AlterB_f',5,'p_AlterB_f','SintacticAnalyzer.py',102),
  ('MoveRight_f -> MoveRight SEMMICOLOM','MoveRight_f',2,'p_MoveRight_f','SintacticAnalyzer.py',107),
  ('MoveLeft_f -> MoveLeft SEMMICOLOM','MoveLeft_f',2,'p_MoveLeft_f','SintacticAnalyzer.py',112),
  ('Hammer_f -> Hammer LPARENTHESIS Norte RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',117),
  ('Hammer_f -> Hammer LPARENTHESIS Sur RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',118),
  ('Hammer_f -> Hammer LPARENTHESIS Este RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',119),
  ('Hammer_f -> Hammer LPARENTHESIS Oeste RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',120),
  ('Stop_f -> Stop SEMMICOLOM','Stop_f',2,'p_Stop_f','SintacticAnalyzer.py',125),
  ('Repeat_f -> Repeat LPARENTHESIS recursivo Break RPARENTHESIS SEMMICOLOM','Repeat_f',6,'p_Repeat_f','SintacticAnalyzer.py',130),
  ('Until_f -> Until LPARENTHESIS recursivo RPARENTHESIS condicional SEMMICOLOM','Until_f',6,'p_Until_f','SintacticAnalyzer.py',135),
  ('While_f -> While condicional LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM','While_f',6,'p_While_f','SintacticAnalyzer.py',140),
  ('Case_f -> Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM','Case_f',10,'p_Case_f','SintacticAnalyzer.py',145),
  ('Case_f -> Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS recursivo RPARENTHESIS Else LPARENTHESIS recursivo RPARENTHESIS SEMMICOLOM','Case_f',14,'p_Case_f','SintacticAnalyzer.py',146),
  ('opciones -> opciones When valorDato Then LPARENTHESIS recursivo RPARENTHESIS','opciones',7,'p_opciones','SintacticAnalyzer.py',150),
  ('opciones -> When valorDato Then LPARENTHESIS recursivo RPARENTHESIS','opciones',6,'p_opciones','SintacticAnalyzer.py',151),
  ('Case2_f -> Case ID opciones SEMMICOLOM','Case2_f',4,'p_Case2_f','SintacticAnalyzer.py',154),
  ('Case2_f -> Case ID opciones Else recursivo SEMMICOLOM','Case2_f',6,'p_Case2_f','SintacticAnalyzer.py',155),
  ('something -> ID COMMA something','something',3,'p_something','SintacticAnalyzer.py',164),
  ('something -> expresionNum COMMA something','something',3,'p_something','SintacticAnalyzer.py',165),
  ('something -> expresionNum','something',1,'p_something','SintacticAnalyzer.py',166),
  ('something -> Number COMMA something','something',3,'p_something','SintacticAnalyzer.py',167),
  ('something -> Number','something',1,'p_something','SintacticAnalyzer.py',168),
  ('something -> TEXTVALUE COMMA something','something',3,'p_something','SintacticAnalyzer.py',169),
  ('something -> empty','something',1,'p_something','SintacticAnalyzer.py',170),
  ('PrintValues_f -> PrintValues LPARENTHESIS something RPARENTHESIS SEMMICOLOM','PrintValues_f',5,'p_PrintValues_f','SintacticAnalyzer.py',174),
  ('empty -> <empty>','empty',0,'p_empty','SintacticAnalyzer.py',180),
  ('condicional -> IsTrue_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',188),
  ('condicional -> Greater_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',189),
  ('condicional -> GreaterEqual_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',190),
  ('condicional -> Equals_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',191),
  ('condicional -> Different_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',192),
  ('condicional -> LessEqual_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',193),
  ('condicional -> Less_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',194),
  ('IsTrue_f -> IsTrue ID SEMMICOLOM','IsTrue_f',3,'p_IsTrue_f','SintacticAnalyzer.py',198),
  ('Greater_f -> expresionNum Greater expresionNum SEMMICOLOM','Greater_f',4,'p_Greater_f','SintacticAnalyzer.py',203),
  ('GreaterEqual_f -> expresionNum GreaterEqual expresionNum SEMMICOLOM','GreaterEqual_f',4,'p_GreaterEqual_f','SintacticAnalyzer.py',209),
  ('Equals_f -> expresionNum Equals expresionNum SEMMICOLOM','Equals_f',4,'p_Equals_f','SintacticAnalyzer.py',214),
  ('Different_f -> expresionNum Different expresionNum SEMMICOLOM','Different_f',4,'p_Different_f','SintacticAnalyzer.py',219),
  ('LessEqual_f -> expresionNum LessEqual expresionNum SEMMICOLOM','LessEqual_f',4,'p_LessEqual_f','SintacticAnalyzer.py',224),
  ('Less_f -> expresionNum Less expresionNum SEMMICOLOM','Less_f',4,'p_Less_f','SintacticAnalyzer.py',229),
  ('varDeclaration -> New ID COMMA LPARENTHESIS tipoDatos COMMA valorDato RPARENTHESIS SEMMICOLOM','varDeclaration',9,'p_varDeclaration','SintacticAnalyzer.py',237),
  ('expresionNum -> ID','expresionNum',1,'p_expresionNum','SintacticAnalyzer.py',243),
  ('expresionNum -> Alter_f','expresionNum',1,'p_expresionNum','SintacticAnalyzer.py',244),
  ('tipoDatos -> Bool','tipoDatos',1,'p_tipoDatos','SintacticAnalyzer.py',248),
  ('tipoDatos -> Num','tipoDatos',1,'p_tipoDatos','SintacticAnalyzer.py',249),
  ('call_f -> CALL LPARENTHESIS ID RPARENTHESIS SEMMICOLOM','call_f',5,'p_call_f','SintacticAnalyzer.py',271),
]
