import game_interface
import random
import time
import pickle
import PyML
import os
dir = os.path.dirname(os.path.abspath(__file__))
svm_ten = open(os.path.join(dir, 'the_svm_ten'), "r")
svm_nine = open(os.path.join(dir, 'the_svm_nine'), "r")
svm_eight = open(os.path.join(dir, 'the_svm_eight'), "r")
svm_seven = open(os.path.join(dir, 'the_svm_seven'), "r")
svm_six = open(os.path.join(dir, 'the_svm_six'), "r")
svm_five = open(os.path.join(dir, 'the_svm_five'), "r")
svm_four = open(os.path.join(dir, 'the_svm_four'), "r")
svm_two = open(os.path.join(dir, 'the_svm_two'), "r")
training_ninek = open(os.path.join(dir, 'training-9k.txt'), "r")
test_onek = open(os.path.join(dir, 'test-1k.txt'), "r")






THE_CURRENT_VIEW = None
THE_PREVIOUS_VIEW = None
THE_DATA = PyML.VectorDataSet('player/training-9k.txt', labelsColumn = -1)
THE_DATA_TWO = PyML.VectorDataSet('player/test-1k.txt', labelsColumn = -1)

THE_NEXT_DIRECTION = game_interface.UP

VICTORY_NUT = 0
CURRENT_LIFE = None
PREVIOUS_LIFE = None

THE_SVM = PyML.SVM()
THE_SVM_TWO = PyML.SVM()
THE_SVM_THREE = PyML.SVM()
THE_SVM_FOUR = PyML.SVM()
THE_SVM_FIVE = PyML.SVM()
THE_SVM_SIX = PyML.SVM()
THE_SVM_SEVEN = PyML.SVM()
THE_SVM_EIGHT = PyML.SVM()

THE_SVM_THREE.load(svm_five, THE_DATA)
THE_SVM_FOUR.load(svm_six, THE_DATA)
THE_SVM_FIVE.load(svm_seven, THE_DATA_TWO)
THE_SVM_SIX.load(svm_eight, THE_DATA)
THE_SVM_SEVEN.load(svm_nine, THE_DATA)
THE_SVM_EIGHT.load(svm_ten, THE_DATA)
THE_SVM_TWO.load(svm_four, THE_DATA)
THE_SVM.load(svm_two, THE_DATA)
LIST_OF_RANDOM_MOVES = []

def get_positive_life_change(current_view, previous_view):
  if(current_view.GetLife() - previous_view.GetLife() > 0):
    return True
  else:
    return False

def get_negative_life_change(current_view, previous_view):
  if(current_view.GetLife() - previous_view.GetLife() < 0):
    return True
  else:
    return False




