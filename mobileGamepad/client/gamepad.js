//handle button events and send data via websockets
$(document).ready(function () {
	var host,
		socket;

	if("WebSocket" in window) {
		connect();
	}

	function connect() {
		try {
			// NOTE: ensure this is correct localhost address on connect
			host = 'ws://192.168.2.16:9001';
			socket = new WebSocket(host);
			console.log(socket.readyState);

			socket.onopen = function () {		
				console.log('CONNECTED');

				var d;
				$('button').bind('click', function (event) {			
					d = $(this).attr('id');
					console.log(d);
					send(d);
				});
			};

			socket.onmessage = function (msg) {
				//pass
			};

			socket.onclose = function () {
				//pass
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