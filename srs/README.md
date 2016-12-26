###overview
	srs做rtmp流媒体服务器

####download
	wget https://codeload.github.com/ossrs/srs/tar.gz/v2.0-b2
	
####installation
	cd srs-2.0-b2
	./configure --prefix=/usr/local/srs \
	--with-ssl \
	--with-hls \
	--with-nginx \
	--with-dvr \
	--with-http-callback \
	--with-http-api \
	--with-stat \
	--with-transcode \
	--with-ingest \
	--with-stream-caster
	
	make && make install
	
####configuration
	rtmp.conf
	listen              1935;
	max_connections     1000;
	vhost __defaultVhost__ {
	}
	http_api {
   		enabled     on;
    	listen      1985;
    	crossdomain on;
	}
	
####start
	cd /usr/local/srs
	./objs/srs -c conf/rtmp.conf
	
####api
	查看api版本
	http://127.0.0.1:1985/api/
	查看rtmp流信息
	http://127.0.0.1:1985/api/v1/streams/