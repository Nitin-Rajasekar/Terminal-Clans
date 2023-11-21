import colorama
import time


from colorama import Fore, Back, Style


from src.input_starter import input_to
from src.input_starter import Get
from src.sup_classes import Person
from src.sup_classes import Building

getch = Get()
n = 50
m = 50

status = 1

rows, cols = (n, m)

z_start = 0
x_start = 0
c_start = 0

v_start = 0
b_start = 0
n_start = 0

k_start = 0
l_start = 0

k_r = 2
k_c = 10

q_r = 28
q_c = 10


x_c = q_c+8
x_r = q_r-8

e_c = q_c+16
e_r = q_r-16

bz_r = 5
bz_c = 20

bx_r = 20
bx_c = 5

arr = [[' ' for i in range(cols)] for j in range(rows)]


bc_r = 30
bc_c = 30

av_r = 25
av_c = 31

ab_r = 10
ab_c = 40

an_r = 45
an_c = 35

bk_r = 5  # balloon
bk_c = 30

bl_r = 40
bl_c = 5


t_r = 5
t_c = 5

h_r = [15, 35, 40, 40, 30]
h_c = [15, 35, 20, 10, 20]

z_r = [15, 40]
z_c = [40, 35]


bbrn_r = [bz_r, bx_r, bc_r]
bbrn_c = [bz_c, bx_c, bc_c]

arch_r = [av_r, ab_r, an_r]
arch_c = [av_c, ab_c, an_c]

ball_r = [bk_r, bl_r]
ball_c = [bk_c, bl_c]


z_attack = [0, 0]

can_wiz_d=0

w_r = []
w_c = []


for i in range(4):
    w_r.append(33)

for i in range(4):
    w_c.append(34+i)

for i in range(4):
    w_r.append(38)

for i in range(4):
    w_c.append(34+i)

for i in range(4):
    w_r.append(34+i)

for i in range(4):
    w_c.append(34)

for i in range(4):
    w_r.append(34+i)

for i in range(4):
    w_c.append(37)

##

for i in range(4):
    w_r.append(13)

for i in range(4):
    w_c.append(14+i)

for i in range(4):
    w_r.append(18)

for i in range(4):
    w_c.append(14+i)

for i in range(4):
    w_r.append(14+i)

for i in range(4):
    w_c.append(14)

for i in range(4):
    w_r.append(14+i)

for i in range(4):
    w_c.append(17)

#

for i in range(4):
    w_r.append(38)

for i in range(4):
    w_c.append(19+i)

for i in range(4):
    w_r.append(43)

for i in range(4):
    w_c.append(19+i)

for i in range(4):
    w_r.append(39+i)

for i in range(4):
    w_c.append(19)

for i in range(4):
    w_r.append(39+i)

for i in range(4):
    w_c.append(22)

#

for i in range(4):
    w_r.append(38)

for i in range(4):
    w_c.append(9+i)

for i in range(4):
    w_r.append(43)

for i in range(4):
    w_c.append(9+i)

for i in range(4):
    w_r.append(39+i)

for i in range(4):
    w_c.append(9)

for i in range(4):
    w_r.append(39+i)

for i in range(4):
    w_c.append(12)

#

for i in range(4):
    w_r.append(28)

for i in range(4):
    w_c.append(19+i)

for i in range(4):
    w_r.append(33)

for i in range(4):
    w_c.append(19+i)

for i in range(4):
    w_r.append(29+i)

for i in range(4):
    w_c.append(19)

for i in range(4):
    w_r.append(29+i)

for i in range(4):
    w_c.append(22)


p_r = []
p_c = []


######

for i in range(50):
    p_r.append(0)

for i in range(50):
    p_r.append(49)

for i in range(50):
    p_r.append(i)

for i in range(50):
    p_r.append(i)


for i in range(50):
    p_c.append(i)

for i in range(50):
    p_c.append(i)

for i in range(50):
    p_c.append(0)

for i in range(50):
    p_c.append(49)


c1_r = 35
c1_c = 10

c2_r = 45
c2_c = 40

cann_r = [c1_r, c2_r]
cann_c = [c1_c, c2_c]

bull_1_r = c1_r
bull_1_c = c1_c

bull_2_r = c2_r
bull_2_c = c2_c


# class definitons


class King:

    health = 300
    beg_health = 300
    damage = 2
    movement_speed = 1
    alive = 1

    # A sample method
    def fun(self):
        if k_man.alive == 1:
            global k_c
            global k_r
            input = input_to(getch)
            if(k_c) > m-3:
                arr[k_r][k_c] = ' '
                k_c = 0
            if(k_r) > n-3:
                arr[k_r][k_c] = ' '
                k_r = 0
            if input == "d":
                arr[k_r][k_c] = ' '
                k_c = k_c+k_man.movement_speed
                arr[k_r][k_c] = Fore.WHITE+'K'

            if input == "a":
                arr[k_r][k_c] = ' '
                k_c = k_c-k_man.movement_speed
                arr[k_r][k_c] = Fore.WHITE+'K'

            if input == "s":
                arr[k_r][k_c] = ' '
                k_r = k_r+k_man.movement_speed
                arr[k_r][k_c] = Fore.WHITE+'K'

            if input == "w":
                arr[k_r][k_c] = ' '
                k_r = k_r-k_man.movement_speed
                arr[k_r][k_c] = Fore.WHITE+'K'

            if input == "k":

                for t in range(5):
                    if abs(h_r[t]-k_r) <= 4 and abs(h_c[t]-k_c) <= 4:
                        hut_list[t].health = hut_list[t].health-k_man.damage

                for t in range(2):
                    if abs(z_r[t]-k_r) <= 4 and abs(z_c[t]-k_c) <= 4:
                        wizard_list[t].health = wizard_list[t].health-k_man.damage

                if abs(t_r-k_r) <= 4 and abs(t-k_c) <= 4:
                    hall.health = hall.health-k_man.damage

            if input == "i":
                for a in range(5):
                    for i in range(h_r[a], h_r[a]+hut_list[a].height):
                        for j in range(h_c[a], h_c[a]+hut_list[a].width):
                            if (i < k_r+6 and i > k_r-6) and (j < k_c+6 and j > k_c-6):
                                hut_list[a].health = hut_list[a].health - \
                                    k_man.damage

                for a in range(2):
                    for i in range(z_r[a], z_r[a]+wizard_list[a].height):
                        for j in range(z_c[a], z_c[a]+wizard_list[a].width):
                            if (i < k_r+6 and i > k_r-6) and (j < k_c+6 and j > k_c-6):
                                wizard_list[a].health = wizard_list[a].health - \
                                    k_man.damage


                for i in range(t_r, t_r+hall.height):
                    for j in range(t_c, t_c+hall.width):
                        if (i < k_r+6 and i > k_r-6) and (j < k_c+6 and j > k_c-6):
                            hall.health = hall.health - k_man.damage

            if k_man.health <= 0:
                arr[k_r][k_c] = ' '
                k_man.alive = 0

                # if goal_zh==6:
                # hall.health=hall.health-1
                # else:
                #  hut_list[goal_zh].health=hut_list[goal_zh].health-1


