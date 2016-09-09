var _ = require('underscore')._;
var fs = require('fs');

var data = JSON.parse(fs.readFileSync(__dirname+"/dataset.json"))
var dir = "/tmp/sen/"
var list = []

_.each(data, function(record, key, list){
	_.each(record["translations"], function(value, engine, list){
		_.each(value["pair"], function(sen, key, list){

		if (sen.index(":")!=-1)
			console.log(sen)    		

		var filename = new Buffer(sen).toString('base64')
    		fs.writeFileSync(dir+filename, sen, 'utf-8')
    		list.push(dir+filename)
			
		}, this)
	}, this)
}, this)

fs.writeFileSync(dir+"list", "", 'utf-8')

_.each(list, function(value, key, list){
   fs.appendFileSync(dir+"list", value+"\n", 'utf-8')
}, this)
