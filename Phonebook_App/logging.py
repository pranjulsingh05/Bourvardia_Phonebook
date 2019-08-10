# pylint: disable=invalid-name
"""
import logging library to make log files.
"""
import logging

# Logging in login.py

login_logger = logging.getLogger('Phonebook_Project Login')
login_logger.setLevel(logging.INFO)

login_file = logging.FileHandler('/home/nineleaps/Documents/Backend/Logs/Phonebook_Project-Login.log')
login_file.setLevel(logging.INFO)

slh = logging.StreamHandler()
slh.setLevel(logging.ERROR)

loginformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

login_file.setFormatter(loginformatter)
slh.setFormatter(loginformatter)

login_logger.addHandler(login_file)
login_logger.addHandler(slh)


# Logging in view.py

view_logger = logging.getLogger('Phonebook_Project View')
view_logger.setLevel(logging.INFO)

vh = logging.FileHandler('/home/nineleaps/Documents/Backend/Logs/Phonebook_Project-View.log')
vh.setLevel(logging.INFO)

vsh = logging.StreamHandler()
vsh.setLevel(logging.ERROR)

Viewformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

vh.setFormatter(Viewformatter)
vsh.setFormatter(Viewformatter)

view_logger.addHandler(vh)
view_logger.addHandler(vsh)


# Logging in profile.py

profile_logger = logging.getLogger('Phonebook_Project View')
profile_logger.setLevel(logging.INFO)

ph = logging.FileHandler('/home/nineleaps/Documents/Backend/Logs/Phonebook_Project-Profile.log')
ph.setLevel(logging.INFO)

psh = logging.StreamHandler()
psh.setLevel(logging.ERROR)

Profileformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ph.setFormatter(Profileformatter)
psh.setFormatter(Profileformatter)

profile_logger.addHandler(ph)
profile_logger.addHandler(psh)