class Queen:

    health = 300
    beg_health = 300
    damage = 2
    movement_speed = 1
    alive = 1
    use_second=0
    curr_second=0
    flag=0
    
    

    # A sample method

    def fun(self):


        if q_man.alive == 1:
            global q_c
            global q_r
            global x_c
            global x_r
            global e_c
            global e_r
            input = input_to(getch)

            if(q_c) > m-3:
                arr[q_r][q_c] = ' '
                q_c = 0
            if(q_r) > n-3:
                arr[q_r][q_c] = ' '
                q_r = 0

            if input == "q":
                for a in range(5):
                    for i in range(h_r[a], h_r[a]+hut_list[a].height):
                        for j in range(h_c[a], h_c[a]+hut_list[a].width):
                            if (i < x_r+3 and i > x_r-3) and (j < x_c+3 and j > x_c-3):
                                hut_list[a].health = hut_list[a].health - \
                                    q_man.damage

                for a in range(2):
                    for i in range(z_r[a], z_r[a]+wizard_list[a].height):
                        for j in range(z_c[a], z_c[a]+wizard_list[a].width):
                            if (i < x_r+3 and i > x_r-3) and (j < x_c+3 and j > x_c-3):
                                wizard_list[a].health = wizard_list[a].health - \
                                    q_man.damage


                for i in range(t_r, t_r+hall.height):
                    for j in range(t_c, t_c+hall.width):
                        if (i < x_r+3 and i > x_r-3) and (j < x_c+3 and j > x_c-3):
                            hall.health = hall.health - q_man.damage
                

            

            if input == "e" and Queen.flag==0:
                Queen.use_second = time.time()
                
                Queen.flag=1
                

            if Queen.flag==1:
                Queen.curr_second = time.time()
                #arr[3][27]=Queen.curr_second-Queen.use_second
                if Queen.curr_second-Queen.use_second>=1:
                    
                    for a in range(5):
                        for i in range(h_r[a], h_r[a]+hut_list[a].height):
                            for j in range(h_c[a], h_c[a]+hut_list[a].width):
                                if (i < e_r+7 and i > e_r-7) and (j < e_c+7 and j > e_c-7):
                                    hut_list[a].health = hut_list[a].health - \
                                        q_man.damage

                    for a in range(2):
                        for i in range(z_r[a], z_r[a]+wizard_list[a].height):
                            for j in range(z_c[a], z_c[a]+wizard_list[a].width):
                                if (i < e_r+7 and i > e_r-7) and (j < e_c+7 and j > e_c-7):
                                    wizard_list[a].health = wizard_list[a].health - \
                                        q_man.damage


                    for i in range(t_r, t_r+hall.height):
                        for j in range(t_c, t_c+hall.width):
                            if (i < e_r+7 and i > e_r-7) and (j < e_c+7 and j > e_c-7):
                                hall.health = hall.health - q_man.damage
                    
                    Queen.flag=0




            if input == "d":
                arr[q_r][q_c] = ' '
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = ' '
                    arr[e_r][e_c] = ' '
                q_c = q_c+q_man.movement_speed
                arr[q_r][q_c] = Fore.WHITE+'Q'
                x_c = q_c
                x_r = q_r
                x_c = x_c+8
                if(x_c) > m-3:
                    x_c = 0
                if(x_r) > n-3:
                    x_r = 0
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = Fore.WHITE+'X'

                e_c = q_c
                e_r = q_r
                e_c = e_c+16
                if(e_c) > m-3:
                    e_c = 0
                if(e_r) > n-3:
                    e_r = 0
                if arr[e_r][e_c] != Fore.MAGENTA+'W':
                    arr[e_r][e_c] = Fore.WHITE+'E'

            if input == "a":
                arr[q_r][q_c] = ' '
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = ' '
                    arr[e_r][e_c] = ' '
                q_c = q_c-q_man.movement_speed
                arr[q_r][q_c] = Fore.WHITE+'Q'
                x_c = q_c
                x_r = q_r
                x_c = x_c-8
                if(x_c) > m-3:
                    x_c = 0
                if(x_r) > n-3:
                    x_r = 0
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = Fore.WHITE+'X'

                e_c = q_c
                e_r = q_r
                e_c = e_c-16
                if(e_c) > m-3:
                    e_c = 0
                if(e_r) > n-3:
                    e_r = 0
                if arr[e_r][e_c] != Fore.MAGENTA+'W':
                    arr[e_r][e_c] = Fore.WHITE+'E'

            if input == "s":
                arr[q_r][q_c] = ' '
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = ' '
                    arr[e_r][e_c] = ' '
                q_r = q_r+q_man.movement_speed
                arr[q_r][q_c] = Fore.WHITE+'Q'
                x_c = q_c
                x_r = q_r
                x_r = x_r+8
                if(x_c) > m-3:
                    x_c = 0
                if(x_r) > n-3:
                    x_r = 0
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = Fore.WHITE+'X'

                e_c = q_c
                e_r = q_r
                e_r = e_r+16
                if(e_c) > m-3:
                    e_c = 0
                if(e_r) > n-3:
                    e_r = 0
                if arr[e_r][e_c] != Fore.MAGENTA+'W':
                    arr[e_r][e_c] = Fore.WHITE+'E'

            if input == "w":
                arr[q_r][q_c] = ' '
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = ' '
                    arr[e_r][e_c] = ' '
                q_r = q_r-q_man.movement_speed
                arr[q_r][q_c] = Fore.WHITE+'Q'
                x_c = q_c
                x_r = q_r
                x_r = x_r-8
                if(x_c) > m-3:
                    x_c = 0
                if(x_r) > n-3:
                    x_r = 0
                if arr[x_r][x_c] != Fore.MAGENTA+'W':
                    arr[x_r][x_c] = Fore.WHITE+'X'

                e_c = q_c
                e_r = q_r
                e_r = e_r-16
                if(e_c) > m-3:
                    e_c = 0
                if(e_r) > n-3:
                    e_r = 0
                if arr[e_r][e_c] != Fore.MAGENTA+'W':
                    arr[e_r][e_c] = Fore.WHITE+'E'

            # if input == "q":

            #     for t in range(5):
            #         if abs(h_r[t]-q_r) <= 4 and abs(h_c[t]-q_c) <= 4:
            #             hut_list[t].health = hut_list[t].health-q_man.damage

            #     if abs(t_r-q_r) <= 4 and abs(t-q_c) <= 4:
            #         hall.health = hall.health-q_man.damage

            if q_man.health <= 0:
                arr[q_r][q_c] = ' '
                q_man.alive = 0

                # if goal_zh==6:
                # hall.health=hall.health-1
                # else:
                #  hut_list[goal_zh].health=hut_list[goal_zh].health-1


