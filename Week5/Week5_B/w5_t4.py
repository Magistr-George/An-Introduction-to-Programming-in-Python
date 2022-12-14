import simplegui

WIDTH = 400
HEIGHT = 300
click_pos = [WIDTH / 2, HEIGHT / 2]

ast_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/asteroid.png")
ast_image_size = [95, 93]
ast_image_center = [ast_image_size[0] / 2, ast_image_size[1] / 2]
 
def draw(canvas):
    canvas.draw_image(ast_image, ast_image_center, ast_image_size, 
                      click_pos, ast_image_size)
    
def click(pos):
    global click_pos
    click_pos = pos
    
frame = simplegui.create_frame("Test image", WIDTH, HEIGHT)
frame.set_canvas_background("Gray")
frame.set_draw_handler(draw)
frame.set_mouseclick_handler(click)

frame.start()
        