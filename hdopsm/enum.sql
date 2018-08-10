# itsystem表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('ItSystem','is_untrained_person_use','0','否');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('ItSystem','is_untrained_person_use','1','是');
# host表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','status','1','在用');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','status','2','工程');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','status','3','故障');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','status','4','下架');

# host表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','assets_type','server','物理机');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','assets_type','vmserver','虚拟机');

# host表枚举
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','system','0','Linux');
insert into t_com_enum(table_name,table_column,value,value_desc)values ('Host','system','1','Windows');

insert into t_com_zone (label_cn) values('ERP类');
insert into t_com_zone (label_cn) values('财务类');
insert into t_com_zone (label_cn) values('研究院类');
insert into t_com_zone (label_cn) values('数据类');
insert into t_com_zone (label_cn) values('外部访问区-DMZ区域');
insert into t_com_zone (label_cn) values('公有云');
insert into t_com_zone (label_cn) values('一般业务区');
insert into t_com_zone (label_cn) values('管理区');
insert into t_com_zone (label_cn) values('海大大厦');

