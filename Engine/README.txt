This is the cpu-only Windows-only version submitted to Gomocup.


----SUPPORTED-COMMANDS----

--Gomocup-protocol--
INFO
--------INFO max_memory 	works only if specified before starting a game (before BEGIN, TURN or BOARD). If one wants to change the settings afterwards, a restart of a program is required.
--------INFO max_memory 0	specifying 0 means no memory limit, in such case the program will use 75% of total system memory, half of which is allocated at start, the rest lazily over the course of the game.
START
--------START 15		only board 15x15 is supported for standard rules.
--------START 20		only board 20x20 is supported for freestyle rules.
RESTART
BEGIN	\
BOARD	| - the search resources will be allocated after first of those methods
TURN	/
TAKEBACK
--------this command might not be implemented correctly as the protocol description does not exactly matches with piskvork behaviour. But the program would remove given stone from its internal state and respond OK.
END
ABOUT

--Gomocup-protocol-extension--
SWAP2BOARD

--YixinBoard---
YXSHOWINFO - used to determine if YixinBoard is used to properly print principal variation MESSAGE

--additional-commands--
PONDER - controls pondering, can be used in three ways
1-------PONDER 		turns on infinite pondering
2-------PONDER [time]	turns on pondering for certain period of time ([time] in milliseconds),
3-------PONDER stop	stops pondering

--commands-send-by-program--
MESSAGE
--------After every turn program sends message summarizing the search results.
	For example 'MESSAGE depth 1-14 ev 56.2 n 3381 n/s 932 tm 3627 pv Oe4 Xe3 Of4 Xg4 Oh5 Xc3 Od3 Xf2 Oc5 Xg3 Og2 Xe1 Oh4 Xb2'
	--------depth [x]-[y] is the minimal (x) and maximal (y) depth of the search (minimal is always 1)
	--------ev [x] is the current probability of winning in %
	--------n [x] is the number of nodes evaluated (not necesarily the number of nodes in the tree)
	--------n/s [x] is the number of nodes evaluated per second (not necesarily the number of neural network evaluations, some nodes are evaluated without it)
	--------tm [x] is the time used for this turn (in milliseconds)
	--------pv [list] is the principal variation, in piskvork format or YixinBoard format, depending on which is being used.
ERROR
UNKNOWN


--CONFIG-FILE--
The default config file (for Gomocup) looks like this:
logging=0
pondering=0
gomocup=1
threads=1
devices=-1

--logging	accepts 0 or 1 and turns off/on logging to file. The logfile will contain the protocol commands and detailed info about the MCTS search results. Note that the program does not cleanup the logs!
--pondering	accepts 0 or 1 and turns off/on automatic pondering during opponent time. It works like if the manager would send PONDER command after every programs turn.
--gomocup	accepts 0 or 1 and switches between using Gomoku-specific features (for 1) and not using them (for 0). Note that Gomocup version networks require this to be set to 1, while the 'full' version networks should have this set to 0.
--threads	accepts integer > 0 specifies the number of threads used by the program. It has two meanings:
		--------if running on CPU, there is always single search thread, and 'threads' parameter controls the number of threads used for neural network calculations. Setting more than 4 threads provide diminishing returns on *most* computers (might not be your case).
		--------if running on GPU, 'threads' parameter controls the number of search threads. Note that with multi-gpu setup, the number of threads should be at least equal to the number of gpus. Sometimes you can get some speedup if you use 2 threads per GPU.
--devices	accepts integers separated by space, the numbers refer to the indices of particular device
		--------CPU has always -1 index
		--------NVIDIA GPUs have indices starting from 0. For example if having 2 GPUs in the system, the config will look like this 'devices=0 1'
		--------Specifying both -1 (CPU) and for example 0 (GPU) is undefined. You should always use only one type of device.
		--------The program will print MESSAGE on startup with all detected devices.
			--------For example 'MESSAGE Detected following devices : CPU : GenuineIntel : 4 x AVX2 with 16252MB of memory'
		--------Next MESSAGE will contain list of devices that will be used.
			--------For example 'MESSAGE Using : CPU : GenuineIntel : 4 x AVX2 with 16252MB of memory'