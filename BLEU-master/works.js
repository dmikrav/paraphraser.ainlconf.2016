var fs = require('fs');
var json = JSON.parse(fs.readFileSync('../dataset.json', 'utf8'));

var n = json.length;

for(var i = 0; i<n; i++) {
 console.log(i);
 console.log(json[i].translations.google.pair);
 console.log(json[i].translations.microsoft.pair);
 console.log(json[i].translations.yandex.pair);
}
