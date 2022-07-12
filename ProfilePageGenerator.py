# README.md

list_parts = [
    "unordered-list",

    "ordered-list",

    "list-element",

    "biggest-title",
    "very-big-title",
    "big-title",
    "medium-title",
    "small-title",
    "smallest-title",

    "paragraph",

    "italic",

    "bold",

    "superscript",

    "subscript",

    "underlined",

    "deleted",

    "citation",

    "link",

    "video",

    "image",

    "piece-of-code",

    "visitor-count",


]

parts = {
    "unordered-list1": '<ul>\n  ',
    "unordered-list2": '\n<ul>',

    "ordered-list1": '<ol>\n  ',
    "ordered-list2": '\n<ol>',

    "list-element1": '<li>',
    "list-element2": '</li>',

    "biggest-title1": '<h1>',
    "biggest-title2": '</h1>',
    "very-big-title1": '<h2>',
    "very-big-title2": '</h2>',
    "big-title1": '<h3>',
    "big-title2": '</h3>',
    "medium-title1": '<h4>',
    "medium-title2": '</h4>',
    "small-title1": '<h5>',
    "small-title2": '</h5>',
    "smallest-title1": '<h6>',
    "smallest-title2": '</h6>',

    "paragraph1": '<p>',
    "paragraph2": '</p>',

    "italic1": '<i>',
    "italic2": '</i>',

    "bold1": '<b>',
    "bold2": '</b>',

    "link1": '<a href="',
    "link2": '">',
    "link3": '</a>',

    "video1": '<video controls="" autoplay="" name="media">\n    <source src="',
    "video2": '" type="video/mp4">\n</video>',

    "image1": '<img src="',
    "image2": '">',

    "piece-of-code1": '<kbd>',
    "piece-of-code2": '</kbd>',

    "superscript1": '<sup>',
    "superscript2": '</sup>',

    "subscript1": '<sub>',
    "subscript2": '</sub>',

    "underlined1": '<ins>',
    "underlined2": '</ins>',

    "deleted1": '<del>',
    "deleted2": '</del>',

    "citation1": '<cite>',
    "citation2": '</cite>',

    "visitor-count1": '![Visitor Count](https://profile-counter.glitch.me/',
    "visitor-count2": '/count.svg)',

}

def list_parts_fun():
    print("List of Elements:\n")
    for i in list_parts:
        print(i)

print("\n\nCOMMANDS:")
print("    List of Elements:         [list]")
print("    Finish:                   [ok]\n")
list_parts_fun()
print("\n")



tot = ""

parte = ""

while True:
    theInput = input("-->    ")
    theInput = theInput.lower()
    print("")
    if theInput == "list":
        list_parts_fun()
    elif theInput != "ok" and theInput != "list":
        ##unordered-list
        if theInput == "unordered-list":
            print("How many element?")
            newInput1 = input("---->    ")
            parte = parts["unordered-list1"]
            for i in range (0, int(newInput1)):
                print(f"What is the name of element {i+1}?")
                newInput2 = input("------>    ")
                if i != int(newInput1):
                    parte += parts["list-element1"] + newInput2 + parts["list-element2"] + "\n    "
                else:
                    parte += parts["list-element1"] + newInput2 + parts["list-element2"]
            parte += parts["unordered-list2"]
        ##ordered-list
        elif theInput == "ordered-list":
            print("How many element?")
            newInput1 = input("---->    ")
            parte = parts["ordered-list1"]
            for i in range (0, int(newInput1)):
                print(f"What is the name of element {i+1}?")
                newInput2 = input("------>    ")
                if i != int(newInput1):
                    parte += parts["list-element1"] + newInput2 + parts["list-element2"] + "\n    "
                else:
                    parte += parts["list-element1"] + newInput2 + parts["list-element2"]
            parte += parts["ordered-list2"]
        ##biggest-title
        elif theInput == "biggest-title":
            parte = parts["biggest-title1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["biggest-title2"]
        ##very-big-title
        elif theInput == "very-big-title":
            parte = parts["very-big-title1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["very-big-title2"]
        ##big-title
        elif theInput == "big-title":
            parte = parts["big-title1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["big-title2"]
        ##medium-title
        elif theInput == "medium-title":
            parte = parts["medium-title1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["medium-title2"]
        #small-title
        elif theInput == "small-title":
            parte = parts["small-title1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["small-title2"]
        ##smallest-title
        elif theInput == "smallest-title":
            parte = parts["smallest-title1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["smallest-title2"]
        ##paragraph
        elif theInput == "paragraph":
            parte = parts["paragraph1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["paragraph2"]
        ##italic
        elif theInput == "italic":
            parte = parts["italic1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["italic2"]
        ##bold
        elif theInput == "bold":
            parte = parts["bold1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["bold2"]
        ##superscript
        elif theInput == "superscript":
            parte = parts["superscript1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["superscript2"]
        ##subscript
        elif theInput == "subscript":
            parte = parts["subscript1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["subscript2"]
        ##underlined
        elif theInput == "underlined":
            parte = parts["underlined1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["underlined2"]
        ##deleted
        elif theInput == "deleted":
            parte = parts["deleted1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["deleted2"]
        ##citation
        elif theInput == "citation":
            parte = parts["citation1"]
            print("what is the text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["citation2"]
        ##piece-of-code
        elif theInput == "piece-of-code":
            parte = parts["piece-of-code1"]
            print("what is the code text?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["piece-of-code2"]
        ##link
        elif theInput == "link":
            parte = parts["link1"]
            print("what is the link? (use the http:// or https:// protocol)")
            newInput1 = input("---->    ")
            print("what is the text?")
            newInput2 = input("---->    ")
            parte += newInput1 + parts["link2"] + newInput2 + parts["link3"]
        ##video
        elif theInput == "video":
            parte = parts["video1"]
            print("what is the video URL? (use the http:// or https:// protocol)")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["video2"]
        ##image
        elif theInput == "image":
            parte = parts["image1"]
            print("what is the image URL? (use the http:// or https:// protocol)")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["image2"]
        ##visitor-count
        elif theInput == "visitor-count":
            parte = parts["visitor-count1"]
            print("what is your GitHub username?")
            newInput1 = input("---->    ")
            parte += newInput1 + parts["visitor-count2"]
        parte += "<br>"
    else:
        file = open("README.md", "w")
        file.write(tot)
        file.close()
        break

    tot += parte + "\n"


