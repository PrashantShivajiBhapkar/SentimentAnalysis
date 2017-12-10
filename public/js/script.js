var i = 1;
var list = [];
var temp = [];

for (i = 1; i < 40; i++) {
	temp = ['Test Word' + i, (Math.random()*100)];
	list.push(temp);
}

var canvasElem = document.getElementById('word_cloud_canvas');

var timer = setInterval(wordCloudTimer, 5000);

function wordCloudTimer() {
	if(WordCloud) {
		WordCloud(canvasElem, { list: list } );
	} else {
		clearInterval(timer);
	}	
}