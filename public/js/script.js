var canvasElem = document.getElementById('word_cloud_canvas');
canvasElem.setAttribute('width', window.innerWidth);
canvasElem.setAttribute('height', window.innerHeight);

function readTextFile(file, callback) {
  var rawFile = new XMLHttpRequest();
  rawFile.overrideMimeType("application/json");
  rawFile.open("GET", file, true);
  rawFile.onreadystatechange = function() {
      if (rawFile.readyState === 4 && rawFile.status == "200") {
          callback(rawFile.responseText);
      }
  }
  rawFile.send(null);
}

function wordCloud(list) {
  WordCloud(canvasElem, { list: list } );
  var timer = setInterval(wordCloud, 5000, list);
}

function getWordCloudData() {
	readTextFile("/static/json/wordCloudData.json", function(text){
    var data = JSON.parse(text);
    var list = [], temp = [];
    for (d in data) {
    	temp = [d, data[d]];
    	list.push(temp);
    }
    wordCloud(list);
	});
}

getWordCloudData();