# Redirector

This tiny application will take an old OHM uuid or legacy id and return the new resource URI.

## How?

During the migration a JSON file will be generated with, for each add-on, the legacy id, ohm uuid and the new resource
URI.
The application listens on the old OHM endpoints, looks up the requested ID and returns the new URL for this add-on.

## Settings

A couple of settings can be set through environment variables:

* redirect_code (307)
* of_resource_url ("https://testforumapp.orbithangar.com/resources")
* resource_mapping_json ("./resources.json")

## Docker

To get it all up and running, a Dockerfile is included. The container is listening on port 8000.
The resources.json file, with all the ID mappings, can be mounted from the host to the container:

```shell
docer run -p 8000:8000 -v /host/path/resources.json:/code/resources.json
```

The `requirements.txt` is gitignored on purpose. It's generated automatically (`poetry export`) through CI/CD when needed.