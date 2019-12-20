from io import BytesIO
from PIL import Image, ImageDraw  # Requires pip3 install pillow
from pyfiglet import figlet_format  # Requires pip3 install pyfiglet
from urllib.request import urlopen
import bz2
import pickle
import re
import requests  # Requires pip3 install requests
import zipfile


# http://www.pythonchallenge.com/pc/def/0.html
def challenge_zero():
    print('2^38 = ' + str(2 ** 38))
    answer = 'Answer: ' + str(2 ** 38)
    print(answer)
    url = 'The next challenge is at http://www.pythonchallenge.com/pc/def/274877906944.html'
    print(url)


# http://www.pythonchallenge.com/pc/def/map.html
def challenge_one():
    html = urlopen("http://www.pythonchallenge.com/pc/def/map.html")
    content = html.read().decode('utf-8')
    coded_message = re.findall("f000f0\">(.*?)</tr>", content, re.DOTALL)[-1]
    coded_url = "map"
    message_trans = coded_message.maketrans(
        "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
    )
    new_url = coded_url.maketrans(
        "abcdefghijklmnopqrstuvwxyz", "cdefghijklmnopqrstuvwxyzab"
    )
    message = '' + coded_message.translate(message_trans)
    message = coded_message.translate(message_trans)
    empt = []

    for index, letter in enumerate(message):
        if index % 78 == 0:
            empt.append('\n')
        empt.append(letter)

    message = "\n\nDecoded message: " + ''.join(empt)
    url = 'The next challenge is at http://www.pythonchallenge.com/pc/def/ocr.html'

    print(
        '\n\n--1) Go to the url:\nhtml = urlopen("http://www.pythonchallenge'
        '.com/pc/def/map.html")'
    )
    print(
        "\n\n--2) Retrieve the content from the url:\ncontent = html.read().d"
        "ecode('utf-8')"
    )
    print(
        "\n\n--3) Parse the data from the url in order to retrieve the coded"
        "\nmessage:\ncoded_message = re.findall('f000f0\\'>(.*?)</tr>', conte"
        "nt, re.DOTALL)[-1]\n\nCoded message:"
        + coded_message
    )
    print(
        "\n\n--4) Use str.maketrans() and str.translate() to shift the alphabet"
        "\nby two characters in order to decode the message:\nmessage_trans ="
        " coded_message.maketrans('abcdefghijklmnopqrstuvwxyz', 'cdefghijklmn"
        "opqrstuvwxyzab')\ndecoded_message = coded_message.translate(message_"
        "trans)"
    )
    print(message)
    print(
        "\n\n--5) After applying this method to the url (where it says 'map')"
        " we get our answer."
    )
    print("\n\nAnswer: " + coded_url.translate(new_url))
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


# http://www.pythonchallenge.com/pc/def/ocr.html
def challenge_two():
    html = urlopen("http://www.pythonchallenge.com/pc/def/ocr.html")
    content = html.read().decode('utf-8')
    data = re.findall(r"<!--(.*?)-->", content, re.DOTALL)[-1]
    answer = "".join(re.findall("[a-z]", data))
    url = 'http://www.pythonchallenge.com/pc/def/equality.html'

    print(
        '\n\n--1) Go to the url:\nhtml = urlopen("http://www.pythonchallenge.'
        'com/pc/def/ocr.html")'
    )
    print(
        "\n\n--2) Retrieve the content from the url:\ncontent = html.read().d"
        "ecode('utf-8')"
    )
    print(
        "\n\n--3) Parse the content from the url in order to retrieve all the"
        "\ndata within the comment:\ndata = re.findall(r'<!--(.*?)-->', conte"
        "nt, re.DOTALL)[-1]"
    )
    print(
        "\n\n****Note: I am not printing out this data out because it will take"
        "\nup over a thousand lines. Just know that it is a lot of special"
        "\ncharacters with a only a few letters sprinkled through out****"
    )
    print(
        "\n\n--4) From the giant mess of data, we need to parse out all letters"
        "\nand join them into one string to get our answer:\nanswer = ''.join"
        "(re.findall('[a-z]', data))"
    )
    print('\n\nAnswer: ' + answer)
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


