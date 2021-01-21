const bs = require("browser-sync").create();
const clipboardy = require('clipboardy');
const axios = require('axios');
const fs = require('fs');

let old_cb; 
let new_cb;

// Chooses dictionary, with a fallback on jisho.org
let url_re = /[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)?/gi;
let alt_dict = process.argv[2];
let dictionary = alt_dict && alt_dict.match(url_re) ? alt_dict : "https://jisho.org/search/";

// Overwrites index.html with starting message
fs.writeFile('index.html', init_msg(), 'utf8', () => {});

// Starts live-reload server
bs.init({
    server: "./"
});

// Checks for clipboard updates every 1000ms
update();
setInterval(update, 1000);


// Requests webpage with the clipboard as search input
async function update() {
	try {
		new_cb = clipboardy.readSync()
		if (old_cb != new_cb) {
			old_cb = new_cb
			const response = await axios.get(`${dictionary}${encodeURIComponent(new_cb)}`);
			fs.writeFile('index.html', response.data, 'utf8', () => {});
			bs.reload("index.html");
		}    
	} catch (error) {
		console.error(error);
	}
}


// Starting webpage. Uses a function for hoisting 
function init_msg() {
 	return `
	<style>
	body {
        color: rgb(209, 177, 144);
        font-family: Arial, sans-serif;
        background-color: rgb(34, 34, 34);
	}
    .placeholder {
        display: flex;
        flex-direction: column;
        justify-content: center;
		align-items: center;
    }
    .placeholder p {
        font-family: Verdana, Arial, sans-serif;
        color: rgb(209, 177, 144);
		max-width: 900px;
    }
	.placeholder p span {
		color: rgb(167, 164, 47);
	}
	.placeholder a {
		color: rgb(199, 92, 87);
	}
	.placeholder a:active {
		color: #ff7670;
	}
    </style>

	<div class="placeholder">
		<h3>Welcome to Cliptionary!</h3>

		<p><strong><u>Reload this page to begin automatic searching</strong></u>. (Ctrl+R) on Windows/Linux, (command+R) on Mac</u></strong></p>
		
		<p>If you accidentally close this tab, head over to terminal and copy/paste the URL into any browser. 
		<br> You'll likely want to use the URL labeled \`Local:\`, for example: https://localhost:3000</p>

		<p>To end clipboard monitoring, go back to your terminal and hit (Ctrl+C). <br>
		Mac users will also want to hit (control+C) not (command+C)</p>

		<p>To change your dictionary, simply provide it as an argument at runtime. <br>
		Example: <span style="font-family: monospace">node cliptionary.js https://www.dictionary.com/browse/</span></p>

		<p>Please note that errors while searching won't update your webpage. 
		Also, be sure your URL is the full URL for searching words on that dictionary</p>

		<a href="https://github.com/ryanjacquess/Cliptionary">Check out the open source code!</a>
	</div>`
}
