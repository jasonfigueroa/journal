This is the repo for the source files used to generate the static files served at [https://jasonfigueroa.github.io](https://jasonfigueroa.github.io). 
*Note: I am using python 2.7.*

## Setup

1. Make a directory to work out of and cd into it
2. Create virtual environment
```virtualenv env```
3. Activate the virtual environment
```source env/bin/activate```
*Note: to deactivate the virtual environment use* ```deactivate```
4. With the virtual environment activated install pelican, markdown, typogrify
```pip install pelican markdown typogrify```
5. Clone the source files from repo found at [https://github.com/jasonfigueroa/journal](https://github.com/jasonfigueroa/journal)

## Local Development

To create the content for local development use:
```make html```
*Note: This uses the pelicanconf.py file to generate the output*
To spin up a local server for development use:
```make serve```
The development site will be located at [http://localhost:8000](http://localhost:8000)

## Publish Site

To publish the content to be pushed to github pages use:
```make publish```
*Note: This uses the publishconf.py file to generate the output*
Push all of the contents found in the directory called **output** to github pages