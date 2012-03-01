# thanks:
# https://github.com/zacharyvoase/dotfiles/blob/master/pythonrc
# https://github.com/sontek/dotfiles/blob/master/_pythonrc.py
# http://brianlyttle.com/2011/10/python-interpreter-tab-completion-on-os-x/

import inspect
import sys
import os
home = os.environ["HOME"]

if not "bpython" in os.environ["_"]:
    try:
        import rlcompleter
        import readline
        readline.set_history_length(1000)
        readline.parse_and_bind(open("%s/.inputrc" % home).read())
        if sys.platform == "darwin":
            readline.parse_and_bind("bind ^I rl_complete")
            # screw you, libedit
        HISTFILE = "%s/.pyhistory." % home
        try:
            readline.read_history_file(HISTFILE)
        except: pass
        import atexit
        atexit.register(lambda: readline.write_history_file(HISTFILE))
    except:
        print >>sys.stderr, "Couldn't get rlcompleter + readline working."

try:
    from see import see
except ImportError:
    print >>sys.stderr, "Please pip install see"

if "DJANGO_SETTINGS_MODULE" in os.environ:
    from django.db.models.loading import get_models
    from django.test.client import Client
    from django.test.utils import setup_test_environment, teardown_test_environment
    from django.conf import settings as S

    class DjangoModels(object):
        """Loop through all the models in INSTALLED_APPS and import them."""
        def __init__(self):
            for m in get_models():
                setattr(self, m.__name__, m)

    M = DjangoModels()
    C = Client()
