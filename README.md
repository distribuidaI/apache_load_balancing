## apache_load_balancing

### Qué mods instalar? Qué dependencias?

Si queremos hacer esto en nuestra máquina, podemos fijarnos en este [artículo](https://www.digitalocean.com/community/tutorials/how-to-use-apache-http-server-as-reverse-proxy-using-mod_proxy-extension)

### Cuál es la idea?

La idea es tener un proxy reverso adelante que funcione como load balancer, que reciba los requests y los balancee a dos servidores.

#### Config de Virtual Box
La configuración más fácil que encontramos para VBOX es poner el adaptador en modo "host only". Debemos:

1. Crear un adaptador Host Only yendo a File -> Preferences -> Network -> Tab de Host only -> apretar el (+)
2. Usar ese adapter en las 3 compus que usemos

Para empezar, podemos usar un appliance de la [Chapu Virtual Machine](https://dl.dropboxusercontent.com/u/13605936/Chapu1.ova)

#### Config del proxy reverso

```
<VirtualHost *:80>
	# The ServerName directive sets the request scheme, hostname and port that
	# the server uses to identify itself. This is used when creating
	# redirection URLs. In the context of virtual hosts, the ServerName
	# specifies what hostname must appear in the request's Host: header to
	# match this virtual host. For the default virtual host (this file) this
	# value is not decisive as it is used as a last resort host regardless.
	# However, you must set it for any further virtual host explicitly.
	#ServerName www.example.com

	ServerAdmin webmaster@localhost
	DocumentRoot /var/www/html

	# Available loglevels: trace8, ..., trace1, debug, info, notice, warn,
	# error, crit, alert, emerg.
	# It is also possible to configure the loglevel for particular
	# modules, e.g.
	#LogLevel info ssl:warn

	ErrorLog ${APACHE_LOG_DIR}/error.log
	CustomLog ${APACHE_LOG_DIR}/access.log combined

	# For most configuration files from conf-available/, which are
	# enabled or disabled at a global level, it is possible to
	# include a line for only one particular virtual host. For example the
	# following line enables the CGI configuration for this host only
	# after it has been globally disabled with "a2disconf".
	#Include conf-available/serve-cgi-bin.conf
	<Proxy balancer://chapu>
        #ATENCION! La ip que asigna VBOX a las host only es dinámica, puede que cambien estas ips. OJO.

        #server 1
        BalancerMember http://192.168.56.102
        #server 2
        BalancerMember http://192.168.56.103
	</Proxy>
    ProxyPass / balancer://chapu/
    ProxyPassReverse / balancer://chapu/
</VirtualHost>
```

## Referencias

### Debug
https://hkrishnan.in/tag/stickysession/