class barbarian(Person):
    health = 20
    beg_health = 20
    damage = 1
    movement_speed = 1
    alive = 1

    def fun(self):
        stat_check()

        global bz_c
        global bz_r
        global bx_c
        global bx_r
        global bc_c
        global bc_r

        global z_start
        global x_start
        global c_start

        global status

        global hut_list
        global hall

        global bbrn_r
        global bbrn_c

        bbrn_r = [bz_r, bx_r, bc_r]
        bbrn_c = [bz_c, bx_c, bc_c]

        input = input_to(getch)
        if input == "z" and b_list[0].alive==1:
            z_start = 1
            arr[bz_r][bz_c] = Fore.YELLOW+'B'
        if input == "x" and b_list[1].alive==1:
            x_start = 1
            arr[bx_r][bx_c] = Fore.YELLOW+'B'
        if input == "c" and b_list[2].alive==1:
            c_start = 1
            arr[bc_r][bc_c] = Fore.YELLOW+'B'

        if(z_start == 1):
            arr[bz_r][bz_c] = Fore.YELLOW+'B'
            zx_diff = 10000
            zy_diff = 10000
            min = zx_diff+zy_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-bz_r)+abs(h_c[i]-bz_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_zr = h_r[i]
                    goal_zc = h_c[i]
                    goal_zh = i

            town_dist = abs(t_r-bz_r)+abs(t_c-bz_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_zh = 6
                goal_zr = t_r
                goal_zc = t_c



            for i in range(2):
                curr_dist = abs(z_r[i]-bz_r)+abs(z_c[i]-bz_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_zr = z_r[i]
                    goal_zc = z_c[i]
                    goal_zh = 7+i


            

            if goal_zr > bz_r:
                arr[bz_r][bz_c] = ' '
                bz_r = bz_r+barbarian.movement_speed
                arr[bz_r][bz_c] = Fore.YELLOW+'B'
                #arr[bz_r-1][bz_c] = ' '

            else:
                arr[bz_r][bz_c] = ' '
                bz_r = bz_r-barbarian.movement_speed
                arr[bz_r][bz_c] = Fore.YELLOW+'B'
                #arr[bz_r+1][bz_c] = ' '

            if goal_zc > bz_c:
                arr[bz_r][bz_c] = ' '
                bz_c = bz_c+barbarian.movement_speed
                arr[bz_r][bz_c] = Fore.YELLOW+'B'
                #arr[bz_r][bz_c-1] = ' '

            else:
                arr[bz_r][bz_c] = ' '
                bz_c = bz_c-barbarian.movement_speed
                arr[bz_r][bz_c] = Fore.YELLOW+'B'
                #arr[bz_r][bz_c+1] = ' '

            if abs(goal_zr-bz_r) <= 1 and abs(goal_zc-bz_c) <= 1:
                if goal_zh == 6:
                    hall.health = hall.health-barbarian.health
                elif goal_zh<6:
                    hut_list[goal_zh].health = hut_list[goal_zh].health-barbarian.health
                elif goal_zh == 7 or goal_zh == 8:
                    wizard_list[goal_zh-7].health = wizard_list[goal_zh-7].health-barbarian.health

            if b_list[0].health <= 0:
                z_start = 0
                arr[bz_r][bz_c] = ' '
                b_list[0].alive = 0

        if(x_start == 1):
            arr[bx_r][bx_c] = Fore.YELLOW+'B'
            xx_diff = 10000
            xy_diff = 10000
            min = xx_diff+xy_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-bx_r)+abs(h_c[i]-bx_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_xr = h_r[i]
                    goal_xc = h_c[i]
                    goal_xh = i

            town_dist = abs(t_r-bx_r)+abs(t_c-bx_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_xh = 6
                goal_xr = t_r
                goal_xc = t_c



            for i in range(2):
                curr_dist = abs(z_r[i]-bx_r)+abs(z_c[i]-bx_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_xr = z_r[i]
                    goal_xc = z_c[i]
                    goal_xh = 7+i


            if goal_xr > bx_r:
                arr[bx_r][bx_c] = ' '
                bx_r = bx_r+barbarian.movement_speed
                arr[bx_r][bx_c] = Fore.YELLOW+'B'

            else:
                arr[bx_r][bx_c] = ' '
                bx_r = bx_r-barbarian.movement_speed
                arr[bx_r][bx_c] = Fore.YELLOW+'B'

            if goal_xc > bx_c:
                arr[bx_r][bx_c] = ' '
                bx_c = bx_c+barbarian.movement_speed
                arr[bx_r][bx_c] = Fore.YELLOW+'B'

            else:
                arr[bx_r][bx_c] = ' '
                bx_c = bx_c-barbarian.movement_speed
                arr[bx_r][bx_c] = Fore.YELLOW+'B'

            if abs(goal_xr-bx_r) <= 1 and abs(goal_xc-bx_c) <= 1:
                if goal_xh == 6:
                    hall.health = hall.health-barbarian.health
                elif goal_xh<6:
                    hut_list[goal_xh].health = hut_list[goal_xh].health-barbarian.health
                elif goal_xh == 7 or goal_xh == 8:
                    wizard_list[goal_xh-7].health = wizard_list[goal_xh-7].health-barbarian.health

            if b_list[1].health <= 0:
                x_start = 0
                arr[bx_r][bx_c] = ' '
                b_list[1].alive = 0

        if(c_start == 1):
            arr[bc_r][bc_c] = Fore.YELLOW+'B'
            cx_diff = 10000
            cy_diff = 10000
            min = cx_diff+cy_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-bc_r)+abs(h_c[i]-bc_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_cr = h_r[i]
                    goal_cc = h_c[i]
                    goal_ch = i

            town_dist = abs(t_r-bc_r)+abs(t_c-bc_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_ch = 6
                goal_cr = t_r
                goal_cc = t_c



            for i in range(2):
                curr_dist = abs(z_r[i]-bc_r)+abs(z_c[i]-bc_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_cr = z_r[i]
                    goal_cc = z_c[i]
                    goal_ch = 7+i




            if goal_cr > bc_r:
                arr[bc_r][bc_c] = ' '
                bc_r = bc_r+barbarian.movement_speed
                arr[bc_r][bc_c] = Fore.YELLOW+'B'

            else:
                arr[bc_r][bc_c] = ' '
                bc_r = bc_r-barbarian.movement_speed
                arr[bc_r][bc_c] = Fore.YELLOW+'B'

            if goal_cc > bc_c:
                arr[bc_r][bc_c] = ' '
                bc_c = bc_c+barbarian.movement_speed
                arr[bc_r][bc_c] =Fore.YELLOW+'B'

            else:
                arr[bc_r][bc_c] = ' '
                bc_c = bc_c-barbarian.movement_speed
                arr[bc_r][bc_c] = Fore.YELLOW+'B'
                #arr[bz_r][bz_c+1] = ' '

            if abs(goal_cr-bc_r) <= 1 and abs(goal_cc-bc_c) <= 1:
                if goal_ch == 6:
                    hall.health = hall.health-barbarian.health
                elif goal_ch<6:
                    hut_list[goal_ch].health = hut_list[goal_ch].health-barbarian.health
                elif goal_ch==7 or goal_ch==8:
                    wizard_list[goal_ch-7].health = wizard_list[goal_ch-7].health-barbarian.health

            if b_list[2].health <= 0:
                c_start = 0
                arr[bc_r][bc_c] = ' '
                b_list[2].alive = 0


class archer(Person):
    health = 10
    beg_health = 10
    damage = 0.5
    movement_speed = 2
    alive = 1
    range=6

    def fun(self):
        stat_check()

        global av_c
        global ab_r
        global an_c
        global av_r
        global ab_c
        global an_r

        global v_start
        global b_start
        global n_start

        global status

        global hut_list
        global hall

        global arch_r
        global arch_c

        arch_r = [av_r, ab_r, an_r]
        arch_c = [av_c, ab_c, an_c]

        # print(Back.RED)
        # print(Style.RESET_ALL)
        input = input_to(getch)
        if input == "v" and a_list[0].alive==1:
            v_start = 1
            arr[av_r][av_c] = Fore.YELLOW+'A'
        if input == "b" and a_list[1].alive==1:
            b_start = 1
            arr[ab_r][ab_c] = Fore.YELLOW+'A'
        if input == "n" and a_list[2].alive==1:
            n_start = 1
            arr[an_r][an_c] = Fore.YELLOW+'A'

        if(v_start == 1):
            arr[av_r][av_c] = Fore.YELLOW+'A'
            vx_diff = 10000
            vy_diff = 10000
            min = vx_diff+vy_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-av_r)+abs(h_c[i]-av_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_vr = h_r[i]
                    goal_vc = h_c[i]
                    goal_vh = i

            town_dist = abs(t_r-av_r)+abs(t_c-av_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_vh = 6
                goal_vr = t_r
                goal_vc = t_c

            for i in range(2):
                curr_dist = abs(z_r[i]-av_r)+abs(z_c[i]-av_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_vh = 7+i
                    goal_vr = z_r[i]
                    goal_vc = z_c[i]

            if goal_vr > av_r:
                arr[av_r][av_c] = ' '
                av_r = av_r+archer.movement_speed
                arr[av_r][av_c] = Fore.YELLOW+'A'
                #arr[av_r-1][av_c] = ' '

            else:
                arr[av_r][av_c] = ' '
                av_r = av_r-archer.movement_speed
                arr[av_r][av_c] = Fore.YELLOW+'A'
                #arr[av_r+1][av_c] = ' '

            if goal_vc > av_c:
                arr[av_r][av_c] = ' '
                av_c = av_c+archer.movement_speed
                arr[av_r][av_c] = Fore.YELLOW+'A'
                #arr[av_r][av_c-1] = ' '

            else:
                arr[av_r][av_c] = ' '
                av_c = av_c-archer.movement_speed
                arr[av_r][av_c] = Fore.YELLOW+'A'
                #arr[av_r][av_c+1] = ' '

            if abs(goal_vr-av_r) <= archer.range and abs(goal_vc-av_c) <= archer.range:
                if goal_vh == 6:
                    hall.health = hall.health-archer.damage
                elif goal_vh<6:
                    hut_list[goal_vh].health = hut_list[goal_vh].health-archer.damage
                elif goal_vh == 7 or goal_vh == 8:
                    wizard_list[goal_vh-7].health = wizard_list[goal_vh-7].health-archer.damage
                arr[av_r][av_c] = Fore.RED+'A'

            if a_list[0].health <= 0:
                v_start = 0
                arr[av_r][av_c] = ' '
                a_list[0].alive = 0

        if(b_start == 1):
            arr[ab_r][ab_c] = Fore.YELLOW+'A'
            bx_diff = 10000
            by_diff = 10000
            min = bx_diff+by_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-ab_r)+abs(h_c[i]-ab_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_br = h_r[i]
                    goal_bc = h_c[i]
                    goal_bh = i

            town_dist = abs(t_r-ab_r)+abs(t_c-ab_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_bh = 6
                goal_br = t_r
                goal_bc = t_c


            for i in range(2):
                curr_dist = abs(z_r[i]-ab_r)+abs(z_c[i]-ab_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_bh = 7+i
                    goal_br = z_r[i]
                    goal_bc = z_c[i]

            if goal_br > ab_r:
                arr[ab_r][ab_c] = ' '
                ab_r = ab_r+archer.movement_speed
                arr[ab_r][ab_c] = Fore.YELLOW+'A'
                #arr[ab_r-1][ab_c] = ' '

            else:
                arr[ab_r][ab_c] = ' '
                ab_r = ab_r-archer.movement_speed
                arr[ab_r][ab_c] = Fore.YELLOW+'A'
                #arr[ab_r+1][ab_c] = ' '

            if goal_bc > ab_c:
                arr[ab_r][ab_c] = ' '
                ab_c = ab_c+archer.movement_speed
                arr[ab_r][ab_c] = Fore.YELLOW+'A'
                #arr[ab_r][ab_c-1] = ' '

            else:
                arr[ab_r][ab_c] = ' '
                ab_c = ab_c-archer.movement_speed
                arr[ab_r][ab_c] = Fore.YELLOW+'A'
                #arr[ab_r][ab_c+1] = ' '

            if abs(goal_br-ab_r) <= archer.range and abs(goal_bc-ab_c) <= archer.range:
                if goal_bh == 6:
                    hall.health = hall.health-archer.damage
                elif goal_bh<6:
                    hut_list[goal_bh].health = hut_list[goal_bh].health-archer.damage
                elif goal_bh == 7 or goal_bh == 8:
                    wizard_list[goal_bh-7].health = wizard_list[goal_bh-7].health-archer.damage
                arr[ab_r][ab_c] = Fore.RED+'A'

            if a_list[1].health <= 0:
                b_start = 0
                arr[ab_r][ab_c] = ' '
                a_list[1].alive = 0

        if(n_start == 1):
            arr[an_r][an_c] = Fore.YELLOW+'A'
            nx_diff = 10000
            ny_diff = 10000
            min = nx_diff+ny_diff
            for i in range(5):
                curr_dist = abs(h_r[i]-an_r)+abs(h_c[i]-an_c)
                if curr_dist < min and hut_list[i].alive == 1:
                    min = curr_dist
                    goal_nr = h_r[i]
                    goal_nc = h_c[i]
                    goal_nh = i

            town_dist = abs(t_r-an_r)+abs(t_c-an_c)
            if town_dist < min and hall.alive == 1:
                min = town_dist
                goal_nh = 6
                goal_nr = t_r
                goal_nc = t_c


            for i in range(2):
                curr_dist = abs(z_r[i]-an_r)+abs(z_c[i]-an_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_nh = 7+i
                    goal_nr = z_r[i]
                    goal_nc = z_c[i]

            


            if goal_nr > an_r:
                arr[an_r][an_c] = ' '
                an_r = an_r+archer.movement_speed
                arr[an_r][an_c] = Fore.YELLOW+'A'
                #arr[an_r-1][an_c] = ' '

            else:
                arr[an_r][an_c] = ' '
                an_r = an_r-archer.movement_speed
                arr[an_r][an_c] = Fore.YELLOW+'A'
                #arr[an_r+1][an_c] = ' '

            if goal_nc > an_c:
                arr[an_r][an_c] = ' '
                an_c = an_c+archer.movement_speed
                arr[an_r][an_c] = Fore.YELLOW+'A'
                #arr[an_r][an_c-1] = ' '

            else:
                arr[an_r][an_c] = ' '
                an_c = an_c-archer.movement_speed
                arr[an_r][an_c] = Fore.YELLOW+'A'
                #arr[an_r][an_c+1] = ' '

            if abs(goal_nr-an_r) <= archer.range and abs(goal_nc-an_c) <= archer.range:
                if goal_nh == 6:
                    hall.health = hall.health-archer.damage
                elif goal_nh<6:
                    hut_list[goal_nh].health = hut_list[goal_nh].health-archer.damage
                elif goal_nh == 7 or goal_nh == 8:
                    wizard_list[goal_nh-7].health = wizard_list[goal_nh-7].health-archer.damage
                arr[an_r][an_c] = Fore.RED+'A'

            if a_list[2].health <= 0:
                n_start = 0
                arr[an_r][an_c] = ' '
                a_list[2].alive = 0


class balloon(Person):
    health = 10
    beg_health = 20
    damage = 2
    movement_speed = 2
    alive = 1

    def fun(self):
        stat_check()

        global bk_c
        global bk_r
        global bl_c
        global bl_r

        global k_start
        global l_start

        global status

        global hut_list
        global hall
        global can_wiz_d

        global ball_r
        global ball_c

        ball_r = [bk_r, bl_r]
        ball_c = [bk_c, bl_c]

        # print(Back.RED)
        # print(Style.RESET_ALL)
        input = input_to(getch)
        if input == "o" and bl_list[0].alive==1:
            k_start = 1
            arr[bk_r][bk_c] = Fore.YELLOW+'O'
        if input == "p" and bl_list[1].alive==1:
            l_start = 1
            arr[bl_r][bl_c] = Fore.YELLOW+'O'
        
        if(k_start == 1):
            if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                arr[bk_r][bk_c] = Fore.YELLOW+'O'
            kx_diff = 10000
            ky_diff = 10000
            min = kx_diff+ky_diff

            if can_wiz_d==1:
                for i in range(5):
                    curr_dist = abs(h_r[i]-bk_r)+abs(h_c[i]-bk_c)
                    if curr_dist < min and hut_list[i].alive == 1:
                        min = curr_dist
                        goal_kr = h_r[i]
                        goal_kc = h_c[i]
                        goal_kh = i

                town_dist = abs(t_r-bk_r)+abs(t_c-bk_c)
                if town_dist < min and hall.alive == 1:
                    min = town_dist
                    goal_kh = 6
                    goal_kr = t_r
                    goal_kc = t_c


            for i in range(2):
                curr_dist = abs(z_r[i]-bk_r)+abs(z_c[i]-bk_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_kh = 7+i
                    goal_kr = z_r[i]
                    goal_kc = z_c[i]

            for i in range(2):
                curr_dist = abs(cann_r[i]-bk_r)+abs(cann_c[i]-bk_c)
                if curr_dist < min and cann_list[i].alive == 1:
                    min = curr_dist
                    goal_kh = 9+i
                    goal_kr = cann_r[i]
                    goal_kc = cann_c[i]


            if goal_kr > bk_r:
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = ' '
                bk_r = bk_r+balloon.movement_speed
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = Fore.YELLOW+'O'
                #arr[bk_r-1][bk_c] = ' '

            else:
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = ' '
                bk_r = bk_r-balloon.movement_speed
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = Fore.YELLOW+'O'
                #arr[bk_r+1][bk_c] = ' '

            if goal_kc > bk_c:
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = ' '
                bk_c = bk_c+balloon.movement_speed
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = Fore.YELLOW+'O'
                #arr[bk_r][bk_c-1] = ' '

            else:
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = ' '
                bk_c = bk_c-balloon.movement_speed
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = Fore.YELLOW+'O'
                #arr[bk_r][bk_c+1] = ' '

            if abs(goal_kr-bk_r) <= 2 and abs(goal_kc-bk_c) <= 2:
                if goal_kh == 6:
                    hall.health = hall.health-balloon.damage
                elif goal_kh<6:
                    hut_list[goal_kh].health = hut_list[goal_kh].health-balloon.damage
                elif goal_kh == 7 or goal_kh == 8:
                    wizard_list[goal_kh-7].health = wizard_list[goal_kh-7].health-balloon.damage
                elif goal_kh == 9 or goal_kh == 10:
                    cann_list[goal_kh-9].health = cann_list[goal_kh-9].health-balloon.damage
                if arr[bk_r][bk_c] != Fore.MAGENTA+'W':
                    arr[bk_r][bk_c] = Fore.YELLOW+'O'

            

            if bl_list[0].health <= 0:
                k_start = 0
                arr[bk_r][bk_c] = ' '
                bl_list[0].alive = 0

        if(l_start == 1):
            if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                arr[bl_r][bl_c] = Fore.YELLOW+'O'
            lx_diff = 10000
            ly_diff = 10000
            min = lx_diff+ly_diff

            if can_wiz_d==1:
                for i in range(5):
                    curr_dist = abs(h_r[i]-bl_r)+abs(h_c[i]-bl_c)
                    if curr_dist < min and hut_list[i].alive == 1:
                        min = curr_dist
                        goal_lr = h_r[i]
                        goal_lc = h_c[i]
                        goal_lh = i

                town_dist = abs(t_r-bl_r)+abs(t_c-bl_c)
                if town_dist < min and hall.alive == 1:
                    min = town_dist
                    goal_lh = 6
                    goal_lr = t_r
                    goal_lc = t_c

            for i in range(2):
                curr_dist = abs(z_r[i]-bl_r)+abs(z_c[i]-bl_c)
                if curr_dist < min and wizard_list[i].alive == 1:
                    min = curr_dist
                    goal_lh = 7+i
                    goal_lr = z_r[i]
                    goal_lc = z_c[i]


            for i in range(2):
                curr_dist = abs(cann_r[i]-bl_r)+abs(cann_c[i]-bl_c)
                if curr_dist < min and cann_list[i].alive == 1:
                    min = curr_dist
                    goal_lh = 9+i
                    goal_lr = cann_r[i]
                    goal_lc = cann_c[i]

            if goal_lr > bl_r:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = ' '
                bl_r = bl_r+balloon.movement_speed
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = Fore.YELLOW+'O'
                #arr[bl_r-1][bl_c] = ' '

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = ' '
                bl_r = bl_r-balloon.movement_speed
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = Fore.YELLOW+'O'
                #arr[bl_r+1][bl_c] = ' '

            if goal_lc > bl_c:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = ' '
                bl_c = bl_c+balloon.movement_speed
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = Fore.YELLOW+'O'
                #arr[bl_r][bl_c-1] = ' '

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = ' '
                bl_c = bl_c-balloon.movement_speed
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = Fore.YELLOW+'O'
                #arr[bl_r][bl_c+1] = ' '

            if abs(goal_lr-bl_r) <= 2 and abs(goal_lc-bl_c) <= 2:
                if goal_lh == 6:
                    hall.health = hall.health-balloon.damage
                elif goal_lh<6:
                    hut_list[goal_lh].health = hut_list[goal_lh].health-balloon.damage
                elif goal_lh == 7 or goal_lh == 8:
                    wizard_list[goal_lh-7].health = wizard_list[goal_lh-7].health-balloon.damage
                elif goal_lh == 9 or goal_lh == 10:
                    cann_list[goal_lh-9].health = cann_list[goal_lh-9].health-balloon.damage
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bl_r][bl_c] = Fore.YELLOW+'O'

            

            if bl_list[1].health <= 0:
                l_start = 0
                arr[bl_r][bl_c] = ' '
                bl_list[0].alive = 0

    # put colour functions


class Town_hall(Building):
    height = 4
    width = 3
    health = 40
    beg_health = 40
    alive = 1


class hut(Building):
    height = 2
    width = 2
    health = 10
    beg_health = 10
    alive = 1


class wall(Building):
    height = 1
    width = 1
    health = 100
    beg_health = 100


class plus(Building):
    height = 1
    width = 1
    health = 100
    beg_health = 100


class cannon(Building):
    height = 1
    width = 1
    health = 20
    beg_health = 20
    damage = 2
    alive=1

    def fun(self):

        global bz_c
        global bz_r
        global bx_c
        global bx_r
        global bc_c
        global bc_r

        global c1_r
        global c1_c
        global c2_r
        global c2_c

        global z_start
        global x_start
        global c_start

        global bull_1_r
        global bull_1_c
        global bull_2_r
        global bull_2_c

        global k_man

        global bk_r
        global bk_c

        global bl_r
        global bl_c

        global k_r
        global k_c

        global q_r
        global q_c

        min_target_1 = 10000
        target_1 = 0

        min_target_2 = 10000
        target_2 = 0

        if abs(c1_r-bz_r)+abs(c1_c-bz_c) < min_target_1 and z_start == 1:
            min_target_1 = abs(c1_r-bz_r)+abs(c1_c-bz_c)
            target_1 = 1

        if abs(c1_r-bx_r)+abs(c1_c-bx_c) < min_target_1 and x_start == 1:
            min_target_1 = abs(c1_r-bx_r)+abs(c1_c-bx_c)
            target_1 = 2

        if abs(c1_r-bc_r)+abs(c1_c-bc_c) < min_target_1 and c_start == 1:
            min_target_1 = abs(c1_r-bc_r)+abs(c1_c-bc_c)
            target_1 = 3

        if abs(c1_r-k_r)+abs(c1_c-k_c) < min_target_1 and k_man.alive == 1:
            min_target_1 = abs(c1_r-k_r)+abs(c1_c-k_c)
            target_1 = 4

        if abs(c1_r-av_r)+abs(c1_c-av_c) < min_target_1 and v_start == 1:
            min_target_1 = abs(c1_r-av_r)+abs(c1_c-av_c)
            target_1 = 5

        if abs(c1_r-ab_r)+abs(c1_c-ab_c) < min_target_1 and b_start == 1:
            min_target_1 = abs(c1_r-ab_r)+abs(c1_c-ab_c)
            target_1 = 6

        if abs(c1_r-an_r)+abs(c1_c-an_c) < min_target_1 and n_start == 1:
            min_target_1 = abs(c1_r-an_r)+abs(c1_c-an_c)
            target_1 = 7

        # if abs(c1_r-bk_r)+abs(c1_c-bk_c) < min_target_1 and k_start == 1:
        #     min_target_1 = abs(c1_r-bk_r)+abs(c1_c-bk_c)
        #     target_1 = 8

        # if abs(c1_r-bl_r)+abs(c1_c-bl_c) < min_target_1 and l_start == 1:
        #     min_target_1 = abs(c1_r-bl_r)+abs(c1_c-bl_c)
        #     target_1 = 9

        if abs(c1_r-q_r)+abs(c1_c-q_c) < min_target_1 and q_man.alive == 1:
            min_target_1 = abs(c1_r-q_r)+abs(c1_c-q_c)
            target_1 = 10

        if target_1 == 1:
            if bull_1_r < bz_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < bz_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-bz_r) <= 2 and abs(bull_1_c-bz_c) <= 2:
                b_list[target_1-1].health = b_list[target_1-1].health-cannon.damage

        if target_1 == 2:
            if bull_1_r < bx_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+2
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-2
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < bx_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+2
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-2
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-bx_r) <= 2 and abs(bull_1_c-bx_c) <= 2:
                b_list[target_1-1].health = b_list[target_1-1].health-cannon.damage

        if target_1 == 3:
            if bull_1_r < bc_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+3
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-3
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < bc_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+3
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-3
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-bc_r) <= 2 and abs(bull_1_c-bc_c) <= 2:
                b_list[target_1-1].health = b_list[target_1-1].health-cannon.damage

        if target_1 == 4:
            if bull_1_r < k_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < k_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-k_r) <= 2 and abs(bull_1_c-k_c) <= 2:
                k_man.health = k_man.health-cannon.damage

        if target_1 == 5:
            if bull_1_r < av_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < av_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-av_r) <= 2 and abs(bull_1_c-av_c) <= 2:
                a_list[target_1-5].health = a_list[target_1-5].health-cannon.damage

        if target_1 == 6:
            if bull_1_r < ab_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < ab_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-ab_r) <= 2 and abs(bull_1_c-ab_c) <= 2:
                a_list[target_1-5].health = a_list[target_1-5].health-cannon.damage

        if target_1 == 7:
            if bull_1_r < an_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < an_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-an_r) <= 2 and abs(bull_1_c-an_c) <= 2:
                a_list[target_1-5].health = a_list[target_1-5].health-cannon.damage

        # if target_1 == 8:
        #     if bull_1_r < bk_r-1:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_r = bull_1_r+1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     else:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_r = bull_1_r-1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     if bull_1_c < bk_c-1:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_c = bull_1_c+1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     else:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_c = bull_1_c-1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     if abs(bull_1_r-bk_r) <= 2 and abs(bull_1_c-bk_c) <= 2:
        #         bl_list[target_1-8].health = bl_list[target_1-8].health-1

        # if target_1 == 9:
        #     if bull_1_r < bl_r-1:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_r = bull_1_r+1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     else:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_r = bull_1_r-1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     if bull_1_c < bl_c-1:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_c = bull_1_c+1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     else:
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = ' '
        #         bull_1_c = bull_1_c-1
        #         if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
        #             arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

        #     if abs(bull_1_r-bl_r) <= 2 and abs(bull_1_c-bl_c) <= 2:
        #         bl_list[target_1-8].health = bl_list[target_1-8].health-1

        if target_1 == 10:
            if bull_1_r < q_r-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_r = bull_1_r-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if bull_1_c < q_c-1:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c+1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            else:
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = ' '
                bull_1_c = bull_1_c-1
                if arr[bull_1_r][bull_1_c] != Fore.MAGENTA+'W':
                    arr[bull_1_r][bull_1_c] = Fore.WHITE+'.'

            if abs(bull_1_r-q_r) <= 2 and abs(bull_1_c-q_c) <= 2:
                q_man.health = q_man.health-cannon.damage

        # cannon 2

        if abs(c2_r-bz_r)+abs(c2_c-bz_c) < min_target_2 and z_start == 1:
            min_target_2 = abs(c2_r-bz_r)+abs(c2_c-bz_c)
            target_2 = 1

        if abs(c2_r-bx_r)+abs(c2_c-bx_c) < min_target_2 and x_start == 1:
            min_target_2 = abs(c2_r-bx_r)+abs(c2_c-bx_c)
            target_2 = 2

        if abs(c2_r-bc_r)+abs(c2_c-bc_c) < min_target_2 and c_start == 1:
            min_target_2 = abs(c2_r-bc_r)+abs(c2_c-bc_c)
            target_2 = 3

        if abs(c2_r-k_r)+abs(c2_c-k_c) < min_target_2 and k_man.alive == 1:
            min_target_2 = abs(c2_r-k_r)+abs(c2_c-k_c)
            target_2 = 4

        if abs(c2_r-av_r)+abs(c2_c-av_c) < min_target_2 and v_start == 1:
            min_target_2 = abs(c2_r-av_r)+abs(c2_c-av_c)
            target_2 = 5

        if abs(c2_r-ab_r)+abs(c2_c-ab_c) < min_target_2 and b_start == 1:
            min_target_2 = abs(c2_r-ab_r)+abs(c2_c-ab_c)
            target_2 = 6

        if abs(c2_r-an_r)+abs(c2_c-an_c) < min_target_2 and n_start == 1:
            min_target_2 = abs(c2_r-an_r)+abs(c2_c-an_c)
            target_2 = 7

        # if abs(c2_r-bk_r)+abs(c2_c-bk_c) < min_target_1 and k_start == 1:
        #     min_target_2 = abs(c2_r-bk_r)+abs(c2_c-bk_c)
        #     target_2 = 8

        # if abs(c2_r-bl_r)+abs(c2_c-bl_c) < min_target_1 and l_start == 1:
        #     min_target_2 = abs(c2_r-bl_r)+abs(c2_c-bl_c)
        #     target_2 = 9

        if abs(c2_r-q_r)+abs(c2_c-q_c) < min_target_2 and q_man.alive == 1:
            min_target_2 = abs(c2_r-q_r)+abs(c2_c-q_c)
            target_2 = 10

        if target_2 == 1:
            if bull_2_r < bz_r-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < bz_c-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-bz_r) <= 2 and abs(bull_2_c-bz_c) <= 2:
                b_list[target_2-1].health = b_list[target_2-1].health-cannon.damage

        if target_2 == 2:
            if bull_2_r < bx_r-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r+2
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r-2
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < bx_c-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c+2
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c-2
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-bx_r) <= 2 and abs(bull_2_c-bx_c) <= 2:
                b_list[target_2-1].health = b_list[target_2-1].health-cannon.damage

        if target_2 == 3:
            if bull_2_r < bc_r-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r+3
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r-3
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < bc_c-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c+3
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c-3
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-bc_r) <= 2 and abs(bull_2_c-bc_c) <= 2:
                b_list[target_2-1].health = b_list[target_2-1].health-cannon.damage

        if target_2 == 4:
            if bull_2_r < k_r-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < k_c-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-k_r) <= 2 and abs(bull_2_c-k_c) <= 2:
                k_man.health = k_man.health-cannon.damage

        if target_2 == 5:
            if bull_2_r < av_r-1:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_r = bull_2_r+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_r = bull_2_r-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < av_c-1:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-av_r) <= 2 and abs(bull_2_c-av_c) <= 2:
                a_list[target_2-5].health = a_list[target_2-5].health-cannon.damage

        if target_2 == 6:
            if bull_2_r < ab_r-1:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_r = bull_2_r+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_r = bull_2_r-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < ab_c-1:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-ab_r) <= 2 and abs(bull_2_c-ab_c) <= 2:
                a_list[target_2-5].health = a_list[target_2-5].health-cannon.damage

        if target_2 == 7:
            if bull_2_r < an_r-1:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_r = bull_2_r+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_r = bull_2_r-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < an_c-1:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                arr[bull_2_r][bull_2_c] = ' '
                bull_2_c = bull_2_c-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-an_r) <= 2 and abs(bull_2_c-an_c) <= 2:
                a_list[target_2-5].health = a_list[target_2-5].health-cannon.damage

        # if target_2 == 8:
        #     if bull_2_r < bk_r-1:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_r = bull_2_r+1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     else:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_r = bull_2_r-1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     if bull_2_c < bk_c-1:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_c = bull_2_c+1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     else:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_c = bull_2_c-1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     if abs(bull_2_r-bk_r) <= 2 and abs(bull_2_c-bk_c) <= 2:
        #         bl_list[target_2-8].health = bl_list[target_2-8].health-1

        # if target_2 == 9:
        #     if bull_2_r < bl_r-1:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_r = bull_2_r+1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     else:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_r = bull_2_r-1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     if bull_2_c < bl_c-1:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_c = bull_2_c+1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     else:
        #         arr[bull_2_r][bull_2_c] = ' '
        #         bull_2_c = bull_2_c-1
        #         if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
        #             arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

        #     if abs(bull_2_r-bl_r) <= 2 and abs(bull_2_c-bl_c) <= 2:
        #         bl_list[target_2-8].health = bl_list[target_2-8].health-1

        if target_2 == 10:
            if bull_2_r < q_r-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_r = bull_2_r-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if bull_2_c < q_c-1:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c+1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            else:
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = ' '

                bull_2_c = bull_2_c-1
                if arr[bull_2_r][bull_2_c] != Fore.MAGENTA+'W':
                    arr[bull_2_r][bull_2_c] = Fore.WHITE+'.'

            if abs(bull_2_r-q_r) <= 2 and abs(bull_2_c-q_c) <= 2:
                k_man.health = k_man.health-cannon.damage

        #############


