
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftGUIONADD CADENA_FILE_PATH DELETE ENTERO EXECUTE FDISK FILE_PATH FIT GUION ID ID_PAR ID_WORD IGUAL MKDISK MOUNT MOUNT_LIST NAME PATH REP RMDISK SIZE TYPE UNIT UNMOUNTcomandos : comando_mkdisk\n                | comando_execute\n                | comando_rep\n                | empty_production\n                | comando_fdisk\n                | comando_rmdisk\n                | comando_mount\n                | comando_mountlist\n                | comando_unmount\n    empty_production : \n    comando_mkdisk : MKDISK lista_mkdisklista_mkdisk : lista_mkdisk parametros_mkdisk\n                | parametros_mkdiskparametros_mkdisk : param_size\n                | param_unit\n                | param_path\n                | param_fitcomando_rmdisk : RMDISK lista_rmdisklista_rmdisk : lista_rmdisk parametros_rmdisk\n                | parametros_rmdiskparametros_rmdisk : param_pathcomando_execute : EXECUTE lista_executelista_execute : lista_execute parametros_execute\n                | parametros_executeparametros_execute : param_pathcomando_mount : MOUNT lista_mountlista_mount : lista_mount parametros_mount\n                | parametros_mountparametros_mount : param_path\n                | param_namecomando_rep : REP lista_replista_rep : lista_rep parametros_rep\n                | parametros_repparametros_rep : param_path\n                | param_name\n                | param_idcomando_fdisk : FDISK lista_fdisklista_fdisk : lista_fdisk parametros_fdisk\n                | parametros_fdiskparametros_fdisk : param_size\n                | param_path\n                | param_name\n                | param_unit\n                | param_type\n                | param_fit\n                | param_delete\n                | param_addcomando_mountlist : MOUNT_LISTcomando_unmount : UNMOUNT lista_unmountlista_unmount : lista_unmount parametros_unmount\n                | parametros_unmountparametros_unmount : param_idparam_size : GUION SIZE IGUAL ENTEROparam_path : GUION PATH IGUAL CADENA_FILE_PATH\n                |  GUION PATH IGUAL FILE_PATHparam_unit : GUION UNIT IGUAL IDparam_name : GUION NAME IGUAL IDparam_fit : GUION FIT IGUAL IDparam_type : GUION TYPE IGUAL IDparam_delete : GUION DELETE IGUAL IDparam_add : GUION ADD IGUAL ENTERO\n                | GUION ADD IGUAL entero_negativoparam_id : GUION ID_WORD IGUAL ID_PARentero_negativo : GUION ENTERO %prec GUION'
    
