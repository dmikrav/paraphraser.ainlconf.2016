var natural = require('natural');
var _ = require('underscore')._;

function mngrp(can, refm, n, smooth)
{
  canstr = can.toLowerCase()
  refmstr = refm.toLowerCase()

  if (n == 0)
    throw new Error("mngrp: n = 0")

  // var tokenizer = new natural.RegexpTokenizer({pattern: /[^a-zA-Z0-9\-\?]+/});


  var can = natural.NGrams.ngrams(canstr.split(" "), n)
  var refm = natural.NGrams.ngrams(refmstr.split(" "), n)

  var refh = {}
  _.each(refm, function(value, key, list){
    if (!(value in refh))
        refh[value] = 0
  
    refh[value] += 1
  }, this)

  var m = 0
  _.each(can, function(ngr, key, list){
    // ngr = ngr
    if (ngr in refh)
    {
      if (refh[ngr] > 0)
        {
        m += 1
        refh[ngr] -= 1
        }
    }
  }, this)

  if (smooth == "lin")
  {
    if (n>1)
      return  (m+1)/(can.length+1)
    else
      return  m/can.length
  }

  if (smooth == "def")
  {
    if (m == 0)
      return  Number.EPSILON/can.length
    else
      return  m/can.length
  }

  if (smooth == "nist")
  {
    if (m == 0)
      return 1/Math.pow(2,n)/can.length
    else
      return  m/can.length
  }

  if (smooth == "k-based")
  {
    if (m == 0)
      return 1/Math.pow(5/(Math.log(refmstr.split(" ").length)),n)/can.length
    else
      return  m/can.length
  }
}

function brevity(can, ref)
{
  can = can.toLowerCase()
  ref = ref.toLowerCase()

  var can = natural.NGrams.ngrams(can.split(" "), 1)
  var ref = natural.NGrams.ngrams(ref.split(" "), 1)

  // console.log("BLEU: brevity: can.length: "+can.length)
  // console.log("BLEU: brevity: ref.length: "+ref.length)
  
  var ex = Math.exp(1-ref.length/can.length)
  // console.log("BLEU: brevity: ex: "+ex)

  return _.min([1, ex])
}

function bleu(can, ref, maxg, smooth)
{
  can = can.toLowerCase()
  ref = ref.toLowerCase()

  can = can.replace(/[!@#$%^&*()<>.,?!+=~`'/":{}-]/g, " ").replace( /\s\s+/g,' ').trim()
  ref = ref.replace(/[!@#$%^&*()<>.,?!+=~`'/":{}-]/g, " ").replace( /\s\s+/g,' ').trim()

  // console.log("BLEU: can: "+can)
  // console.log("BLEU: ref: "+ref)

  var P = 1

  _(maxg).times(function(n){ 
    var temp = mngrp(can, ref, n+1, smooth)
    // console.log("BLEU: P_"+(n+1)+": "+temp)
    P *= temp
  });

  // console.log("P="+P)
  P = Math.pow(P,1/maxg)  

  // console.log("BLEU: exp P="+P)

  var brev = brevity(can, ref)
  // console.log("BLEU: brevity: "+brev)

  if (_.isFinite(P*brev))
    return P*brev
  else
    return 0
  // return P
}

module.exports = {
  bleu:bleu
}
/*
console.log(bleu("show must go on", "show must go off", 1, "lin"))
console.log(bleu("show must go on", "show must go off", 2, "lin"))
console.log(bleu("show must go on", "show must go off", 3, "lin"))
console.log(bleu("show must go on", "show must go off", 4, "lin"))

console.log(bleu("show must go on", "show must go off", 1, "def"))
console.log(bleu("show must go on", "show must go off", 2, "def"))
console.log(bleu("show must go on", "show must go off", 3, "def"))
console.log(bleu("show must go on", "show must go off", 4, "def"))

console.log(bleu("show must go on", "show must go off", 1, "nist"))
console.log(bleu("show must go on", "show must go off", 2, "nist"))
console.log(bleu("show must go on", "show must go off", 3, "nist"))
console.log(bleu("show must go on", "show must go off", 4, "nist"))

console.log(bleu("show must go on", "show must go off", 1, "k-based"))
console.log(bleu("show must go on", "show must go off", 2, "k-based"))
console.log(bleu("show must go on", "show must go off", 3, "k-based"))
console.log(bleu("show must go on", "show must go off", 4, "k-based"))
*/