class wizard(Building):
    height = 2
    width = 2
    health = 10
    beg_health = 10
    alive = 1
    damage = 2

    def fun(self):

        global bz_c
        global bz_r
        global bx_c
        global bx_r
        global bc_c
        global bc_r

        global z_r
        global z_c
        global z_r
        global z_c

        global z_attack

        global z_start
        global x_start
        global c_start

        global bbrn_r
        global bbrn_c

        global wizard_list

        global k_man

        z_min_target_1 = 10000
        z_target_1 = 0

        z_min_target_2 = 10000
        z_target_2 = 0

        z_attack[0] = 0
        z_attack[1] = 0

        za_r_1 = -1
        za_c_1 = -1

        za_r_2 = -1
        za_c_2 = -1

        if abs(z_r[0]-bz_r)+abs(z_c[0]-bz_c) < z_min_target_1 and abs(z_r[0]-bz_r)+abs(z_c[0]-bz_c) < 10 and z_start == 1:
            z_min_target_1 = abs(z_r[0]-bz_r)+abs(z_c[0]-bz_c)
            za_r_1 = bz_r
            za_c_1 = bz_c
            z_target_1 = 1

        if abs(z_r[0]-bx_r)+abs(z_c[0]-bx_c) < z_min_target_1 and abs(z_r[0]-bx_r)+abs(z_c[0]-bx_c) < 10 and x_start == 1:
            z_min_target_1 = abs(z_r[0]-bx_r)+abs(z_c[0]-bx_c)
            za_r_1 = bx_r
            za_c_1 = bx_c
            z_target_1 = 2

        if abs(z_r[0]-bc_r)+abs(z_c[0]-bc_c) < z_min_target_1 and abs(z_r[0]-bc_r)+abs(z_c[0]-bc_c) < 10 and c_start == 1:
            z_min_target_1 = abs(z_r[0]-bc_r)+abs(z_c[0]-bc_c)
            za_r_1 = bc_r
            za_c_1 = bc_c
            z_target_1 = 3

        if abs(z_r[0]-k_r)+abs(z_c[0]-k_c) < z_min_target_1 and abs(z_r[0]-k_r)+abs(z_c[0]-k_c) < 10 and k_man.alive == 1:
            z_min_target_1 = abs(z_r[0]-k_r)+abs(z_c[0]-k_c)
            za_r_1 = k_r
            za_c_1 = k_c
            z_target_1 = 4

        if abs(z_r[0]-av_r)+abs(z_c[0]-av_c) < z_min_target_1 and abs(z_r[0]-av_r)+abs(z_c[0]-av_c) < 10 and v_start == 1:
            z_min_target_1 = abs(z_r[0]-av_r)+abs(z_c[0]-av_c)
            za_r_1 = av_r
            za_c_1 = av_c
            z_target_1 = 5

        if abs(z_r[0]-ab_r)+abs(z_c[0]-ab_c) < z_min_target_1 and abs(z_r[0]-ab_r)+abs(z_c[0]-ab_c) < 10 and b_start == 1:
            z_min_target_1 = abs(z_r[0]-ab_r)+abs(z_c[0]-ab_c)
            za_r_1 = ab_r
            za_c_1 = ab_c
            z_target_1 = 6

        if abs(z_r[0]-an_r)+abs(z_c[0]-an_c) < z_min_target_1 and abs(z_r[0]-an_r)+abs(z_c[0]-an_c) < 10 and n_start == 1:
            z_min_target_1 = abs(z_r[0]-an_r)+abs(z_c[0]-an_c)
            za_r_1 = an_r
            za_c_1 = an_c
            z_target_1 = 7

        if abs(z_r[0]-bk_r)+abs(z_c[0]-bk_c) < z_min_target_1 and abs(z_r[0]-bk_r)+abs(z_c[0]-bk_c) < 10 and k_start == 1:
            z_min_target_1 = abs(z_r[0]-bk_r)+abs(z_c[0]-bk_c)
            za_r_1 = bk_r
            za_c_1 = bk_c
            z_target_1 = 8

        if abs(z_r[0]-bl_r)+abs(z_c[0]-bl_c) < z_min_target_1 and abs(z_r[0]-bl_r)+abs(z_c[0]-bl_c) < 10 and l_start == 1:
            z_min_target_1 = abs(z_r[0]-bl_r)+abs(z_c[0]-bl_c)
            za_r_1 = bl_r
            za_c_1 = bl_c
            z_target_1 = 9

        if abs(z_r[0]-q_r)+abs(z_c[0]-q_c) < z_min_target_1 and abs(z_r[0]-q_r)+abs(z_c[0]-q_c) < 10 and q_man.alive == 1:
            z_min_target_1 = abs(z_r[0]-q_r)+abs(z_c[0]-q_c)
            za_r_1 = q_r
            za_c_1 = q_c
            z_target_1 = 10

        # if z_target_1 == 1:
        #     #arr[z_r[0]][z_c[0]] = Fore.Green+'J'
        #     z_attack[0] = 1
        #     b_list[z_target_1-1].health = b_list[z_target_1-1].health-1

        # if z_target_1 == 2:
        #     z_attack[0] = 1
        #     b_list[z_target_1-1].health = b_list[z_target_1-1].health-1

        # if z_target_1 == 3:
        #     z_attack[0] = 1
        #     b_list[z_target_1-1].health = b_list[z_target_1-1].health-1

        # if z_target_1 == 4:
        #     z_attack[0] = 1
        #     k_man.health = k_man.health-1

        if z_target_1 > 0:
            z_attack[0] = 1

        for a in range(3):
            for i in range(bbrn_r[a], bbrn_r[a]+1):
                for j in range(bbrn_c[a], bbrn_c[a]+1):
                    if z_attack[0] == 1:
                        if (i < za_r_1+3 and i > za_r_1-3) and (j < za_c_1+3 and j > za_c_1-3):
                            b_list[a].health = b_list[a].health - wizard.damage

        for a in range(3):
            for i in range(arch_r[a], arch_r[a]+1):
                for j in range(arch_c[a], arch_c[a]+1):
                    if z_attack[0] == 1:
                        if (i < za_r_1+3 and i > za_r_1-3) and (j < za_c_1+3 and j > za_c_1-3):
                            a_list[a].health = a_list[a].health - wizard.damage

        for a in range(2):
            
            for i in range(ball_r[a], ball_r[a]+1):
                for j in range(ball_c[a], ball_c[a]+1):
                    if z_attack[0] == 1: 
                        if (i < za_r_1+3 and i > za_r_1-3) and (j < za_c_1+3 and j > za_c_1-3):                           
                            bl_list[a].health = bl_list[a].health - \
                                wizard.damage

        if z_attack[0] == 1:
            if (k_r < za_r_1+4 and k_c > za_r_1-3) and (k_r < za_c_1+4 and k_c > za_c_1-3):
                k_man.health = k_man.health - wizard.damage

        if z_attack[0] == 1:
            if (q_r < za_r_1+4 and q_c > za_r_1-3) and (q_r < za_c_1+4 and q_c > za_c_1-3):
                q_man.health = q_man.health - wizard.damage

        ########################

        if abs(z_r[1]-bz_r)+abs(z_c[1]-bz_c) < z_min_target_2 and abs(z_r[1]-bz_r)+abs(z_c[1]-bz_c) < 10 and z_start == 1:
            z_min_target_2 = abs(z_r[1]-bz_r)+abs(z_c[1]-bz_c)
            za_r_2 = bz_r
            za_c_2 = bz_c
            z_target_2 = 1

        if abs(z_r[1]-bx_r)+abs(z_c[1]-bx_c) < z_min_target_2 and abs(z_r[1]-bx_r)+abs(z_c[1]-bx_c) < 10 and x_start == 1:
            z_min_target_2 = abs(z_r[1]-bx_r)+abs(z_c[1]-bx_c)
            za_r_2 = bx_r
            za_c_2 = bx_c
            z_target_2 = 2

        if abs(z_r[1]-bc_r)+abs(z_c[1]-bc_c) < z_min_target_2 and abs(z_r[1]-bc_r)+abs(z_c[1]-bc_c) < 10 and c_start == 1:
            z_min_target_2 = abs(z_r[1]-bc_r)+abs(z_c[1]-bc_c)
            za_r_2 = bc_r
            za_c_2 = bc_c
            z_target_2 = 3

        if abs(z_r[1]-k_r)+abs(z_c[1]-k_c) < z_min_target_2 and abs(z_r[1]-k_r)+abs(z_c[1]-k_c) < 10 and k_man.alive == 1:
            z_min_target_2 = abs(z_r[1]-k_r)+abs(z_c[1]-k_c)
            za_r_2 = k_r
            za_c_2 = k_c
            z_target_2 = 4

        if abs(z_r[1]-av_r)+abs(z_c[1]-av_c) < z_min_target_1 and abs(z_r[1]-av_r)+abs(z_c[1]-av_c) < 10 and v_start == 1:
            z_min_target_2 = abs(z_r[1]-av_r)+abs(z_c[1]-av_c)
            za_r_2 = av_r
            za_c_2 = av_c
            z_target_2 = 5

        if abs(z_r[1]-ab_r)+abs(z_c[1]-ab_c) < z_min_target_1 and abs(z_r[1]-ab_r)+abs(z_c[1]-ab_c) < 10 and b_start == 1:
            z_min_target_2 = abs(z_r[1]-ab_r)+abs(z_c[1]-ab_c)
            za_r_2 = ab_r
            za_c_2 = ab_c
            z_target_2 = 6

        if abs(z_r[1]-an_r)+abs(z_c[1]-an_c) < z_min_target_1 and abs(z_r[1]-an_r)+abs(z_c[1]-an_c) < 10 and n_start == 1:
            z_min_target_2 = abs(z_r[1]-an_r)+abs(z_c[1]-an_c)
            za_r_2 = an_r
            za_c_2 = an_c
            z_target_2 = 7

        if abs(z_r[1]-bk_r)+abs(z_c[1]-bk_c) < z_min_target_1 and abs(z_r[1]-bk_r)+abs(z_c[1]-bk_c) < 10 and k_start == 1:
            z_min_target_2 = abs(z_r[1]-bk_r)+abs(z_c[1]-bk_c)
            za_r_2 = bk_r
            za_c_2 = bk_c
            z_target_2 = 8

        if abs(z_r[1]-bl_r)+abs(z_c[1]-bl_c) < z_min_target_1 and abs(z_r[1]-bl_r)+abs(z_c[1]-bl_c) < 10 and l_start == 1:
            z_min_target_2 = abs(z_r[1]-bl_r)+abs(z_c[1]-bl_c)
            za_r_2 = bl_r
            za_c_2 = bl_c
            z_target_2 = 9

        if abs(z_r[1]-q_r)+abs(z_c[1]-q_c) < z_min_target_1 and abs(z_r[1]-q_r)+abs(z_c[1]-q_c) < 10 and q_man.alive == 1:
            z_min_target_2 = abs(z_r[1]-q_r)+abs(z_c[1]-q_c)
            za_r_2 = q_r
            za_c_2 = q_c
            z_target_2 = 10

        # if z_target_2 == 1:
        #     #arr[z_r[0]][z_c[0]] = Fore.Green+'J'
        #     z_attack[1] = 1
        #     b_list[z_target_2-1].health = b_list[z_target_2-1].health-1

        # if z_target_2 == 2:
        #     z_attack[1] = 1
        #     b_list[z_target_2-1].health = b_list[z_target_2-1].health-1

        # if z_target_2 == 3:
        #     z_attack[1] = 1
        #     b_list[z_target_2-1].health = b_list[z_target_2-1].health-1

        # if z_target_2 == 4:
        #     z_attack[1] = 1
        #     k_man.health = k_man.health-1

        if z_target_2 > 0:
            z_attack[1] = 1

        for a in range(3):
            for i in range(bbrn_r[a], bbrn_r[a]+1):
                for j in range(bbrn_c[a], bbrn_c[a]+1):
                    # arr[3][25]=Fore.GREEN+str(abs(z_r[0]-ab_r)+abs(z_c[0]-ab_c))
                    # arr[3][27]=Fore.GREEN+str(z_min_target_1)
                    # arr[3][29]=Fore.GREEN+str(z_target_1)
                   
                    
                    #arr[3][27]=Fore.GREEN+str(za_c_1)
                    #arr[3][29]=Fore.GREEN+str(z_target_1)
                    # arr[3][27]=Fore.GREEN+str(min_target_2)
                    # arr[3][29]=Fore.GREEN+str(z_target_2)
                    #abs(c2_r-an_r)+abs(c2_c-an_c) < min_target_2
                    #arr[3][27] = Fore.GREEN+str(k_man.alive)
                    if z_attack[1] == 1:
                        if (i < za_r_2+2 and i > za_r_2-2) and (j < za_c_2+2 and j > za_c_2-2):
                            b_list[2].health = b_list[2].health - wizard.damage

        for a in range(3):
            for i in range(arch_r[a], arch_r[a]+1):
                for j in range(arch_c[a], arch_c[a]+1):
                    if z_attack[1] == 1:
                        if (i < za_r_2+3 and i > za_r_2-3) and (j < za_c_2+3 and j > za_c_2-3):
                            a_list[a].health = a_list[a].health - wizard.damage

        for a in range(2):
            for i in range(ball_r[a], ball_r[a]+1):
                for j in range(ball_c[a], ball_c[a]+1):
                    if z_attack[1] == 1:
                        if (i < za_r_2+3 and i > za_r_2-3) and (j < za_c_2+3 and j > za_c_2-3):
                            bl_list[a].health = bl_list[a].health - wizard.damage
                                

        if z_attack[1] == 1:
            if (k_r < za_r_2+3 and k_c > za_r_2-3) and (k_r < za_c_2+3 and k_c > za_c_2-3):
                k_man.health = k_man.health - wizard.damage

        if z_attack[1] == 1:
            if (q_r < za_r_1+3 and q_c > za_r_1-3) and (q_r < za_c_1+3 and q_c > za_c_2-3):
                q_man.health = q_man.health - wizard.damage


