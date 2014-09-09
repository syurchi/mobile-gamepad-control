//handle recieved direction through websockets
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
			console.log(socket.readyState);

			socket.onopen = function () {
				console.log(socket.readyState);
				console.log('CONNECTED');
			};

			socket.onmessage = function (direction) {
				console.log('MOVING: ' + direction);
				move(direction);
			};

			socket.onclose = function () {
				console.log('CLOSED');
			};
		} catch (e) {
			console.log('ERROR: ' + e);
		}
	}

	function move(d) {
		if(d == 'up')
			$('.square').animate({ 'up': '+=100px' }, 'fast' );
		else if(d == 'left')
			$('.square').animate({ 'left': '+=100px' }, 'fast' );
		else if(d == 'right')
			$('.square').animate({ 'right': '-=100px' }, 'fast' );
		else
			$('.square').animate({ 'down': '-=100px' }, 'fast' );
	}
});