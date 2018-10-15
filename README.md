# messenger-analytics
Analytics and visualizations for Facebook Messenger downloaded data, including frequency-sorted graphs of most-messaged friends.

## Summary
These scripts will perform local analysis of your Facebook Messenger conversation logs and display useful statistics and
visualizations. Note that *none* of this data is sent anywhere, other than caches of the statistics being saved locally to
a file path of your choosing.

## Install
You must have a version of Python 3 running on your system, then after cloning this repository, run:
```
pip install -r requirements.txt
```

You'll also need to download your Facebook Messenger conversation data locally.
1. Visit https://www.facebook.com/settings?tab=your_facebook_information
2. Click "View" under "Download Your Information"
3. Click "Deselect All" and then select only the checkbox for "Messages"
4. Click "Create File"
5. Facebook will notify you by email that your information download request has been received and will email you again after it's done processing.
6. After receiving an email when processing is done, click the "Available Tabs" link in that email.
7. Click "Download" for the file listed on that page (which should say <b>Messages (File Size)</b>).
8. Unzip the file after it downloads to a location of your choice, and note the full filepath for passing to `process_data.py`.

## Usage
To see options, run:
```
python3 process_data.py --help
```

At minimum, you'll need to specify:
```
python3 process_data.py DATA_PATH
```
where that argument points to the messages/ subdirectory under the unzipped Messenger downloaded JSON zip archive.

## TODO
- add visualization of frequency-sorted data
- add more analyses (inc. reaction data)
- perform basic data analysis of text used by the user and their friends
- clustering / word clouds
- rewrite in node.js or save statistics in JSON/MessagePack format
- render a front-end for data visualization using d3 or something similar
- write an Electron app with a local server

