#!/usr/bin/python
# -*-coding=utf-8-*-
import wykop , sched , time
from time import sleep,strftime,localtime
from pync import Notifier



class wypok:
    def __init__(self):
        self.api = wykop.WykopAPI("klucz","sekret")
        self._auth()
        s=sched.scheduler(time.time,time.sleep)

        def check_for_messages(sc):
            try:
                print "Odświeżam wykop o "+strftime("%H:%M:%S",localtime())
                get_from_wypok = self.api.request("mywykop","notifications","JSON")
                for key in get_from_wypok:
                    if key.new ==True:
                        if key.type == "entry_comment_directed":
                            print(key.author+" dodal komentarz")
                            Notifier.notify(key.author+"\ndodal komentarz.", title="Wykop.pl",appIcon="sciezka/do/foleru/Powiadomienia-z-Wykop.pl-dla-OSX-master/images.jpg",sound="default",open=key.url)
                        elif key.type=="pm":
                            print("PW od "+key.author)
                            Notifier.notify("PW od\n"+key.author, title="Wykop.pl",appIcon="sciezka/do/foleru/Powiadomienia-z-Wykop.pl-dla-OSX-master/images.jpg",sound="default",open=key.url)
                        elif key.type=="observe":
                            print("#stalkujo !"+key.author)
                            Notifier.notify("#stalkujo !"+key.author, title="Wykop.pl",appIcon="sciezka/do/foleru/Powiadomienia-z-Wykop.pl-dla-OSX-master/images.jpg",sound="default",open=key.url)

            except:
                self._auth()
            sc.enter(300, 1, check_for_messages, (sc,))
        s.enter(1,1,check_for_messages,(s,))
        s.run()

    def _auth(self):
        self.api.authenticate("nick", "klucz_połączenia")
        print "Autoryzacja poprawna"





wykop = wypok()

