var measure_en = require("./en/bleu.js");
var measure_ru = require("./ru/bleu.js");
var fs = require('fs');
var json = JSON.parse(fs.readFileSync('../dataset.json', 'utf8'));
var n = json.length;

for(var i = 0; i<n; i++) {
 var str1 = json[i].source_acronym_resolved[0]; 
 var str2 = json[i].source_acronym_resolved[1];
 var dist = {
	"bleu_lin_1": measure_ru.bleu(str1, str2, 1, "lin"),
	"bleu_lin_2": measure_ru.bleu(str1, str2, 2, "lin"),
	"bleu_lin_3": measure_ru.bleu(str1, str2, 3, "lin"),
	"bleu_lin_4": (measure_ru.bleu(str1, str2, 3, "lin")==1 && measure_ru.bleu(str1, str2, 4, "lin")==0)? 1:measure_ru.bleu(str1, str2, 4, "lin"),   

	"bleu_def_1": measure_ru.bleu(str1, str2, 1, "def"),
	"bleu_def_2": measure_ru.bleu(str1, str2, 2, "def"),
	"bleu_def_3": measure_ru.bleu(str1, str2, 3, "def"),
	"bleu_def_4": (measure_ru.bleu(str1, str2, 3, "def")==1 && measure_ru.bleu(str1, str2, 4, "def")==0)? 1:measure_ru.bleu(str1, str2, 4, "def"),   

	"bleu_nist_1": measure_ru.bleu(str1, str2, 1, "nist"),
	"bleu_nist_2": measure_ru.bleu(str1, str2, 2, "nist"),
	"bleu_nist_3": measure_ru.bleu(str1, str2, 3, "nist"),
	"bleu_nist_4": (measure_ru.bleu(str1, str2, 3, "nist")==1 && measure_ru.bleu(str1, str2, 4, "nist")==0)? 1:measure_ru.bleu(str1, str2, 4, "nist")
 }
 json[i].blue_metrics = dist;

 var arr = [json[i].translations.google, json[i].translations.microsoft, json[i].translations.yandex];
 for (var x = 0; x < 3; x++) {
  var str1 = arr[x].pair[0]; 
  var str2 = arr[x].pair[1];
  var dist = {
	"bleu_lin_1": measure_en.bleu(str1, str2, 1, "lin"),
	"bleu_lin_2": measure_en.bleu(str1, str2, 2, "lin"),
	"bleu_lin_3": measure_en.bleu(str1, str2, 3, "lin"),
	"bleu_lin_4": measure_en.bleu(str1, str2, 4, "lin"),

	"bleu_def_1": measure_en.bleu(str1, str2, 1, "def"),
	"bleu_def_2": measure_en.bleu(str1, str2, 2, "def"),
	"bleu_def_3": measure_en.bleu(str1, str2, 3, "def"),
	"bleu_def_4": measure_en.bleu(str1, str2, 4, "def"),

	"bleu_nist_1": measure_en.bleu(str1, str2, 1, "nist"),
	"bleu_nist_2": measure_en.bleu(str1, str2, 2, "nist"),
	"bleu_nist_3": measure_en.bleu(str1, str2, 3, "nist"),
	"bleu_nist_4": measure_en.bleu(str1, str2, 4, "nist"),

	"bleu_k-based_1": measure_en.bleu(str1, str2, 1, "k-based"),
	"bleu_k-based_2": measure_en.bleu(str1, str2, 2, "k-based"),
	"bleu_k-based_3": measure_en.bleu(str1, str2, 3, "k-based"),
	"bleu_k-based_4": measure_en.bleu(str1, str2, 4, "k-based")
  }
  arr[x].blue_metrics = dist; 
 }
}

console.log(JSON.stringify(json, null, 1));

