#         ![Logo](https://github.com/ryanjacquess/Cliptionary/blob/main/icon1.png)
Ever started reading in a new language only to quickly realize the importance of a dictionary crutch? Remember how irritated you got opening a new search window every second word?

Fear no more! Cliptionary has got your back. With automatic searches right from your clipboard, you can forget about manually searching every word!

## <em> Just highlight , right-click and copy the text on screen and you will see your definition/translation pop up on the dictionary tab that has been opened.* </em>

The default dictionary is jisho.org. Specify your own dictionary as an optional argument
```sh
$ node ./cliptionary.js
$ node ./cliptionary.js https://www.dictionary.com/browse/
```
Pretty useful anytime you're constantly searching up words in the same language. From Shakespeare plays to visual novels to Japanese light novels, Cliptionary automates your repetitive search actions. We particularly recommend using it in split screen with your source text!

## Setting up
Cliptionary requires the following dependencies to be installed on your system:
 - git
 - npm
 - node.js

### macOS with homebrew
In terminal:
```sh
$ brew install node
$ git clone this repo or download and extract the Cliptionary folder to your desktop directory
$ cd Cliptionary (or enter the directory it is saved in)
$ npm install
$ node ./cliptionary.js
```
If you don't have brew, get it [here](https://brew.sh/#install)
Alternatively you could directly install [npm and node](https://www.npmjs.com/get-npm) from their website.
### Windows
In command line or powershell:
```sh
> git clone this repo or download and extract the Cliptionary folder to your desktop directory
> cd desktop/Cliptionary (or enter the directory it is saved in)
> npm install
> node cliptionary.js
```
*Sometimes the dictionary tab might not open ,in that case, just close the command line or terminal and re-run node Cliptionary.js for windows or node ./Cliptionary.js for macOS in the Cliptionary directory.

<!--This project was made as a submission to HackEd 2021.
