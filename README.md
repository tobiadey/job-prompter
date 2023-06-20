# JobPrompter

### Setup API Server
 1. Enter server directory: `cd server`
 2. Initialize virtual env: `make venv`
 3. Activate it with: `. env/bin/activate`
 4. Install dependencies: `make install`
 5. Run backend server: `make run-server`

### Setup Client Server
 1. Enter client directory: `cd client`
 2. Run client server: `yarn start`
 3. Optional: run backend server `yarn start-api` Only if steps 1-4 have been completed.

### Postgres setup:


### UML
(UML FIGMA)[figma.com]

### API Testing
Prerequisite: Steps 1-4 of API setup have been completed.
- Run unit tests: `cd server && make test`
- Run unit tests: `cd client && yarn test-api` 


### Client Testing
Prerequisite: ?
- Run unit tests: 
- Run unit tests: 


### Notes
- Make code pretty: `make format`
- Lint code: `make lint`


