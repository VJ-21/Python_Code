def hello(name,lang):
    Countries={
        "India":"Multi-lang",
        "Gerogia":"English",
        "Korea":"Korean"
    }
    msg=f"This country {name} speaks {Countries[name]}"
    print(msg)


if  __name__=='__main__':
    import argparse
    parser=argparse.ArgumentParser(description="This commandline used for passing values from terminal to get values from dictionary")
    parser.add_argument('-n','--name',metavar="Key of the dict",required=True,choices=['India','Gerogia','Korea'])
    parser.add_argument('-l','--lang',metavar="Value of the dict",required=True,choices=['Multi-lang','English','Korean'])
    arguments=parser.parse_args()

hello(arguments.name,arguments.lang)