# end class definitions


# function definitions

def end_check():
    input = input_to(getch)
    if input == "t":
        quit()


def stat_check():
    global status
    global can_wiz_d
    if hut_list[0].alive == 0 and hut_list[1].alive == 0 and hut_list[2].alive == 0 and hut_list[3].alive == 0 and hut_list[4].alive == 0 and hall.alive == 0 and wizard_list[0].alive==0 and wizard_list[1].alive==0:
        status = 0
        print(Fore.GREEN+"\nVictory to the attacking team")
        exit()

    if b_list[0].alive == 0 and b_list[1].alive == 0 and b_list[2].alive == 0 and k_man.alive == 0 and q_man.alive == 0 and a_list[0].alive == 0 and a_list[1].alive == 0 and a_list[2].alive == 0 and bl_list[0].alive == 0 and bl_list[1].alive == 0:
        status = 0
        print(Fore.GREEN+"\nvictory to the defending team")
        exit()

    if wizard_list[0].alive==0 and wizard_list[1].alive==0 and cann_list[0].alive==0 and cann_list[1].alive==0:
        can_wiz_d=1


def spell():
    input = input_to(getch)
    if input == "r":
        k_man.movement_speed = 2
        k_man.damage = k_man.damage*2

        q_man.movement_speed = 2
        q_man.damage = q_man.damage*2
    if input == "h":
        k_man.health = k_man.health*1.5
        if k_man.health>k_man.beg_health:
            k_man.health=k_man.beg_health

        q_man.health = q_man.health*1.5
        if q_man.health>q_man.beg_health:
            q_man.health=q_man.beg_health

        for a in range(3):
            b_list[a].health=b_list[a].health*1.5
            if b_list[a].health>b_list[a].beg_health:
                b_list[a].health=b_list[a].beg_health

        for a in range(3):
            a_list[a].health=a_list[a].health*1.5
            if a_list[a].health>a_list[a].beg_health:
                a_list[a].health=a_list[a].beg_health

        for a in range(2):
            bl_list[a].health=bl_list[a].health*1.5
            if bl_list[a].health>bl_list[a].beg_health:
                bl_list[a].health=bl_list[a].beg_health

        


