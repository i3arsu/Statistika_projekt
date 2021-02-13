import pygame
import pygame_gui
import numpy as np
import matplotlib.pyplot as plt
import time
import csv

WIDTH = 1100
HEIGHT= 800
UI_WIDTH = 400
border = 50 # distance from edge where people start beeing repelled 

pygame.init()
display = pygame.display.set_mode((WIDTH+UI_WIDTH,HEIGHT))
manager = pygame_gui.UIManager((UI_WIDTH,HEIGHT))
elements = [] # too disable/enable elements

population = 200 # number of people in the simulation
infected = 2 # percantage of people infected at the start
infectionRadius = 30 # how close does a person need to be to a infetcted to get infected
infectionChance = 40 # chance that a person will get infected every tick
infectionDuration = 14 # duration of the infection in ticks
quarantine = False 
quarantineStart = 4 

## UI START ##

quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, HEIGHT-110), (100, 50)),
                                             text='Quit',
                                             manager=manager)
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((UI_WIDTH-110, HEIGHT-110), (100, 50)),
                                             text='Start',
                                             manager=manager)
stop_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((UI_WIDTH/2-50, HEIGHT-110), (100, 50)),
                                             text='Stop',
                                             manager=manager)
stop_button.disable()

elements.append(quit_button)
elements.append(start_button)

populationSlider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 25), (300, 20)),
                                            start_value=population,
                                            value_range=(2,500),
                                            manager=manager
                                            )
_pop = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((100,5),(200,20)),
                                              text = "population",
                                              manager=manager,
                                              parent_element = populationSlider
                                              )
populationLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((10,25),(40,20)),
                                              text = str(population),
                                              manager=manager,
                                              parent_element = populationSlider
                                              )
elements.append(populationSlider)
elements.append(_pop)
elements.append(populationLabel)

infectedSlider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 75), (300, 20)),
                                            start_value=infected,
                                            value_range=(1,99),
                                            manager=manager
                                            )
_inf = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((100,55),(200,20)),
                                              text = "infected",
                                              manager=manager,
                                              parent_element = infectedSlider
                                              )
infectedLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((10,75),(40,20)),
                                              text = str(infected),
                                              manager=manager,
                                              parent_element = infectedSlider
                                              )
elements.append(infectedSlider)
elements.append(_inf)
elements.append(infectedLabel)

infectedRadiusSlider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 125), (300, 20)),
                                            start_value=infectionRadius,
                                            value_range=(5,50),
                                            manager=manager
                                            )
_infRad = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((100,105),(200,20)),
                                              text = "infected Radius",
                                              manager=manager,
                                              parent_element = infectedRadiusSlider
                                              )
infectedRadiusLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((10,125),(40,20)),
                                              text = str(infectionRadius),
                                              manager=manager,
                                              parent_element = infectedRadiusSlider
                                              )
elements.append(infectedRadiusSlider)
elements.append(_infRad)
elements.append(infectedRadiusLabel)

infectionChanceSlider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 175), (300, 20)),
                                            start_value=infectionChance,
                                            value_range=(1,99),
                                            manager=manager
                                            )
_infCha = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((100,155),(200,20)),
                                              text = "infected Chance",
                                              manager=manager,
                                              parent_element = infectionChanceSlider
                                              )
infectionChanceLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((10,175),(40,20)),
                                              text = str(infectionChance),
                                              manager=manager,
                                              parent_element = infectionChanceSlider
                                              )
elements.append(infectionChanceSlider)
elements.append(_infCha)
elements.append(infectionChanceLabel)

infectionDurationSlider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50, 225), (300, 20)),
                                            start_value=infectionDuration,
                                            value_range=(1,60),
                                            manager=manager
                                            )
_infDur = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((100,205),(200,20)),
                                              text = "infected Duration",
                                              manager=manager,
                                              parent_element = infectionDurationSlider
                                              )
infectionDurationLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((10,225),(40,20)),
                                              text = str(infectionDuration),
                                              manager=manager,
                                              parent_element = infectionDurationSlider
                                              )
elements.append(infectionDurationSlider)
elements.append(_infDur)
elements.append(infectionDurationLabel)

quarantine_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((190, 275), (20, 20)),
                                                 text = " ",
                                             manager=manager)
