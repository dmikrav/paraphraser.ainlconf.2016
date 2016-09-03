var _ = require('underscore')._;
var fs = require('fs');
var async = require('async');

var data = JSON.parse(fs.readFileSync("/tmp/yandex"))
// var data = JSON.parse(fs.readFileSync(__dirname+"/merged.json"))

var total = data.length
var cur = 0


async.eachSeries(data, function(value, callback){ 

  cur += 1
    
  if (!("yandex" in value["translations"]))
  {
    yandex.translate(value["source"][0], { to: "en", from: "ru" }, function(err, res) {
      tr1 = res.text[0]
      
      yandex.translate(value["source"][1], { to: "en", from: "ru" }, function(err, res1) {
        tr2 = res1.text[0]
      
        console.log(cur +" from "+total)
        value["translations"]["yandex"] = {"pair":[tr1, tr2]}
        fs.writeFileSync("/tmp/yandex_new", JSON.stringify(data, null, 4), 'utf-8')

        callback()
      });
    });
  }
  else
  {
    async.setImmediate(function () {
      callback(null);
    });
  }

  }, 
    function(err){      
      console.log(JSON.stringify(data, null, 4))
      process.exit(0)
  })
