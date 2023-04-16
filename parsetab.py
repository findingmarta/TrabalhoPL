
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'ATTRIBUTE CLASS ID TAG TEXTtag : TAGtag : TAG IDtag : TAG class_listtag : TAG ID class_listtag : TAG TEXTtag : TAG attr_listtag : TAG ID attr_listtag : TAG class_list attr_listtag : TAG ID class_list attr_listattr : ATTRIBUTEattr : ATTRIBUTE TEXTattr_list : attrattr_list : attr_list "," attrclass : CLASSclass_list : classclass_list : class_list class'
    
_lr_action_items = {'TAG':([0,],[2,]),'$end':([1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,],[0,-1,-2,-3,-5,-6,-15,-12,-14,-10,-4,-7,-8,-16,-11,-9,-13,]),'ID':([2,],[3,]),'TEXT':([2,10,],[5,16,]),'CLASS':([2,3,4,7,9,11,14,],[9,9,9,-15,-14,9,-16,]),'ATTRIBUTE':([2,3,4,7,9,11,14,15,],[10,10,10,-15,-14,10,-16,10,]),',':([6,8,10,12,13,16,17,18,],[15,-12,-10,15,15,-11,15,-13,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'tag':([0,],[1,]),'class_list':([2,3,],[4,11,]),'attr_list':([2,3,4,11,],[6,12,13,17,]),'class':([2,3,4,11,],[7,7,14,14,]),'attr':([2,3,4,11,15,],[8,8,8,8,18,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> tag","S'",1,None,None,None),
  ('tag -> TAG','tag',1,'p_tag','main.py',34),
  ('tag -> TAG ID','tag',2,'p_tag_with_id','main.py',38),
  ('tag -> TAG class_list','tag',2,'p_tag_with_class','main.py',42),
  ('tag -> TAG ID class_list','tag',3,'p_tag_with_id_and_class','main.py',46),
  ('tag -> TAG TEXT','tag',2,'p_tag_with_text','main.py',50),
  ('tag -> TAG attr_list','tag',2,'p_tag_with_attr','main.py',54),
  ('tag -> TAG ID attr_list','tag',3,'p_tag_with_id_attr','main.py',58),
  ('tag -> TAG class_list attr_list','tag',3,'p_tag_with_class_attr','main.py',62),
  ('tag -> TAG ID class_list attr_list','tag',4,'p_tag_with_id_class_attr','main.py',66),
  ('attr -> ATTRIBUTE','attr',1,'p_attr','main.py',70),
  ('attr -> ATTRIBUTE TEXT','attr',2,'p_attr_with_value','main.py',74),
  ('attr_list -> attr','attr_list',1,'p_attr_list','main.py',82),
  ('attr_list -> attr_list , attr','attr_list',3,'p_attr_list_multiple','main.py',86),
  ('class -> CLASS','class',1,'p_class','main.py',90),
  ('class_list -> class','class_list',1,'p_class_list_single','main.py',94),
  ('class_list -> class_list class','class_list',2,'p_class_list_multiple','main.py',98),
]
