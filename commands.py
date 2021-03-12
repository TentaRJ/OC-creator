import time
import random
from main_ideas import *
from personality_ideas import *
from gimmick_ideas import *

class commands:
  def add():
    print('\n-----\nArguments:\n[Main, Personality, Gimmick]\n')
    print('Example: "Robot, Cheerful, Obsessive"' )
    i=str(input("What do you want to add?\nDon't forget to add ','\nType CANCEL to cancel!\nType NONE to not add an argument!\n\n"))
    stop=False
    if 'cancel' in i.lower():
      print("\nCanceling!\n")
      return
    i=i.split(", ")
    try:
      print(f'arguments:\n{i[0]} {i[1]} {i[2]}')
    except:
      print("\nError!\n")
      return
    if "none" in i[0].lower():
      stop=True
    main=open('main_ideas.py', 'r+')
    data=main.read()
    if i[0].lower() in data.lower():
      print("No duplicates! I found a duplicate in the main ideas!\n")
    else:
      main.close()
      main=open('main_ideas.py', 'w')
      if stop==False:
        main.write(f"{data[:-1]}, '{i[0]}']")
      if stop==True:
        main.write(data)
      main.close()
      print("\nAll done!\n")
    stop=False
    if "none" in i[1].lower():
      stop=True
    main=open('personality_ideas.py', 'r+')
    data=main.read()
    if i[1].lower() in data.lower():
      print("No duplicates! I found a duplicate in the Personality ideas!\n")
    else:
      main.close()
      main=open('personality_ideas.py', 'w')
      if stop==False:
        main.write(f"{data[:-1]}, '{i[1]}']")
      if stop==True:
        main.write(data)
      main.close()
      print("\nAll done!\n")
    stop=False
    if "none" in i[2].lower():
      stop=True
    main=open('gimmick_ideas.py', 'r+')
    data=main.read()
    if i[2].lower() in data.lower():
      print("No duplicates! I found a duplicate in the Gimmick ideas!\n")
    else:
      main.close()
      main=open('gimmick_ideas.py', 'w')
      if stop==False:
        main.write(f"{data[:-1]}, '{i[2]}']")
      if stop==True:
        main.write(data)
      main.close()
      print("\nAll done!\n")

  def view():
    print(f'\n-----\nVisible values are:\n1. main_ideas\n2. personality_ideas\n3. gimmick_ideas')
    try:
      i=input(f'What would you like to view? ')
    except:
      print("Uh oh! An error happened! Maybe you didn't put a number?")
    if i=='1':
      value="main_ideas.py"
    elif i=='2':
      value="personality_ideas.py"
    elif i=='3':
      value="gimmick_ideas.py"
    else:
      print("\nError! Wrong number!\n")
      return
    main=open(value, "r")
    data=main.read()
    if 'main_ideas=[' in data:
      start=12
    if 'personality_ideas=[' in data:
      start=19
    if 'gimmick_ideas=[' in data:
      start=15
    print(f'\nValues are:')
    data=data[start:-1]
    for x in data.split(', '):
      print(x)
    time.sleep(1)

  def gen():
    print(f'\n-----\nGenerating!')
    time.sleep(1.3)
    main=0
    for x in main_ideas:
      main=main+1
    per=0
    for x in personality_ideas:
      per=per+1
    gim=0
    for x in gimmick_ideas:
      gim=gim+1
    main=random.randint(0, main-1); per=random.randint(0, per-1); gim=random.randint(0, gim-1)
    print(main, per, gim)
    print(f'Main: {main_ideas[main]}\nPersonality: {personality_ideas[per]}\nGimmick: {gimmick_ideas[gim]}\n')

  def genmult():
    try:
      i=int(input("\n-----\nHow many ideas would you like to generate?\n(NUMBERS ONLY, MAX OF 10)\n"))
    except:
      print('\nError! Did you put a number in?\n')
      return
    print(f'\n-----\nGenerating!')
    time.sleep(1.3)
    if i >=11:
      print("No more than 10 at a time...")
      return
    while i>0:
      time.sleep(0.5)
      main=0
      for x in main_ideas:
        main=main+1
      per=0
      for x in personality_ideas:
        per=per+1
      gim=0
      for x in gimmick_ideas:
        gim=gim+1
      main=random.randint(0, main-1); per=random.randint(0, per-1); gim=random.randint(0, gim-1)
      print(main, per, gim)
      print(f'Main: {main_ideas[main]}\nPersonality: {personality_ideas[per]}\nGimmick: {gimmick_ideas[gim]}\n')
      i=i-1
    print("All done!")
    time.sleep(3)

  def option(i):
    if i=='1':
      commands.add()
    elif i=='2':
      commands.view()
    elif i=='3':
      commands.gen()
    elif i=='4':
      commands.genmult()
    else:
      print("\nError!\n")