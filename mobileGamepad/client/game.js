//handle recieved direction through websockets
$(document).ready(function () {
	var host,
		socket;

	connect();

	function connect() {
		try {
			host = 'ws://0.0.0.0:9001';
			socket = new WebSocket(host);

			socket.onopen = function () {
				console.log('CONNECTED');
			};

			socket.onmessage = function (data) {
				var direction 
				direction = parse(data.data);
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
			$('.square').animate({ 'marginTop': '-=100px' }, 'fast' );
		else if(d == 'left')
			$('.square').animate({ 'marginLeft': '-=100px' }, 'fast' );
		else if(d == 'right')
			$('.square').animate({ 'marginLeft': '+=100px' }, 'fast' );
		else
			$('.square').animate({ 'marginTop': '+=100px' }, 'fast' );
	}

	function parse(d) {
		str = d.split(/\W/).join();
		str = str.replace(/\,/g, '');
		return str;
	}
});