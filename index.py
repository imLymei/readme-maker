import getopt, sys


# Remove 1st argument from the
# list of command line arguments
argumentList = sys.argv[3:]

# Options
options = "nNtvro:"

# Long options
long_options = [ "Next", "Node","Tailwind","Vite","React","Online="]

haveNpm = False
title = sys.argv[1]

if (title == "h" or title == "Help"):
    isHelp = True
    print ("\nThis command makes a preset README.md file.\n args: Title Description [Options]\n Options:\n  h, Help: Display help\n  -Next: adds Next.js in the frameworks\n  -Node: adds Node.js in the frameworks\n  -Tailwind: adds Tailwind CSS in the frameworks\n  -Vite: adds Vite.js in the frameworks\n  -React: adds React.js in the frameworks\n  -o, --Online: If the project has a online access use this option and set the link to the server/website")

else:
    description = sys.argv[2]
    isHelp = False

    file = open("README.md","w",encoding="UTF-8")
    file.write("# " + title +"\n\n")
    file.write(description + "\n\n")
    file.write("## Frameworks\n\n")

try:
	# Parsing argument
    arguments, values = getopt.getopt(argumentList, options, long_options)
	
	# checking each argument
    for currentArgument, currentValue in arguments:

        if currentArgument in ("-n", "--Next"):
            file.write("- [Next.js](https://nextjs.org)\n")
            npm = "npm run dev"
            haveNpm = True
        
        elif currentArgument in ("-N", "--Node"):
            file.write("- [Node.js](https://nodejs.org)\n")
            haveNpm = True

        elif currentArgument in ("-t", "--Tailwind"):
            file.write("- [Tailwind CSS](https://tailwindcss.com)\n")

        elif currentArgument in ("-r", "--React"):
            file.write("- [React.js](https://reactjs.org)\n")
            npm = "npm start"
            haveNpm = True

        elif currentArgument in ("-v", "--Vite"):
            file.write("- [Vite.js](https://vitejs.dev)\n")
            npm = "npm run dev"
            haveNpm = True

    if(isHelp == False):
        file.write("\n## How to use it?\n\n")
        
        for currentArgument, currentValue in arguments:
            if currentArgument in ("-o","--Online"):
                file.write("### Online access\n\n")
                file.write(("Just click in the website of the repository or [here]( % s )!\n\n") % (currentValue))
                file.write("##### or\n\n")
                
        file.write("### Local access\n\n")

        if(haveNpm):
            file.write("1. Install node modules in the project with `npm install`\n\n")
            file.write("2. Start the local server using `" + npm + "`\n\n")
            file.write("##### [Back to the top](#)\n\n")
            file.write("###### Create by [Felipe Cardoso](https://lymei.art)")
            file.close()
        else:
            file.write("Just open index.html in live server\n\n")
            file.write("##### [Back to the top](#)\n\n")
            file.write("###### Create by [Felipe Cardoso](https://lymei.art)")
            file.close()

except getopt.error as err:
	# output error, and return with an error code
	print (str(err))
