superuser : nicolas
password :azerty123

from django.contrib.auth.models import User
from accounts.models import Profile, Follow 
from events.models import Involvement, Event
import dateutil.parser

""" DATE """
dated1=dateutil.parser.parse('2017-12-12 12:00:00-00')
dated2=dateutil.parser.parse('2017-12-13 12:00:00-00')
dated3=dateutil.parser.parse('2017-12-14 12:00:00-00')
dated4=dateutil.parser.parse('2017-12-15 12:00:00-00')

datef1=dateutil.parser.parse('2017-12-13 12:00:00-00')
datef2=dateutil.parser.parse('2017-12-14 12:00:00-00')
datef3=dateutil.parser.parse('2017-12-15 12:00:00-00')
datef4=dateutil.parser.parse('2017-12-16 12:00:00-00')

""" USER """
matthieu_user=User.objects.create_user("matthieu", "matthieu@connect.com", "mdpconnect")
matthieu_user.first_name="Matthieu"
matthieu_user.last_name="Bernard"
matthieu_user.save()

emma_user=User.objects.create_user("emma", "emma@connect.com", "mdpconnect")
emma_user.first_name="Emma"
emma_user.last_name="Durand"
emma_user.save()

justine_user=User.objects.create_user("justine", "justine@connect.com", "mdpconnect")
justine_user.first_name="Justine"
justine_user.last_name="Fauché"
justine_user.save()

jean_user=User.objects.create_user("jean", "jean@connect.com", "mdpconnect")
jean_user.first_name="Jean"
jean_user.last_name="Dupond"
jean_user.save()

""" PROFILE """
matthieu=Profile(user=matthieu_user)
matthieu.save()

jean=Profile(user=jean_user)
jean.save()

emma=Profile(user=emma_user)
emma.save()

justine=Profile(user=justine_user)
justine.save()

""" EVENT """
anniversaire_matthieu=Event(title="Anniversaire de Matthieu", admin=matthieu, place="Roynac", description="Je fête mon anniversaire !!", date_start=dated1, date_end=datef1)
anniversaire_matthieu.save()

anniversaire_jacques=Event(title="Anniversaire de Jacques", admin=matthieu, place="Grenoble", description="Je fête mon anniversaire chez Titi !!", date_start=dated1, date_end=datef1)
anniversaire_jacques.save()

cremaillaire=Event(title="Crémaillaire", admin=jean, place="Montélimar", description="Grosse crémaillaire chez moi !!!", date_start=dated1, date_end=datef1)
cremaillaire.save()

anniversaire_justine=Event(title="Anniversaire de Justine", admin=justine, place="Roynac", description="Je fête mon anniversaire !!", date_start=dated1, date_end=datef1)
anniversaire_justine.save()

Involvement(event=anniversaire_jacques, profile=matthieu).save()
Involvement(event=anniversaire_jacques, profile=jean).save()
Involvement(event=anniversaire_jacques, profile=emma).save()
Involvement(event=anniversaire_jacques, profile=justine).save()
Involvement(event=anniversaire_matthieu, profile=justine).save()
Involvement(event=anniversaire_matthieu, profile=matthieu).save()
Involvement(event=cremaillaire, profile=matthieu).save()
Involvement(event=cremaillaire, profile=jean).save()
Involvement(event=cremaillaire, profile=justine).save()
Involvement(event=anniversaire_justine, profile=matthieu).save()
Involvement(event=anniversaire_justine, profile=jean).save()
Involvement(event=anniversaire_justine, profile=emma).save()
Involvement(event=anniversaire_justine, profile=justine).save()



