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
    if self.id == state.get_cur_player():
      succ.sort(key=lambda x: self.evaluate(x[1]), reverse=True)
    elif self.id == (1 - state.get_cur_player()):
      succ.sort(key=lambda x: self.evaluate(x[1]))
    # if len(succ) > 40:
    #   return succ[:40]
    return succ[:len(succ)//4]

  """
  The cutoff function returns true if the alpha-beta/minimax
  search has to stop and false otherwise.
  """
  def cutoff(self, state, depth):
    return state.game_over() or depth == 5

  """
  The evaluate function must return an integer value
  representing the utility function of the board.
  """
  def evaluate(self, state):
    utility = 0
    for i in range(3) :
      adj_bridges_max = state.adj_bridges(self.id, i)
      adj_bridges_min = state.adj_bridges(1 - self.id, i)
      adj_pawns_max = state.adj_pawns(self.id, i)
      adj_pawns_min = state.adj_pawns(1 - self.id, i)
      utility += 5 * list(adj_bridges_min.values()).count(False)
      utility -= 4 * list(adj_bridges_max.values()).count(False)
      for key in adj_bridges_max:
        if adj_bridges_min[key] and adj_pawns_min[key]:
          utility += 3
        if adj_bridges_max[key] and adj_pawns_max[key]:
          utility -= 3
      # if len(state.move_dir(1 - self.id, i)) <= 1:
      #   utility += 1
      # if len(state.move_dir(self.id, i)) <= 1:
      #   utility -= 1
      # if list(adj_bridges_min.values()).count(False) == 4:
      #   utility += 1
    return utility