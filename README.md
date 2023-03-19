# Raspberry-Pi-Door-Camera-DropboxAPI-Automation
A Python script for a Raspberry Pi project that automates the opening and closing of a door at specified times and captures photos during that time frame using a servo motor, a camera, and uploading photos to Dropbox API.


<h1>Raspberry Pi Door Automation</h1>
<p>This is a Python script for a Raspberry Pi project that uses a servo motor, a camera, and a Dropbox API to automate the opening and closing of a door at specified times and capture photos during that time frame.</p>
<h2>Tools and Libraries</h2>
<p>The script requires the following tools and libraries:</p>
<ul>
  <li><strong>dropbox</strong></li>
  <li><strong>RPi.GPIO</strong></li>
  <li><strong>time</strong></li>
  <li><strong>datetime</strong></li>
  <li><strong>picamera</strong></li>
</ul>
<h2>Usage</h2>
<ol>
  <li>Connect the servo motor and fan to the GPIO pins of the Raspberry Pi.</li>
  <li>Create a Dropbox account and generate an access token.</li>
  <li>Update the <code>timesets</code> list with the desired times to open the door.</li>
  <li>Update the <code>NO_Of_Seconds</code> variable with the desired time to keep the door open and capture photos.</li>
  <li>Update the <code>access_token</code> variable with the Dropbox access token.</li>
  <li>Run the script.</li>
</ol>
<p>The script will continuously check the current time and if it matches any of the times in the <code>timesets</code> list, the servo motor moves the door, the fan turns on, the camera takes photos and uploads them to Dropbox. After the specified number of seconds, the servo motor moves the door back to its initial position, the fan turns off, and the GPIO pins are cleaned up.</p>