_quar = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((100,250),(200,20)),
                                              text = "quarantine",
                                              manager=manager,
                                              parent_element = quarantine_button
                                              )
quarantineLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((145,275),(40,20)),
                                              text = str(quarantine),
                                              manager=manager,
                                              parent_element = quarantine_button
                                              )
elements.append(quarantine_button)
elements.append(_quar)
elements.append(quarantineLabel)


quarantineStartSlider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((50,325), (300, 20)),
                                            start_value=quarantineStart,
                                            value_range=(1,59),
                                            manager=manager
                                            )
_quarS = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((100,305),(200,20)),
                                              text = "quarantine Start",
                                              manager=manager,
                                              parent_element = infectionDurationSlider
                                              )
quarantineStartLabel = pygame_gui.elements.UILabel(relative_rect = pygame.Rect((10,325),(40,20)),
                                              text = str(quarantineStart),
                                              manager=manager,
                                              parent_element = infectionDurationSlider
                                              )

elements.append(quarantineStartSlider)
elements.append(_quarS)
elements.append(quarantineStartLabel)

## UI END ##


class person:
    def __init__(self):
        self.pos = np.array((border+UI_WIDTH+(WIDTH-border)*np.random.random(),border+(HEIGHT-border)*np.random.random()))
        ang = np.random.random()*np.pi*2
        self.vel = np.array((np.cos(ang),np.sin(ang)))
        self.max_speed = 200
        self.max_steer = 50
        
        self.quarantine = False
        self.infected = False
        self.infection_duration = 0
        self.immune = False
        
    def update(self,delta):
        if self.quarantine:
            offset = (np.array((UI_WIDTH/2,HEIGHT-260))-self.pos)
            if np.linalg.norm(offset) < 90:
                offset = np.array((0,0))
        else:
            offset = np.array((0,0))
            offset[0] = absMax(max((UI_WIDTH+border) - self.pos[0],0),min((((UI_WIDTH+WIDTH) - self.pos[0]) - border),0))
            offset[1] = absMax(max(border - self.pos[1],0),min(((HEIGHT -self.pos[1]) - border),0))
        
        if offset.any(): # repel if near edge
            self.vel += offset/3
        else:
            steering = self.wander()
            steering *= self.max_steer/np.linalg.norm(steering) # limit
            self.vel += steering
            self.vel *= self.max_speed/np.linalg.norm(self.vel) # limit
        self.pos += self.vel * delta
        
    def wander(self):
        distance = 200 # distance to circle
        initial_force = self.vel * distance/np.linalg.norm(self.vel) # vector to circle center
        angle = np.random.random()*np.pi*2 # random angle
        angle = np.array((np.cos(angle),np.sin(angle)))*50 # displacement vector
        return initial_force + angle # wander vector
    
    def draw(self):
        if self.infected:
            color = (255,20,20) # red = infected
        elif not self.immune:
            color = (20,255,20) # green = healthy
        else:
            color = (100,100,100)# gray = immune
        pygame.draw.circle(display,color,self.pos,5)
        
def absMax(a,b):
    if abs(a) > abs(b):
        return a
    else:
        return b

def enableUI(b):
    if not b: # False = disable
        stop_button.enable()
        for e in elements:
            e.disable()
    else:
        stop_button.disable()
        for e in elements:
            e.enable()
            
simulation = False
setup = True

