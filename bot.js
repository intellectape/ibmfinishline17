var Botkit = require('botkit');
var Forecast = require('forecast.io');

var forecast = new Forecast(options);
var scrape = require('./bot');

const SLACK_TOKEN = "";

//var childProcess = require("child_process");

var controller = Botkit.slackbot({
    debug: false
        //include "log: false" to disable logging
        //or a "logLevel" integer from 0 to 7 to adjust logging verbosity
});

// connect the bot to a stream of messages
controller.spawn({
    token: "",
}).startRTM()

// give the bot something to listen for.
//controller.hears('string or regex',['direct_message','direct_mention','mention'],function(bot,message) {
controller.on(['mention', 'direct_mention', 'direct_message'], function(bot, data) {
    var message = data.text;

    if (message == "Hello") {

    }

});