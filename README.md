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