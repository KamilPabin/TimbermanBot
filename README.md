# Timberman Bot

This is a proof of concept script that allows computer to play the Timberman VS game.

### Requirements

This scripts uses `python3` and virtual environment. To use it please first install python3.  
Libraries used by this script:
1. mss,
2. keyboard,
3. PIL (Python Image Library),
4. time.

### How to use it
When running for the first time:
1. Start by going to the `TimbermanBot` directory,
2. Initialize virtual environment `python3 -m venv env`,
3. Source environment `source env/bin/activate`,
4. Install required libraries,
    * `pip install mss`,
    * `pip install time`,
    * `pip install keyboard`,
    * `pip install PIL`.
    
If virtual environment exists just call `source env/bin/activate`

To start the script run `python3 main.py`

At this point script should wait for the input from the user.
To start first maximize Timberman VS and start the game. After starting the game wait until 
a countdown disappears, then press _S_ key, script should start chopping the tree. 

### How it works
Script starts by taking a screenshot of the entire tree and build virtual representation of the tree by looking at the branches.
First two logs never have branches, so they are skipped during tree building. Then as the tree is chopped, script scans the tree 
at the height of fifth log to avoid false positive detection of the branch that could be triggered by recently chopped log.
Log scanning is a simple screenshot, which then is converted to grayscale image, which is then passed by low pass filter. To find if log
has a branch it's just a matter of checking if resulting image contains any black pixels.  

### Limitations
As this is a proof of concept the scripts is currently limited to 1440x900p resolution.
The speed at which tree can be chopped is only limited by the game animation, which is theoretical maximum.


### Troubleshooting
If you have any problems with running the script please try by upgrading pip `pip install --upgrade pip`,
and then reinstalling required libraries.