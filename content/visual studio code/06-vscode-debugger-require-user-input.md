Title: VS Code Debug Console Apps w/User Input
Date: 2018-01-20 17:05
Tags: visual studio code
Slug: vscode-debug-console-apps-with-user-input

I’ve been developing a few little console apps in C# using Visual Studio Code. The latest one I’ve been working on requires some input from the user. In particular, System. Console.ReadKey() and System.Console.ReadLine(). 

With this latest project, on launching the debugger I ran into an unhandled exception of type System.InvalidOperationException. The description read, “Cannot read keys when either application does not have a console or when console input has been redirected.”

To get around this exception you have to make a change to a configuration file called, launch.json.

You’ll want to click on the little gear at the top in the Debug Sidebar.

![screenshot of debugger settings gear icon](images/launch-json-gear-crop.png)

That will open the launch.json file.

![screenshot of launch.json file](images/launch-json-file-crop.png)

In the launch.json file change the value of the console property from internalConsole to integratedTerminal.

![screenshot of the necessary change to launch.json](images/change-to-launch-json-crop.png)

This will direct all output from the debugger to Visual Studio Code’s integrated terminal.

<span style="color:red;">Note: On launching the debugger you may have to manually open the terminal to see the output.</span>

If you ever want to change it back, just reverse the changes made to the launch.json file.

That's it!
