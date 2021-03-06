# Redirector

This tiny application will take an old OHM uuid or legacy id and return the new resource URI.

## How?

During the migration a JSON file will be generated with, for each add-on, the legacy id, ohm uuid and the new resource
URI.
The application listens on the old OHM endpoints, looks up the requested ID and returns the new URL for this add-on.
The resources.json file is fetched from one of the spaces on Digital Ocean.

Since this app has only 2 routes (that share the same function), almost everything happens in the main.py module.

## Settings

A couple of settings can be set through environment variables:

* redirect_code (307)
* of_resource_url ("https://testforumapp.orbithangar.com/resources")
* spaces_key
* spaces_secret
* spaces_endpoint ("https://nyc3.digitaloceanspaces.com")
* space_name ("ohm")
* resource_json_location ("resources/resources.json")

## Docker

To get it all up and running, a Dockerfile is included. The container is listening on port 8000.
Don't forget to set all required environment variables.

## Notes

Please note that this project is managed with Poetry.
The requirements.txt is genereated and commited to the repository through GitHub actions.