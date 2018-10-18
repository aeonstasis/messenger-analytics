# messenger-analytics [![Build Status](https://travis-ci.org/aaron-zou/messenger-analytics.svg?branch=electron)](https://travis-ci.org/aaron-zou/messenger-analytics)
Interactive Facebook Messenger analytics and visualization desktop application.


## Summary
These scripts will perform local analysis of your Facebook Messenger conversation logs and display useful statistics and
visualizations. Note that *none* of this data is sent anywhere, other than caches of the statistics being saved locally to
a file path of your choosing.

## Development

Tested on Ubuntu 18.04 LTS.

When building from source, run the following in the root of the directory:

```
npm install --runtime=electron
./node_modules/.bin/electron-rebuild
```

# Packaging (Placeholder)
```
pyinstaller pycalc/api.py --distpath pycalcdist
rm -rf build/
rm -rf api.spec
./node_modules/.bin/electron-packager . --electron-version=4.0.0-beta.1 --overwrite --ignore="pycalc$" --no-prune
```

## Install
In progress

### Downloading your Messenger data

1. Visit https://www.facebook.com/settings?tab=your_facebook_information
2. Click "View" under "Download Your Information"
3. Set "Format" to JSON and choose a date range under "Date Range"
4. Click "Deselect All" and then select only the checkbox for "Messages"
5. Click "Create File"
6. Facebook will notify you by email that your information download request has been received and will email you again after it's done processing.
7. After receiving an email when processing is done, click the "Available Tabs" link in that email.
8. Click "Download" for the file listed on that page (which should say <b>Messages (File Size)</b>).
9. Unzip the file after it downloads to a location of your choice, and note the full filepath for passing to `process_data.py`.

## Usage
In progress

## Acknowledgement
The template for an Electron front-end communicating with a Python backend is from [fyears/electron-python-example](https://github.com/fyears/electron-python-example)

## TODO
- add visualization of frequency-sorted data
- add more analyses, inc. reaction data
- perform basic data analysis of text used by the user and their friends
- clustering / word clouds
- render a front-end for data visualization using d3 or something similar
- capture animated GIF for "downloading Messenger data" README