# http://www.pythonchallenge.com/pc/def/equality.html
def challenge_three():
    html = urlopen("http://www.pythonchallenge.com/pc/def/equality.html")

    content = html.read().decode('utf-8')
    data = re.findall(r"<!--(.*?)-->", content, re.DOTALL)[-1]

    empt = []

    for index, char in enumerate(data):
        if char.islower() and data[index + 1].isupper() and data[index + 2].isupper() and data[index + 3].isupper() and data[index + 4].islower():
            if data[index - 1].isupper() and data[index - 2].isupper() and data[index - 3].isupper() and data[index - 4].islower():
                empt.append(char)

    answer = "\n\nAnswer: " + "".join(empt)
    url = 'Next challenge is at http://www.pythonchallenge.com/pc/def/linkedlist.php'

    print(
        '\n\n--1) Go to the url:\nhtml = urlopen("http://www.pythonchallenge.'
        'com/pc/def/equality.html")'
    )
    print(
        "\n\n--2) Retrieve the content from the url:\ncontent = html.read().d"
        "ecode('utf-8')"
    )
    print(
        "\n\n--3) Parse the content from the url in order to retrieve all the"
        "\ndata within the commented section:\ndata = re.findall(r'<!--(.*?)-"
        "->', content, re.DOTALL)[-1]"
    )
    print(
        "\n\n--4) Iterate through the data. We will need to access each character "
        "\nin addition to the character's index:\nfor index, char in enumerat"
        "e(data):"
    )
    print(
        "\n\n--5) Create an if statement so that if a lowercase letter has exactly"
        "\nthree uppercase letters, on either side, append the lowercase letter"
        "\nto a list:\nif char.islower() and data[index + 1].isupper() and da"
        "ta[index + 2].isupper() and data[index + 3].isupper() and data[index"
        " + 4].islower():\nif data[index - 1].isupper() and data[index - 2].i"
        "supper() and data[index - 3].isupper() and data[index - 4].islower()"
        ":\nempt.append(char)"
    )
    print(answer)
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


# http://www.pythonchallenge.com/pc/def/linkedlist.php
def challenge_four():
    count = 0
    nothing = "12345"
    ready = input(
        "\n\nThis challenge will take a little over a minute to complete. It"
        "\nwill go through 400 separate pages (in reference to the comment made in"
        "\nthe page's source code): <!-- urllib may help. DON'T TRY ALL NOTHINGS,"
        "\nsince it will never end. 400 times is more than enough. -->\n\n"
        "Continue? {Yes} or {No}>"
    )
    if ready.lower() == 'yes':
        while count <= 400:
            html = urlopen(
                "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
                + nothing
            )
            content = html.read().decode('utf-8')
            data = re.findall(r"[\d.]", content, re.DOTALL)
            nothing = "".join(data)
            count += 1
            print(str(count) + ": " + content)
            html.close()
        answer = '\n\nAnswer: peak.html'
        url = 'Next challenge is at http://www.pythonchallenge.com/pc/def/peak.html'
        print(
            "\n\n--1) Create a variable named 'count' and set it equal to 0:"
            "\ncount = 0"
        )
        print(
            "\n\n--2) Create another variable with the value of the initial "
            "\n'nothing' from the challenge page:\nnothing = '12345'"
        )
        print(
            "\n\n--3) Create a while loop that will run as long as 'count' is"
            "\nless than or equal to 400:\nwhile count <= 400:"
        )
        print(
            "\n\n--4) Go to the url, but instead of copying the url, concatenate"
            "\nthe 'nothing' variable onto the url in order to allow it to ch"
            "ange dynamically:\nhtml = urlopen('http://www.pythonchallenge.co"
            "m/pc/def/linkedlist.php?nothing=' + nothing)"
        )
        print(
            "\n\n--5) Retrieve the content from the url:\ncontent = html.read"
            "().decode('utf-8')"
        )
        print(
            "\n\n--6) Parse the content from the url in order to retrieve any"
            "\nnumbers on the page:\ndata = re.findall(r'[\d.]', content, re.D"
            "OTALL)"
        )
        print(
            "\n\n--7) We now have the numbers needed to replace the 'nothing'"
            "\nvariable, but they are separated in a list so we must join them"
            "\ntogether into one string:\nnothing = ''.join(data)"
        )
        print("\n\n--8) increase the variable 'count' by one:\ncount += 1")
        print("\n\nthe answer is found at the 357nth iteration")
        print(
            "\n\n****Note: There is another way to complete this challenge by"
            "\ndividing the 'nothing' by two. You will still need the while"
            "\nloop and to replace the 'nothing' in the url.****"
        )
        print(answer)
        print(url)
        print('\n\n                         ^Scroll up to review steps^')
    elif ready.lower() == 'no':
        challenge_selector('4')
    else:
        print("\n\nI'm sorry, I didn't understand that. type Yes or No.")
        challenge_four()


