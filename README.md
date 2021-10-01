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