def render():

    CURSOR_UP_ONE = '\x1b[1A'
    ERASE_LINE = '\x1b[2K'

    for i in range(n+3):
        print("\033[A\033[A\33[2K")

    for row in arr:
        print(*row)

    if kq == 1:
        print("King's health "+str(k_man.health)+"/"+str(k_man.beg_health)+" ")
    elif kq == 2:
        print("Queen's health "+str(q_man.health)+"/"+str(q_man.beg_health)+" ")

    # print("hi")
    # print("hi")
    # print("\033[A\033[A")
    # print("hi")
    # print("hi")
    # print("\033[A\033[A")

    print("Barbarian group 1(z)'s health " +
          str(b_list[0].health)+"/"+str(b_list[0].beg_health), end="       ")
    print("Barbarian group 2(x)'s health " +
          str(b_list[1].health)+"/"+str(b_list[1].beg_health), end="       ")
    print("Barbarian group 3(c)'s health " +
          str(b_list[2].health)+"/"+str(b_list[2].beg_health))

    # print("\033[A\033[A\33[2K")

    # print("\033[A\033[A\33[2K")

    print("Archer 1(v)'s health " +
          str(a_list[0].health)+"/"+str(a_list[0].beg_health), end="       ")
    print("Archer 2(b)'s health " +
          str(a_list[1].health)+"/"+str(a_list[1].beg_health), end="       ")
    print("Archer 3(n)'s health " +
          str(a_list[2].health)+"/"+str(a_list[2].beg_health), end="       ")

    print("Balloon 1(k)'s health " +
          str(bl_list[0].health)+"/"+str(bl_list[0].beg_health), end="       ")
    print("Balloon 2(l)'s health " +
          str(bl_list[1].health)+"/"+str(bl_list[1].beg_health), end="       ")

    # print("hi")
    # print("\033[A\033[A")


