import logging


""" Logging in login.py """
login_logger = logging.getLogger('Phonebook Login')
login_logger.setLevel(logging.INFO)

lh = logging.FileHandler('/home/nineleaps/Documents/Backend/Logs/Phonebook-Login.log')
lh.setLevel(logging.INFO)

slh = logging.StreamHandler()
slh.setLevel(logging.ERROR)

Loginformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

lh.setFormatter(Loginformatter)
slh.setFormatter(Loginformatter)

login_logger.addHandler(lh)
login_logger.addHandler(slh)


""" Logging in view.py """
view_logger = logging.getLogger('Phonebook View')
view_logger.setLevel(logging.INFO)

vh = logging.FileHandler('/home/nineleaps/Documents/Backend/Logs/Phonebook-View.log')
vh.setLevel(logging.INFO)

vsh = logging.StreamHandler()
vsh.setLevel(logging.ERROR)

Viewformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

vh.setFormatter(Viewformatter)
vsh.setFormatter(Viewformatter)

view_logger.addHandler(vh)
view_logger.addHandler(vsh)


""" Logging in profile.py """
profile_logger = logging.getLogger('Phonebook View')
profile_logger.setLevel(logging.INFO)

ph = logging.FileHandler('/home/nineleaps/Documents/Backend/Logs/Phonebook-Profile.log')
ph.setLevel(logging.INFO)

psh = logging.StreamHandler()
psh.setLevel(logging.ERROR)

Profileformatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

ph.setFormatter(Profileformatter)
psh.setFormatter(Profileformatter)

profile_logger.addHandler(ph)
profile_logger.addHandler(psh)

