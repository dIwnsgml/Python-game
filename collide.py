def detect_collide(element, character):
    if(abs(element.xcor() - character.xcor()) < 30 and abs(element.ycor() - character.ycor() + 40) < 10):