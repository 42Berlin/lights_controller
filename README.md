# lights_controller
Scripts that can be run to control the light veins in ground and first floor at 42 Berlin

## Resolume Arena

Lights veins are controlled via Resolume Arena, a lightweigth software that displays video clips on our light veins installation.  
Resolume Arena provides an API to remotely control the lights, which is available **from cluster computers** at 42 Berlin.

## API links

[API controller](http://10.11.250.225:8080/api/docs/example/)  
[API documentation](http://10.11.250.225:8080/api/docs/rest/)

## Example

`python3 lights_clip_connect.py 2 5`

This simply selects the clip on the 2nd row and 5th column of the [controller](http://10.11.250.225:8080/api/docs/example/), and the lights turns green!

![API controller](../media/lights_api_controller.png?raw=true)

How it works? It uses the [API](http://10.11.250.225:8080/api/docs/rest/) clip .../connect POST request, as below:

curl -X POST "http://10.11.250.225:8080/api/v1/composition/layers/2/clips/5/connect"

![API documentation](../media/lights_api_documentation.png?raw=true)

## What's next

You are more than welcome to contribute to this repository, you can make a pull request or contact us directly if you want to add your own scripts. **Have fun**, play around, and control the lights! 