# hawkingBank

Getting started (assuming you are on a unix system)

1. Create a directory and clone the repository into it
2. From the base directory run `python3 -m venv venv` to create a virtual environment folder
3. Enter your virtual environment `source venv/bin/activate` note: all instructions for the rest of time will assume 
you've done this (when you are done developing you can leave the virtual environment using `deactivate`)
4. Install dependencies `pip install -r requirements.txt`
5. Create a temporary folder (it's useful to have) `mkdir tmp`
5. Run the development server `flask run`
6. If all is well you should be able to visit `localhost:5000` in your browser and see a hello world
7. Take the file `pre-commit` from your base directory and place it in `/.git/hooks`
8. Run the command `chmod +x .git/hooks/pre-commit` to make the hook executable

You are now ready to develop. Stick to the master branch for now...

All code will be linted according to the google coding standards:
http://google.github.io/styleguide/pyguide.html

If your code does not conform to the standards you will find the pylinter will
refuse to allow you to commit. 

If you must break code standards for a legit reason (it can happen) you can comment the code 
with `# pylint: disable={error name}` please do not abuse this!

To do:
* Script for initialising dev environment
* Config and variables framework
* Unit test framework
* Logging / monitoring framework
* Threading support
* ORM
* Requests
* Pipeline
* Non-dev server
* etc.

Other:
* If you introduce new content that should not be added to the repo please add it to the `.gitignore`
* All code will be linted according to the google coding standards:
http://google.github.io/styleguide/pyguide.html
* If your code does not conform to the standards you will find the pylinter will
refuse to allow you to commit. 
* If you must break code standards for a legit reason (it can happen) you can comment the code 
with `# pylint: disable={error name}` please do not abuse this!