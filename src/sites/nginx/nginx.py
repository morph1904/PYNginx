import nginx
import subprocess as shell


def nginx_create(site):
    conf = nginx.Conf()
    server = nginx.Server()

    server.add(
        nginx.Key('listen', '80'),
        nginx.Key('server_name', site.domain),
        nginx.Location('/',
                       nginx.Key('proxy_pass', site.proxy_destination),
                       nginx.Key('proxy_http_version', '1.1'),
                       nginx.Key('proxy_set_header', 'Connection $http_connection'),
                       nginx.Key('proxy_set_header', 'Origin http://$host'),
                       nginx.Key('proxy_set_header', 'Upgrade $http_upgrade'),
                       )
    )
    conf.add(server)
    nginx.dumpf(conf, '/etc/nginx/sites-enabled' + site.domain + '.conf')

    return True


def ssl_create(site):
    nginxstop = shell.call('service nginx stop', shell=True)
    nginxstart = shell.call('service nginx start', shell=True)