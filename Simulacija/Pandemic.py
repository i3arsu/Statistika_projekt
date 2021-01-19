import pygame
import pygame_gui
import numpy as np
import matplotlib.pyplot as plt
import time

WIDTH = 1100
HEIGHT= 800
UI_WIDTH = 400
border = 50

pygame.init()
sysFont = pygame.font.SysFont(None, 30)
display = pygame.display.set_mode((WIDTH+UI_WIDTH,HEIGHT))
manager = pygame_gui.UIManager((UI_WIDTH,HEIGHT))
elements = []

population = 100
infected = 2
infectionRadius = 30
infectionChance = 1
infectionDuration = 10

quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((10, HEIGHT-110), (100, 50)),
                                             text='Quit',
                                             manager=manager)
start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((UI_WIDTH-110, HEIGHT-110), (100, 50)),
                                             text='Start',
                                             manager=manager)
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
                                            value_range=(5,60),
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

class person:
    def __init__(self):
        self.pos = np.array((UI_WIDTH+WIDTH*np.random.random(),HEIGHT*np.random.random()))
        ang = np.random.random()*np.pi*2
        self.vel = np.array((np.cos(ang),np.sin(ang)))
        self.max_speed = 200
        self.max_steer = 50

        self.infected = False
        self.infection_duration = 0
        self.immune = False
        
    def update(self,delta):
        offset = np.array((0,0))
        offset[0] = absMax(max((UI_WIDTH+border) - self.pos[0],0),min((((UI_WIDTH+WIDTH) - self.pos[0]) - border),0))
        offset[1] = absMax(max(border - self.pos[1],0),min(((HEIGHT -self.pos[1]) - border),0))
        if offset.any():
            self.vel += offset/3
        else:
            steering = self.wander()
            steering *= self.max_steer/np.linalg.norm(steering)
            self.vel += steering
            self.vel *= self.max_speed/np.linalg.norm(self.vel)   
        self.pos += self.vel * delta   
    def wander(self):
        distance = 10
        initial_force = self.vel * distance/np.linalg.norm(self.vel)
        angle = np.random.random()*np.pi*2
        angle = np.array((np.cos(angle),np.sin(angle)))
        return initial_force + angle
    
    def draw(self):
        if self.infected:
            color = (255,20,20)
        elif not self.immune:
            color = (20,255,20)
        else:
            color = (100,100,100)
        pygame.draw.circle(display,color,self.pos,5)
        
def absMax(a,b):
    if abs(a) > abs(b):
        return a
    else:
        return b
    
simulation = False
setup = True

last = time.time_ns()
timer = 0

while setup:
    now = time.time_ns()
    delta = (now-last)/(1000**3)
    last = now
    
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                setup = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == quit_button:
                    setup = False
                elif event.ui_element == start_button:
                    simulation = True
                    setup = False
                    for e in elements:
                        e.disable()
                    
            if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
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

data = {
'sick' : [int(population*infected/100)],
'healthy' : [population-int(population*infected/100)],
'immune' : [0]
    }

healthy = [person() for i in range(population-int(population*infected/100))]
sick = [person() for i in range(int(population*infected/100))]
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
        manager.process_events(event)
                
    if timer > 1:
        timer = 0
        if len(sick) == 0:
            simulation = False
            break
        for s in sick:
            for h in healthy:
                if np.linalg.norm(s.pos - h.pos) < infectionRadius and np.random.random()*100 < infectionChance:
                    h.infected = True
                    healthy.remove(h)
                    sick.insert(0,h)
                        
            s.infection_duration += 1
            if s.infection_duration > infectionDuration:
                s.infected = False
                s.immune = True
                sick.remove(s)
                immune.append(s)
                
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

    pygame.draw.line(display,(0,0,0),(UI_WIDTH,0),(UI_WIDTH,HEIGHT),2)
    manager.draw_ui(display)
    pygame.display.update()
    

pygame.quit()

fig, ax = plt.subplots()
ax.stackplot(range(len(data['sick'])),data.values(),labels=data.keys(),colors=["#A31010","#1FA310","#A4A4A4"])
ax.legend(loc='upper left')
plt.show()


