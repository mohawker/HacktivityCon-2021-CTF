# Scripting
## OTP Smasher
### Problem Type: Computer Vision Scripting
The challenge brings you to a webpage, with an image (of numbers), an input box and a counter. 

![](https://i.imgur.com/gVWCCyZ.png)

If you type in the correct number within the correct amount of time, the counter will increment. Our intuition was that once the counter reached a certain number, the page will show `flag.png`. (As corroborated by the source code - No screenshot)

We use `pwntools` to connect to the server and `pytesseract` for image_to_text OCR capabilities. Our final script looked something like this, where we repeatedly read the image to text, before sending it to the server. We had to use certain cv2 threshold values and the config `--psm 6 digits` for `image_to_string` to obtain accurate readings. 

![](https://i.imgur.com/bDOAU9A.png)

After 45 runs, we managed to obtain `flag.png`. The flag was also available on the webpage.

![](https://i.imgur.com/TktXx6o.png)

## Word Church
### Problem Type: LeetCode Problem ... with no complexity requirements :) 

You are presented with a 16 x 16 letter grid, and a given word. In order to pass the challenge, you have to enter the coordinates of each of the letters of the given word on the letter grid **30 times**. 

![](https://i.imgur.com/lO9J571.png)

Unleashing our inner *SWE*, we wrote this script out:
![](https://i.imgur.com/zaT4qJ8.png)
The solution runs in worst case *O(n^3)* time complexity surpringly. It traverses the entire grid, finds the first letter of the word, and checks all 8 directions of grid if the word can be found. 

Not my proudest leetcode solution (can definitely improve time and mem complexity), but Hey, it got the job done. 

Flag obtained was: flag{ac670e1f34da9eb748b3f241eb03f51b}





