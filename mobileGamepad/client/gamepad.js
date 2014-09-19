//handle button events and send data via websockets
$(document).ready(function () {
	var host,
		socket;

	if("WebSocket" in window) {
		connect();
	}

	function connect() {
		try {
			host = 'ws://0.0.0.0:9001';
			socket = new WebSocket(host);

			socket.onopen = function () {
				$('.button').bind('click', function (event) {
					console.log('EVENT DATA: ' + event);
					socket.send('down');
				});
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

		// $('.button').click(function (event) {
		// console.log('EVENT DATA: ' + event);
		// send('down');
		// });
	}
});