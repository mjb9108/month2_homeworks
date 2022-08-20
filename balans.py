from envparse import env
import os
env.read_envfile('.env')
many = int(os.environ.get('MY_MONEY'))