# http://www.pythonchallenge.com/pc/def/peak.html
def challenge_five():
    html = urlopen("http://www.pythonchallenge.com/pc/def/banner.p")
    data = pickle.load(html)

    answer = '\n\nAnswer: channel'
    url = 'Next challenge is at http://www.pythonchallenge.com/pc/def/channel.html'
    print(
        '\n\n--1) Go to the url:\nhtml = urlopen("http://www.pythonchallenge.'
        'com/pc/def/banner.p")'
    )
    print(
        '\n\n--2) The data is serialized and, based off the hint given from'
        '\nthe initial page, we can deserialize the data using the pickle librar'
        'y:\ndata = pickle.load(html)'
    )
    print(
        '\n\n--3) Deserializing the data will result in multiple tuples. Create'
        '\na for loop to iterate through those tuples:\nfor item in data:'
    )
    print(
        '\n\n--4) Now, using list comprehension nested inside of the for loop,'
        '\nwe can multiply coordinates x and y, join each result together and'
        '\nprint them out:\nprint("".join([x * y for x, y in item]))'
    )
    for item in data:
        print("".join([x * y for x, y in item]))
    print(answer)
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


# http://www.pythonchallenge.com/pc/def/channel.html
def challenge_six():
    file = zipfile.ZipFile('channel.zip')
    readme = file.read('readme.txt').decode('utf-8')

    count = 0
    nothing = "90052"
    comments = []
    while count <= 908:
        text = file.read(nothing + '.txt').decode('utf-8')
        comments.append(file.getinfo(nothing + ".txt").comment.decode('utf-8'))
        data = re.findall(r"[\d.]", text, re.DOTALL)
        nothing = "".join(data)
        count += 1
        print(str(count) + ": " + text)
    comments = ''.join(comments)
    answer_one = 'Answer 1: hockey'
    answer_two = 'Answer 2: oxygen'
    url = 'Next challenge is at http://www.pythonchallenge.com/pc/def/oxygen.html'
    print(
        "\n\n--1) In the url, change '.html' to '.zip' It will then prompt you"
        "\nto download a zip folder. download it and place it wherever you want,"
        "\nbut remember the path. The folder is provided with this program so that it can run."
    )
    print(
        "\n\n--2) Use the zipfile library to open the zip folder:\nfile = zip"
        "file.ZipFile('channel.zip')"
    )
    print(
        "\n\n--3) Locate and read the readme:\nreadme = file.read('readme.txt"
        "').decode('utf-8')\nprint(readme)"
    )
    print(
        "\n\nreadme:\n"
        + readme
    )
    print(
        "\n\n--4) Create a variable named 'count' and set it equal to 0:"
        "\ncount = 0"
    )
    print(
        "\n\n--5) Create another variable with the value of the initial 'nothing'"
        "\nreferenced in the readme:\nnothing = '90052'"
    )
    print(
        "\n\n--6) Create a while loop that will run as long as 'count' is"
        "\nless than or equal to 908 (number of files inside the zipped folder):"
        "\nwhile count <= 908:"
    )
    print(
        "\n\n--7) read the file corresponding to the current 'nothing':\nte"
        "xt = file.read(nothing + '.txt').decode('utf-8')"
    )
    print(
        "\n\n--8) The very last file will tell us to 'collect the comments' so"
        "\nlet's go ahead and do that now. Using .getinfo() and .comment, we"
        "\ncan append a list with the comments from the files and then decode"
        "\nthem:\ncomments.append(file.getinfo(nothing + '.txt').comment.deco"
        "de('utf-8'))"
    )
    print(
        "\n\n--9) Parse the content from the file in order to retrieve any"
        "\nnumbers inside:\ndata = re.findall(r'[\d.]', text, re.D"
        "OTALL)"
    )
    print(
        "\n\n--10) We now have the numbers needed to replace the 'nothing'"
        "\nvariable, but they are separated in a list so we must join them"
        "\ntogether into one string:\nnothing = ''.join(data)"
    )
    print("\n\n--11) increase the 'count' variable by 1:\ncount += 1")
    print(
        "\n\n--12) And finally, join the comment list together and print it"
        "\nout to see the answer:\ncomments = ''.join(comments)\nprint(comments)"
    )
    print(comments)
    print(answer_one)
    print(answer_two)
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


