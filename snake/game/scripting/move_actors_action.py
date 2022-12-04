from game.scripting.action import Action

class MoveActorsAction(Action):
    """
    An action that moves an actor
    
    The responsibility of MoveActorsAction is to get the next move of the actor and move the actor


    """
    def execute(self, cast, script):
        """Executes the next move for each member of the cast
        
        Args:
            cast: the cast of actors
            script: script from action
        """
        for actor in cast.get_all_actors():
            actor.move_next()