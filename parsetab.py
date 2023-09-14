
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftGUION2FS 3FS ADD CADENA_FILE_PATH DELETE ENTERO EXECUTE FDISK FILE_PATH FIT FS GUION ID ID_PAR ID_WORD IGUAL MKDISK MKFS MOUNT MOUNT_LIST NAME PATH REP RMDISK SIZE TYPE UNIT UNMOUNTcomandos : comando_mkdisk\n                | comando_execute\n                | comando_rep\n                | empty_production\n                | comando_fdisk\n                | comando_rmdisk\n                | comando_mount\n                | comando_mountlist\n                | comando_unmount\n                | comando_mkfs\n    empty_production : \n    comando_mkdisk : MKDISK lista_mkdisklista_mkdisk : lista_mkdisk parametros_mkdisk\n                | parametros_mkdiskparametros_mkdisk : param_size\n                | param_unit\n                | param_path\n                | param_fitcomando_rmdisk : RMDISK lista_rmdisklista_rmdisk : lista_rmdisk parametros_rmdisk\n                | parametros_rmdiskparametros_rmdisk : param_pathcomando_execute : EXECUTE lista_executelista_execute : lista_execute parametros_execute\n                | parametros_executeparametros_execute : param_pathcomando_mount : MOUNT lista_mountlista_mount : lista_mount parametros_mount\n                | parametros_mountparametros_mount : param_path\n                | param_namecomando_rep : REP lista_replista_rep : lista_rep parametros_rep\n                | parametros_repparametros_rep : param_path\n                | param_name\n                | param_idcomando_fdisk : FDISK lista_fdisklista_fdisk : lista_fdisk parametros_fdisk\n                | parametros_fdiskparametros_fdisk : param_size\n                | param_path\n                | param_name\n                | param_unit\n                | param_type\n                | param_fit\n                | param_delete\n                | param_addcomando_mountlist : MOUNT_LISTcomando_unmount : UNMOUNT lista_unmountlista_unmount : lista_unmount parametros_unmount\n                | parametros_unmountparametros_unmount : param_idcomando_mkfs : MKFS lista_mkfslista_mkfs : lista_mkfs parametros_mkfs\n                | parametros_mkfsparametros_mkfs : param_id\n                | param_type\n                | param_fsparam_size : GUION SIZE IGUAL ENTEROparam_path : GUION PATH IGUAL CADENA_FILE_PATH\n                |  GUION PATH IGUAL FILE_PATHparam_unit : GUION UNIT IGUAL IDparam_name : GUION NAME IGUAL IDparam_fit : GUION FIT IGUAL IDparam_type : GUION TYPE IGUAL IDparam_delete : GUION DELETE IGUAL IDparam_add : GUION ADD IGUAL ENTERO\n                | GUION ADD IGUAL entero_negativoparam_id : GUION ID_WORD IGUAL ID_PARparam_fs : GUION FS IGUAL 2FS\n                | GUION FS IGUAL 3FSentero_negativo : GUION ENTERO %prec GUION'
    