last = time.time_ns()
timer = 0
while setup or simulation:
    while setup:
        now = time.time_ns()
        delta = (now-last)/(1000**3)
        last = now
    
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    setup = False
            elif event.type == pygame.QUIT:
                setup = False
            elif event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == quit_button:
                        setup = False
                    elif event.ui_element == start_button:
                        simulation = True
                        setup = False
                        enableUI(False)
                    elif event.ui_element == quarantine_button:
                        quarantine = not quarantine
                        quarantine_button.set_text("X" if quarantine else " ")
                        quarantineLabel.set_text(str(quarantine))
                    
                elif event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == populationSlider:
                        populationLabel.set_text(str(event.value))              
                    elif event.ui_element == infectedSlider:
                        infectedLabel.set_text(str(event.value))
                    elif event.ui_element == infectedRadiusSlider:
                        infectedRadiusLabel.set_text(str(event.value))
                    elif event.ui_element == infectionChanceSlider:
                        infectionChanceLabel.set_text(str(event.value))
                    elif event.ui_element == infectionDurationSlider:
                        infectionDurationLabel.set_text(str(event.value))
                    elif event.ui_element == quarantineStartSlider:
                        quarantineStartLabel.set_text(str(event.value))
            manager.process_events(event)

        manager.update(delta)

        display.fill((51,51,51))
    
        manager.draw_ui(display)
        pygame.draw.line(display,(0,0,0),(UI_WIDTH,0),(UI_WIDTH,HEIGHT),2)
        pygame.display.update()

    population = int(populationLabel.text)
    infected = int(infectedLabel.text)
    infectionRadius = int(infectedRadiusLabel.text)
    infectionChance = int(infectionChanceLabel.text)
    infectionDuration = int(infectionDurationLabel.text)
    #quarantine 
    quarantineStart = int(quarantineStartLabel.text)
    
    data = {
    'sick' : [max(int(population*infected/100),1)],
    'healthy' : [population-max(int(population*infected/100),1)],
    'immune' : [0]
        }

    total_cases = [max(int(population*infected/100),1)]
    
    healthy = [person() for i in range(population-max(int(population*infected/100),1))]
    sick = [person() for i in range(max(int(population*infected/100),1))]
    immune = []
    for s in sick:
        s.infected = True
    
    while simulation:

        now = time.time_ns()
        delta = (now-last)/(1000**3)
        last = now
        timer += delta
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    simulation = False
            if event.type == pygame.QUIT:
                simulation = False
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == stop_button:
                        simulation = False
                        setup = True
                        enableUI(True)
            manager.process_events(event)
                    
        if timer > 1: # a tick = 1 second
            to_remove = []
            to_add = []
            timer = 0
            
            if len(sick) == 0:
                simulation = False
                break
            
            for s in sick:
                s.infection_duration += 1
                if s.quarantine:
                    if s.infection_duration > infectionDuration:
                        s.infected = False
                        s.immune = True
                        to_remove.append(s)                   
                    continue
                for h in healthy:
                    if np.linalg.norm(s.pos - h.pos) < infectionRadius and np.random.random()*100 < infectionChance and not h.infected:
                        h.infected = True
                        to_add.append(h)
                            
                if quarantine and s.infection_duration > quarantineStart and not s.quarantine:
                    s.quarantine = True
                    s.pos = (UI_WIDTH/2,HEIGHT-260)
                    s.max_speed = 100
                if s.infection_duration > infectionDuration:
                    s.infected = False
                    s.immune = True
                    to_remove.append(s)
                    
            total_cases.append(total_cases[-1]+len(to_add))    
            for s in to_remove:
                immune.append(s)
                sick.remove(s)
            for h in to_add:
                sick.append(h)
                healthy.remove(h)
                
            data['sick'].append(len(sick))
            data['healthy'].append(len(healthy)) 
            data['immune'].append(len(immune))
                
        display.fill((51,51,51))

        manager.update(delta)       
        
        for s in sick:  
            s.update(delta)
            s.draw()
            
        for h in healthy:  
            h.update(delta)
            h.draw()
            
        for i in immune:
            i.update(delta)
            i.draw()
            
        if quarantine:
            pygame.draw.circle(display,(0,0,0),(UI_WIDTH/2,HEIGHT-260),100,2)
            
        pygame.draw.line(display,(0,0,0),(UI_WIDTH,0),(UI_WIDTH,HEIGHT),2)
        manager.draw_ui(display)
        pygame.display.update()
    

pygame.quit()

fig, ax = plt.subplots()
ax.stackplot(range(len(data['sick'])),data.values(),labels=data.keys(),colors=["#A31010","#1FA310","#A4A4A4"])
ax.legend(loc='upper left')
plt.show()

with open('simulation.csv',mode='w', newline='') as cf:
    wr = csv.writer(cf)
    elements = list(data.keys())
    elements.append('total_cases')
    elements.append('population')
    wr.writerow(elements)
    for i in range(len(data['sick'])):
        wr.writerow([data['sick'][i],data['healthy'][i],data['immune'][i],total_cases[i],population])
