//where we will handle button events and send data via websockets
$(document).ready(function () {

	function create() {
		var host = 'ws://localhost:9000/socketHandler.py';
		var socket = new WebSocket(host);
	}
});