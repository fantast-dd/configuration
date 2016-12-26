## nginx做http反向代理,web server,rtmp server

### 安装
	useradd -M -s /sbin/nologin www
	# proxy，webserver
   	./configure --user=www --group=www --prefix=/storage/server/nginx-1.8.0 --with-http_stub_status_module
   	# rtmp server

### Roles

| Modules	 	      		 	             | proxy | web server | rtmp server |
| ------------------------------------------ | ----- | ---------- | ----------- |
| [Core functionality](#functionality)	   	 | yes   | yes        |
| [ngx_http_core_module](#http_core)    	 | yes   | yes        |
| [ngx_http_headers_module](#http_headers) 	 | yes   | yes        |
| [ngx_http_rewrite_module](#http_rewrite) 	 | yes   | yes        |
| [ngx_http_proxy_module](#http_proxy)		 | yes   | no         |
| [ngx_http_gzip_module](#http_gzip)		 | yes   | yes        |
| [ngx_http_upstream_module](#http_upstream) | yes   | yes        |
| [ngx_http_fastcgi_module](#http_fastcgi)	 | no    | yes        |

### 参数配置说明

- - - - - -
#### functionality

- user
>设置nginx运行的用户与用户组

- error_log
>定义错误日志路径及等级

- pid
>定义pid文件路径

- worker_processes
>设置worker process的进程数

- worker_rlimit_nofile
>设置nginx能打开的最大FD数量

- use
>设置选用哪种I/O模型

- worker_connections
>设置最大连接数

- accept_mutex
>"惊群问题" 建议pv较大关闭，较小开启

- multi_accept

- include
>包含其它的配置文件

- - - - - -

#### http_core

- server_names_hash_bucket_size [32/64/128]
>指定servername的hash表大小

- client_header_buffer_size [default 1k],large_client_header_buffers [4 4k/8k]
> nginx默认的request header长度上限是4k，如果超过了这个值，nginx会直接返回400错误，通过以下两个参数调整request header上限。默认用client_header_buffer_size这个buffer来读取request header值，如果request header过大，会使用large_client_header_buffers来读取

- client_max_body_size
>运行客户端请求的最大单文件字节数

- client_body_buffer_size 
>设置连接请求body的缓冲区大小

- sendfile
>web server设置on proxy设置没有什么意义

- tcp_nopush
>只有设置了sendfile才起作用

- tcp_nodelay
>作用于socket参数TCP_NODELAY

- server_tokens
>设置隐藏nginx版本号

- keepalive_timeout
>设置keepalive超时时间 0关闭keepalive

- client_header_timeout
>定义读客户端请求头的超时时间

- client_body_timeout
>定义读客户端请求body的超时时间

- reset_timedout_connection off
>是否重置超时的连接

- send_timeout
>设置传输response到客户端的超时时间

- server_name
>设置主机域名，可以设置多个

- server_name_in_redirect
>是否开启只使用第一个域名（当server_name中有多个域名的时候）

- default_type
>定义response的默认MIME type

- location
>根据请求URI设置配置

- root
>为请求设置根目录

- - - - - -

#### http_headers
##### The ngx_http_headers_module module allows adding the “Expires” and “Cache-Control” header fields, and arbitrary fields, to a response header.

- add_header
>给response header添加field

- expires
>是否添加或修改response header中的"Expires"和"Cache-Control"fields

- - - - - -

#### http_rewrite
##### The ngx_http_rewrite_module module is used to change request URI using PCRE regular expressions, return redirects, and conditionally select configurations.

- set
>设置变量的值

- rewrite
>URI重定向

- - - - - -

#### http_proxy
##### The ngx_http_proxy_module module allows passing requests to another server.

- proxy_connect_timeout
>与proxied server建立连接的超时时间

- proxy_read_timeout
>设置读取proxied server response的超时时间

- proxy_send_timeout
>设置发送请求给proxied server的超时时间

- proxy_buffer_size 4k|8k
>设置缓冲区的大小，从proxied server读取的第一部分response会放在这里，小的response header通常位于这里

- proxy_buffers 8 4k|8k
>设置缓冲区的数量和大小，从proxied server读取的response会放在这里

- proxy_busy_buffers_size

- proxy_temp_file_write_size

- proxy_next_upstream
>定义哪些与proxied server通信的状态为失败

- proxy_set_header
>重新定义或添加fields到请求头

- proxy_http_version
>设置与proxied server通信的http版本号，建议1.1版本与proxied server实现keepalive连接

- proxy_redirect
>是否修改proxied server返回头信息中的"Location"和"Refresh"fields

- proxy_pass
>设置proxied server的协议和地址，一个可以映射过去的URI

- - - - - -

#### http_gzip
##### The ngx_http_gzip_module module is a filter that compresses responses using the “gzip” method. This often helps to reduce the size of transmitted data by half or even more.

- gzip
>是否开启gzip压缩

- gzip_disable
>对指定的User-Agent不进行压缩

- gzip_proxied
>做proxy时启用，根据某些请求和应答头（via）来决是否对代理请求的应答启用gzip压缩

- gzip_min_length
>设置压缩的页面的最小字节数 建议1k

- gzip_buffers
>设置多大的缓存来存储gzip的压缩结果数据流

- gzip_http_version
>设置可以压缩的最小http版本

- gzip_comp_level
>设置压缩等级，建议2

- gzip_types
>需要压缩的MIME类型

- gzip_vary
>是否在返回头里面插入"Vary: Accept-Encoding"

- - - - - -

#### http_upstream
##### The ngx_http_upstream_module module is used to define groups of servers that can be referenced by the proxy_pass, fastcgi_pass, uwsgi_pass, scgi_pass, and memcached_pass directives.

- upstream
>定义一组proxied server

- server
>定义server的ip地址和其它参数

    - weight
    > 设置server的权重

    - max_fails
    > server通信的失败次数

    - fail_timeout
    > fail_timeout时间段内，如果失败的通信次数大于指定的max_fails，则认为proxied server down，并持续fail_timeout定义的时间段

- keepalive
>设置每个worker process与upstream servers最大的长连接数

- - - - - -

#### http_fastcgi
##### The ngx_http_fastcgi_module module allows passing requests to a FastCGI server.

- fastcgi_connect_timeout
>与FastCGI server建立连接的超时时间

- fastcgi_send_timeout
>设置发送请求给FastCGI server的超时时间

- fastcgi_read_timeout
>设置读取FastCGI server response的超时时间

- fastcgi_buffer_size 4k|8k
>设置缓冲区的大小，从FastCGI server读取的第一部分response会放在这里，小的response header通常位于这里

- fastcgi_buffers 8 4k|8k
>设置缓冲区的数量和大小，从FastCGI server读取的response会放在这里

- fastcgi_busy_buffers_size

- fastcgi_temp_file_write_size

- fastcgi_temp_path
>定义一个目录存放从FastCGI server接收的数据

- fastcgi_pass
>设置FastCGI serevr的地址，可以是ip或者domain name

- fastcgi_index
>设置index文件

- fastcgi_param
>设置给FastCGI server传送的参数

- - - - - -
