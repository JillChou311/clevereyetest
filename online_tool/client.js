
/* server setting*/
var MQTT_HOST = "s5-ns001.securepilot.com";
var MQTT_PORT = 80;
var SERVICE = "CVR";

/* client info settng*/
var CLIENT_ID = '700010073';
var CLIENT_USERNAME = '700010073';
var CLIENT_PWD = '22523301';

/* MQTT topic*/
var client_topic = 'client/' + CLIENT_ID + '/' + CLIENT_ID + '-' + SERVICE;
var system_topic = 'client/' + CLIENT_ID + '/' + CLIENT_ID + '-SYS';

var mqtt = require('mqtt');
var client  = mqtt.connect({'port': MQTT_PORT, 'host': MQTT_HOST,
                            'protocolId': 'MQIsdp', 'protocolVersion': 3, cmd: 'connect', 'clientId': CLIENT_ID,
                            'username': CLIENT_USERNAME, 'password': CLIENT_PWD});

client.on('connect', function () {
    console.log ('connect');
    client.subscribe(system_topic);
    client.subscribe(client_topic);
    client.publish('@SYS/notify/online', '{"client":' + '"' + CLIENT_ID + '-test-PC"}');
});
 
client.on('message', function (topic, message) {
    // message is Buffer 
    console.log ('--------------------------');
    console.log('topic: ' +  topic);
    console.log(message.toString());
    console.log(new Buffer(JSON.parse(message.toString()).content, 'base64').toString());
    console.log ('--------------------------');
});

client.on('error', function (e) {
    console.error ('error: ' + JSON.stringify(e)); 
});