# http://www.pythonchallenge.com/pc/def/oxygen.html
def challenge_seven():
    image = Image.open(BytesIO(requests.get(
        'http://www.pythonchallenge.com/pc/def/oxygen.png').content)
                       )
    row = []
    for x in range(image.width):
        row.append(image.getpixel((x, image.height / 2)))
    # row = [image.getpixel((x, image.height / 2)) for x in range(image.width)]
    row = row[::7]
    ords = [r for r, g, b, a in row if r == g == b]
    message = ''.join(map(chr, ords))
    message = '\n\nmessage: ' + message
    answer = re.findall("\d+", "".join(map(chr, ords)))
    answer = "\n\nAnswer: " + "".join(map(chr, map(int, answer)))
    url = 'Next challenge is at http://www.pythonchallenge.com/pc/def/integrity.html'

    print(
        "\n\n--1) Retrieve the image:\nimage = Image.open(BytesIO(requests.ge"
        "t('http://www.pythonchallenge.com/pc/def/oxygen.png').content))"
    )
    print(
        "\n\n--2) We want the grayscale esection of the image so we iterate"
        "\nthrough the pixels in that section and append them to a list:\nfor"
        " x in range(image.width):\nrow.append(image.getpixel((x, image.heigh"
        "t / 2)))"
    )
    print(
        "\n\n--3) If we try to print out row at this point we can see that there"
        "\nare repeats of each item. This will cause an error later on. We can"
        "\nremove this issue by telling the programming to skip over the repeats:"
        "\nrow = row[::7]"
    )
    print(
        "\n\n--4) Some tuples in our list don't represent gray scale items. We"
        "\ncan isolate those items, convert them to ASCII characters and join"
        "\nthem together:\nords = [r for r, g, b, a in row if r == g == b]\n"
        "message = ''.join(map(chr, ords))"
    )
    print(message)
    print(
        "\n\n--5) Now we simply parse out the list of numbers and convert them"
        "\nto ASCII to get our answer:\nanswer = re.findall('\d+', "".join(ma"
        "p(chr, ords)))\nanswer = "".join(map(chr, map(int, answer)))"
    )

    print(answer)
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


# http://www.pythonchallenge.com/pc/def/integrity.html
def challenge_eight():
    username = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
    password = b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'

    username = '\n\nUsername: ' + bz2.decompress(username).decode('utf-8')
    password = 'Password: ' + bz2.decompress(password).decode('utf-8')
    url = 'Next challenge is at http://www.pythonchallenge.com/pc/return/good.html'

    print(
        "\n\n--1) This challenge is pretty straight forward. use bz2 to decompress"
        "\nthe 'un' and 'pw' in the commented section of the source code and"
        "\nthen decode it:\n"
        r"username = bz2.decompress(b'BZh91AY&SYA\xaf\x82\r"
        r"\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1B"
        r"A\x06\xbe\x084').decode('utf-8')"
        + "\n"
        + r"password = bz2.decompress(b'BZh91A"
          r"Y&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1"
          r"BBP\x91\xf08').decode('utf-8')"
    )
    print(username)
    print(password)
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


