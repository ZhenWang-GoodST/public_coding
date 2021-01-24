#!/usr/bin/python3 #

import os 

commands = []
commands.append('python "collecte_paper_from_name_citation_with_key_words.py" D:\\desktop\\github\\notebooks\\paper_list\\ICRA2018-citations-abstract  ICRA2018-citations-abstract ICRA2018-name-pure-citations-abstract ')
commands.append('python "collecte_paper_from_name_citation_with_key_words.py" D:\\desktop\\github\\notebooks\\paper_list\\ICRA2019-citations-abstract  ICRA2019-citations-abstract ICRA2019-name-pure-citations-abstract ')
commands.append('python "collecte_paper_from_name_citation_with_key_words.py" D:\\desktop\\github\\notebooks\\paper_list\\ICRA2020-citations-abstract  ICRA2020-citations-abstract ICRA2020-name-pure-citations-abstract ')
commands.append('python "collecte_paper_from_name_citation_with_key_words.py" D:\\desktop\\github\\notebooks\\paper_list\\IROS2018-citations-abstract  IROS2018-citations-abstract IROS2018-name-pure-citations-abstract ')

for command in commands:
    os.system(command)
    print()