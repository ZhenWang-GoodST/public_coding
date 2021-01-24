#!/usr/bin/python3 #

import os 

commands = []
#commands.append('python "paper collection.py" d:\desktop\github\icra2020-paper-list\ ICRA2020 planning ')
#commands.append('python "paper collection.py" d:\desktop\github\icra2020-paper-list\ ICRA2020 map ')
#commands.append('python "paper collection.py" d:\desktop\github\icra2020-paper-list\ ICRA2020 slam ')
#commands.append('python "paper collection.py" d:\desktop\github\icra2020-paper-list\ ICRA2020 cloud ')
#commands.append('python "paper collection.py" d:\desktop\github\icra2020-paper-list\ ICRA2020 robot ')
#commands.append('python "paper collection.py" d:\desktop\github\icra2020-paper-list\ ICRA2020 simultaneous ')
#commands.append('python "paper collection.py" d:\desktop\github\icra2020-paper-list\ ICRA2020 vehicle ')
#commands.append('python "paper collection.py" D:\desktop\github\icra2020-paper-list\ ICRA2020 learn ')

#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 planning ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 map ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 slam ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 cloud ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 robot ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 simultaneous ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 vehicle ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 learn ')

#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 planning ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 map ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 slam ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 cloud ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 robot ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 simultaneous ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 vehicle ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 learn ')

#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 planning ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 map ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 slam ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 cloud ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 robot ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 simultaneous ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 vehicle ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 learn ')

commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ iros2018 planning ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ iros2018 map ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ iros2018 slam ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ iros2018 cloud ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ iros2018 robot ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ iros2018 simultaneous ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ iros2018 vehicle ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ IROS2018 learn ')
                                                                                
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 planning ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 map ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 slam ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 cloud ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 robot ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 simultaneous ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 vehicle ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 learn ')

#commands.append('python "paper collection.py" D:\desktop\github\icra2020-paper-list\ ICRA2020 mult ')
#commands.append('python "paper collection.py" D:\desktop\github\ICRA2019-paper-list\ ICRA2019 mult ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2019-paper-list\ IROS2019 mult ')
#commands.append('python "paper collection.py" D:\desktop\github\IROS2020-paper-list\ IROS2020 mult ')
#commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\ICRA2018\ ICRA2018 mult ')
commands.append('python "paper collection.py" D:\desktop\github\\notebooks\paper_list\IROS2018\ IROS2018 mult ')


for command in commands:
    os.system(command)
    print()