b_list = []
b_list.append(barbarian())
b_list.append(barbarian())
b_list.append(barbarian())

a_list = []
a_list.append(archer())
a_list.append(archer())
a_list.append(archer())

bl_list = []
bl_list.append(balloon())
bl_list.append(balloon())


k_man = King()
q_man = Queen()

char = input("Enter 1 for king, 2 for queen")
print("\033[A\033[A\33[2K")
if char == "1":
    kq = 1
elif char == "2":
    kq = 2
else:
    print("Invalid input")
    quit()

if kq == 1:
    q_man.alive = 0
    q_man.health = 0

if kq == 2:
    k_man.alive = 0
    k_man.health = 0

if kq==1:
    arr[k_r][k_c] = Fore.WHITE+'K'

elif kq==2:
    arr[q_r][q_c] = Fore.WHITE+'Q'

arr[bz_r][bz_c] = Fore.CYAN+'B'
arr[bx_r][bx_c] = Fore.CYAN+'B'
arr[bc_r][bc_c] = Fore.CYAN+'B'

arr[av_r][av_c] = Fore.CYAN+'A'
arr[ab_r][ab_c] = Fore.CYAN+'A'
arr[an_r][an_c] = Fore.CYAN+'A'

arr[bk_r][bk_c] = Fore.CYAN+'O'
arr[bl_r][bl_c] = Fore.CYAN+'O'


