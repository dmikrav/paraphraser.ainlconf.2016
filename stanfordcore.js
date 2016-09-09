var _ = require('underscore')._;
var fs = require('fs');
var md5 = require('md5');

var data = JSON.parse(fs.readFileSync(__dirname+"/dataset.json"))
var dir = "/tmp/sen/"
var listt = []

_.each(data, function(record, key, list){
	_.each(record["translations"], function(value, engine, list){
		_.each(value["pair"], function(sen, key, list){

		var filename = md5(sen)
	
		

		if (sen.indexOf(":")!=-1)
			sen = sen.substring(sen.indexOf(":")+1)
	
    		fs.writeFileSync(dir+filename, sen, 'utf-8')
    		listt.push(dir+filename)
			
		}, this)
	}, this)
}, this)

fs.writeFileSync(dir+"list", "", 'utf-8')

_.each(listt, function(value, key, list){
   fs.appendFileSync(dir+"list", value+"\n", 'utf-8')
}, this)
