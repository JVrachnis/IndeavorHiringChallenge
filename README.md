# IndeavorHiringChallenge
This is a project on response to the Indeavor hiring challenge

###To initiate the project:
####(1) migrate the tables by:
```bash
sudo docker-compose run api python manage.py migrate
sudo docker-compose run api_replica_1 python manage.py migrate
sudo docker-compose run api_replica_2 python manage.py migrate
```
####(2) create admin user:
```bash
run sudo docker-compose run api python manage.py createsuperuser
```
####(4) bring up the container:
##### make sure you have the right acces
```bash
sudo chown -R $USER:$USER .
docker-compose up
```
####((5) login the admin site on the api server:
http://0.0.0.0:8000/api/admin
####((6) register new application:
http://0.0.0.0:8000/api/o/applications/register/
with
`Client id = e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0`
`Client secret = kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup`
`Client type = public`
`Authorization grant type = Resource owner password-based`
name can be whatever
nothing else needs change
####(7) access the actual web site:
https://0.0.0.0/
####(8) add self-signed certificate to trusted
    'example for chrome':
    https://www.pico.net/kb/how-do-you-get-chrome-to-accept-a-self-signed-certificate/
####(9) register and play around
##API
####Structure
+ #####https://0.0.0.0/api/ (No POST/PUT/DELETE)
	Most thigns in here need authedication
	In the request header add `Authorization: Bearer {token}`
	with GET , it will repsond with all the urls of the api
  + #####https://0.0.0.0/api/register/ (POST only) (No authedication required)
   + The request data must contain the folowing keys: username,password1,password2
     + username: must be unic to the server
	 + password1:
		+ must be a strong password
		+ must contain at least 8 characters
		+ shouldnt contain the username
		+ can’t be a commonly used password
		+ can’t be entirely numeric
	 + password2: same as password1
	+ if success, the repsonse will be 'username':{username} as json
	+ if something is wrong it will respone with {error_key}:[{error_message}] for each key as json
  + #####https://0.0.0.0/api/empoloyees/ (DELETE not allowed)
  The fields are: name,surname,hiring_date,skillset,url
  Can use filtering by adding &search=search_term ,and its searching in   name,surname,hiring_date,skillset
  Example using curl:
  ```bash
  curl -X GET -H 'Authorization: Bearer P7HtbHbOR7D2I3VW0sCUAZP9XpaH4f' 'https://0.0.0.0/api/employees/?search=e' --insecure
  ```
  Example resault`
  [{"name":"heergo","surname":"ffas","hiring_date":"2021-09-29T21:04:14Z","skillset":["tatata"],"url":"https://0.0.0.0:443/api/employees/49/"},{"name":"Γιάννης","surname":"Βραχνης","hiring_date":"2021-10-01T13:20:06.782541Z","skillset":["hellp","me"],"url":"https://0.0.0.0:443/api/employees/48/"}]`
     + #####https://0.0.0.0/api/empoloyees/{id}/
	 **Required fields for create are: name,surname,skillset**
  + #####https://0.0.0.0/api/skills/
  The fields are: name, description,categories,created,url
  Can use filtering by adding &search=search_term ,and its searching in   
  name, description,categories__name
    + #####https://0.0.0.0/api/skills/{name}/
	**Required fields for create are: name, description,categories,created,url**
+ #####https://0.0.0.0/o/ (Nothing)
  + #####https://0.0.0.0/o/token/ (POST)
  **The request must have header: Authorization: Basic {btoa_credentials}
  where btoa_credentials = btoa('client_id:client_secret')
  And in the data contain username,password , grant_type=password **
  can specify  scope= read  / scope=write / scope=read write in the data to restreact the scope
  Example using curl:
  ```bash
  curl -X POST -u "e5AnSIkaVJjTCECv28ZXmPxgDzeAjBXe4n4v63n0:kbCmhs2ExhCYOcggI8AjCzXwZHCsElHhSfE2v3cXzzMeZLJmMYFhKdA58teRY42MWAINnFOiYYoKO31nvEFUmjBJigUICDbS6gIa6WxVmIyMXmDxBSwVDoCAfOYJmCup" -d 'grant_type=password&username=admin&password=123qwe!@#QWE' 'https://0.0.0.0/api/o/token/' --insecure
  ```
  repsonts with `{"access_token": "{access_token}", "expires_in": 36000, "token_type": "Bearer", "scope": "read write groups", "refresh_token": "{refresh_token}"}`

  + #####https://0.0.0.0/o/refresh/ (POST)
  **like https://0.0.0.0/o/token/ but the data should contain:
  grant_type=refresh_token,refresh_token={refresh_token} instead**
  repsonts with `{"access_token": "{access_token}", "expires_in": 36000, "token_type": "Bearer", "scope": "read write groups", "refresh_token": "{refresh_token}"}`
  + #####https://0.0.0.0/o/revoke_token/ (POST)
  **like https://0.0.0.0/o/token/ but the data should contain:
  grant_type={access_token} instead**
  doesnt repsone
  + #####https://0.0.0.0/o/checkauth/ (POST/GET)
  **authedication is the same as https://0.0.0.0/api/**
  repsonts with {"success"}
##Project Structure
+ ###BACKEND:
  + #####The api is cqrs,rest based`
    + #####A master server handles:
       + #####Authentication:
        + #####Registration:
          + happens without some kind of authentication, just api call without credentials
        + getting access,refresh token from client credentials + user credentials
        + access tokens pass to the api replicas
        + refresh token stays only on the master and used to refresh the access token
    + Create/update objects from api
  + #####A messeger server 'rabbit' handles:
      + Passing the data to the api replica consumers
  + #####The consumers handle the update of the data
  + #####The api replica servers handle the serving and cashing of the data (using redis)
  + #####The web servers handle only passing html and static data (doesnt have authentication)
  + #####The nginx server handles:
    +  #####ssl authentication
    + #####reverse proxy:
        + separating web,query and command
    + #####load balancing:
        + 2 query servers (api replicas)
        + 1 command server (apo server)
        + 2 web server
+ ###Front end:
  + #####The front end is a web site using bootstrap , jquery ajax for dynamic loading
   + #####A client class is the backbone that connects the api to the web, contains all
     + Ajax requests
  + #####Everything is template based
  + #####All in one page, everything is updated dynamically in the client side
    + #####View employees / skills is updating a table in the home page
       + can export the table to excel (had some issues with the list of skills / skill categories and option buttons)
   + #####Everything else is modal popups
      + adding employees / skills can be done by importing files (they must have proper headers, some issues with skills / skill categories)
      + employees header:
        + name,surname hiring_date,skillset (skillset cant contait more than one, you can add more later)
        + name,description,categories (categories cant contait more than one, you can add more later)
