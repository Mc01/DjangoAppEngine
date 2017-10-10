# Project boilerplate for GAE

Runs on Google App Engine and Datastore

## Installation

- Install Google App Engine Launcher from https://storage.googleapis.com/appengine-sdks/featured/GoogleAppEngineLauncher-1.9.57.dmg
- (Alternatively) Install Google App Engine SDK from https://cloud.google.com/appengine/docs/standard/python/download
- Add this directory as existing project to GAE Launcher (or SDK)
- Run `pip install -r requirements.txt -t lib` (be sure to use Python version 2)
- Start project through Launcher
- Visit `http://localhost:8000` for local management console
- Visit `http://localhost:8080` for running application

## Management

To setup management commands you need following:
- setup virtualenv from requirements
- link your `app.yaml` to sitepackages in virtualenv

### Local

- manage Datastore by models `./manage.py shell_plus`
- create admin user `./manage.py createsuperuser`

### Remote

- manage Datastore by models `./manage.py --sandbox=remote shell_plus`
- create admin user `./manage.py --sandbox=remote createsuperuser`

## Known issues

- unique constraint is very costly (slow downs Datastore),
- `app.yaml` and `index.yaml` is global for all deployed versions (you need to deploy to `1` if you want something on `test`)
- data in Datastore are global for all deployed versions (use separate GAE project to test Datastore)
