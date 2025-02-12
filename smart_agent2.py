from agent import AlphaBetaAgent
import time
import numpy as np

inf = float("inf")

def search(state, player, depth_lim, prune=True):
    """Perform a MiniMax/AlphaBeta search and return the best action.

    Arguments:
    state -- initial state
    player -- a concrete instance of class AlphaBetaPlayer
    prune -- whether to use AlphaBeta pruning

    """
    def max_value(state, alpha, beta, depth):
        if player.cutoff(state, depth, depth_lim):
            return player.evaluate(state), None
        val = -inf
        action = None
        for a, s in player.successors(state):
            v, _ = min_value(s, alpha, beta, depth + 1)
            if v > val:
                val = v
                action = a
                if prune:
                    if v >= beta:
                        return v, a
                    alpha = max(alpha, v)
        return val, action

    def min_value(state, alpha, beta, depth):
        if player.cutoff(state, depth, depth_lim):
            return player.evaluate(state), None
        val = inf
        action = None
        for a, s in player.successors(state):
            v, _ = max_value(s, alpha, beta, depth + 1)
            if v < val:
                val = v
                action = a
                if prune:
                    if v <= alpha:
                        return v, a
                    beta = min(beta, v)
        return val, action

    _, action = max_value(state, -inf, inf, 0)
    return action



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
    time_spent = 0
    depth_lim = 1
    exe_time = 0
    while time_spent + exe_time * 480 ** (1/2) <= 0.4 * self.time_left:
       exe_time = time.time()
       action = search(state, self, depth_lim)
       exe_time = time.time() - exe_time
       time_spent += exe_time
       depth_lim += 1
    
    return action

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
    return succ

  """
  The cutoff function returns true if the alpha-beta/minimax
  search has to stop and false otherwise.
  """
  def cutoff(self, state, depth, depth_lim):
    return state.game_over() or depth == depth_lim

  """
  The evaluate function must return an integer value
  representing the utility function of the board.
  """
  def evaluate(self, state):
    utility = 0
    for i in range(3) :
      utility += len(state.move_dir(self.id, i)) - 2 * len(state.move_dir(1 - self.id, i))
      adj_bridges_min = state.adj_bridges(1 - self.id, i)
#      adj_bridges_max = state.adj_bridges(self.id, i)
      if list(adj_bridges_min.values()).count(False) == 4:
        utility += 1
#      if list(adj_bridges_max.values()).count(False) == 4:
#        utility -= 1
    return utility