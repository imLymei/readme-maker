import getopt, sys

argumentList = sys.argv[3:]

options = "pjnNtvro:"
long_options = [ "Python", "Javascript", "Next", "Node","Tailwind","Vite","React","Online="]

haveNpm = False
isPython = False
title = sys.argv[1]

if (title.lower() == "h" or title.lower() == "help"):
    isHelp = True
    print ("\nThis command makes a preset README.md file.\n args: [Title/help request] Description [Options]\n Options:\n  -p, --Python: adds python in the languages\n  -j, --Javascript: adds javascript in the languages\n  -n, --Next: adds Next.js in the frameworks\n  -N, --Node: adds Node.js in the frameworks\n  -t, --Tailwind: adds Tailwind CSS in the frameworks\n  -v, --Vite: adds Vite.js in the frameworks\n  -r, --React: adds React.js in the frameworks\n  -o, --Online: If the project has a online access use this option and set the link to the server/website")

else:
    description = sys.argv[2]
    isHelp = False

    file = open("README.md","w",encoding="UTF-8")
    file.write("# " + title +"\n\n")
    file.write(description + "\n\n")
    file.write("## 💻Frameworks/Languages\n\n")

try:
    arguments, values = getopt.getopt(argumentList, options, long_options)

    for currentArgument, currentValue in arguments:

        if currentArgument in ("-p", "--Python"):
            file.write("- [Python](https://www.python.org)\n")
            runCommand = "python3 index.py"
            isPython = True
            
        elif currentArgument in ("-j", "--Javascript"):
            file.write("- [Javascript](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript)\n")

        elif currentArgument in ("-n", "--Next"):
            file.write("- [Next.js](https://nextjs.org)\n")
            runCommand = "npm run dev"
            haveNpm = True
        
        elif currentArgument in ("-N", "--Node"):
            file.write("- [Node.js](https://nodejs.org)\n")
            haveNpm = True

        elif currentArgument in ("-t", "--Tailwind"):
            file.write("- [Tailwind CSS](https://tailwindcss.com)\n")

        elif currentArgument in ("-r", "--React"):
            file.write("- [React.js](https://reactjs.org)\n")
            runCommand = "npm start"
            haveNpm = True

        elif currentArgument in ("-v", "--Vite"):
            file.write("- [Vite.js](https://vitejs.dev)\n")
            runCommand = "npm run dev"
            haveNpm = True

    if(isHelp == False):
        file.write("\n## 🚀How to use it?\n\n")
        
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-o","--Online"):
                file.write("### Online access\n\n")
                file.write(("Just click in the website of the repository or [here]( % s )!\n\n") % (currentValue))
                file.write("##### or\n\n")
                
        file.write("### Local access\n\n")

        if(haveNpm):
            file.write("Install node modules in the project and start the server:\n")
            file.write(("\n```\n#install npm\nnpm install\n\n#start server\n% s\n```\n\n") % (runCommand))
            file.write("##### [Back to the top](#)\n\n")
            file.write("###### Create by [Felipe Cardoso](https://lymei.art)")
            file.close()
            print("Arquivo criado")
        elif(isPython):
            file.write(("Run the index.py:\n```\n% s\n```\n\n") % (runCommand))
            file.write("##### [Back to the top](#)\n\n")
            file.write("###### Create by [Felipe Cardoso](https://lymei.art)")
            file.close()
            print("Arquivo criado")
        else:
            file.write("Just open index.html in live server\n\n")
            file.write("##### [Back to the top](#)\n\n")
            file.write("###### Create by [Felipe Cardoso](https://lymei.art)")
            file.close()
            print("Arquivo criado")
            

except getopt.error as err:
	print (str(err))
