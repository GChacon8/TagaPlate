
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightNewleftLessLessEqualGreaterGreaterEqualEqualsDifferentrightLPARENTHESISRPARENTHESISADD Alter AlterB Bool Break CALL COMMA Case DIV Different Else Equals Este False Greater GreaterEqual Hammer ID IsTrue LPARENTHESIS Less LessEqual MUL MoveLeft MoveRight New Norte Num Number Oeste PRINCIPAL PrintValues Proc RPARENTHESIS Repeat SEMMICOLOM SUB Stop Sur TEXTVALUE Then True Until Values When Whilestart : instrucciones\n            main :  Proc PRINCIPAL LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOMProced : Proc ID LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOMinstrucciones : instrucciones instruccion\n                instrucciones : instruccioninstruccion : varDeclaration\n                     | Values_f\n                     | Alter_f\n                     | AlterB_f\n                     | MoveRight_f\n                     | MoveLeft_f\n                     | Hammer_f\n                     | Stop_f\n                     | IsTrue_f\n                     | Repeat_f\n                     | Until_f\n                     | While_f\n                     | Case_f\n                     | Case2_f\n                     | CaseElse\n                     | PrintValues_f\n                     | call_f\n                     | main\n                     | Proced\n                     | emptyValues_f : Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOMvalorDato : True\n                | False\n                | Number\n                | Alter_f\n                | AlterB_fAlter_f : Alter LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM\n               | Alter LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM\n               | Alter LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM\n               | Alter LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOMAlterB_f : AlterB LPARENTHESIS ID RPARENTHESIS SEMMICOLOMMoveRight_f : MoveRight SEMMICOLOMMoveLeft_f : MoveLeft SEMMICOLOMHammer_f : Hammer LPARENTHESIS Norte RPARENTHESIS SEMMICOLOM\n                 | Hammer LPARENTHESIS Sur RPARENTHESIS SEMMICOLOM\n                 | Hammer LPARENTHESIS Este RPARENTHESIS SEMMICOLOM\n                 | Hammer LPARENTHESIS Oeste RPARENTHESIS SEMMICOLOMStop_f : Stop SEMMICOLOMRepeat_f : Repeat LPARENTHESIS instrucciones Break RPARENTHESIS SEMMICOLOMUntil_f : Until LPARENTHESIS instrucciones RPARENTHESIS condicionalWhile_f : While condicional LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOMCase_f : Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOMCase_f : Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS Else LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOMopciones : When valorDato Then LPARENTHESIS instrucciones RPARENTHESISCase2_f : Case ID opciones SEMMICOLOMCaseElse : Case ID opciones Else instrucciones SEMMICOLOMCadena : ID COMMA Cadena\n                 | Number COMMA Cadena\n                 | TEXTVALUE COMMA Cadena\n                 \n                 Cadena : Number\n                | TEXTVALUE\n                | ID\n                | empty\n                 PrintValues_f : PrintValues LPARENTHESIS Cadena RPARENTHESIS SEMMICOLOM empty : condicional : IsTrue_f\n                   | Greater_f\n                   | GreaterEqual_f\n                   | Equals_f\n                   | Different_f\n                   | LessEqual_f\n                   | Less_fIsTrue_f : IsTrue LPARENTHESIS ID RPARENTHESIS SEMMICOLOM\n                | IsTrue LPARENTHESIS ID RPARENTHESISGreater_f : expresionNum Greater expresionNum SEMMICOLOM\n                 | expresionNum Greater expresionNum GreaterEqual_f : expresionNum GreaterEqual expresionNum SEMMICOLOM\n                        |  expresionNum GreaterEqual expresionNumEquals_f : expresionNum Equals expresionNum SEMMICOLOM\n                | expresionNum Equals expresionNum Different_f : expresionNum Different expresionNum SEMMICOLOM\n                    | expresionNum Different expresionNum LessEqual_f : expresionNum LessEqual expresionNum SEMMICOLOM\n                    | expresionNum LessEqual expresionNumLess_f : expresionNum Less expresionNum SEMMICOLOM\n              | expresionNum Less expresionNumvarDeclaration : New ID COMMA LPARENTHESIS tipoDatos COMMA valorDato RPARENTHESIS SEMMICOLOM expresionNum : ID\n                    | Alter_f \n                    | NumbertipoDatos : Bool\n                 | Numcall_f : CALL LPARENTHESIS ID RPARENTHESIS SEMMICOLOM'
    
