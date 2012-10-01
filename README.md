Artechetype (terrible pun) is a grab-and-go starter django+js I use when making new digital projects.  You're welcome to as well, and if you come across improvements, pull requests are welcome.

NOTE: I'm still working on it. Don't use it quite yet.

Setup for this app
==================

1. Clone it down.

2. Set up a virtualenv for it.  `pip install -r requirements.txt`

3. Edit your `/etc/hosts` file, and add: ```127.0.0.1   myportlandschools.herokuapp.com```

4. `cd projects`

5. `./manage.py syncdb`  (For some reason, this was occasionally failing on me.  If so, just run it again.)

6. `./manage.py migrate`

7. Fire up the test server, but on port 80: `sudo manage.py runserver 0.0.0.0:80`

8. You can now get to the app at: http://myportlandschools.herokuapp.com


Note: When you want to actually use the live app, you'll need to comment that line out of your `/etc/hosts` file.