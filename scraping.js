var osmosis = require('osmosis');
const request = require("tinyreq");
const cheerio = require("cheerio");

var userURL = "https://www.miniclip.com/games/page/en/privacy-policy/";
var jsonP = [];

request(userURL, function(err, body, callback) {
    //console.log(err || body); // Print out the HTML
    // Parse the HTML 
    let $ = cheerio.load(body);

    // Take the h2.title element and show the text

    jsonP.push($("p").text());
    console.log(jsonP.length);
});

console.log(jsonP);