## mysql table-partition

#### 导入存储过程
 
	mysql -uroot -p123456 zabbix < create.sql
	mysql -uroot -p123456 zabbix < drop.sql
	mysql -uroot -p123456 zabbix < verify.sql
	mysql -uroot -p123456 zabbix < maintenance.sql
	mysql -uroot -p123456 zabbix < partition_call.sql

#### How to use
	CALL partition_maintenance('<zabbix_db_name>', '<table_name>', <days_to_keep_data>, <hourly_interval>, <num_future_intervals_to_create>)
	# example
	CALL partition_maintenance(zabbix, 'history_uint', 31, 24, 14);
	
	/storage/server/mysql/bin/mysql -uroot -p123456 zabbix -e "CALL partition_maintenance_all('zabbix');"
