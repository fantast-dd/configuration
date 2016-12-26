###overview
	keepalived
	
####Download
	wget http://www.keepalived.org/software/keepalived-1.3.0.tar.gz
	
####Installation
	yum install kernel 

	./configure --prefix=/usr/local/keepalived \
	--sysconf=/etc \
	--with-kernel-dir=/usr/src/kernels/2.6.32-642.11.1.el6.x86_64/
	
	make && make install