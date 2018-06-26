import os
from os.path import expanduser
import webbrowser
home = expanduser("~")
class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'


os.system("clear")
def menu():
    print "\n"
    print color.YELLOW+"     Welcome to the FastMenu"+color.END
    print color.YELLOW+"     -----------------------------------------------"+color.END
    print "     "+color.YELLOW+"|"+color.END+" 1. Start a new Angular Project              "+color.YELLOW+"|"
    print color.YELLOW+"     -----------------------------------------------"+color.END  
    print "     "+color.YELLOW+"|"+color.END+" 2. Start a new HTML Blank Project           "+color.YELLOW+"|"
    print color.YELLOW+"     -----------------------------------------------"+color.END
    print "     "+color.YELLOW+"|"+color.END+" 3. Start a new Ionic Blank Project          "+color.YELLOW+"|"
    print color.YELLOW+"     -----------------------------------------------"+color.END
    print "     "+color.YELLOW+"|"+color.END+" 4. Exit FastMenu                            "+color.YELLOW+"|"
    print color.YELLOW+"     -----------------------------------------------"+color.END
    print "\n"
    option = input(color.YELLOW+"   Select option: "+color.END)
    print "\n"
    if option == 1:
        name = raw_input(color.RED+"  Angular Proyect Name: "+color.END)
        os.system("cd $HOME/Desktop; ng new "+name+"")
        print "\n"
    elif option == 2:
        name = raw_input(color.RED+"   HTML Proyect Name: "+color.END)
        os.system("cd $HOME/Desktop; mkdir "+name+";touch $HOME/Desktop/"+name+"/index.html")
        os.system("mkdir $HOME/Desktop/"+name+"/img")
        os.system("mkdir $HOME/Desktop/"+name+"/css")
        os.system("mkdir $HOME/Desktop/"+name+"/js")
        os.system("touch $HOME/Desktop/"+name+"/css/style.css")
        os.system("touch $HOME/Desktop/"+name+"/js/main.js")
        os.system("cd $HOME")
        f = open(home+'/Desktop/'+name+'/index.html','w')
        add = raw_input(color.BLUE+"   Add Bootstrap and Icons (Y/n): "+color.END)

        if add == 'y' or add == 'Y':
            mensaje = '''<html lang="en">
<head>
    <title>'''+name+'''</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/css/bootstrap.min.css" integrity="sha384-WskhaSGFgHYWDcbwN70/dfYBj47jz9qbsMId/iRN3ewGhXQFZCSftd1LZCfmhktB" crossorigin="anonymous">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
                <a class="navbar-brand" href="#">'''+name+'''</a>
                <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                  <span class="navbar-toggler-icon"></span>
                </button>
              
                <div class="collapse navbar-collapse" id="navbarSupportedContent">
                  <ul class="navbar-nav mr-auto">
                    <li class="nav-item active">
                      <a class="nav-link" href="#">Home <span class="sr-only">(current)</span></a>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link" href="#">Link</a>
                    </li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" id="navbarDropdown" role="button" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                        Dropdown
                      </a>
                      <div class="dropdown-menu" aria-labelledby="navbarDropdown">
                        <a class="dropdown-item" href="#">Action</a>
                        <a class="dropdown-item" href="#">Another action</a>
                        <div class="dropdown-divider"></div>
                        <a class="dropdown-item" href="#">Something else here</a>
                      </div>
                    </li>
                    <li class="nav-item">
                      <a class="nav-link disabled" href="#">Disabled</a>
                    </li>
                  </ul>
                  <form class="form-inline my-2 my-lg-0">
                    <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
                    <button class="btn btn-dark my-2 my-sm-0" type="submit"><i class="material-icons">search</i></button>
                  </form>
                </div>
              </nav>
</body>
<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.3/umd/popper.min.js" integrity="sha384-ZMP7rVo3mIykV+2+9J3UJ46jBk0WLaUAdn689aCwoqbBJiSnjAK/l8WvCWPIPm49" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.1.1/js/bootstrap.min.js" integrity="sha384-smHYKdLADwkXOn1EmN1qk/HfnUcbVRZyYmZ4qpPea6sjB/pTJ0euyQp0Mk8ck+5T" crossorigin="anonymous"></script>
</html>'''
        else:
            adMat = raw_input(color.PURPLE+"   Add materialize complete (Y/n) "+color.END)
            if adMat == "y" or adMat == "Y":
                mensaje = '''<html lang="en">
<head>
    <title>'''+name+'''</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/css/materialize.min.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<body>
    <nav class="nav blue">
        <div class="container">
                <div class="nav-wrapper">
                  <a href="#" class="brand-logo">'''+name+'''</a>
                  <ul id="nav-mobile" class="right hide-on-med-and-down">
                    <li><a href="sass.html">Sass</a></li>
                    <li><a href="badges.html">Components</a></li>
                    <li><a href="collapsible.html">JavaScript</a></li>
                  </ul>
                </div>
        </div>
    </nav>
</body>
<script src="https://code.jquery.com/jquery-3.3.1.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0-rc.2/js/materialize.min.js"></script>
</html>'''
            else:
                adIcon = raw_input(color.GREEN+"   Add only the Icons (Y/n) "+color.END)
                if adIcon == "y" or adIcon == "Y":
                    mensaje = '''<html lang="en">
<head>
    <title>'''+name+'''</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons" rel="stylesheet">
</head>
<style>
    *{
        padding:0;
        margin:0;
        box-sizing: border-box;
        font-family:Avenir Next;
    }
</style>
<body>
    <h1>Hello World <i class="material-icons">favorite</i></h1>
</body>
</html>'''
                else:
                    mensaje = '''<html lang="en">
<head>
    <title>'''+name+'''</title>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
</head>
<style>
    *{
        padding:0;
        margin:0;
        box-sizing: border-box;
        font-family:Avenir Next;
    }
</style>
<body>
    
</body>
</html>'''

    elif option == 3:
        name = raw_input(color.CYAN+"  Ionic Proyect Name: "+color.END)
        os.system("ionic start "+name)
        print "\n"

    elif option == 4:
        print "\n"
        return 0
    
    f.write(mensaje)
    f.close()
    webbrowser.open_new('file://'+home+'/Desktop/'+name+'/index.html')
    print "\n"

menu()