_lr_action_items = {'MKDISK':([0,],[11,]),'EXECUTE':([0,],[12,]),'REP':([0,],[13,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,17,19,20,21,22,23,24,26,27,28,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,55,56,57,59,64,65,68,72,73,74,84,85,86,87,88,89,90,91,92,94,95,96,],[-10,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-48,-11,-13,-14,-15,-16,-17,-22,-24,-25,-31,-33,-34,-35,-36,-37,-39,-40,-41,-42,-43,-44,-45,-46,-47,-18,-20,-21,-26,-28,-29,-30,-49,-51,-52,-12,-23,-32,-38,-19,-27,-50,-53,-56,-54,-55,-58,-57,-63,-59,-60,-61,-62,-64,]),'FDISK':([0,],[14,]),'RMDISK':([0,],[15,]),'MOUNT':([0,],[16,]),'MOUNT_LIST':([0,],[17,]),'UNMOUNT':([0,],[18,]),'GUION':([11,12,13,14,15,16,18,19,20,21,22,23,24,26,27,28,30,31,32,33,34,36,37,38,39,40,41,42,43,44,45,47,48,49,50,51,52,53,55,56,57,59,64,65,68,72,73,74,83,84,85,86,87,88,89,90,91,92,94,95,96,],[25,29,35,46,29,54,58,25,-13,-14,-15,-16,-17,29,-24,-25,35,-33,-34,-35,-36,46,-39,-40,-41,-42,-43,-44,-45,-46,-47,29,-20,-21,54,-28,-29,-30,58,-51,-52,-12,-23,-32,-38,-19,-27,-50,93,-53,-56,-54,-55,-58,-57,-63,-59,-60,-61,-62,-64,]),'SIZE':([25,46,],[60,60,]),'UNIT':([25,46,],[61,61,]),'PATH':([25,29,35,46,54,],[62,62,62,62,62,]),'FIT':([25,46,],[63,63,]),'NAME':([35,46,54,],[66,66,66,]),'ID_WORD':([35,58,],[67,67,]),'TYPE':([46,],[69,]),'DELETE':([46,],[70,]),'ADD':([46,],[71,]),'IGUAL':([60,61,62,63,66,67,69,70,71,],[75,76,77,78,79,80,81,82,83,]),'ENTERO':([75,83,93,],[84,94,96,]),'ID':([76,78,79,81,82,],[85,88,89,91,92,]),'CADENA_FILE_PATH':([77,],[86,]),'FILE_PATH':([77,],[87,]),'ID_PAR':([80,],[90,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'comandos':([0,],[1,]),'comando_mkdisk':([0,],[2,]),'comando_execute':([0,],[3,]),'comando_rep':([0,],[4,]),'empty_production':([0,],[5,]),'comando_fdisk':([0,],[6,]),'comando_rmdisk':([0,],[7,]),'comando_mount':([0,],[8,]),'comando_mountlist':([0,],[9,]),'comando_unmount':([0,],[10,]),'lista_mkdisk':([11,],[19,]),'parametros_mkdisk':([11,19,],[20,59,]),'param_size':([11,14,19,36,],[21,38,21,38,]),'param_unit':([11,14,19,36,],[22,41,22,41,]),'param_path':([11,12,13,14,15,16,19,26,30,36,47,50,],[23,28,32,39,49,52,23,28,32,39,49,52,]),'param_fit':([11,14,19,36,],[24,43,24,43,]),'lista_execute':([12,],[26,]),'parametros_execute':([12,26,],[27,64,]),'lista_rep':([13,],[30,]),'parametros_rep':([13,30,],[31,65,]),'param_name':([13,14,16,30,36,50,],[33,40,53,33,40,53,]),'param_id':([13,18,30,55,],[34,57,34,57,]),'lista_fdisk':([14,],[36,]),'parametros_fdisk':([14,36,],[37,68,]),'param_type':([14,36,],[42,42,]),'param_delete':([14,36,],[44,44,]),'param_add':([14,36,],[45,45,]),'lista_rmdisk':([15,],[47,]),'parametros_rmdisk':([15,47,],[48,72,]),'lista_mount':([16,],[50,]),'parametros_mount':([16,50,],[51,73,]),'lista_unmount':([18,],[55,]),'parametros_unmount':([18,55,],[56,74,]),'entero_negativo':([83,],[95,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> comandos","S'",1,None,None,None),
  ('comandos -> comando_mkdisk','comandos',1,'p_comandos','interprete.py',96),
  ('comandos -> comando_execute','comandos',1,'p_comandos','interprete.py',97),
  ('comandos -> comando_rep','comandos',1,'p_comandos','interprete.py',98),
  ('comandos -> empty_production','comandos',1,'p_comandos','interprete.py',99),
  ('comandos -> comando_fdisk','comandos',1,'p_comandos','interprete.py',100),
  ('comandos -> comando_rmdisk','comandos',1,'p_comandos','interprete.py',101),
  ('comandos -> comando_mount','comandos',1,'p_comandos','interprete.py',102),
  ('comandos -> comando_mountlist','comandos',1,'p_comandos','interprete.py',103),
  ('comandos -> comando_unmount','comandos',1,'p_comandos','interprete.py',104),
  ('empty_production -> <empty>','empty_production',0,'p_empty_production','interprete.py',109),
  ('comando_mkdisk -> MKDISK lista_mkdisk','comando_mkdisk',2,'p_comando_mkdisk','interprete.py',115),
  ('lista_mkdisk -> lista_mkdisk parametros_mkdisk','lista_mkdisk',2,'p_lista_mkdisk','interprete.py',120),
  ('lista_mkdisk -> parametros_mkdisk','lista_mkdisk',1,'p_lista_mkdisk','interprete.py',121),
  ('parametros_mkdisk -> param_size','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',129),
  ('parametros_mkdisk -> param_unit','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',130),
  ('parametros_mkdisk -> param_path','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',131),
  ('parametros_mkdisk -> param_fit','parametros_mkdisk',1,'p_parametros_mkdisk','interprete.py',132),
  ('comando_rmdisk -> RMDISK lista_rmdisk','comando_rmdisk',2,'p_comando_rmdisk','interprete.py',137),
  ('lista_rmdisk -> lista_rmdisk parametros_rmdisk','lista_rmdisk',2,'p_lista_rmdisk','interprete.py',142),
  ('lista_rmdisk -> parametros_rmdisk','lista_rmdisk',1,'p_lista_rmdisk','interprete.py',143),
  ('parametros_rmdisk -> param_path','parametros_rmdisk',1,'p_parametros_rmdisk','interprete.py',151),
  ('comando_execute -> EXECUTE lista_execute','comando_execute',2,'p_comando_execute','interprete.py',156),
  ('lista_execute -> lista_execute parametros_execute','lista_execute',2,'p_lista_execute','interprete.py',163),
  ('lista_execute -> parametros_execute','lista_execute',1,'p_lista_execute','interprete.py',164),
  ('parametros_execute -> param_path','parametros_execute',1,'p_parametros_execute','interprete.py',172),
  ('comando_mount -> MOUNT lista_mount','comando_mount',2,'p_comando_mount','interprete.py',177),
  ('lista_mount -> lista_mount parametros_mount','lista_mount',2,'p_lista_mount','interprete.py',181),
  ('lista_mount -> parametros_mount','lista_mount',1,'p_lista_mount','interprete.py',182),
  ('parametros_mount -> param_path','parametros_mount',1,'p_parametros_mount','interprete.py',190),
  ('parametros_mount -> param_name','parametros_mount',1,'p_parametros_mount','interprete.py',191),
  ('comando_rep -> REP lista_rep','comando_rep',2,'p_comando_rep','interprete.py',196),
  ('lista_rep -> lista_rep parametros_rep','lista_rep',2,'p_lista_rep','interprete.py',200),
  ('lista_rep -> parametros_rep','lista_rep',1,'p_lista_rep','interprete.py',201),
  ('parametros_rep -> param_path','parametros_rep',1,'p_parametros_rep','interprete.py',209),
  ('parametros_rep -> param_name','parametros_rep',1,'p_parametros_rep','interprete.py',210),
  ('parametros_rep -> param_id','parametros_rep',1,'p_parametros_rep','interprete.py',211),
  ('comando_fdisk -> FDISK lista_fdisk','comando_fdisk',2,'p_comando_fdisk','interprete.py',216),
  ('lista_fdisk -> lista_fdisk parametros_fdisk','lista_fdisk',2,'p_lista_fdisk','interprete.py',220),
  ('lista_fdisk -> parametros_fdisk','lista_fdisk',1,'p_lista_fdisk','interprete.py',221),
  ('parametros_fdisk -> param_size','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',229),
  ('parametros_fdisk -> param_path','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',230),
  ('parametros_fdisk -> param_name','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',231),
  ('parametros_fdisk -> param_unit','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',232),
  ('parametros_fdisk -> param_type','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',233),
  ('parametros_fdisk -> param_fit','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',234),
  ('parametros_fdisk -> param_delete','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',235),
  ('parametros_fdisk -> param_add','parametros_fdisk',1,'p_parametros_fdisk','interprete.py',236),
  ('comando_mountlist -> MOUNT_LIST','comando_mountlist',1,'p_comando_mountlist','interprete.py',241),
  ('comando_unmount -> UNMOUNT lista_unmount','comando_unmount',2,'p_comando_unmount','interprete.py',246),
  ('lista_unmount -> lista_unmount parametros_unmount','lista_unmount',2,'p_lista_unmount','interprete.py',250),
  ('lista_unmount -> parametros_unmount','lista_unmount',1,'p_lista_unmount','interprete.py',251),
  ('parametros_unmount -> param_id','parametros_unmount',1,'p_parametros_unmount','interprete.py',259),
  ('param_size -> GUION SIZE IGUAL ENTERO','param_size',4,'p_param_size','interprete.py',264),
  ('param_path -> GUION PATH IGUAL CADENA_FILE_PATH','param_path',4,'p_param_path','interprete.py',268),
  ('param_path -> GUION PATH IGUAL FILE_PATH','param_path',4,'p_param_path','interprete.py',269),
  ('param_unit -> GUION UNIT IGUAL ID','param_unit',4,'p_param_unit','interprete.py',273),
  ('param_name -> GUION NAME IGUAL ID','param_name',4,'p_param_name','interprete.py',277),
  ('param_fit -> GUION FIT IGUAL ID','param_fit',4,'p_param_fit','interprete.py',281),
  ('param_type -> GUION TYPE IGUAL ID','param_type',4,'p_param_type','interprete.py',285),
  ('param_delete -> GUION DELETE IGUAL ID','param_delete',4,'p_param_delete','interprete.py',289),
  ('param_add -> GUION ADD IGUAL ENTERO','param_add',4,'p_param_add','interprete.py',293),
  ('param_add -> GUION ADD IGUAL entero_negativo','param_add',4,'p_param_add','interprete.py',294),
  ('param_id -> GUION ID_WORD IGUAL ID_PAR','param_id',4,'p_param_id','interprete.py',298),
  ('entero_negativo -> GUION ENTERO','entero_negativo',2,'p_entero_negativo','interprete.py',304),
]
