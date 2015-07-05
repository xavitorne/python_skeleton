from fabric.api import *

version = "0.1"

# the user to use for the remote commands
env.user = 'user_name
'
# the servers where the commands are executed, ip of the host:
env.hosts = ['']

def clean():
    run('rm -rf /tmp/project_name /tmp/project_name.tar.gz')

def pack():
    # create a new source distribution as tarball
    local('python setup.py sdist --formats=gztar', capture=False)

def deploy():
    clean()
    # figure out the release name and version
    dist = local('python setup.py --fullname', capture=True).strip()

    # upload the source tarball to the temporary folder on the server
    put('dist/%sdev.tar.gz' % dist, '/tmp/project_name.tar.gz')

    # create a place where we can unzip the tarball, then enter
    # that directory and unzip it
    with cd('/var/www/project_name'):
        run('source env/bin/activate')
        run('mkdir /tmp/project_name')
        with cd('/tmp/project_name'):
            run('tar xzf /tmp/project_name.tar.gz')
            with cd('/tmp/project_name/project_name-'+version+'dev'):
                # now setup the package with our virtual environment's
                # python interpreter
                run('/var/www/project_name/env/bin/python setup.py install')
    with cd('/var/www/project_name'):
        run ('killall /var/www/project_name/env/bin/python')
        run ('env/bin/pserve app.ini &')

    # now that all is set up, delete the folder again
    clean()

    # and finally touch the .wsgi file so that mod_wsgi triggers
    # a reload of the application
    #run('touch /var/www/project_name/app.ini')
    #run('deactivate')
