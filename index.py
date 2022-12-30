import sys

arguments = sys.argv

title = arguments[1]
description = arguments[2]
frameworks = arguments[3].split(" ")
onlineAccess = arguments[4]
haveNpm = False
npm = "npm run dev"



file = open("README.md","w")
file.write("# " + title +"\n\n")
file.write(description + "\n\n")
file.write("## Frameworks\n\n")
for i in range(0,len(frameworks)):
    if (frameworks[i].lower() == "next"):
        file.write("- [Next.js](https://nextjs.org)\n")
        npm = "npm run dev"
    
    elif (frameworks[i].lower() == "node"):
        file.write("- [Node.js](https://nodejs.org)\n")
        haveNpm = True

    elif (frameworks[i].lower() == "tailwindcss"):
        file.write("- [Tailwind CSS](https://tailwindcss.com)\n")

    elif (frameworks[i].lower() == "react"):
        file.write("- [React.js](https://reactjs.org)\n")
        npm = "npm start"

    elif (frameworks[i].lower() == "vite"):
        file.write("- [Vite.js](https://vitejs.dev)\n")
        npm = "npm run dev"

file.write("\n## How to use it?\n\n")

if (onlineAccess != "0"):
    file.write("### Online access\n\n")
    file.write("Just click in the website of the repository or [here](" + onlineAccess + ")!\n\n")
    file.write("##### or\n\n")

file.write("### Local access\n\n")

if(haveNpm):
    file.write("1. Install node modules in the project with `npm install`\n\n")
    file.write("2. Start the local server using `" + npm + "`\n\n")
    file.write("##### [Back to the top](https://github.com/imLymei/tower-of-hanoi#Tower-of-Hanoi)\n\n")
    file.write("###### Create by [Felipe Cardoso](https://lymei.art)")

file.close()
