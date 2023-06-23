# JobPrompter

Explain applications purpose...

- Application Structure & UserFlow - [UML](https://www.figma.com/)
- UML Designed by Myself - Tobi
- [UI Design](https://www.figma.com/)
- UI Designed by [Bunmi Adewunmi](https://www.bunmiadewunmi.com/)

### Setup Backend Server

1.  Enter backend directory: `cd backend`
2.  Initialize virtual env: `make venv`
3.  Activate it with: `. env/bin/activate`
4.  Install dependencies: `make install`
5.  Run backend server: `make server-dev` or `make server-prod`

### Setup Client Server

1.  Enter client directory: `cd client`
2.  Run client server: `yarn start`
3.  Optional: Run backend server `yarn start-server-dev` or `yarn start-server-prod` Only if steps 1-4 have been completed.

### Postgres setup(local):

1.  Install PostgreSQL
2.  Create db user `user` with password `user`: `createuser -sP user`
3.  Create unit test db: `createdb -O user job_prompter_test`
4.  Create development db: `createdb -O user job_prompter_dev`

### Redis setup:

1. `brew install redis`
2. `brew services start redis`

### Backened Testing

Prerequisite: Steps 1-4 of Backend setup has been completed.

- Run unit tests: `cd backend && make test`
- Run unit tests: `cd client && yarn test-backend`

### Client Testing

Prerequisite: ?

- Run unit tests:
- Run unit tests:

### Database changes

To create migration and apply changes to the database:

- Enter backend directory: `cd backend`
- update model in `models.py`
- run `make db-migrate`
- rename migration (the `change_summary` part)
- add migration to repository
- run `make db-upgrade`

### Backened Notes

- Make code pretty: `make format`
- Lint code: `make lint`

### Client Notes

- xxx

### Learn More

You can learn more in the [Create React App documentation](https://facebook.github.io/create-react-app/docs/getting-started).

To learn React, check out the [React documentation](https://reactjs.org/).

##### Code Splitting

This section has moved here: [https://facebook.github.io/create-react-app/docs/code-splitting](https://facebook.github.io/create-react-app/docs/code-splitting)

#####  Analyzing the Bundle Size

This section has moved here: [https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size](https://facebook.github.io/create-react-app/docs/analyzing-the-bundle-size)

#####  Making a Progressive Web App

This section has moved here: [https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app](https://facebook.github.io/create-react-app/docs/making-a-progressive-web-app)

#####  Advanced Configuration

This section has moved here: [https://facebook.github.io/create-react-app/docs/advanced-configuration](https://facebook.github.io/create-react-app/docs/advanced-configuration)

#####  Deployment

This section has moved here: [https://facebook.github.io/create-react-app/docs/deployment](https://facebook.github.io/create-react-app/docs/deployment)

#####  `npm run build` fails to minify

This section has moved here: [https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify](https://facebook.github.io/create-react-app/docs/troubleshooting#npm-run-build-fails-to-minify)
