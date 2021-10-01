# IndeavorHiringChallenge
This is a project on response to the Indeavor hiring challenge

To initiate the project:
(1) migrate the tables by:
run sudo docker-compose run api python manage.py migrate
run sudo docker-compose run api_replica_1 python manage.py migrate
run sudo docker-compose run api_replica_2 python manage.py migrate
(2) create admin user:
run sudo docker-compose run api python manage.py createsuperuser

(4) bring up the container:
docker-compose up
(5) login the admin site on the api server:
http://0.0.0.0:8000/api/admin
(6) register new application:
http://0.0.0.0:8000/api/o/applications/register/
with Client id = e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0
     Client secret = kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup
     Client type = public
     Authorization grant type = Resource owner password-based
name can be whatever
nothing else needs change
(7) access the actual web site:
https://0.0.0.0/
(8) add self-signed certificate to trusted
    'example for chrome':
    https://www.pico.net/kb/how-do-you-get-chrome-to-accept-a-self-signed-certificate/
(9) register and play around

structure:
backend:
  the api is cqrs,rest based
    with a master server that handles:
      authentication:
        registration:
          happens without some kind of authentication, just api call without credentials
        getting access,refresh token from client credentials + user credentials
          access tokens pass to the api replicas
          refresh token stays only on the master and used to refresh the access token
      create/update objects from api
    the data is passed to a messeger server 'rabbit' that handles:
      passing the data to the api replica consumers
    the consumers handle the update of the data
    the api replica servers handle the serving and cashing of the data (using redis)
    the web servers handle only passing html and static data (doesnt have authentication)
    the nginx server handles:
      ssl authentication
      reverse_proxy:
        separating web,query and command
      load_balancing:
        2 query servers (api replicas)
        1 command server (apo server)
        2 web server
front end:
  the front end is a web site using bootstrap , jquery ajax for dynamic loading
  a client class is the backbone that connects the api to the web, contains all
    ajax requests
  everything is template based 
