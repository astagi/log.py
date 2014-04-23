Log.py
======
When console.log and debugger fail all you need is a minimal server to log your messages

Usage
-----
Install dependencies

    $ pip install -r requirements.txt

Launch your server

    $ python log.py

Log a message

    var to_debug = {message : 'Hi!'};
    $.post("http://0.0.0.0:12345/log", to_debug,
        function(result){

        }
    );
