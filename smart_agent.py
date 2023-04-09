from agent import AlphaBetaAgent
import minimax

"""
Agent skeleton. Fill in the gaps.
"""
class MyAgent(AlphaBetaAgent):

  """
  This is the skeleton of an agent to play the Tak game.
  """
  def get_action(self, state, last_action, time_left):
    self.last_action = last_action
    self.time_left = time_left
    return minimax.search(state, self)

  """
  The successors function must return (or yield) a list of
  pairs (a, s) in which a is the action played to reach the
  state s.
  """
  def successors(self, state):
    succ = []
    actions = state.get_current_player_actions()
    for action in actions :
      s = state.copy()
      s.apply_action(action)
      succ.append((action, s))
    return succ

  """
  The cutoff function returns true if the alpha-beta/minimax
  search has to stop and false otherwise.
  """
  def cutoff(self, state, depth):
    return state.game_over() or depth == 2

  """
  The evaluate function must return an integer value
  representing the utility function of the board.
  """
  def evaluate(self, state):
    utility = 0
    for i in range(3) :
      utility += list(state.adj_bridges(1-self.id, i).values()).count(False)
      utility -= list(state.adj_bridges(self.id, i).values()).count(False)
    return utility