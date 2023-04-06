def jump():
    collide = False
    screen.onkeypress(None, 'Up')
    global character_dir
    global character_animation
    destination_y = wall.ycor() + 45
    character_animation = 1
    jump_angle = 90
    character.setheading(jump_angle)
    if keyboard.is_pressed('Left') or character_dir == -1:
        character.setheading(jump_angle)
        while(character.ycor() > wall.ycor() + 40 and collide == False):
            character.forward(20)
            """ character.right(jump_angle) """
            character.setheading(jump_angle)
            time.sleep(0.0000001)
            canvas.xview_scroll(-8, "units")
            if(jump_angle < 250):
                jump_angle += 8
        character_dir = -1
    else:
        """ trtl.Turtle().goto(character.xcor() + 200, character.ycor()) """
        for i in range(floor_info[1]):
            if(abs(character.xcor() - 80 - (floor_info[0][i][1] + floor_info[0][i][2]) / 2) <= abs(floor_info[0][i][1] - floor_info[0][i][2]) / 2):
                destination_y = floor_info[0][i][0] + 50
                print("tt")
                break
        print(stuck)
        if(stuck == False):
            while(character.ycor() >= destination_y and collide == False):
                stuck_collision()
                character.forward(20)
                """ character.right(jump_angle) """
                character.setheading(jump_angle)
                time.sleep(0.0000001)
                canvas.xview_scroll(8, "units")
                if(jump_angle > -70):
                    jump_angle -= 8
            character.sety(destination_y)
        else:
            while(collide == False):
                stuck_collision()
                print(collide)
                character.forward(20)
                """ character.right(jump_angle) """
                character.setheading(jump_angle)
                time.sleep(0.0000001)
                canvas.xview_scroll(8, "units")
                if(jump_angle > -70):
                    jump_angle -= 8

        """ if(character.ycor() > wall_info[i][0]): 
            character.sety(wall_info[i][0] + 40)
        else:
            create_gravity(border, character) """
        character_dir = 1
        
    """ else:
        print("x")
        while(character.ycor() < 160):
          character.sety(character.ycor() + 0.2)
        while(character.ycor() > 45):
          character.sety(character.ycor() - 0.2)
        canvas.yview_scroll(0, "units") """
    
    """ create_gravity(border, character) """
    character.setheading(0)
    gravity()
    screen.onkeypress(jump, 'Up')
    character_animation = 0
    """ standing() """
