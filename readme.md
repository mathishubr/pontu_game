# FANORONA
The present repository contains open-source code from MIFY-AI, which has been adapted for the LINFO1361 assignment.


## Setup

The game was implemented in **Python** and works with versions greater than or equal to **3.6+**. Just clone this repository or download the zip to get everything you need to run the game.

### Get Python and dependencies


You can download the **3.6+** version of Python [here](https://www.python.org/downloads/).
(Don't forget to add python to the path if you are on Windows)

Next, install the dependencies for the game by running the following command (note that you may need to replace ```pip``` by ```pip3``` if you have different versions of python).


```bash
pip install -r requirements.txt
```

### Run the code

You can run a match by executing the ```main.py``` script as follows (you may need to replace ```python``` by ```python3``` if you have different versions of python). A dummy AI agent is given in ```random_agent.py```.


**Usage:**

      python main.py -ai0 ai_0.py -ai1 ai_1.py -s 0.5


      -ai0 
          path to the ai that will play as player 0
      -ai1 
           path to the ai that will play as player 1
      -s 
           time(in second) to show the board(or a move)
      -t
           total number of seconds credited to each agent


**Example:**

        python main.py -ai0 ai_0.py -ai1 ai_1.py -s 1.5

        python main.py -ai0 random_agent.py -ai1 random_agent.py -s 1

You can start the game by clicking ```Game > New Game``` (or ```Ctrl-N``` / ```Cmd-N```). At the end of the game, you can save it in a ```.trace``` file, which you can then replay by clicking ```Game > Load Game```.


### Allowed time for each AI
The ```-t``` option allows you to specify the overall time (in seconds) allowed for all AI moves of each agent. If an agent exceeds his budget, he automatically loses the game.

**Example:**

         python main.py -ai0 ai_0.py -ai1 ai_1.py -s 1.5 -t 120

         python main.py -ai0 random_agent.py -ai1 random_agent.py -s 1 -t 120