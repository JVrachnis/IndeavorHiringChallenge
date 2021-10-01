# IndeavorHiringChallenge
This is a project on response to the Indeavor hiring challenge<br />
<br />
To initiate the project:<br />
(1) migrate the tables by:<br />
run sudo docker-compose run api python manage.py migrate<br />
run sudo docker-compose run api_replica_1 python manage.py migrate<br />
run sudo docker-compose run api_replica_2 python manage.py migrate<br />
(2) create admin user:<br />
run sudo docker-compose run api python manage.py createsuperuser<br />
<br />
(4) bring up the container:<br />
docker-compose up<br />
(5) login the admin site on the api server:<br />
http://0.0.0.0:8000/api/admin<br />
(6) register new application:<br />
http://0.0.0.0:8000/api/o/applications/register/<br />
with Client id = e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0<br />
     Client secret = kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup<br />
     Client type = public<br />
     Authorization grant type = Resource owner password-based<br />
name can be whatever<br />
nothing else needs change<br />
(7) access the actual web site:<br />
https://0.0.0.0/<br />
(8) add self-signed certificate to trusted<br />
    'example for chrome':<br />
    https://www.pico.net/kb/how-do-you-get-chrome-to-accept-a-self-signed-certificate/<br />
(9) register and play around<br />
<br />
structure:<br />
backend:<br />
  the api is cqrs,rest based<br />
    with a master server that handles:<br />
      authentication:<br />
        registration:<br />
          happens without some kind of authentication, just api call without credentials<br />
        getting access,refresh token from client credentials + user credentials<br />
          access tokens pass to the api replicas<br />
          refresh token stays only on the master and used to refresh the access token<br />
      create/update objects from api<br />
    the data is passed to a messeger server 'rabbit' that handles:<br />
      passing the data to the api replica consumers<br />
    the consumers handle the update of the data<br />
    the api replica servers handle the serving and cashing of the data (using redis)<br />
    the web servers handle only passing html and static data (doesnt have authentication)<br />
    the nginx server handles:<br />
      ssl authentication<br />
      reverse_proxy:<br />
        separating web,query and command<br />
      load_balancing:<br />
        2 query servers (api replicas)<br />
        1 command server (apo server)<br />
        2 web server<br />
front end:<br />
  the front end is a web site using bootstrap , jquery ajax for dynamic loading<br />
  a client class is the backbone that connects the api to the web, contains all<br />
    ajax requests<br />
  everything is template based<br />
  all in one page, everything is updated dynamically<br />
    view employees / skills is updating a table in the home page<br />
      can export the table to excel (had some issues with the list of skills / skill categories and option buttons)<br />
    everything else is modal popups<br />
      adding employees / skills can be done by importing files (they must have proper headers, some issues with skills / skill categories)<br />
