window.onload = function() {
	var url = "https://github.com/nanyangcheng/chengpeng.github.io/blob/master/head_first_html5/chapter6/sales.json";
	var request = new XMLHttpRequest();
	request.open("GET", url);
	request.onload = function() {
		if (request.status == 200) {
			updateSales(request.responseText);
		}
	};
	request.send(null);
}

function updateSales(responseText) {
	var salesDiv = document.getElementById("sales");
	var sales = JSON.parse(responseText);
	salesDiv.innerHTML = responseText;
	}
}