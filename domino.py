#!/usr/bin/env python3
import requests
import os
import re
from bs4 import BeautifulSoup
url="http://xcgwv22shpmuzybdsnalqcufejtjlvqoukyybnjvrd3ppzsiti4anvyd.onion.ws/"
#url="http://anir0y.in" #Debug 
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
title = soup.title.text
if title == "Onion.Ws Tor2Web Gateway":
    print("""
       |\      _,,,---,,_
   /,`.-'`'    -.  ;-;;,_
  |,4-  ) )-,_..;\ (  `'-'
 '---''(_/--'  `-'\_)  Site is OffLine
 Author: @anir0y
    """)
else:
    print("""
          _.---.._             _.---...__
   .-'   /\   \          .'  /\     /
   `.   (  )   \        /   (  )   /
     `.  \/   .'\      /`.   \/  .'
       ``---''   )    (   ``---''
               .';.--.;`.
             .' /_...._\ `.
           .'   `.a  a.'   `.
          (        \/        )
           `.___..-'`-..___.'
              \          /
               `-.____.-'  Online
    Now You can search with phone/email
    """)
    fkid=input("Enter Your Phone or Email: ")

    headers={"content-type":"text"}
    res = requests.get('http://xcgwv22shpmuzybdsnalqcufejtjlvqoukyybnjvrd3ppzsiti4anvyd.onion.ws/api/search/'+fkid)
    f = open("db.log", "w")
    f.write(str(res.text))
    f.close()
    #runme="cat *log | jq | grep 'total_num_orders\|total_price_spent\|delivery_address\|order_time_gmt' | tee new.db"
    runme="cat *log | jq | grep 'total_num_orders\|total_price_spent' | tee new.db"
    #print(runme)
    os.system(runme)
