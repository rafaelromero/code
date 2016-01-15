Pebble.addEventListener("ready",
    function(e) {
        console.log("zHello world! - Sent from your javascript application.");

        Pebble.getTimelineToken(function(token){console.log('token ' + token);},
				function(error){console.log('err ' + error);});

    }
);


