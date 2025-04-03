from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake

score=0

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=Snake()
food=Food()
scoreboard=Scoreboard()



screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


is_game_on=True
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.segments[0].xcor()>280 or snake.segments[0].xcor()<-280 or snake.segments[0].ycor()>280 or snake.segments[0].ycor()<-280:
        game_is_on=False
        scoreboard.game_over()

    for segment in snake.segments[1:]:
        if segment==snake.segments[0]:
            pass
        elif snake.segments[0].distance(segment)<10:
            game_is_on=False
            scoreboard.game_over()
            


screen.exitonclick()