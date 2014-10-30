//handle button events and send data via websockets
$(document).ready(function () {
	var host,
		socket;

	if("WebSocket" in window) {
		connect();
	}

	function connect() {
		try {
			// NOTE: ensure this is write localhost address on connect
			host = 'ws://192.168.0.101:9001';
			socket = new WebSocket(host);
			console.log(socket.readyState);

			socket.onopen = function () {
				console.log('CONNECTED');
				// $('.button').bind('click', function (event) {
				// 	console.log('EVENT DATA: ' + event);
				console.log('sending down direction');
				socket.send('down');
				// });
			};

			socket.onmessage = function (msg) {

			};

			socket.onclose = function () {

			};
		} catch (e) {
			console.log('ERROR: ' + e);
		}

		function send(direction) {
			try {
				socket.send(direction);
				console.log('DIRECTION: ' + direction);
			} catch (e) {
				console.log('ERROR: direction data not able to send \n' + e);
			}
		}
	}
});