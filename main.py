import time
import json
from commands import *
from main_ideas import *
from personality_ideas import *
from gimmick_ideas import *

active = True
actions = ['Add\nAdd an idea!\n','View\nView ideas!\n', 'Generate\nGenerate a character idea!\n','Generate Multiple Ideas\nGenerate multiple character ideas!']

print(f"Hey there!\nThis an OC character generator made by *TentaRJ*!\nI love you all!\n💖\n")
time.sleep(2)

while active==True:
  time.sleep(1)
  main=0
  for x in main_ideas:
    main=main+1
  per=0
  for x in personality_ideas:
    per=per+1
  gim=0
  for x in gimmick_ideas:
    gim=gim+1
  print(f'Availabe:\n{main} main ideas\n{per} personality ideas\n{gim} gimmick ideas\n\nActions available:\n')
  y=0
  for x in actions:
    y=y+1
    print(f'☑ {y}: {x}')
  try:
    i=input(f'Action: ')
  except:
    i=''
  commands.option(i)