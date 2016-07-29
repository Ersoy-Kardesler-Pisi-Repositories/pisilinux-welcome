from setuptools import setup, find_packages
from os import listdir, system


langs = []
for l in listdir('languages'):
    if l.endswith('ts'):
        system('lrelease-qt5 languages/%s' % l)
        langs.append(('languages/%s' % l).replace('.ts', '.qm'))


system('pyrcc5 welcome.qrc -o welcome/resource.py')

datas = [('/usr/share/applications', ['data/pisilinux-welcome.desktop']),
         ('/etc/skel/.config/autostart', ['data/pisilinux-welcome.desktop']),
         ('/usr/share/icons/hicolor/scalable/apps', ['images/pisilinux-welcome.svg']),
         ('/usr/share/welcome/languages', langs),
         ('/usr/share/welcome/data', ["data/pisilinux-2-0-kurulum-belgesi.pdf", "data/pisilinux-welcome.desktop"])]

setup(
    name = "pisilinux-welcome",
    scripts = ["pisilinux-welcome"],
    packages = find_packages(),
    version = "1.0",
    license = "GPL v3",
    description = "PisiLinux Welcome",
    author = "Metehan Özbek",
    author_email = "mthnzbk@gmail.com",
    url = "https://github.com/PisiLinuxNew/pisilinux-welcome",
    keywords = ["PyQt5"],
    data_files = datas
)

