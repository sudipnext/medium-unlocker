const parseBtn = document.getElementById("parse-btn")
let purl = ""


parseBtn.addEventListener("click", function(){    
    chrome.tabs.query({active: true, currentWindow: true}, function(tabs){
        purl += tabs[0].url;
        window.open(`https://medium-unlocker.onrender.com/unlock/?url=${purl}`)
        purl = ""
    })
})