# http://www.pythonchallenge.com/pc/return/good.html
def challenge_nine():
    url = 'http://www.pythonchallenge.com/pc/return/good.html'
    username = 'huge'
    password = 'file'
    html = requests.get(url, auth=(username, password))
    content = html.content.decode('utf-8')

    first = re.findall(r"first:(.*?)second:", content, re.DOTALL)[-1]
    first = first.replace("\n", "")
    first = first.split(",")
    first = list(map(int, first))
    # print(first)

    second = re.findall(r"second:(.*?)-->", content, re.DOTALL)[-1]
    second = second.replace("\n", "")
    second = second.split(",")
    second = list(map(int, second))
    # print(second)

    image = Image.new('RGB', (500, 500))
    draw = ImageDraw.Draw(image)
    draw.polygon(first, fill='white')
    draw.polygon(second, fill='black')
    image.show()
    answer = '\n\nAnswer: bull'
    url = 'Next challenge is at http://www.pythonchallenge.com/pc/def/bull.html'
    print(
        "\n\n--1) In order to access the url we will need to use the username"
        "\nand password aquired from the previous challenge:\nhtml = requests"
        ".get('http://www.pythonchallenge.com/pc/return/good.html', auth=('hu"
        "ge', 'file'))"
    )
    print(
        "\n\n--2) Decode the content from the url:\ncontent = html.content.de"
        "code('utf-8')"
    )
    print(
        "\n\n--3) We will need to separate the two sections in the comments"
        "\nlabeled 'first' and 'second':\nfirst = re.findall(r'first:(.*?)sec"
        "ond:', content, re.DOTALL)[-1]\nsecond = re.findall(r'second:(.*?)--"
        ">', content, re.DOTALL)[-1]"
    )
    print(
        "\n\n****note: I will be using the 'first' variable for the rest of"
        "\nthese examples, but everything done to that variable will need to"
        "\nbe repeated for the 'second' variable****"
    )
    print(
        "\n\n--4) Now, clean the data. Replace all '\\n's in the data:\nfirst"
        " = first.replace('\\n', '')"
    )
    print(
        "\n\n--5) Separate the items, into a list of numbers, by comma :\nfirs"
        "t = first.split(',')"
    )
    print(
        "\n\n--6) Convert list of numbers into integers:\nfirst = list(map(in"
        "t, first))"
    )
    print(
        "\n\n--7) We are going to have to create an image, but we first need"
        "\nto create our canvas. We can do this by using the PILLOW library:"
        "\nimage = Image.new('RGB', (500, 500))"
    )
    print(
        "\n\n--8) Now we can tell the program to start drawing our polygons with"
        "\nthe coordinates that we aquired with our 'first' and 'second' variables:"
        "\ndraw = ImageDraw.Draw(image)\ndraw.polygon(first, fill='white')\nd"
        "raw.polygon(second, fill='black')"
    )
    print(
        "\n\n--9) Finally we can reveal our image which will give us the clue"
        "\nfor this challenge:\nimage.show()"
    )
    print(answer)
    print(url)
    print('\n\n                         ^Scroll up to review steps^')


def another_one(selector):
    running = True
    while running:
        message = '\nWould you like me to complete another challenge?\n      ' \
                  '(Yes or No)\n'
        print(message)
        choice = input('> ')
        if choice.lower() == 'yes':
            challenge_selector(selector)
        elif choice.lower() == 'no':
            print("\n\nThank you for your time.")
            print(figlet_format('GOODBYE', font='digital'))
            exit()
        else:
            print("\nI'm sorry, I didn't understand that. type Yes or No.\n")