_lr_action_items = {'MKDISK':([0,],[12,]),'EXECUTE':([0,],[13,]),'REP':([0,],[14,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,18,21,22,23,24,25,26,28,29,30,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,57,58,59,61,62,63,64,65,67,72,73,76,80,81,82,83,95,96,97,98,99,100,101,102,103,105,106,107,108,109,],[-11,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-49,-12,-14,-15,-16,-17,-18,-23,-25,-26,-32,-34,-35,-36,-37,-38,-40,-41,-42,-43,-44,-45,-46,-47,-48,-19,-21,-22,-27,-29,-30,-31,-50,-52,-53,-54,-56,-57,-58,-59,-13,-24,-33,-39,-20,-28,-51,-55,-60,-63,-61,-62,-65,-64,-70,-66,-67,-68,-69,-71,-72,-73,]),'FDISK':([0,],[15,]),'RMDISK':([0,],[16,]),'MOUNT':([0,],[17,]),'MOUNT_LIST':([0,],[18,]),'UNMOUNT':([0,],[19,]),'MKFS':([0,],[20,]),'GUION':([12,13,14,15,16,17,19,20,21,22,23,24,25,26,28,29,30,32,33,34,35,36,38,39,40,41,42,43,44,45,46,47,49,50,51,52,53,54,55,57,58,59,61,62,63,64,65,67,72,73,76,80,81,82,83,93,95,96,97,98,99,100,101,102,103,105,106,107,108,109,],[27,31,37,48,31,56,60,66,27,-14,-15,-16,-17,-18,31,-25,-26,37,-34,-35,-36,-37,48,-40,-41,-42,-43,-44,-45,-46,-47,-48,31,-21,-22,56,-29,-30,-31,60,-52,-53,66,-56,-57,-58,-59,-13,-24,-33,-39,-20,-28,-51,-55,104,-60,-63,-61,-62,-65,-64,-70,-66,-67,-68,-69,-71,-72,-73,]),'SIZE':([27,48,],[68,68,]),'UNIT':([27,48,],[69,69,]),'PATH':([27,31,37,48,56,],[70,70,70,70,70,]),'FIT':([27,48,],[71,71,]),'NAME':([37,48,56,],[74,74,74,]),'ID_WORD':([37,60,66,],[75,75,75,]),'TYPE':([48,66,],[77,77,]),'DELETE':([48,],[78,]),'ADD':([48,],[79,]),'FS':([66,],[84,]),'IGUAL':([68,69,70,71,74,75,77,78,79,84,],[85,86,87,88,89,90,91,92,93,94,]),'ENTERO':([85,93,104,],[95,105,109,]),'ID':([86,88,89,91,92,],[96,99,100,102,103,]),'CADENA_FILE_PATH':([87,],[97,]),'FILE_PATH':([87,],[98,]),'ID_PAR':([90,],[101,]),'2FS':([94,],[107,]),'3FS':([94,],[108,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'comandos':([0,],[1,]),'comando_mkdisk':([0,],[2,]),'comando_execute':([0,],[3,]),'comando_rep':([0,],[4,]),'empty_production':([0,],[5,]),'comando_fdisk':([0,],[6,]),'comando_rmdisk':([0,],[7,]),'comando_mount':([0,],[8,]),'comando_mountlist':([0,],[9,]),'comando_unmount':([0,],[10,]),'comando_mkfs':([0,],[11,]),'lista_mkdisk':([12,],[21,]),'parametros_mkdisk':([12,21,],[22,67,]),'param_size':([12,15,21,38,],[23,40,23,40,]),'param_unit':([12,15,21,38,],[24,43,24,43,]),'param_path':([12,13,14,15,16,17,21,28,32,38,49,52,],[25,30,34,41,51,54,25,30,34,41,51,54,]),'param_fit':([12,15,21,38,],[26,45,26,45,]),'lista_execute':([13,],[28,]),'parametros_execute':([13,28,],[29,72,]),'lista_rep':([14,],[32,]),'parametros_rep':([14,32,],[33,73,]),'param_name':([14,15,17,32,38,52,],[35,42,55,35,42,55,]),'param_id':([14,19,20,32,57,61,],[36,59,63,36,59,63,]),'lista_fdisk':([15,],[38,]),'parametros_fdisk':([15,38,],[39,76,]),'param_type':([15,20,38,61,],[44,64,44,64,]),'param_delete':([15,38,],[46,46,]),'param_add':([15,38,],[47,47,]),'lista_rmdisk':([16,],[49,]),'parametros_rmdisk':([16,49,],[50,80,]),'lista_mount':([17,],[52,]),'parametros_mount':([17,52,],[53,81,]),'lista_unmount':([19,],[57,]),'parametros_unmount':([19,57,],[58,82,]),'lista_mkfs':([20,],[61,]),'parametros_mkfs':([20,61,],[62,83,]),'param_fs':([20,61,],[65,65,]),'entero_negativo':([93,],[106,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> comandos","S'",1,None,None,None),
  ('comandos -> comando_mkdisk','comandos',1,'p_comandos','interprete.py',103),
  ('comandos -> comando_execute','comandos',1,'p_comandos','interprete.py',104),
  ('comandos -> comando_rep','comandos',1,'p_comandos','interprete.py',105),
  ('comandos -> empty_production','comandos',1,'p_comandos','interprete.py',106),
  ('comandos -> comando_fdisk','comandos',1,'p_comandos','interprete.py',107),
  ('comandos -> comando_rmdisk','comandos',1,'p_comandos','interprete.py',108),
  ('comandos -> comando_mount','comandos',1,'p_comandos','interprete.py',109),
  ('comandos -> comando_mountlist','comandos',1,'p_comandos','interprete.py',110),
  ('comandos -> comando_unmount','comandos',1,'p_comandos','interprete.py',111),
  ('comandos -> comando_mkfs','comandos',1,'p_comandos','interprete.py',112),
  ('empty_production -> <empty>','empty_production',0,'p_empty_production','interprete.py',117),
  ('comando_mkdisk -> MKDISK lista_mkdisk','comando_mkdisk',2,'p_comando_mkdisk','interprete.py',123),
  ('lista_mkdisk -> lista_mkdisk parametros_mkdisk','lista_mkdisk',2,'p_lista_mkdisk','interprete.py',128),
  ('lista_mkdisk -> parametros_mkdisk','lista_mkdisk',1,'p_lista_mkdisk','interprete.py',129),
  ('parametros_mkdisk -> param_size','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',137),
  ('parametros_mkdisk -> param_unit','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',138),
  ('parametros_mkdisk -> param_path','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',139),
  ('parametros_mkdisk -> param_fit','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',140),
  ('comando_rmdisk -> RMDISK lista_rmdisk','comando_rmdisk',2,'p_comando_rmdisk','interprete.py',145),
  ('lista_rmdisk -> lista_rmdisk parametros_rmdisk','lista_rmdisk',2,'p_lista_rmdisk','interprete.py',150),
  ('lista_rmdisk -> parametros_rmdisk','lista_rmdisk',1,'p_lista_rmdisk','interprete.py',151),
  ('parametros_rmdisk -> param_path','parametros_rmdisk',1,'p_parametros_rmdisk','interprete.py',159),
  ('comando_execute -> EXECUTE lista_execute','comando_execute',2,'p_comando_execute','interprete.py',164),
  ('lista_execute -> lista_execute parametros_execute','lista_execute',2,'p_lista_execute','interprete.py',171),
  ('lista_execute -> parametros_execute','lista_execute',1,'p_lista_execute','interprete.py',172),
  ('parametros_execute -> param_path','parametros_execute',1,'p_parametros_execute','interprete.py',180),
  ('comando_mount -> MOUNT lista_mount','comando_mount',2,'p_comando_mount','interprete.py',185),
  ('lista_mount -> lista_mount parametros_mount','lista_mount',2,'p_lista_mount','interprete.py',189),
  ('lista_mount -> parametros_mount','lista_mount',1,'p_lista_mount','interprete.py',190),
  ('parametros_mount -> param_path','parametros_mount',1,'p_parametros_mount','interprete.py',198),
  ('parametros_mount -> param_name','parametros_mount',1,'p_parametros_mount','interprete.py',199),
  ('comando_rep -> REP lista_rep','comando_rep',2,'p_comando_rep','interprete.py',204),
  ('lista_rep -> lista_rep parametros_rep','lista_rep',2,'p_lista_rep','interprete.py',208),
  ('lista_rep -> parametros_rep','lista_rep',1,'p_lista_rep','interprete.py',209),
  ('parametros_rep -> param_path','parametros_rep',1,'p_parametros_rep','interprete.py',217),
  ('parametros_rep -> param_name','parametros_rep',1,'p_parametros_rep','interprete.py',218),
  ('parametros_rep -> param_id','parametros_rep',1,'p_parametros_rep','interprete.py',219),
  ('comando_fdisk -> FDISK lista_fdisk','comando_fdisk',2,'p_comando_fdisk','interprete.py',224),
  ('lista_fdisk -> lista_fdisk parametros_fdisk','lista_fdisk',2,'p_lista_fdisk','interprete.py',228),
  ('lista_fdisk -> parametros_fdisk','lista_fdisk',1,'p_lista_fdisk','interprete.py',229),
  ('parametros_fdisk -> param_size','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',237),
  ('parametros_fdisk -> param_path','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',238),
  ('parametros_fdisk -> param_name','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',239),
  ('parametros_fdisk -> param_unit','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',240),
  ('parametros_fdisk -> param_type','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',241),
  ('parametros_fdisk -> param_fit','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',242),
  ('parametros_fdisk -> param_delete','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',243),
  ('parametros_fdisk -> param_add','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',244),
  ('comando_mountlist -> MOUNT_LIST','comando_mountlist',1,'p_comando_mountlist','interprete.py',249),
  ('comando_unmount -> UNMOUNT lista_unmount','comando_unmount',2,'p_comando_unmount','interprete.py',254),
  ('lista_unmount -> lista_unmount parametros_unmount','lista_unmount',2,'p_lista_unmount','interprete.py',258),
  ('lista_unmount -> parametros_unmount','lista_unmount',1,'p_lista_unmount','interprete.py',259),
  ('parametros_unmount -> param_id','parametros_unmount',1,'p_parametros_unmount','interprete.py',267),
  ('comando_mkfs -> MKFS lista_mkfs','comando_mkfs',2,'p_comando_mkfs','interprete.py',272),
  ('lista_mkfs -> lista_mkfs parametros_mkfs','lista_mkfs',2,'p_lista_mkfs','interprete.py',276),
  ('lista_mkfs -> parametros_mkfs','lista_mkfs',1,'p_lista_mkfs','interprete.py',277),
  ('parametros_mkfs -> param_id','parametros_mkfs',1,'p_parametros_mkfs','interprete.py',285),
  ('parametros_mkfs -> param_type','parametros_mkfs',1,'p_parametros_mkfs','interprete.py',286),
  ('parametros_mkfs -> param_fs','parametros_mkfs',1,'p_parametros_mkfs','interprete.py',287),
  ('param_size -> GUION SIZE IGUAL ENTERO','param_size',4,'p_param_size','interprete.py',292),
  ('param_path -> GUION PATH IGUAL CADENA_FILE_PATH','param_path',4,'p_param_path','interprete.py',296),
  ('param_path -> GUION PATH IGUAL FILE_PATH','param_path',4,'p_param_path','interprete.py',297),
  ('param_unit -> GUION UNIT IGUAL ID','param_unit',4,'p_param_unit','interprete.py',301),
  ('param_name -> GUION NAME IGUAL ID','param_name',4,'p_param_name','interprete.py',305),
  ('param_fit -> GUION FIT IGUAL ID','param_fit',4,'p_param_fit','interprete.py',309),
  ('param_type -> GUION TYPE IGUAL ID','param_type',4,'p_param_type','interprete.py',313),
  ('param_delete -> GUION DELETE IGUAL ID','param_delete',4,'p_param_delete','interprete.py',317),
  ('param_add -> GUION ADD IGUAL ENTERO','param_add',4,'p_param_add','interprete.py',321),
  ('param_add -> GUION ADD IGUAL entero_negativo','param_add',4,'p_param_add','interprete.py',322),
  ('param_id -> GUION ID_WORD IGUAL ID_PAR','param_id',4,'p_param_id','interprete.py',326),
  ('param_fs -> GUION FS IGUAL 2FS','param_fs',4,'p_param_fs','interprete.py',330),
  ('param_fs -> GUION FS IGUAL 3FS','param_fs',4,'p_param_fs','interprete.py',331),
  ('entero_negativo -> GUION ENTERO','entero_negativo',2,'p_entero_negativo','interprete.py',337),
]
