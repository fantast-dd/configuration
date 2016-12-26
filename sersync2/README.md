### SLAVE:

yum	 install rsync -y

vim /etc/rsyncd.conf
	
	uid=root
	gid=root
	max connections=36000
	use chroot= yes
	log file=/var/log/rsyncd.log
	pid file=/var/run/rsyncd.pid
	lock file=/var/run/rsyncd.lock

	[www]
	path=/storage/www # 对应master需要同步的目录
	ignore errors = yes
	read only = no
	hosts allow = 192.168.10.6  # master ip
	hosts deny = *

#### 运行
	rsync --daemon


### MASTER:

yum install rsync -y

download sersync2:
	
	wget http://sersync.googlecode.com/files/sersync2.5_64bit_binary_stable_final.tar.gz

### sersync 启动参数
    -r  # 在监控前 先同步一次目录
    -d  # 后台运行
    -o  # 指定配置文件

#### 运行
	/m2odata/server/sersync/sersync2 -r -d -o /m2odata/server/sersync/confxml.xml