def place():
    #arr[k_r][k_c] = Fore.WHITE+'K'

    hall.find_colour()
    if hall.colour == 'G':
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = Fore.GREEN+'T'
    elif hall.colour == 'Y':
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = Fore.YELLOW+'T'
    elif hall.colour == 'R':
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = Fore.RED+'T'
    else:
        for i in range(t_r, t_r+hall.height):
            for j in range(t_c, t_c+hall.width):
                arr[i][j] = ' '

    hut_list[0].find_colour()
    hut_list[1].find_colour()
    hut_list[2].find_colour()
    hut_list[3].find_colour()
    hut_list[4].find_colour()

    for a in range(5):
        if hut_list[a].colour == 'G':
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = Fore.GREEN+'H'
        elif hut_list[a].colour == 'Y':
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = Fore.YELLOW+'H'
        elif hut_list[a].colour == 'R':
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = Fore.RED+'H'
        else:
            for i in range(h_r[a], h_r[a]+hut_list[a].height):
                for j in range(h_c[a], h_c[a]+hut_list[a].width):
                    arr[i][j] = ' '

    wizard_list[0].find_colour()
    wizard_list[1].find_colour()

    for a in range(2):
        if wizard_list[a].colour == 'G':
            for i in range(z_r[a], z_r[a]+wizard_list[a].height):
                for j in range(z_c[a], z_c[a]+wizard_list[a].width):
                    if z_attack[a] == 0:
                        arr[i][j] = Fore.GREEN+'Z'
                    else:
                        arr[i][j] = Fore.GREEN+'\033[2;32;41mZ\033[0;0m'
        elif wizard_list[a].colour == 'Y':
            for i in range(z_r[a], z_r[a]+wizard_list[a].height):
                for j in range(z_c[a], z_c[a]+wizard_list[a].width):
                    if z_attack[a] == 0:
                        arr[i][j] = Fore.YELLOW+'Z'
                    else:
                        arr[i][j] = Fore.YELLOW+'\033[2;33;41mZ\033[0;0m'
        elif wizard_list[a].colour == 'R':
            for i in range(z_r[a], z_r[a]+wizard_list[a].height):
                for j in range(z_c[a], z_c[a]+wizard_list[a].width):
                    if z_attack[a] == 0:
                        arr[i][j] = Fore.RED+'Z'
                    else:
                        arr[i][j] = Fore.RED+'\033[2;30;41mZ\033[0;0m'
        else:
            for i in range(z_r[a], z_r[a]+wizard_list[a].height):
                for j in range(z_c[a], z_c[a]+wizard_list[a].width):
                    arr[i][j] = ' '

    plus_obj = wall()
    plus_obj.find_colour()
    for a in range(200):
        if plus_obj.colour == 'G':
            for i in range(p_r[a], p_r[a]+plus_obj.height):
                for j in range(p_c[a], p_c[a]+plus_obj.width):
                    arr[i][j] = Fore.CYAN+'+'
        elif wall_obj.colour == 'Y':
            for i in range(p_r[a], p_r[a]+plus_obj.height):
                for j in range(p_c[a], p_c[a]+plus_obj.width):
                    arr[i][j] = Fore.CYAN+'+'
        elif wall_obj.colour == 'R':
            for i in range(p_r[a], p_r[a]+plus_obj.height):
                for j in range(p_c[a], p_c[a]+plus_obj.width):
                    arr[i][j] = Fore.CYAN+'+'
        else:
            for i in range(p_r[a], p_r[a]+plus_obj.height):
                for j in range(p_c[a], p_c[a]+plus_obj.width):
                    arr[i][j] = Fore.CYAN+'+'

    

    cann_list[0].find_colour()
    cann_list[1].find_colour()

    for a in range(2):
        if cann_list[a].colour == 'G':
            for i in range(cann_r[a], cann_r[a]+cann_list[a].height):
                for j in range(cann_c[a], cann_c[a]+cann_list[a].width):
                    arr[i][j] = Fore.GREEN+'C'
                    
        elif cann_list[a].colour == 'Y':
            for i in range(cann_r[a], cann_r[a]+cann_list[a].height):
                for j in range(cann_c[a], cann_c[a]+cann_list[a].width):
                    arr[i][j] = Fore.YELLOW+'C'
                    
        elif cann_list[a].colour == 'R':
            for i in range(cann_r[a], cann_r[a]+cann_list[a].height):
                for j in range(cann_c[a], cann_c[a]+cann_list[a].width):
                    arr[i][j] = Fore.RED+'C'
                    
        else:
            for i in range(cann_r[a], cann_r[a]+cann_list[a].height):
                for j in range(cann_c[a], cann_c[a]+cann_list[a].width):
                    arr[i][j] = ' '

    
    print(Style.RESET_ALL)


def revise():
    nsd = King()
    nsd.fun()
    rzs = Queen()
    rzs.fun()
    Barb = barbarian()
    Barb.fun()
    Cann = cannon()
    Cann.fun()
    Arch = archer()
    Arch.fun()
    Ball = balloon()
    Ball.fun()
    Wiz = wizard()
    Wiz.fun()


# end function definitions


hut_list = []
hut_list.append(hut())
hut_list.append(hut())
hut_list.append(hut())
hut_list.append(hut())
hut_list.append(hut())

wizard_list = []
wizard_list.append(wizard())
wizard_list.append(wizard())

cann_list = []
cann_list.append(cannon())
cann_list.append(cannon())

hall = Town_hall()


# putting things on the grid

wall_obj = wall()
wall_obj.find_colour()
for a in range(len(w_r)):
    if wall_obj.colour == 'G':
        for i in range(w_r[a], w_r[a]+wall_obj.height):
            for j in range(w_c[a], w_c[a]+wall_obj.width):
                arr[i][j] = Fore.MAGENTA+'W'
    elif wall_obj.colour == 'Y':
        for i in range(w_r[a], w_r[a]+wall_obj.height):
            for j in range(w_c[a], w_c[a]+wall_obj.width):
                arr[i][j] = Fore.MAGENTA+'W'
    elif wall_obj.colour == 'R':
        for i in range(w_r[a], w_r[a]+wall_obj.height):
            for j in range(w_c[a], w_c[a]+wall_obj.width):
                arr[i][j] = Fore.MAGENTA+'W'
    else:
        for i in range(w_r[a], w_r[a]+wall_obj.height):
            for j in range(w_c[a], w_c[a]+wall_obj.width):
                arr[i][j] = Fore.MAGENTA+'W'

