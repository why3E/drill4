from pico2d import *

#화면 크기 및 이미지 로드
TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.png')
character_image = load_image('my_character.png')

# 캐릭터 왼쪽,오른쪽 걷는 동작 프레임 최대한 맞춘 위치
frame_info = [
    {'x_move':86, 'num' : 1,'wide':32},
    {'x_move':119, 'num' : 5,'wide':28},
    {'x_move':259, 'num' : 5,'wide':28},
    {'x_move':370, 'num' : 4,'wide':32},
    {'x_move':499, 'num' : 2,'wide':32},
]
# 캐릭터 위,아래 걷는 동작 프레임 최대한 맞춘 위치
frame_info2 = [
    {'x_move':113, 'num' : 5,'wide':27},
]

#방향키 4개와 esc입력 처리
def handle_events():
    global running, dix,diy,check,ycheck

    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            running = False

        elif event.type == SDL_KEYDOWN:

            if event.key == SDLK_RIGHT:
                dix += 1
                check = 0
            elif event.key == SDLK_LEFT:
                dix -= 1
                check = -1
            elif event.key == SDLK_UP:
                diy += 1
                ycheck = 1
            elif event.key == SDLK_DOWN:
                diy -= 1
                ycheck = 1
            elif event.key == SDLK_ESCAPE:
                running = False

        elif event.type == SDL_KEYUP:

            if event.key == SDLK_RIGHT:
                dix -= 1
                check = 0
            elif event.key == SDLK_LEFT:
                dix += 1
                check = -1
            elif event.key == SDLK_UP:
                diy -= 1
                ycheck = 0
            elif event.key == SDLK_DOWN:
                diy += 1
                ycheck = 0

# main
#캐릭터 좌표
x,y = TUK_WIDTH // 2, TUK_HEIGHT // 2
#입력된 키의 이동값
dix, diy = 0, 0
#캐릭터 연출을 위한 반복문의 변수
count, i, check= 0, 0,0
ycheck=0
ia = 0
running = True


while running:
    clear_canvas()

# 캐릭터 연출을 위한 반복문
    if i==frame_info[count]['num']:
        i =0
        count = count +1

    if ia==frame_info2[0]['num']:
        ia=0
        
    count = count%5

    tuk_ground.draw(TUK_WIDTH // 2, TUK_HEIGHT // 2)

#왼쪽을 봤을때 왼쪽 모션
    if dix == -1 or check == -1:
        if ycheck == 1:
            character_image.clip_composite_draw(frame_info2[0]['x_move']+frame_info2[0]['wide']*ia,0, frame_info2[0]['wide'], 45,0,'h', x, y ,128,128)
            ia = ia +1
        else:
            character_image.clip_composite_draw(frame_info[count]['x_move']+frame_info[count]['wide']*i,160, frame_info[count]['wide'], 40,0,'h', x, y ,128,128)
            i = i+1
#오른쪽을 봤을때 오른쪽 모션
    else :
        if ycheck==1:
            character_image.clip_draw(frame_info2[0]['x_move']+frame_info2[0]['wide']*ia,0, frame_info2[0]['wide'], 45, x, y ,128,128)
            ia = ia +1
        else:
            character_image.clip_draw(frame_info[count]['x_move']+frame_info[count]['wide']*i,160, frame_info[count]['wide'], 40, x, y ,128,128)
            i = i+1

    
    update_canvas()
    handle_events()

#눌린 키에 따라 x,y값 변화
    x += dix*10
    y += diy*10

# 만약 화면 크기 이상으로 이동되면 프로그램 진행 중지
    if x >= TUK_WIDTH or y>= TUK_HEIGHT or x<=0 or y<=0:
        running = False
        
    delay(0.05)