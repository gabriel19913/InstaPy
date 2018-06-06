import os
import time
from tempfile import gettempdir

from selenium.common.exceptions import NoSuchElementException

from instapy import InstaPy

insta_username = 'grifedocapacete'
insta_password = 'lucas10'

# set headless_browser=True if you want to run InstaPy on a server

# set these in instapy/settings.py if you're locating the
# library in the /usr/lib/pythonX.X/ directory:
#   Settings.database_location = '/path/to/instapy.db'
#   Settings.chromedriver_location = '/path/to/chromedriver'

session = InstaPy(username=insta_username,
                  password=insta_password,
                  headless_browser=False,
                  multi_logs=True)

try:
    session.login()

    # settings
    session.set_relationship_bounds(enabled=True,
				 potency_ratio=-1.21,
				  delimit_by_numbers=True,
				   max_followers=4590,
				    max_following=5555,
				     min_followers=45,
				      min_following=77)
    session.set_do_comment(True, percentage=10)
    session.set_comments(['Que ótima foto!', 'Foto legal!!!', 'Boa foto!', 'Essa foto está linda!', 'Essa imagem é muito boa!', 'Que imagem incrível!', 'Você conseguiu tirar uma bela foto!', 'Parabéns por essa bela foto!'])
    session.set_dont_include(['friend1', 'friend2', 'friend3'])
    session.set_dont_like(['pizza', 'girl'])

    # actions

    #session.set_user_interact(amount=5, randomize=True, percentage=100, media='Photo')
    #session.like_by_locations(['213255513'], amount=10)
    #session.comment_by_locations(['213255513'], amount=10)
    session.set_delimit_liking(enabled=True, max=300, min=None)
    session.set_delimit_commenting(enabled=True, max=None, min=10)
    session.set_user_interact(amount=2, percentage=70, randomize=True, media='Photo')
    session.follow_likers (['peelscapacetes' , 'ls2brasil'], photos_grab_amount = 2, follow_likers_per_photo = 3, randomize=True, sleep_delay=600, interact=True)
    session.like_by_tags(['capacete', 'duasrodas', 'instamoto'], amount=10, interact=True)

except Exception as exc:
    # if changes to IG layout, upload the file to help us locate the change
    if isinstance(exc, NoSuchElementException):
        file_path = os.path.join(gettempdir(), '{}.html'.format(time.strftime('%Y%m%d-%H%M%S')))
        with open(file_path, 'wb') as fp:
            fp.write(session.browser.page_source.encode('utf8'))
        print('{0}\nIf raising an issue, please also upload the file located at:\n{1}\n{0}'.format(
            '*' * 70, file_path))
    # full stacktrace when raising Github issue
    raise

finally:
    # end the bot session
    session.end()
