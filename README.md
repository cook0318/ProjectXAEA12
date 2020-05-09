# PROJECT X Æ A-12

This libary will contain functions to generate random strings, sentences, and paragraphs using Python. It is inspired by the recent rumours that Elon Musk and Grimes have named their newborn "X Æ A-12". I was talking to a friend and we joked that they must have used a random string generator to get that name. I then realized Python does come with a Random Integer module, but not a Random String module. I'm sure there are libraries out their, but I decided to make my own.

### __Notes__

##### Importing
import xaea12 as xae

##### Getting single values
If you want a single character simply put a minLength & maxLength of 1 and a single character will be generated. By setting 3 of the character types to False and keeping one as True, you can specifically generate a lowercase letter, symbol, etc.

The same can be done for a one-word sentece. Set minWords & maxWords to 1 and a single word, with a capitalized first character and period will be generated.

### __Functions__

##### xae.getString(*int minLength, int maxLength, bool lowercase, bool caps, bool symbols, bool numbers*)

Returns a random string of specified characters. By setting lowercase, caps, symbols, and numbers to True or False,
you can control which characters your string will be comprised of. 

##### xae.getSentence(*int minWords, int maxWords, int minWordLength, int maxWordLength, bool lowercase, bool caps, bool symbols, bool numbers*):

Returns a random sentence with a length between minWords and maxWords. All other parameters are used to define the characters used for the strings in the sentece. Sentences will be returned with a capital letter and period.





### __Default Values__
-lowercase : True

-uppercase: False

-symbols: False

-numbers: False

-minWordLength: 3

-maxWordLength: 10

-minWords: 3

-maxWords: 10


### __Definitions__
The four character types specified above are lowercase, uppercase, symbols, and numbers.

Lowercase includes any of the following characters: abcdefghijklmnopqrstuvwxyz

Uppercase includes any of the following characters: ABCDEFGHIJKLMNOPQRSTUVWXYZ

Numbers includes any of the following characters: 1234567890

Symbols includes any of the following characters: !@#$%^&*()~`,./<>?;:'"[]{}-=_+
