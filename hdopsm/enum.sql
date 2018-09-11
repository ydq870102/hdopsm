# itsystem表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('ItSystem','is_untrained_person_use','0','否');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('ItSystem','is_untrained_person_use','1','是');

# host表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','status','1','在用');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','status','2','工程');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','status','3','故障');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','status','4','下架');

# host表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','assets_type','server','物理机');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','assets_type','vmserver','虚拟机');

# host表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','system','0','Linux');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('SysDevice','system','1','Windows');

# process表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Process','cluster_role','0','主用');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Process','cluster_role','1','备用');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Process','cluster_role','2','冷备');

# process表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Database','cluster_role','0','主用');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Database','cluster_role','1','备用');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Database','cluster_role','2','冷备');