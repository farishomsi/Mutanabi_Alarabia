console.log('popup running');
setup();
function setup(){
  let bgpage = chrome.extension.getBackgroundPage();
   window.word = bgpage.word ;
  console.log(word);
}

async function postData(url = '', data = {}) {
  // Default options are marked with *
  const response = await fetch(url, {
    method: 'POST', // *GET, POST, PUT, DELETE, etc.
    mode: 'cors', // no-cors, *cors, same-origin
    cache: 'no-cache', // *default, no-cache, reload, force-cache, only-if-cached
    credentials: 'same-origin', // include, *same-origin, omit
    redirect: 'follow', // manual, *follow, error
    referrerPolicy: 'no-referrer', // no-referrer, *no-referrer-when-downgrade, origin, origin-when-cross-origin, same-origin, strict-origin, strict-origin-when-cross-origin, unsafe-url
    body: JSON.stringify(data) // body data type must match "Content-Type" header
  });
  return response.json(); // parses JSON response into native JavaScript objects
}

postData('http://osamafityani.pythonanywhere.com/',{dscr: window.word} ).then(summaryData=>{
  let sentenceScores = summaryData['stringSentenceScores'];
  let orderedSentences = summaryData['orderedSentences'];

  let sentencesSorted = Object.keys(sentenceScores).sort(function(a,b){return sentenceScores[a]-sentenceScores[b]}).reverse()

  let summarizationFactor = 1 - document.getElementById("sliderInput").value / 100;
  let selectRange = Math.floor(summarizationFactor * sentencesSorted.length);
  window.summary = '';

  let selectedSentences = sentencesSorted.slice(0,selectRange);


  for(let sentenceIndex in orderedSentences){
    if(selectedSentences.includes(orderedSentences[sentenceIndex])){
      window.summary += orderedSentences[sentenceIndex];
      window.summary +=' ';
    }
  }

  console.log(window.summary);

  document.getElementById("summaryText").value = window.summary;

        document.getElementById("sound").addEventListener("click", function(){
      var msg = new SpeechSynthesisUtterance();
        msg.text = window.summary;
        window.speechSynthesis.speak(msg);

        document.getElementById("sound").addEventListener("click", function(){
      window.speechSynthesis.cancel();
    });
    });

  return summaryData;


}).then(summaryData=>{

$('input[type="range"]').on("change mousemove", function () {
            var actualValue = 1 - Math.floor($(this).val() / 10) / 10;

            let sentenceScores = summaryData['stringSentenceScores'];
              console.log(sentenceScores);
              let orderedSentences = summaryData['orderedSentences'];
              console.log(orderedSentences)


              let sentencesSorted = Object.keys(sentenceScores).sort(function(a,b){return sentenceScores[a]-sentenceScores[b]}).reverse()

              let summarizationFactor = 1 - document.getElementById("sliderInput").value / 100;
              let selectRange = Math.floor(summarizationFactor * sentencesSorted.length);
              window.summary = '';

              let selectedSentences = sentencesSorted.slice(0,selectRange);


              for(let sentenceIndex in orderedSentences){
                if(selectedSentences.includes(orderedSentences[sentenceIndex])){
                  window.summary += orderedSentences[sentenceIndex];
                  window.summary +=' ';
                }
              }

              console.log(window.summary);

              document.getElementById("summaryText").value = summary;

              document.getElementById("sound").addEventListener("click", function(){
  var msg = new SpeechSynthesisUtterance();
    msg.text = window.summary;
    window.speechSynthesis.speak(msg);

    document.getElementById("sound").addEventListener("click", function(){
      window.speechSynthesis.cancel();
    });
});

        });
  });

