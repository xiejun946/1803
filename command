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
博有无线    博友无线只有nginx服务
同步h5配置文件     ansible nginx -m copy -u centos -s -a "src=/opt/bywxnginx_h5.conf  dest=/usr/local/nginx/conf/vhost3"
同步电脑文件       ansible nginx -m copy -u centos -s -a "src=/opt/bywxnginx_pc.conf  dest=/usr/local/nginx/conf/vhost3"
 重启          ansible nginx -m shell -a "sudo lnmp nginx reload"


易彩博友博友无线都是一样，每周更新一次redis文件，同步到前端服务器，有文件读取文件，没有文件就读取redis
cd /home/git/yicai/gcapi
sudo php generate_dsn_file.php
ansible websrv -m copy -s -a 'src=/home/git/yicai/gcapi/config_dsn dest=/home/git/yicai/gcapi mode=777'
