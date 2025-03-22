import pygame as pg
import pop
import physics as px
from vectors import Vec
import random

# Global configuration
VIEW = True
S = 100  # pixels per meter

def scale(vec: Vec) -> tuple[int, int]:
    return (int(S * vec.x) + 300, 700 - int(S * vec.y))

def create_hill_surface(radius: int) -> pg.Surface:

    bg_color   = (60, 160, 80) 
    dark_color = (25,  90, 25) 

    hill_r_m = radius / S

    def slope_magnitude(d: float) -> float:
        if d <= 0:
            return 0
        if d < px.Hill_R / 2.0:
            return 0.25 * d
        elif d < px.Hill_R: 
            return 1.0 / d
        else:
            return 0.0


    slope_max = max(px.Hill_R / 8.0, 2.0 / px.Hill_R)


    def blend_color(c1, c2, t: float):
        return (
            int(c1[0] + t * (c2[0] - c1[0])),
            int(c1[1] + t * (c2[1] - c1[1])),
            int(c1[2] + t * (c2[2] - c1[2]))
        )

    surf = pg.Surface((radius * 2, radius * 2), pg.SRCALPHA)


    for r in range(radius, 0, -1):
        d_m = r / S  
        local_slope = slope_magnitude(d_m)
        
        if slope_max > 0:
            frac = local_slope / slope_max
        else:
            frac = 0.0
        

        color = blend_color(bg_color, dark_color, frac)

        pg.draw.circle(surf, color, (radius, radius), r)

    return surf

def setup(width: int, height: int) -> None:
    global screen, clock, hill_surf
    pg.init()
    screen = pg.display.set_mode((width, height))
    pg.display.set_caption("Mountain")
    clock = pg.time.Clock()


    hill_radius = int(S * px.Hill_R)

    hill_surf = create_hill_surface(hill_radius)

    globals()['hill_surf'] = hill_surf

def background() -> None:
    global hill_surf
    screen.fill((60, 160, 80))

    pg.draw.circle(screen, (0, 0, 0), scale(px.HOLE), int(S * 0.054))

    hill_rect = hill_surf.get_rect(center=scale(px.Hill))
    screen.blit(hill_surf, hill_rect)
    
    pg.draw.circle(screen, (120, 120, 120), scale(px.TRWALL), int(S * px.TRWALL_R))
    pg.draw.circle(screen, (120, 120, 120), scale(px.BLWALL), int(S * px.BLWALL_R))
    pg.draw.circle(screen, (120, 120, 120), scale(px.TLWALL), int(S * px.TLWALL_R))
    pg.draw.rect(screen, (120, 120, 120), (
        int(S * px.RWALL_T.x) + 300,
        700 - int(S * px.RWALL_T.y),
        int(0.1 * S),
        int(px.RWALL_length * S)
    ))
    pg.draw.rect(screen, (120, 120, 120), (
        int(S * px.LWALL_T.x) + 300,
        700 - int(S * px.LWALL_T.y),
        int(0.1 * S),
        int(px.LWALL_length * S)
    ))

def render() -> None:
    background() 
    for i in range(len(pop.population)):
        if isinstance(pop.population[i], pop.Family):
            for j in range(len(pop.population[i].familyMembers)):
                if pop.population[i].familyMembers[j].visible == True:
                    pg.draw.circle(screen, pop.population[i].familyMembers[j].color,scale(pop.population[i].familyMembers[j].pos), int(S * pop.population[i].familyMembers[j].r))
    clock.tick(60)
    pg.display.flip()

def check_interactions() -> None:
    global VIEW
    for event in pg.event.get():
        if event.type == pg.QUIT:
            VIEW = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_SPACE:
                px.run = True