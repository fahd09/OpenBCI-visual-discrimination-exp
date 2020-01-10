# OpenBCI-visual-discrimination-exp
Experimenting with NodeJS and OpenBCI

# Instructions

First, install libraries:
```
npm install
pip install -r requirements.txt
```

If you don't have npm, install it first.

1- Attached electrodes to your head (or someone else's).
2- Run `node ganglion-lsl.js` in the terminal.
3- On a separate terminal session, run the experiment `python visual_disc_exp` or you can open psychopy and click on `Run` icon (the green icon on the top).
4- Go back to terminal and, in a new session, run `python lsl-record.py`
5- Start the experiment. When finished, just go back to the terminal sessions and press CTRL+C to terminate recordings. The files will be saved automatically.

Now you can run `jupyter notebook` and navigate to `analysis` to see the results.

You might experience some pain with bluetooth connection to the MacOS, in which case you need to install `noble-mac` library, separatly.