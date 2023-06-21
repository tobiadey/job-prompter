# JobPrompter
Explain applications purpose...
* (UML - Application Structure & UserFlow)[figma.com]
* (UI Design)[figma.com]
* (UI Designed by Bunmi Adewunmi) [bunmiadewunmi.com]

### Setup Backend Server
 1. Enter backend directory: `cd backend`
 2. Initialize virtual env: `make venv`
 3. Activate it with: `. env/bin/activate`
 4. Install dependencies: `make install`
 5. Run backend server: `make server-dev` or `make server-prod`

### Setup Client Server
 1. Enter client directory: `cd client`
 2. Run client server: `yarn start`
 3. Optional: Run backend server `yarn start-server-dev` or `yarn start-server-prod` Only if steps 1-4 have been completed.

### Postgres setup(local):
 1. Install PostgreSQL
 2. Create db user `user` with password `user`: `createuser -sP user`
 3. Create unit test db: `createdb -O user job_prompter_test`
 4. Create development db: `createdb -O user job_prompter_dev`

### Backened Testing
Prerequisite: Steps 1-4 of Backend setup has been completed.
* Run unit tests: `cd backend && make test`
* Run unit tests: `cd client && yarn test-api` 

### Client Testing
Prerequisite: ?
* Run unit tests: 
* Run unit tests: 

### Database changes
To create migration and apply changes to the database:
* Enter backend directory: `cd backend`
* update model in `models.py`
* run `make db-migrate`
* rename migration (the `change_summary` part)
* add migration to repository
* run `make db-upgrade`

### Backened Notes
* Make code pretty: `make format`
* Lint code: `make lint`

### Client Notes
* xxx