博友
重启apache          ansible apache -u centos -s -m shell -a "cd /usr/local/apache/bin;./apachectl graceful"
重启nginx           ansible nginx -u centos -s -m shell -a "lnmp nginx reload"
同步apachepc          ansible apache -u centos -s -m copy -a "src=/usr/local/apache/conf/vhost/pc.conf dest=/usr/local/apache/conf/vhost"
同步nginx pc          ansible nginx -u centos -s -m copy -a "src=/opt/nginx_pc.conf dest=/usr/local/nginx/conf/vhost"
易彩
重启ngin     ansible nginx -m shell -a "sudo lnmp nginx reload"
重启apache   ansible websrv  -m shell -a "cd /usr/local/apache/bin;sudo ./apachectl graceful"
同步apachepc   ansible websrv -u centos -s -m copy -a "src=/usr/local/apache/conf/vhost2/ycpc.conf dest=/usr/local/apache/conf/vhost2"
同步nginxpc    ansible nginx -u centos -s -m copy -a "src=/opt/nginx_pc.conf dest=/usr/local/nginx/conf/vhost"
