# PROJECT X Æ A-12

This libary will contain functions to generate random strings, sentences, and paragraphs using Python. It is inspired by the recent rumours that Elon Musk and Grimes have named their newborn "X Æ A-12". I was talking to a friend and we joked that they must have used a random string generator to get that name. I then realized Python does come with a Random Integer module, but not a Random String module. I'm sure there are libraries out their, but I decided to make my own.

### Importing
*import xaea12 as xae*

### Functions

##### getString
xae.getString(int minLength, int maxLength, bool lowercase, bool caps, bool symbols, bool numbers)

Returns a random string of specified characters. By setting lowercase, caps, symbols, and numbers to True or False,
you can control which characters your string will be comprised of. Default values are:
-lowercase : True
-uppercase: False
-symbols: False
-numbers: False






### Definitions
The four character types specified above are lowercase, uppercase, symbols, and numbers.
Lowercase includes any of the following characters: abcdefghijklmnopqrstuvwxyz
Uppercase includes any of the following characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ
Numbers includes any of the following characters: 1234567890
Symbols includes any of the following characters: !@#$%^&*()~`,./<>?;:'"[]{}-=_+
