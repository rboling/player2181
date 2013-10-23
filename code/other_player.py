import game_interface
import random
import time
import pickle

def get_move(view):
  
  eat=False
  
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
      else:
      #make it return nut
          eat = True
      #game_interface.curses_debug(1, str())
      #print "top \n"
      #print  top   
      #print "\n"
  if view.GetPlantInfo()==game_interface.STATUS_POISONOUS_PLANT:
      game_interface.curses_debug(2, "POISON") 
      ratio.write("POISON \n")
  if view.GetPlantInfo()==game_interface.STATUS_NUTRITIOUS_PLANT:
      game_interface.curses_debug(2, "HAPPINESS") 
      ratio.write("NUTRITIOUS \n")
      
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
  return (random.randint(0, 4), eat)



















