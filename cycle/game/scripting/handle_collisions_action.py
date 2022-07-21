import constants
from game.casting.snake import Snake_1, Snake_2
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_game_over(cast)
    
    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snakes   = []
        segments = []

        snake_1 = cast.get_first_actor("snake_1")
        snake_2 = cast.get_first_actor("snake_2")
        snakes.append(snake_1)
        snakes.append(snake_2)

        head_1 = snake_1.get_segments()[0]
        head_2 = snake_2.get_segments()[0]

        segment_1 = snake_1.get_segments()[1:]
        segment_2 = snake_2.get_segments()[1:]
        segments.append(segment_1)
        segments.append(segment_2)

        for sn in snakes:
            for s in segments:
                for segment in s:
                    if head_1.get_position().equals(segment.get_position()):
                        self._is_game_over = True

        for sn in snakes:
            for s in segments:
                for segment in s:
                    if head_2.get_position().equals(segment.get_position()):
                        self._is_game_over = True


    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            segments = []
            snake_1 = cast.get_first_actor("snake_1")
            snake_2 = cast.get_first_actor("snake_2")

            segment_1 = snake_1.get_segments()
            segment_2 = snake_2.get_segments()
            segments.append(segment_1)
            segments.append(segment_2)

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()
            message.set_text("Game Over!")
            message.set_position(position)
            cast.add_actor("messages", message)

            for s in segments:
                for segment in s:
                    segment.set_color(constants.WHITE)