_lr_action_items = {'New':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[24,24,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,24,24,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,24,24,24,24,24,-69,24,-71,-73,-75,-77,-79,-81,-50,24,24,24,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,24,-59,-88,-44,-46,-51,24,-2,-3,-26,24,24,24,-82,-32,-33,-34,-35,-47,24,24,-48,]),'Values':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[25,25,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,25,25,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,25,25,25,25,25,-69,25,-71,-73,-75,-77,-79,-81,-50,25,25,25,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,25,-59,-88,-44,-46,-51,25,-2,-3,-26,25,25,25,-82,-32,-33,-34,-35,-47,25,25,-48,]),'Alter':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,35,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,82,83,84,85,86,87,88,90,97,98,100,107,109,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,166,168,169,170,171,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[26,26,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,26,-4,-37,-38,-43,26,26,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,26,26,26,26,26,26,26,26,26,26,26,26,26,26,-69,26,26,-71,-73,-75,-77,-79,-81,-50,26,26,26,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,26,-59,-88,26,26,26,26,26,-44,-46,-51,26,-2,-3,-26,26,26,26,-82,-32,-33,-34,-35,-47,26,26,-48,]),'AlterB':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,90,97,98,100,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,166,168,169,170,171,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[27,27,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,27,27,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,27,27,27,27,27,27,27,-69,27,-71,-73,-75,-77,-79,-81,-50,27,27,27,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,27,-59,-88,27,27,27,27,27,-44,-46,-51,27,-2,-3,-26,27,27,27,-82,-32,-33,-34,-35,-47,27,27,-48,]),'MoveRight':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[28,28,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,28,28,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,28,28,28,28,28,-69,28,-71,-73,-75,-77,-79,-81,-50,28,28,28,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,28,-59,-88,-44,-46,-51,28,-2,-3,-26,28,28,28,-82,-32,-33,-34,-35,-47,28,28,-48,]),'MoveLeft':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[29,29,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,29,29,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,29,29,29,29,29,-69,29,-71,-73,-75,-77,-79,-81,-50,29,29,29,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,29,-59,-88,-44,-46,-51,29,-2,-3,-26,29,29,29,-82,-32,-33,-34,-35,-47,29,29,-48,]),'Hammer':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[30,30,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,30,30,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,30,30,30,30,30,-69,30,-71,-73,-75,-77,-79,-81,-50,30,30,30,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,30,-59,-88,-44,-46,-51,30,-2,-3,-26,30,30,30,-82,-32,-33,-34,-35,-47,30,30,-48,]),'Stop':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[31,31,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,31,31,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,31,31,31,31,31,-69,31,-71,-73,-75,-77,-79,-81,-50,31,31,31,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,31,-59,-88,-44,-46,-51,31,-2,-3,-26,31,31,31,-82,-32,-33,-34,-35,-47,31,31,-48,]),'IsTrue':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,35,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,88,97,98,107,109,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[32,32,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,32,-4,-37,-38,-43,32,32,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,32,32,32,32,32,32,-69,32,32,-71,-73,-75,-77,-79,-81,-50,32,32,32,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,32,-59,-88,-44,-46,-51,32,-2,-3,-26,32,32,32,-82,-32,-33,-34,-35,-47,32,32,-48,]),'Repeat':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[33,33,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,33,33,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,33,33,33,33,33,-69,33,-71,-73,-75,-77,-79,-81,-50,33,33,33,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,33,-59,-88,-44,-46,-51,33,-2,-3,-26,33,33,33,-82,-32,-33,-34,-35,-47,33,33,-48,]),'Until':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[34,34,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,34,34,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,34,34,34,34,34,-69,34,-71,-73,-75,-77,-79,-81,-50,34,34,34,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,34,-59,-88,-44,-46,-51,34,-2,-3,-26,34,34,34,-82,-32,-33,-34,-35,-47,34,34,-48,]),'While':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[35,35,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,35,35,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,35,35,35,35,35,-69,35,-71,-73,-75,-77,-79,-81,-50,35,35,35,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,35,-59,-88,-44,-46,-51,35,-2,-3,-26,35,35,35,-82,-32,-33,-34,-35,-47,35,35,-48,]),'Case':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[36,36,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,36,36,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,36,36,36,36,36,-69,36,-71,-73,-75,-77,-79,-81,-50,36,36,36,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,36,-59,-88,-44,-46,-51,36,-2,-3,-26,36,36,36,-82,-32,-33,-34,-35,-47,36,36,-48,]),'PrintValues':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[37,37,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,37,37,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,37,37,37,37,37,-69,37,-71,-73,-75,-77,-79,-81,-50,37,37,37,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,37,-59,-88,-44,-46,-51,37,-2,-3,-26,37,37,37,-82,-32,-33,-34,-35,-47,37,37,-48,]),'CALL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[38,38,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,38,38,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,38,38,38,38,38,-69,38,-71,-73,-75,-77,-79,-81,-50,38,38,38,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,38,-59,-88,-44,-46,-51,38,-2,-3,-26,38,38,38,-82,-32,-33,-34,-35,-47,38,38,-48,]),'Proc':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,51,53,54,55,56,57,58,59,60,62,63,79,80,81,97,98,107,110,111,112,113,114,115,116,118,119,131,132,141,142,143,144,145,146,148,150,151,152,153,154,155,157,159,163,172,173,175,176,177,178,180,185,186,192,194,195,196,197,198,200,202,203,205,],[39,39,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,39,39,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,39,39,39,39,39,-69,39,-71,-73,-75,-77,-79,-81,-50,39,39,39,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,39,-59,-88,-44,-46,-51,39,-2,-3,-26,39,39,39,-82,-32,-33,-34,-35,-47,39,39,-48,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,53,54,55,56,57,58,59,60,62,63,107,111,112,113,114,115,116,118,141,142,143,144,145,146,148,150,151,152,153,154,155,159,163,172,173,175,177,178,180,194,195,196,197,198,200,205,],[-60,0,-1,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,-69,-71,-73,-75,-77,-79,-81,-50,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,-59,-88,-44,-46,-51,-2,-3,-26,-82,-32,-33,-34,-35,-47,-48,]),'Break':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,50,53,54,55,56,57,58,59,60,62,63,79,107,111,112,113,114,115,116,118,141,142,143,144,145,146,148,150,151,152,153,154,155,159,163,172,173,175,177,178,180,194,195,196,197,198,200,205,],[-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,-60,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,108,-69,-71,-73,-75,-77,-79,-81,-50,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,-59,-88,-44,-46,-51,-2,-3,-26,-82,-32,-33,-34,-35,-47,-48,]),'RPARENTHESIS':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,40,45,46,48,51,53,54,55,56,57,58,59,60,62,63,66,73,74,75,76,77,78,80,81,91,92,93,94,95,96,97,98,107,108,110,111,112,113,114,115,116,117,118,121,122,123,124,125,127,128,129,131,132,136,141,142,143,144,145,146,148,150,151,152,153,154,155,159,160,161,162,163,172,173,175,176,177,178,179,180,181,182,183,184,185,186,192,194,195,196,197,198,200,202,203,205,],[-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,-4,-37,-38,-43,-60,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,-60,102,103,104,105,106,107,109,-60,126,-57,-55,-56,-58,130,-60,-60,-69,147,149,-71,-73,-75,-77,-79,-81,156,-50,-27,-28,-29,-30,-31,-60,-60,-60,164,165,167,-36,-39,-40,-41,-42,-68,-45,-70,-72,-74,-76,-78,-80,-59,-52,-53,-54,-88,-44,-46,-51,-60,-2,-3,187,-26,188,189,190,191,-60,193,199,-82,-32,-33,-34,-35,-47,-60,204,-48,]),'SEMMICOLOM':([3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,28,29,31,40,45,46,48,53,54,55,56,57,58,59,60,62,63,89,102,103,104,105,106,107,111,112,113,114,115,116,118,119,126,130,141,142,143,144,145,146,147,148,149,150,151,152,153,154,155,157,159,163,164,165,167,172,173,175,177,178,180,187,188,189,190,191,193,194,195,196,197,198,199,200,204,205,],[-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-17,-18,-19,-20,-21,-22,-23,-24,-25,45,46,48,-4,-37,-38,-43,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,118,141,142,143,144,145,-69,-71,-73,-75,-77,-79,-81,-50,-60,159,163,-36,-39,-40,-41,-42,-68,172,-45,173,-70,-72,-74,-76,-78,-80,175,-59,-88,177,178,180,-44,-46,-51,-2,-3,-26,194,195,196,197,198,-49,-82,-32,-33,-34,-35,200,-47,205,-48,]),'ID':([24,35,36,39,42,43,44,49,66,67,82,83,84,85,86,87,88,109,127,128,129,],[41,60,65,69,71,72,73,78,92,96,60,60,60,60,60,60,60,60,92,92,92,]),'LPARENTHESIS':([25,26,27,30,32,33,34,37,38,52,53,54,55,56,57,58,59,60,62,63,64,68,69,70,107,111,112,113,114,115,116,146,150,151,152,153,154,155,158,174,195,196,197,198,201,],[42,43,44,47,49,50,51,66,67,81,-61,-62,-63,-64,-65,-66,-67,-83,-84,-85,88,97,98,99,-69,-71,-73,-75,-77,-79,-81,-68,-70,-72,-74,-76,-78,-80,176,185,-32,-33,-34,-35,202,]),'Number':([35,66,82,83,84,85,86,87,88,90,100,109,127,128,129,166,168,169,170,171,],[63,93,63,63,63,63,63,63,63,123,123,63,93,93,93,123,123,123,123,123,]),'When':([36,65,],[64,90,]),'PRINCIPAL':([39,],[68,]),'COMMA':([41,71,72,92,93,94,133,134,135,137,138,139,140,],[70,100,101,127,128,129,166,-86,-87,168,169,170,171,]),'Norte':([47,],[74,]),'Sur':([47,],[75,]),'Este':([47,],[76,]),'Oeste':([47,],[77,]),'Greater':([60,61,62,63,195,196,197,198,],[-83,82,-84,-85,-32,-33,-34,-35,]),'GreaterEqual':([60,61,62,63,195,196,197,198,],[-83,83,-84,-85,-32,-33,-34,-35,]),'Equals':([60,61,62,63,195,196,197,198,],[-83,84,-84,-85,-32,-33,-34,-35,]),'Different':([60,61,62,63,195,196,197,198,],[-83,85,-84,-85,-32,-33,-34,-35,]),'LessEqual':([60,61,62,63,195,196,197,198,],[-83,86,-84,-85,-32,-33,-34,-35,]),'Less':([60,61,62,63,195,196,197,198,],[-83,87,-84,-85,-32,-33,-34,-35,]),'TEXTVALUE':([66,127,128,129,],[94,94,94,94,]),'Else':([89,193,199,],[119,-49,201,]),'True':([90,100,166,168,169,170,171,],[121,121,121,121,121,121,121,]),'False':([90,100,166,168,169,170,171,],[122,122,122,122,122,122,122,]),'Bool':([99,],[134,]),'Num':([99,],[135,]),'ADD':([101,],[137,]),'SUB':([101,],[138,]),'MUL':([101,],[139,]),'DIV':([101,],[140,]),'Then':([120,121,122,123,124,125,141,156,195,196,197,198,],[158,-27,-28,-29,-30,-31,-36,174,-32,-33,-34,-35,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'start':([0,],[1,]),'instrucciones':([0,50,51,81,97,98,119,176,185,202,],[2,79,80,110,131,132,157,186,192,203,]),'instruccion':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[3,40,3,3,40,40,3,3,3,40,3,40,40,40,3,3,40,40,3,40,]),'varDeclaration':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'Values_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'Alter_f':([0,2,35,50,51,79,80,81,82,83,84,85,86,87,88,90,97,98,100,109,110,119,131,132,157,166,168,169,170,171,176,185,186,192,202,203,],[6,6,62,6,6,6,6,6,62,62,62,62,62,62,62,124,6,6,124,62,6,6,6,6,6,124,124,124,124,124,6,6,6,6,6,6,]),'AlterB_f':([0,2,50,51,79,80,81,90,97,98,100,110,119,131,132,157,166,168,169,170,171,176,185,186,192,202,203,],[7,7,7,7,7,7,7,125,7,7,125,7,7,7,7,7,125,125,125,125,125,7,7,7,7,7,7,]),'MoveRight_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'MoveLeft_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'Hammer_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'Stop_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'IsTrue_f':([0,2,35,50,51,79,80,81,88,97,98,109,110,119,131,132,157,176,185,186,192,202,203,],[12,12,53,12,12,12,12,12,53,12,12,53,12,12,12,12,12,12,12,12,12,12,12,]),'Repeat_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'Until_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'While_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'Case_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'Case2_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'CaseElse':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'PrintValues_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'call_f':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'main':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'Proced':([0,2,50,51,79,80,81,97,98,110,119,131,132,157,176,185,186,192,202,203,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'empty':([0,2,50,51,66,79,80,81,97,98,110,119,127,128,129,131,132,157,176,185,186,192,202,203,],[23,23,23,23,95,23,23,23,23,23,23,23,95,95,95,23,23,23,23,23,23,23,23,23,]),'condicional':([35,88,109,],[52,117,148,]),'Greater_f':([35,88,109,],[54,54,54,]),'GreaterEqual_f':([35,88,109,],[55,55,55,]),'Equals_f':([35,88,109,],[56,56,56,]),'Different_f':([35,88,109,],[57,57,57,]),'LessEqual_f':([35,88,109,],[58,58,58,]),'Less_f':([35,88,109,],[59,59,59,]),'expresionNum':([35,82,83,84,85,86,87,88,109,],[61,111,112,113,114,115,116,61,61,]),'opciones':([65,],[89,]),'Cadena':([66,127,128,129,],[91,160,161,162,]),'valorDato':([90,100,166,168,169,170,171,],[120,136,179,181,182,183,184,]),'tipoDatos':([99,],[133,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> start","S'",1,None,None,None),
  ('start -> instrucciones','start',1,'p_start','SintacticAnalyzer.py',33),
  ('main -> Proc PRINCIPAL LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM','main',6,'p_main','SintacticAnalyzer.py',39),
  ('Proced -> Proc ID LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM','Proced',6,'p_Proced','SintacticAnalyzer.py',47),
  ('instrucciones -> instrucciones instruccion','instrucciones',2,'p_list_instrucciones','SintacticAnalyzer.py',55),
  ('instrucciones -> instruccion','instrucciones',1,'p_one_instruccion','SintacticAnalyzer.py',60),
  ('instruccion -> varDeclaration','instruccion',1,'p_instruccion','SintacticAnalyzer.py',65),
  ('instruccion -> Values_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',66),
  ('instruccion -> Alter_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',67),
  ('instruccion -> AlterB_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',68),
  ('instruccion -> MoveRight_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',69),
  ('instruccion -> MoveLeft_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',70),
  ('instruccion -> Hammer_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',71),
  ('instruccion -> Stop_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',72),
  ('instruccion -> IsTrue_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',73),
  ('instruccion -> Repeat_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',74),
  ('instruccion -> Until_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',75),
  ('instruccion -> While_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',76),
  ('instruccion -> Case_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',77),
  ('instruccion -> Case2_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',78),
  ('instruccion -> CaseElse','instruccion',1,'p_instruccion','SintacticAnalyzer.py',79),
  ('instruccion -> PrintValues_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',80),
  ('instruccion -> call_f','instruccion',1,'p_instruccion','SintacticAnalyzer.py',81),
  ('instruccion -> main','instruccion',1,'p_instruccion','SintacticAnalyzer.py',82),
  ('instruccion -> Proced','instruccion',1,'p_instruccion','SintacticAnalyzer.py',83),
  ('instruccion -> empty','instruccion',1,'p_instruccion','SintacticAnalyzer.py',84),
  ('Values_f -> Values LPARENTHESIS ID COMMA valorDato RPARENTHESIS SEMMICOLOM','Values_f',7,'p_Values_f','SintacticAnalyzer.py',90),
  ('valorDato -> True','valorDato',1,'p_valorDato','SintacticAnalyzer.py',94),
  ('valorDato -> False','valorDato',1,'p_valorDato','SintacticAnalyzer.py',95),
  ('valorDato -> Number','valorDato',1,'p_valorDato','SintacticAnalyzer.py',96),
  ('valorDato -> Alter_f','valorDato',1,'p_valorDato','SintacticAnalyzer.py',97),
  ('valorDato -> AlterB_f','valorDato',1,'p_valorDato','SintacticAnalyzer.py',98),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA ADD COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',104),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA SUB COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',105),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA MUL COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',106),
  ('Alter_f -> Alter LPARENTHESIS ID COMMA DIV COMMA valorDato RPARENTHESIS SEMMICOLOM','Alter_f',9,'p_Alter_f','SintacticAnalyzer.py',107),
  ('AlterB_f -> AlterB LPARENTHESIS ID RPARENTHESIS SEMMICOLOM','AlterB_f',5,'p_AlterB_f','SintacticAnalyzer.py',113),
  ('MoveRight_f -> MoveRight SEMMICOLOM','MoveRight_f',2,'p_MoveRight_f','SintacticAnalyzer.py',118),
  ('MoveLeft_f -> MoveLeft SEMMICOLOM','MoveLeft_f',2,'p_MoveLeft_f','SintacticAnalyzer.py',123),
  ('Hammer_f -> Hammer LPARENTHESIS Norte RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',128),
  ('Hammer_f -> Hammer LPARENTHESIS Sur RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',129),
  ('Hammer_f -> Hammer LPARENTHESIS Este RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',130),
  ('Hammer_f -> Hammer LPARENTHESIS Oeste RPARENTHESIS SEMMICOLOM','Hammer_f',5,'p_Hammer_f','SintacticAnalyzer.py',131),
  ('Stop_f -> Stop SEMMICOLOM','Stop_f',2,'p_Stop_f','SintacticAnalyzer.py',136),
  ('Repeat_f -> Repeat LPARENTHESIS instrucciones Break RPARENTHESIS SEMMICOLOM','Repeat_f',6,'p_Repeat_f','SintacticAnalyzer.py',141),
  ('Until_f -> Until LPARENTHESIS instrucciones RPARENTHESIS condicional','Until_f',5,'p_Until_f','SintacticAnalyzer.py',146),
  ('While_f -> While condicional LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM','While_f',6,'p_While_f','SintacticAnalyzer.py',151),
  ('Case_f -> Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM','Case_f',10,'p_Case0_f','SintacticAnalyzer.py',156),
  ('Case_f -> Case When LPARENTHESIS condicional RPARENTHESIS Then LPARENTHESIS instrucciones RPARENTHESIS Else LPARENTHESIS instrucciones RPARENTHESIS SEMMICOLOM','Case_f',14,'p_Case1_f','SintacticAnalyzer.py',161),
  ('opciones -> When valorDato Then LPARENTHESIS instrucciones RPARENTHESIS','opciones',6,'p_opciones','SintacticAnalyzer.py',167),
  ('Case2_f -> Case ID opciones SEMMICOLOM','Case2_f',4,'p_Case2_f','SintacticAnalyzer.py',171),
  ('CaseElse -> Case ID opciones Else instrucciones SEMMICOLOM','CaseElse',6,'p_CaseElse','SintacticAnalyzer.py',175),
  ('Cadena -> ID COMMA Cadena','Cadena',3,'p_Cadena1','SintacticAnalyzer.py',185),
  ('Cadena -> Number COMMA Cadena','Cadena',3,'p_Cadena1','SintacticAnalyzer.py',186),
  ('Cadena -> TEXTVALUE COMMA Cadena','Cadena',3,'p_Cadena1','SintacticAnalyzer.py',187),
  ('Cadena -> Number','Cadena',1,'p_Cadena2','SintacticAnalyzer.py',195),
  ('Cadena -> TEXTVALUE','Cadena',1,'p_Cadena2','SintacticAnalyzer.py',196),
  ('Cadena -> ID','Cadena',1,'p_Cadena2','SintacticAnalyzer.py',197),
  ('Cadena -> empty','Cadena',1,'p_Cadena2','SintacticAnalyzer.py',198),
  ('PrintValues_f -> PrintValues LPARENTHESIS Cadena RPARENTHESIS SEMMICOLOM','PrintValues_f',5,'p_PrintValues_f','SintacticAnalyzer.py',209),
  ('empty -> <empty>','empty',0,'p_empty','SintacticAnalyzer.py',215),
  ('condicional -> IsTrue_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',223),
  ('condicional -> Greater_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',224),
  ('condicional -> GreaterEqual_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',225),
  ('condicional -> Equals_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',226),
  ('condicional -> Different_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',227),
  ('condicional -> LessEqual_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',228),
  ('condicional -> Less_f','condicional',1,'p_condicional_f','SintacticAnalyzer.py',229),
  ('IsTrue_f -> IsTrue LPARENTHESIS ID RPARENTHESIS SEMMICOLOM','IsTrue_f',5,'p_IsTrue_f','SintacticAnalyzer.py',234),
  ('IsTrue_f -> IsTrue LPARENTHESIS ID RPARENTHESIS','IsTrue_f',4,'p_IsTrue_f','SintacticAnalyzer.py',235),
  ('Greater_f -> expresionNum Greater expresionNum SEMMICOLOM','Greater_f',4,'p_Greater_f','SintacticAnalyzer.py',240),
  ('Greater_f -> expresionNum Greater expresionNum','Greater_f',3,'p_Greater_f','SintacticAnalyzer.py',241),
  ('GreaterEqual_f -> expresionNum GreaterEqual expresionNum SEMMICOLOM','GreaterEqual_f',4,'p_GreaterEqual_f','SintacticAnalyzer.py',247),
  ('GreaterEqual_f -> expresionNum GreaterEqual expresionNum','GreaterEqual_f',3,'p_GreaterEqual_f','SintacticAnalyzer.py',248),
  ('Equals_f -> expresionNum Equals expresionNum SEMMICOLOM','Equals_f',4,'p_Equals_f','SintacticAnalyzer.py',253),
  ('Equals_f -> expresionNum Equals expresionNum','Equals_f',3,'p_Equals_f','SintacticAnalyzer.py',254),
  ('Different_f -> expresionNum Different expresionNum SEMMICOLOM','Different_f',4,'p_Different_f','SintacticAnalyzer.py',259),
  ('Different_f -> expresionNum Different expresionNum','Different_f',3,'p_Different_f','SintacticAnalyzer.py',260),
  ('LessEqual_f -> expresionNum LessEqual expresionNum SEMMICOLOM','LessEqual_f',4,'p_LessEqual_f','SintacticAnalyzer.py',265),
  ('LessEqual_f -> expresionNum LessEqual expresionNum','LessEqual_f',3,'p_LessEqual_f','SintacticAnalyzer.py',266),
  ('Less_f -> expresionNum Less expresionNum SEMMICOLOM','Less_f',4,'p_Less_f','SintacticAnalyzer.py',271),
  ('Less_f -> expresionNum Less expresionNum','Less_f',3,'p_Less_f','SintacticAnalyzer.py',272),
  ('varDeclaration -> New ID COMMA LPARENTHESIS tipoDatos COMMA valorDato RPARENTHESIS SEMMICOLOM','varDeclaration',9,'p_varDeclaration','SintacticAnalyzer.py',280),
  ('expresionNum -> ID','expresionNum',1,'p_expresionNum','SintacticAnalyzer.py',286),
  ('expresionNum -> Alter_f','expresionNum',1,'p_expresionNum','SintacticAnalyzer.py',287),
  ('expresionNum -> Number','expresionNum',1,'p_expresionNum','SintacticAnalyzer.py',288),
  ('tipoDatos -> Bool','tipoDatos',1,'p_tipoDatos','SintacticAnalyzer.py',294),
  ('tipoDatos -> Num','tipoDatos',1,'p_tipoDatos','SintacticAnalyzer.py',295),
  ('call_f -> CALL LPARENTHESIS ID RPARENTHESIS SEMMICOLOM','call_f',5,'p_call_f','SintacticAnalyzer.py',302),
]
