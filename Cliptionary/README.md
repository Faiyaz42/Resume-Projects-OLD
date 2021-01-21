#         ![Logo](https://github.com/ryanjacquess/Cliptionary/blob/main/icon1.png)
Ever started reading in a new language only to quickly realize the importance of a dictionary crutch? Remember how irritated you got opening a new search window every second word?

Fear no more! Cliptionary has got your back. With automatic searches right from your clipboard, you can forget about manually searching every word!

The default dictionary is jisho.org. Specify your own dictionary as an optional argument
```sh
$ node ./watchClipboard.js
$ node ./watchClipboard.js https://www.dictionary.com/browse/
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
$ git clone https://github.com/ryanjacquess/Cliptionary
$ cd Cliptionary
$ npm install
$ node ./cliptionary.js
```
If you don't have brew, get it [here](https://brew.sh/#install)
Alternatively you could directly install [npm and node](https://www.npmjs.com/get-npm) from their website.
### Windows
In command line or powershell:
```sh
> git clone https://github.com/ryanjacquess/Cliptionary
> cd Cliptionary
> npm install
> node cliptionary.js
```

This project was made as a submission to HackEd 2021
