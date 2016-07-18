# State Server Solution

With the state server, you can pass a set of coordinates and find out which state those coordinates fall into.
There are no special libraries needed to run the application, just Python 2.7.5 or higher.

## Using State Server

You can spawn a server instance by going to the root folder and doing the following:

  $ ./state-server

With a second terminal you can issue a curl command:

  $ curl  -d "longitude=-77.036133&latitude=40.513799" http://localhost:8080/

Which in this instance return "Pennsylvania". If invalid data is passed or no state for the given
coordinates is found, a 400 error is returned with a corresponding error message.

## Testing

There are unit tests that go along with the state server. They can be run before starting the
server by including the optional parameter "test" in state-server like so, or individually:

  $ ./state-server test

or

  $ python state_tests.py


