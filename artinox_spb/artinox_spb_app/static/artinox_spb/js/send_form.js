'use strict'

let httpRequest;
httpRequest.overrideMimeType('text/html')

if (window.XMLHttpRequest) {
	httpRequest = new XMLHttpRequest();
} else if (window.ActiveXObject) {
	httpRequest = new ActiveXObject("Microsoft.XMLHTTP")
}