def challenge_selector(selector):
    top_separator = ('=' * 84) + '\n'
    bottom_separator = ('=' * 84) + '\n'
    challenge_list = [
        ('\n{0 or Zero}' + ('-' * 15) + 'warming up'),
        ('{1 or One}' + ('-' * 16) + 'What about making trans?'),
        ('{2 or Two}' + ('-' * 16) + 'ocr'),
        ('{3 or Three}' + ('-' * 14) + 're'),
        ('{4 or Four}' + ('-' * 15) + 'follow the chain'),
        ('{5 or Five}' + ('-' * 15) + 'peak hell'),
        ('{6 or Six}' + ('-' * 16) + 'now there are pairs'),
        ('{7 or Seven}' + ('-' * 14) + 'smarty'),
        ('{8 or Eight}' + ('-' * 14) + 'working hard?'),
        ('{9 or Nine}' + ('-' * 15) + 'connect the dots'),
        ('{Exit}' + ('-' * 20) + 'quit'),
    ]

    if selector == 'initial':
        print(top_separator)
        print(figlet_format('   D U B\n        S T E P\n            H E N',
                            font='alligator'))
        welcome_message = "Thank you for taking the time to check out my program." \
                          "\nYou can access the Python Challenge website at" \
                          "\n\n    --http://www.pythonchallenge.com/\n\n" \
                          "or jump straight into the first challenge by going" \
                          " to \n\n    --http://www.pythonchallenge.com/pc" \
                          "/def/0.html\n\nI will add more challenges when I g" \
                          "et around to completing them myself"

        print(welcome_message)
        print(bottom_separator)
        selector = "By typing the number of a challenge (i.e. {0} or {Zero}" \
                   "\nfor the challenge titled 'warming up') you will be provided" \
                   "\nwith the answer, as well as an explanation of how to complete" \
                   "\nthe challenge. I would suggest taking a crack at finding" \
                   "\nthe solutions yourself before using this tool, but with" \
                   "\nthat being said, \n\nWhich challenge would you like to complete?"
        print(selector)
        for option in challenge_list:
            print(option)
        selector = input('> ')
    else:
        print(top_separator)
        message = "Choose another challenge to complete.\n      Previous challenge: " \
                  + selector
        print(message)
        for option in challenge_list:
            print(option)
        selector = input('> ')

    if selector.lower() == 'zero' or selector == '0':
        print(top_separator)
        challenge_zero()
        print(bottom_separator)
    elif selector.lower() == 'one' or selector == '1':
        print(top_separator)
        challenge_one()
        print(bottom_separator)
    elif selector.lower() == 'two' or selector == '2':
        print(top_separator)
        challenge_two()
        print(bottom_separator)
    elif selector.lower() == 'three' or selector == '3':
        print(top_separator)
        challenge_three()
        print(bottom_separator)
    elif selector.lower() == 'four' or selector == '4':
        print(top_separator)
        challenge_four()
        print(bottom_separator)
    elif selector.lower() == 'five' or selector == '5':
        print(top_separator)
        challenge_five()
        print(bottom_separator)
    elif selector.lower() == 'six' or selector == '6':
        print(top_separator)
        challenge_six()
        print(bottom_separator)
    elif selector.lower() == 'seven' or selector == '7':
        print(top_separator)
        challenge_seven()
        print(bottom_separator)
    elif selector.lower() == 'eight' or selector == '8':
        print(top_separator)
        challenge_eight()
        print(bottom_separator)
    elif selector.lower() == 'nine' or selector == '9':
        print(top_separator)
        challenge_nine()
        print(bottom_separator)
    elif selector.lower() == 'exit':
        print("\n\nThank you for your time.")
        print(figlet_format('GOODBYE', font='digital'))
        exit()
    else:
        print(
            "I'm sorry. I have not completed that challenge myself, but you c"
            "an try a different challenge"
        )
        challenge_selector(selector)
    another_one(selector)


challenge_selector('initial')
