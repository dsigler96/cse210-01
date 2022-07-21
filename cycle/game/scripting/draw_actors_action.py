from game.scripting.action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        snakes = []
        segments = []

        snake_1 = cast.get_first_actor("snake_1")
        snake_2 = cast.get_first_actor("snake_2")
        snakes.append(snake_1)
        snakes.append(snake_2)


        segment_1 = snake_1.get_segments()
        segment_2 = snake_2.get_segments()
        segments.append(segment_1)
        segments.append(segment_2)

        messages = cast.get_actors("messages")

        for sn in snakes:
            for segment in segments:
                self._video_service.clear_buffer()
                self._video_service.draw_actors(segment)
                self._video_service.draw_actors(messages, True)
                self._video_service.flush_buffer()