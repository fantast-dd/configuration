## vsftpd 虚拟用户配置  

####一、安装
	yum install vsftpd -y
	chkconfig vsftpd

####二、 配置文件
	/etc/vsftpd/vsftpd.conf

####三、认证
	yum -y install db4 db4-utils
	创建用户密码文本，奇数行是用户名，偶数行是密码
	vim /etc/vsftpd/vuser_passwd.txt
		test
		123456
	生成虚拟用户认证的db文件
	db_load -T -t hash -f /etc/vsftpd/vuser_passwd.txt /etc/vsftpd/vuser_passwd.db
	vim /etc/pam.d/vsftpd
		auth required pam_userdb.so db=/etc/vsftpd/vuser_passwd
		account required pam_userdb.so db=/etc/vsftpd/vuser_passwd
	创建虚拟用户配置文件
	mkdir /etc/vsftpd/vuser_conf/
	vim /etc/vsftpd/vuser_conf/test # 注意配置文件里面不能有多余空格，不然会报错
		local_root=/storage/asset/
		write_enable=YES
		anon_umask=022
		anon_world_readable_only=NO
		anon_upload_enable=YES
		anon_mkdir_write_enable=YES
		anon_other_write_enable=YES

####四、设置FTP根目录权限
	vsftpd要求对主目录不能有写的权限所以ftp为755，主目录下面的子目录再设置777权限
	mkdir /storage/asset
	chmod 755 /storage
	chmod 777 /storage/asset
	建立限制用户访问目录的空文件，没有此文件，登陆会报错
	touch /etc/vsftpd/chroot_list