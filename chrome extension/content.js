console.log('content file running');

window.addEventListener('mouseup',wordSelected);

function wordSelected(){
  console.log("word SELECTED");
  let selectedText = window.getSelection().toString();
  console.log(selectedText);
  if (selectedText.length > 0){
    let message ={
      text : selectedText
    };
      chrome.runtime.sendMessage(message);
  }
}