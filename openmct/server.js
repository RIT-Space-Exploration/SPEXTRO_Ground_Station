var expressWs = require('express-ws');
var express = require('express');
var app = express();
expressWs(app);

var port = process.env.PORT || 8080

app.use(express.static(__dirname));

app.listen(port, function () {
	    console.log('Open MCT hosted at http://localhost:' + port);
});