def get_move(view):
  global THE_CURRENT_VIEW
  global THE_PREVIOUS_VIEW
  global THE_DATA
  global THE_SVM
  global LIST_OF_RANDOM_MOVES
  global THE_NEXT_DIRECTION
  global VICTORY_NUT
  global PREVIOUS_LIFE
  global CURRENT_LIFE
  THE_CURRENT_VIEW = view
  eat=False
  if view.GetRound()==1 or view.GetRound()==0 or view.GetRound() == 2:
      view.data_list=[]
  
  CURRENT_LIFE = view.GetLife()


  
  #the output to determine how good this method is
  ratio=open("ratio.txt","a")
  
  
  #check if the plant you just ate was Nut or Poi and record it
  """
  if view.GetPlantInfo()==game_interface.STATUS_POISONOUS_PLANT:
      game_interface.curses_debug(2, "POISON") 
      ratio.write("POISON \n")
      poi_lis=[]
      img=[]
      for i in xrange(11):
          img_temp=view.GetImage()
          poi_lis.append(img_temp)
          #trying to even out the noise. Will make a new data point which only has the 
          #majority value out of 11 tries in each spot
      for a in range(36):
          zero=0
          one=0
          for b in range(11):
              if poi_lis[b][a]==0:
                  zero+=1
              else:
                  one+=1
          #builds the new list
          if zero>one:
              img.append(0)
          else:
              img.append(1)
      
      text_file=open("PoisonK_Neigh.txt","a")
      text_file.write(str(img)+"\n")
      #pickle.dump(img,text_file)
      #text_file.write("\n")
      text_file.close()
  
  if view.GetPlantInfo()==game_interface.STATUS_NUTRITIOUS_PLANT:
      game_interface.curses_debug(2, "HAPPINESS") 
      ratio.write("NUTRITIOUS \n")
      nut_lis=[]
      img=[]
      for i in xrange(11):
          img_temp=view.GetImage()
          nut_lis.append(img_temp)
          #trying to even out the noise. Will make a new data point which only has the 
          #majority value out of 11 tries in each spot
      for a in range(36):
          zero=0
          one=0
          for b in range(11):
              if nut_lis[b][a]==0:
                  zero+=1
              else:
                  one+=1
          #builds the new list
          if zero>one:
              img.append(0)
          else:
              img.append(1)
      
      text_file=open("NutritiousK_Neigh.txt","a")
      text_file.write(str(img)+"\n")
      #pickle.dump(img,text_file)
      #text_file.write("\n")
      text_file.close()
   
  
  """
      
  list_to_use = []

  current = list(view.GetImage())


  if view.GetPlantInfo()==game_interface.STATUS_POISONOUS_PLANT and len(current) > 0:
      view.data_list.append([current,"poi"])
  if view.GetPlantInfo()==game_interface.STATUS_NUTRITIOUS_PLANT and len(current) > 0:
      view.data_list.append([current,"nut"])
  
  #original svm
  
  if len(current) > 0 and current != None:
    list_to_use.append(current)
    data_to_use = PyML.VectorDataSet(list_to_use)
    testing_value = THE_SVM.test(data_to_use) 
    testing_value_two = THE_SVM_TWO.test(data_to_use)
    testing_value_three = THE_SVM_THREE.test(data_to_use)
    testing_value_four = THE_SVM_FOUR.test(data_to_use)
    testing_value_five = THE_SVM_FIVE.test(data_to_use)
    testing_value_six = THE_SVM_SIX.test(data_to_use)
    testing_value_seven = THE_SVM_SEVEN.test(data_to_use)
    testing_value_eight = THE_SVM_EIGHT.test(data_to_use)



    #testing_value_three = THE_SVM_.test(data_to_use)   
    if testing_value_eight.getPredictedClass()[0] == 1 and testing_value_seven.getPredictedClass()[0] == 1 and testing_value_six.getPredictedClass()[0] == 1 and testing_value.getPredictedClass()[0] == 1 and testing_value_five.getPredictedClass()[0] == 1 and testing_value_two.getPredictedClass()[0] == 1 and testing_value_three.getPredictedClass()[0] == 1 and testing_value_four.getPredictedClass()[0] == 1:
    #    game_interface.curses_debug(2,"NUTRITIOUS")
      #VICTORY_NUT = 1
      eat = True

    else:
    #  game_interface.curses_debug(2,"POISON")
      eat = False 
  else:
    eat = False
    #game_interface.curses_debug(2, "NO INFO")
      
  #comments end here
  """
   #data_list is the conglomerate of both pois and nut. Keeps the label on it   
   #current is what we are testing now
  text_nut=open("NutritiousK_Neigh.txt","rb").read().splitlines()
  text_pois=open("PoisonK_neigh.txt","rb").read().splitlines()
  
  #splits up the tuples into usable chunks and lumps on the label
  data_list=[]
  
  
  for val in range(len(text_nut)):
      data_list.append([map(int, text_nut[val][1:-1].split(",")),"nut"])
  for val in range(len(text_pois)):
      data_list.append([map(int, text_pois[val][1:-1].split(",")),"poi"])    
      
  
  
  # Modified k nearest neighbor code. Cannot do Euc dist as too many attr, but can
  # do other things
  #gets the image of the plant
  
  neighbors=[]
  k=11
  if view.GetPlantInfo() == game_interface.STATUS_UNKNOWN_PLANT:
      current=list(view.GetImage())
      for b in range(len(data_list)):
          neighbors.append([0,b])
  #neighbors=[0, current place]
  
      for a in range(len(data_list)):
          for attr in range(36):
              if current[attr]==data_list[a][0][attr]:
                  neighbors[a][0]=neighbors[a][0]+1
   
      #finding the k values with the highest values in neighbor
      sorted_list=sorted(neighbors,key=lambda x:int(x[0]))
      again=sorted_list.reverse()
      top=[]
      
      for a in range(k):
          top.append(data_list[sorted_list[a][1]][1])
          print top
      
     
            
      
      #find majority label of those in top
      poi_counter=0 
      for a in range(k):
          if top[a]=="poi":
              poi_counter+=1
      if poi_counter > k/2:
          eat=False
       #make it return poi
      elif len(current) > 0 and current != None:
        if testing_value.getPredictedClass()[0] == 1:
          eat = True
      #make it return nut
          #eat = True
      else:
          eat = False

    """
    #eat false

      #game_interface.curses_debug(1, str())
      #print "top \n"
      #print  top   
      #print "\n"
  #if view.GetPlantInfo()==game_interface.STATUS_POISONOUS_PLANT:
  #    game_interface.curses_debug(2, "POISON") 
  #    ratio.write("POISON \n")
  #if view.GetPlantInfo()==game_interface.STATUS_NUTRITIOUS_PLANT:
  #    game_interface.curses_debug(2, "HAPPINESS") 
  #    ratio.write("NUTRITIOUS \n") 
  #comments start here
      
  """
   #noisy data building
  if view.GetPlantInfo()==game_interface.STATUS_POISONOUS_PLANT:
       noisy_poi=open("noisy_poi.txt","a")
       for i in xrange(10):
           img=list(view.GetImage())
           noisy_poi.write(str(img) + "\n")
           
  if view.GetPlantInfo()==game_interface.STATUS_NUTRITIOUS_PLANT:
       noisy_nut=open("noisy_nut.txt","a")
       for i in xrange(10):
           img=list(view.GetImage())
           noisy_nut.write(str(img) + "\n")
           
  """ 
  
  #base code
   #Choose a random direction.
   #If there is a plant in this location, then try and eat it.
  #hasPlant = view.GetPlantInfo() == game_interface.STATUS_UNKNOWN_PLANT
   #Choose a random direction
  #if hasPlant:
    #game_interface.curses_debug(1, "yum") 
    
    #for i in xrange(5):
     # print view.GetImage()
  time.sleep(0.1)

  #the_direction = random.randint(0,4)

  #comments begin
  #the_direction = random.randint(0,4)
  #game_interface.curses_debug(2, "da shiz")
  #if CURRENT_LIFE != None and PREVIOUS_LIFE != None:
  #  if CURRENT_LIFE - PREVIOUS_LIFE > 0:
  #    game_interface.curses_debug(2, "hell yeah")
  #  elif CURRENT_LIFE - PREVIOUS_LIFE < -1:
  #    game_interface.curses_debug(2, "mommy winter")
    #else:
    #  game_interface.curses_debug(2, "free bird")



  """  
  if view.GetRound() == 0 or view.GetRound() == 1 or view.GetRound() == 2:
    the_direction = random.randint(0,4)
  else:
    if CURRENT_LIFE - PREVIOUS_LIFE > 0:
      the_direction = random.randint(0,4)
      game_interface.curses_debug(2, "hurts so good")
      VICTORY_NUT = 1
      #for i in range(4):
      #  LIST_OF_RANDOM_MOVES.append(1)
    elif CURRENT_LIFE - PREVIOUS_LIFE < -1:
      VICTORY_NUT = 0
      game_interface.curses_debug(2, "mommy winter")
      the_direction = THE_NEXT_DIRECTION
    else:
      if VICTORY_NUT == 1:
        the_direction = random.randint(0,4)
      else:
        the_direction = THE_NEXT_DIRECTION
  if THE_NEXT_DIRECTION == game_interface.UP:
    THE_NEXT_DIRECTION = game_interface.LEFT
  elif THE_NEXT_DIRECTION == game_interface.LEFT:
    THE_NEXT_DIRECTION = game_interface.UP
  """
  #comments end
  #making game centric comparisons 
  """
  if view.GetPlantInfo()==game_interface.STATUS_POISONOUS_PLANT:
      data_coord_poi=open("game_poi_20.txt","a")
      #img=list(view.GetImage())
      X=view.GetXPos()
      Y=view.GetYPos()
      data_coord_poi.write(str([X,Y])+"\n")
  if view.GetPlantInfo()==game_interface.STATUS_NUTRITIOUS_PLANT:
      data_coord_nut=open("game_nut_20.txt","a")
      #img=list(view.GetImage())
      X=view.GetXPos()
      Y=view.GetYPos()
      data_coord_nut.write(str([X,Y])+"\n")
  """
 
  if random.uniform(0,1)>0.5 and len(view.data_list)>4 and len(current) > 0:
    neighbors=[]
    k=5
    if view.GetPlantInfo() == game_interface.STATUS_UNKNOWN_PLANT:
      current=list(view.GetImage())
      for b in range(len(view.data_list)):
        neighbors.append([0,b])
    #neighbors=[0, current place]

      for a in range(len(view.data_list)):
        for attr in range(36):
          if len(current) > 35:
            if current[attr]==view.data_list[a][0][attr]:
              neighbors[a][0]=neighbors[a][0]+1

      #finding the k values with the highest values in neighbor
      sorted_list=sorted(neighbors,key=lambda x:int(x[0]))
      again=sorted_list.reverse()
      top=[]

      for a in range(k):
        top.append(view.data_list[sorted_list[a][1]][1])
        print top


    

      #find majority label of those in top
      poi_counter=0 
      for a in range(k):
        if top[a]=="poi":
          poi_counter+=1
      if poi_counter > k/2:
        eat=False
       #make it return poi
      elif len(current) > 0 and current != None:
        if testing_value_eight.getPredictedClass()[0] == 1 and testing_value_seven.getPredictedClass()[0] == 1 and testing_value_six.getPredictedClass()[0] == 1 and testing_value.getPredictedClass()[0] == 1 and testing_value_two.getPredictedClass()[0] == 1 and testing_value_three.getPredictedClass()[0] == 1 and testing_value_four.getPredictedClass()[0] == 1 and testing_value_five.getPredictedClass()[0] == 1:
          eat = True

      #make it return nut
        #eat = True
      else:
        eat = False



  the_direction = random.randint(0,4)
  PREVIOUS_LIFE = view.GetLife()
  return (the_direction, eat)



















