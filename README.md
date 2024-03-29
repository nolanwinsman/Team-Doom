# ViZDoom [![PyPI version](https://badge.fury.io/py/vizdoom.svg)](https://badge.fury.io/py/vizdoom) ![Build](https://github.com/mwydmuch/ViZDoom/workflows/Build/badge.svg)

ViZDoom allows developing AI **bots that play Doom using only the visual information** (the screen buffer). It is primarily intended for research in machine visual learning, and deep reinforcement learning, in particular.

ViZDoom is based on [ZDoom](https://github.com/rheit/zdoom) to provide the game mechanics.

![vizdoom_deadly_corridor](http://www.cs.put.poznan.pl/mkempka/misc/vizdoom_gifs/vizdoom_corridor_segmentation.gif)


## Features
- Multi-platform (Linux, macOS, Windows),
- API for Python, C++, Lua, Java and Julia (thanks to [Jun Tian](https://github.com/findmyway)),
- Easy-to-create custom scenarios (visual editors, scripting language and examples available),
- Async and sync single-player and multi-player modes,
- Fast (up to 7000 fps in sync mode, single threaded),
- Lightweight (few MBs),
- Customizable resolution and rendering parameters,
- Access to the depth buffer (3D vision),
- Automatic labeling game objects visible in the frame,
- Off-screen rendering,
- Episodes recording,
- Time scaling in async mode.

ViZDoom API is **reinforcement learning** friendly (suitable also for learning from demonstration, apprenticeship learning or apprenticeship via inverse reinforcement learning, etc.).


## Cite as
> M Wydmuch, M Kempka & W Jaśkowski, ViZDoom Competitions: Playing Doom from Pixels, IEEE Transactions on Games, in print,
[arXiv:1809.03470](https://arxiv.org/abs/1809.03470)
```
@article{wydmuch2018vizdoom,
  title={ViZDoom Competitions: Playing Doom from Pixels},
  author={Wydmuch, Marek and Kempka, Micha{\l} and Ja{\'s}kowski, Wojciech},
  journal={IEEE Transactions on Games},
  year={2018},
  publisher={IEEE}
}
```
or

> M. Kempka, M. Wydmuch, G. Runc, J. Toczek & W. Jaśkowski, ViZDoom: A Doom-based AI Research Platform for Visual Reinforcement Learning, IEEE Conference on Computational Intelligence and Games, pp. 341-348, Santorini, Greece, 2016	([arXiv:1605.02097](http://arxiv.org/abs/1605.02097))
```
@inproceedings{Kempka2016ViZDoom,
  author    = {Micha{\l} Kempka and Marek Wydmuch and Grzegorz Runc and Jakub Toczek and Wojciech Ja\'skowski},
  title     = {{ViZDoom}: A {D}oom-based {AI} Research Platform for Visual Reinforcement Learning},
  booktitle = {IEEE Conference on Computational Intelligence and Games},  
  year      = {2016},
  url       = {http://arxiv.org/abs/1605.02097},
  address   = {Santorini, Greece},
  Month     = {Sep},
  Pages     = {341--348},
  Publisher = {IEEE},
  Note      = {The best paper award}
}
```


## Python quick start

### Ubuntu
```
sudo apt install cmake libboost-all-dev libsdl2-dev libfreetype6-dev libgl1-mesa-dev libglu1-mesa-dev libpng-dev libjpeg-dev libbz2-dev libfluidsynth-dev libgme-dev libopenal-dev zlib1g-dev timidity tar nasm
pip install vizdoom
```
(we recommend using at least Ubuntu 18.04+ with Python 3.7+)

### macOS
```
brew install cmake boost sdl2
pip install vizdoom
```
(we recommend using at least macOS High Sierra 10.13+ with Python 3.7+)


## Windows build
For Windows we are providing compiled runtime binaries and development libraries:

### [1.1.8pre](https://github.com/mwydmuch/ViZDoom/releases/tag/1.1.8pre) (2019-08-28):
- [Python 2.7 (64-bit)](https://github.com/mwydmuch/ViZDoom/releases/download/1.1.8pre/ViZDoom-1.1.8pre-Win-Python27-x86_64.zip)
- [Python 3.5 (64-bit)](https://github.com/mwydmuch/ViZDoom/releases/download/1.1.8pre/ViZDoom-1.1.8pre-Win-Python35-x86_64.zip)
- [Python 3.6 (64-bit)](https://github.com/mwydmuch/ViZDoom/releases/download/1.1.8pre/ViZDoom-1.1.8pre-Win-Python36-x86_64.zip)
- [Python 3.7 (64-bit)](https://github.com/mwydmuch/ViZDoom/releases/download/1.1.8pre/ViZDoom-1.1.8pre-Win-Python37-x86_64.zip)

See **[Installation of Windows binaries](doc/Building.md#windows_bin)**


## Building instructions

- **[PyPI (pip)](doc/Building.md#pypi)**
- [Linux](doc/Building.md#linux_build)
- [MacOS](doc/Building.md#macos_build)
- [Windows](doc/Building.md#windows_build)


## Examples

Before running the provided examples, make sure that [freedoom2.wad](https://freedoom.github.io/download.html) is placed in the same directory as the ViZDoom executable (on Linux and macOS it should be done automatically by the building process):

- [Python](examples/python) (contain learning examples implemented in PyTorch, TensorFlow and Theano)
- [C++](examples/c%2B%2B)
- [Julia](examples/julia)

Python examples are currently the richest, so we recommend to look at them, even if you plan to use other language. API is almost identical for all languages.

**See also the [tutorial](http://vizdoom.cs.put.edu.pl/tutorial).**


## Documentation

Detailed description of all types and methods:

- **[DoomGame](doc/DoomGame.md)**
- **[Types](doc/Types.md)**
- [Configuration files](doc/ConfigFile.md)
- [Exceptions](doc/Exceptions.md)
- [Utilities](doc/Utilities.md)

Additional documents:

- **[FAQ](doc/FAQ.md)**
- [Changelog](doc/Changelog.md) for 1.1.X version.

Also full documentation of engine and ACS scripting language can be found on
[ZDoom Wiki](https://zdoom.org/wiki/).

Useful parts:

- [ZDoom Wiki: ACS (scripting language)](https://zdoom.org/wiki/ACS)
- [ZDoom Wiki: CVARs (console variables)](https://zdoom.org/wiki/CVARs)
- [ZDoom Wiki: CCMD (console commands)](https://zdoom.org/wiki/CCMDs)


## Awesome Doom tools/projects

- [SLADE3](http://slade.mancubus.net/) - great Doom map (scenario) editor for Linux, MacOS and Windows.
- [Doom Builder 2](http://www.doombuilder.com/) - another great Doom map editor for Windows.
- [OBLIGE](http://oblige.sourceforge.net/) - Doom random map generator and [PyOblige](https://github.com/mwydmuch/PyOblige) is a simple Python wrapper for it.
- [Omgifol](https://github.com/devinacker/omgifol) - nice Python library for manipulating Doom maps.
- [NavDoom](https://github.com/agiantwhale/navdoom) - Maze navigation generator for ViZDoom (similar to DeepMind Lab).
- [MazeExplorer](https://github.com/microsoft/MazeExplorer) - More sophisticated maze navigation generator for ViZDoom.
- [ViZDoomGym](https://github.com/shakenes/vizdoomgym) - OpenAI Gym Wrapper for ViZDoom.
- [Sample Factory](https://github.com/alex-petrenko/sample-factory) - A high performance reinforcement learning framework for ViZDoom.

## Contributions

This project is maintained and developed in our free time. All bug fixes, new examples, scenarios and other contributions are welcome! We are also open to features ideas and design suggestions.


## License

Code original to ViZDoom is under MIT license. ZDoom uses code from several sources with [varying licensing schemes](http://zdoom.org/wiki/license).



## Modifications to ViZDoom

Our modifications to this code were to two of the main files

Doom.py
test.py

We added two more files to to improve ease of use when running the simulations and display data

Load_In_Data.py
graph-data.py


graph-data.py requires having completed multiple evaluations and the existence of results files

For demonstration purposes the scenario can be changed in the load_in_data.py default_data class. This is where most variables are changed. Towards the bottom is the skip_learning and skip_evaluation booleans. Both of these cannot be the same value.

For a user attempting to do learning for the first time, they need to run doom.py with skip_learning set to False and skip_evaluation set to True. The num loops variable towards the top of load_in_data.py specifies the number of training cycles that will be completed. 

After training is complete the user needs to rename the folders of the .pth files so they match the number at the end of each folder

Then swap the booleans and make sure the variables in load_in_data.py point to the correct folders and pth files.

After configuring all of the variables in load_in_data.py run: python doom.py and the simulations will start.

To see the data using graph-data.py create a list and append to the list similar to the examples given and set toChoose to the list you just created.


We have acted with honesty and integrity in producing this work and are unaware of anyone who has not.

Nolan Winsman, Ethan Poe, Tim Fields