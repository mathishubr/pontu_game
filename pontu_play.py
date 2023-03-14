from pontu_tools import *
import argparse

if __name__ == '__main__':
  parser = argparse.ArgumentParser()
  parser.add_argument("-ai0", help="path to the ai that will play as player 0")
  parser.add_argument("-ai1", help="path to the ai that will play as player 1")
  parser.add_argument("-t", help="time out: total number of seconds credited to each AI player")
  parser.add_argument("-f", help="indicates the player (0 or 1) that plays first; random otherwise")
  args = parser.parse_args()

  agent0 = args.ai0 if args.ai0 != None else "human_agent"
  agent1 = args.ai1 if args.ai1 != None else "human_agent"
  time_out = float(args.t) if args.t != None else 900.0
  first = int(args.f) if args.f == '1' or args.f == '0' else None

  initial_state = PontuState()
  if first is not None:
    initial_state.cur_player = first
  agent0 = getattr(__import__(agent0), 'MyAgent')()
  agent0.set_id(0)
  agent1 = getattr(__import__(agent1), 'MyAgent')()
  agent1.set_id(1)
  res = play_game(initial_state, [agent0.get_name(), agent1.get_name()], [agent0, agent1], time_out)
  print(res)
